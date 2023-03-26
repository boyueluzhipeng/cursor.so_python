import requests
import json
import os
import inspect


class CursorBot:
    def __init__(self) -> None:
        pass

    def __get_response(self, message, file_path, abs_path, startNum=0, endNum=-1):
        url = "https://aicursor.com/conversation"
        msgType = 'generate'
        currentFileContents = open(file_path, "r").read()
        total_lines = len(currentFileContents.splitlines())
        currentSelection = None
        precedingCode = []
        suffixCode= []
        if endNum != -1:
            if endNum > total_lines:
                endNum = total_lines
            precedingCode = currentFileContents.splitlines()[0:startNum]
            currentSelection = currentFileContents.splitlines()[startNum:endNum]
            suffixCode = currentFileContents.splitlines()[endNum:total_lines]
            precedingCode = "\n".join(precedingCode)
            if precedingCode != "":
                precedingCode = [precedingCode]
            else:
                precedingCode = []
            currentSelection = "\n".join(currentSelection)
            suffixCode = "\n".join(suffixCode)
            if suffixCode != "":
                suffixCode = [suffixCode]
            else:
                suffixCode = []
            msgType = 'edit'
        
        payload = {
            "userRequest": {
                "message": message,
                "currentRootPath": abs_path,
                "currentFileName": file_path,
                "currentFileContents": currentFileContents,
                "precedingCode": precedingCode,
                "currentSelection": currentSelection,
                "suffixCode": suffixCode,
                "copilotCodeBlocks": [],
                "customCodeBlocks": [],
                "codeBlockIdentifiers": [],
                "msgType": msgType,
                "maxOrigLine": None
            },
            "userMessages": [],
            "botMessages": [],
            "contextType": "copilot",
            "rootPath": "/Users/luzhipeng/lu/cursor/cursor"
        }
        payload = json.dumps(payload)

        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Cursor/0.1.1 Chrome/108.0.5359.62 Electron/22.0.0 Safari/537.36",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate, br"
        }

        try:
            response = requests.request("POST", url, headers=headers, data=payload, stream=True)
            for line in response.iter_lines():
                # line 是 b'data: "<|BEGIN_type|>" 这样格式，转换成字符串
                line = line.decode('utf-8')
                # 去掉前面的 "data: "
                line_arr = line.split("data: ")
                for l in line_arr:
                    if l != "":
                        try:
                            final_l = json.loads(l)
                            yield final_l
                        except json.decoder.JSONDecodeError as e:
                            yield l
        except requests.exceptions.ChunkedEncodingError as e:
            print(e)
    
        
    def get_code_stream(self, message, startNum=0, endNum=-1, file_path=None, abs_path=None):
        if file_path is None:
            # 获取调用该函数的文件路径
            current_file_path = inspect.stack()[1].filename
        else:
            current_file_path = file_path
        if abs_path is None:
            current_abs_path = os.path.abspath(current_file_path)
        else:
            current_abs_path = abs_path
        print(current_file_path)
        response = self.__get_response(message, current_file_path, current_abs_path, startNum, endNum)
        type_str = 'generate'
        is_message = False
        for line in response:
            if line == "":
                continue
            if line.startswith('<|BEGIN_type|>'):
                type_str += line.replace('<|BEGIN_type|>', '')
            elif line.endswith('<|END_type|>'):
                type_str += line.replace('<|END_type|>', '')
            elif line.startswith('<|BEGIN_message|>'):
                is_message = True
                tmp_line = line.replace('<|BEGIN_message|>', '')
                if is_message:
                    yield type_str, tmp_line
            elif line.endswith('<|END_message|>'):
                tmp_line += line.replace('<|END_message|>', '')
                yield type_str, tmp_line
                is_message = False
            else:
                if is_message:
                    yield type_str, line
            
        



