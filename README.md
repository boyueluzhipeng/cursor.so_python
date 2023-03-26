Chatbot基于OpenAI GPT-3.5技术，提供了一个简单易用的API来创建聊天机器人。您只需要提供API密钥并进行一些简单的配置，就可以开始使用Chatbot来与用户进行自然语言交互。

本项目提供了流式和非流式两种问答方式，并支持多个对话。此外，还提供了一些实用程序函数，如create_session和create_completer，以帮助您更轻松地与Chatbot交互。

## 示例说明

以下是一个Chatbot的示例，说明如何创建一个聊天会话：

```python
from chatbot import Chatbot

# 创建一个Chatbot对象
chatbot = Chatbot(api_key="YOUR_API_KEY")

# 发起一个聊天会话
while True:
    # 获取用户输入
    user_input = input(">> ")

    # 使用Chatbot进行回复
    response = chatbot.ask(user_input)

    # 输出Chatbot的回复
    print(f"Bot: {response}")
```

在上述示例中，我们使用Chatbot创建了一个聊天会话，并通过ask方法与用户进行交互。每次用户输入后，Chatbot会自动回复。

## 传参解释

下面是Chatbot可接受的传参及其含义：

- api_key：API密钥，从https://platform.openai.com/account/api-keys获取。
- engine：模型引擎名称，默认为gpt-3.5-turbo。
- proxy：代理服务器URL。
- max_tokens：每次请求最大生成tokens数量，默认为3000。
- temperature：用于控制生成文本的随机性的温度参数，默认为0.5。
- top_p：用于控制生成文本的多样性的top p参数，默认为1.0。
- reply_count：每次对话中Chatbot产生回复的数量，默认为1。
- system_prompt：Chatbot启动时系统提示语，默认为"You are ChatGPT, a large language model trained by OpenAI. Respond conversationally"。


ask_stream方法是用于流式地向Chatbot发起问题的方法，它会逐步返回生成的回复，并将这些回复添加到聊天记录中。以下是在示例代码中使用ask_stream方法的示例：

```python
from chatbot import Chatbot

# 创建一个Chatbot对象
chatbot = Chatbot(api_key="YOUR_API_KEY")

# 发起一个聊天会话
while True:
    # 获取用户输入
    user_input = input(">> ")

    # 使用Chatbot进行回复
    for response in chatbot.ask_stream(user_input):
        # 输出Chatbot的部分回复
        print(f"Bot: {response}")
```

在这个示例中，我们使用了for循环来遍历分段返回的多个回复，并将这些回复逐个输出。

## 结语

以上是Chatbot的介绍、示例说明以及传参解释。如果您在使用过程中有任何问题或建议，请随时联系我们。



# CursorBot 说明文档

`CursorBot` 类是一个 Python 模块，提供了与 [Cursor AI](https://aicursor.com/) API 进行交互的接口。这个模块可以根据用户输入生成或编辑代码片段。

## 安装
要使用 `CursorBot`，首先需要安装必要的依赖项：

```bash
pip install requests
```

然后，下载 `CursorBot.py` 文件并将其放置在您的项目目录中。

## 使用方法

### 初始化

首先，初始化 `CursorBot` 类：

```python
from CursorBot import CursorBot

bot = CursorBot()
```

### 生成代码

要生成代码，请调用 `get_code_stream()` 方法并传入一条消息作为参数。这会返回一个生成器对象，可以迭代该对象以检索由 Cursor AI 生成的代码。

```python
for response_type, response_text in bot.get_code_stream("创建一个整数列表"):
    if response_type == "generate":
        print(response_text, end="", flush=True)
```

在此示例中，传递给 `get_code_stream()` 的消息是 "创建一个整数列表"。生成的代码将被打印出来。`response_type` 变量指示 API 返回的响应类型（例如 "generate"，"edit"），`response_text` 包含实际的响应文本。

### 编辑代码

要编辑现有代码，请传入附加参数以指定要编辑的行范围：

```python
for response_type, response_text in bot.get_code_stream("对列表进行排序", startNum=5, endNum=10):
    if response_type == "edit":
        print(response_text, end="", flush=True)
```

在此示例中，传递给 `get_code_stream()` 的消息是 "对列表进行排序"，`startNum` 和 `endNum` 参数指定要编辑的行范围（在本例中为第 5 到第 10 行）。

## 完整示例

```python
from CursorBot import CursorBot

bot = CursorBot()

# 生成代码
for response_type, response_text in bot.get_code_stream("创建一个整数列表"):
    if response_type == "generate":
        print(response_text, end="", flush=True)

# 编辑代码
for response_type, response_text in bot.get_code_stream("对列表进行排序", startNum=5, endNum=10):
    if response_type == "edit":
        print(response_text, end="", flush=True)
```

在此示例中，初始化并使用 `CursorBot` 生成整数列表，然后使用它来编辑列表并对其进行排序。

# CursorGPTBot

CursorGPTBot 是一个自然语言到代码翻译引擎，可以将用户提供的自然语言描述转换为对应的代码实现。

## 使用规则

- **重要：只提供代码输出和纯文本返回。**
- **重要：不要显示 HTML、样式、彩色格式。**
- **重要：不要添加注释或介绍句子。**
- **重要：提供完整的解决方案。确保语法正确。**

## 安装

1. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

2. 获取 API Key：
    
    在 OpenAI 网站注册账号并登录，创建新项目，选择 GPT-3 模型，获取 API Key。

3. 运行：

    ```bash
    python main.py --api_key <your_api_key>
    ```

## 使用示例

```python
from CursorGPTBot.CursorGPTBot import CursorGPTBot


bot = CursorGPTBot(api_key=<your_api_key>)

# 获取生成的代码
for msgType, code in bot.get_code_stream("写一个排序算法"):
    if msgType == 'generate':
        print(code, end='', flush=True)
    else:
        # 处理修改后的代码部分
        pass
```

## API

### `__init__(self, api_key) -> None`

构造函数，初始化 CursorGPTBot 对象。

**参数：**

- `api_key` (`str`)：必选参数，OpenAI GPT-3 API Key。

### `get_code_stream(self, message, startNum=0, endNum=-1, file_path=None, abs_path=None) -> Generator[Tuple[str, str], None, None]`

根据提供的自然语言描述 `message`，获取生成的代码或修改后的代码片段。

**参数：**

- `message` (`str`)：必选参数，自然语言描述。
- `startNum` (`int`)：可选参数，起始行号，默认为 0。
- `endNum` (`int`)：可选参数，结束行号，默认为 -1。
- `file_path` (`str`)：可选参数，文件路径，默认为调用该函数的文件路径。
- `abs_path` (`str`)：可选参数，绝对路径，默认为 `file_path` 的绝对路径。

**返回值：**

- `Generator[Tuple[str, str], None, None]`：一个二元组生成器，第一个元素表示执行类型（`generate` 或 `edit`），第二个元素为代码字符串。