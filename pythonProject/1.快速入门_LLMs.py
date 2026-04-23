# 免费API限制使用deepseek-r1，deepseek-v3，gpt-3.5-turbo，gpt-4o-mini，gpt-4o和embeddings模型
from langchain_openai import OpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.prompts import PromptTemplate
import my_API
# 初始化 LLM（文本生成模型）  text-davinci-003不在免费调用模型中
llm = OpenAI(
    model="text-davinci-003",
    api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",
    base_url="https://api.chatanywhere.tech/v1"
)
# gpt-3.5-turbo只能通过ChatOpenAI调用
# 初始化 Chat Model（聊天模型）
chat_model = my_API.chat_model
# 使用 invoke 方法代替 predict  两者都是调用语言模型的方式，predict已过时
# chat_response = chat_model.invoke(text)
text = [
    SystemMessage("你是一位资深的大学指导教师"),
    HumanMessage("你觉得保研好还是考研好"),
    AIMessage("保研需要好成绩"),
    HumanMessage("详细说一说需要什么好成绩")
]
chat_response = chat_model.invoke(text,temperature = 0.7) # temperature控制输出随机度，一般0-1 常0.7
# 多行输出
if "\n" in chat_response.content:
    lines = chat_response.content.split("\n")
    for i, line in enumerate(filter(None, lines), 1):  # 过滤空行
        print(f"{line.strip()}")
else:
    print(chat_response.content)
