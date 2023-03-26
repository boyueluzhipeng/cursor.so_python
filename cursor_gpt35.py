import os
from ChatGPT.ChatGPT import Chatbot
import inspect


promopt = """
Act as a natural language to code translation engine.
Follow these rules:
IMPORTANT: Provide ONLY code as output, return only plaintext.
IMPORTANT: Do not show html, styled, colored formatting.
IMPORTANT: Do not add notes or intro sentences.
IMPORTANT: Provide full solution. Make sure syntax is correct.
"""


class CursorGPTBot:
    
    def __init__(self, api_key):
        self.bot = Chatbot(api_key=api_key, system_prompt=promopt)
        
    def get_code_stream(self, message, startNum=0, endNum=-1, file_path=None, abs_path=None):
        if file_path is None:
            current_file_path = inspect.stack()[1].filename
        else:
            current_file_path = file_path
            
        if abs_path is None:
            abs_file_path = os.path.abspath(current_file_path)
        else:
            abs_file_path = abs_path
            
        # print("abs_file_path: ", abs_file_path, "current_file_path: ", current_file_path)
            
        # 根据startNum和endNum获取代码片段
        msgType = 'generate'
        currentFileContents = open(current_file_path, "r").read()
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
        
        if currentSelection is None:
            currentSelection = ""
        if currentSelection == "":
            msgType = 'generate'
            
        code_language = 'python'
        # 根据文件路径获取代码语言
        if abs_file_path.endswith('.py'):
            code_language = 'python'
        elif abs_file_path.endswith('.js'):
            code_language = 'javascript'
        elif abs_file_path.endswith('.html'):
            code_language = 'html'
        elif abs_file_path.endswith('.css'):
            code_language = 'css'
        elif abs_file_path.endswith('.java'):
            code_language = 'java'
        elif abs_file_path.endswith('.c'):
            code_language = 'c'
        elif abs_file_path.endswith('.cpp'):
            code_language = 'cpp'
        elif abs_file_path.endswith('.go'):
            code_language = 'go'
        # 拼凑下需要发送的消息
        if msgType == 'generate':
            prompt = f'帮我{message}的{code_language}的程序,\n#code_only'
        else:
            prompt = f'上面是{code_language}程序, {currentSelection}是我想要修改的部分, 要求是{message},\n#code_only'
        # print("prompt: ", prompt)
        response = self.bot.ask_stream(prompt)
        for code in response:
            yield msgType, code
            
                
                
            
