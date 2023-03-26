from cursor import CursorBot


bot = CursorBot()
code_stream = bot.get_code_stream("写一个flask的程序", 0, 1)

for code_type, code in code_stream:
    print(code, end="", flush=True)
    # pass