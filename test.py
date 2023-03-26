from cursor_gpt35 import CursorGPTBot

bot = CursorGPTBot(api_key="YOUR_API_KEY")


stream = bot.get_code_stream("添加一个动态路由", 0, 10, file_path="/Users/luzhipeng/lu/cursor/cursor_server/flask_test.py", abs_path="/Users/luzhipeng/lu/cursor/cursor_server/flask_test.py")

for code_type, code in stream:
    print(code, end="", flush=True)