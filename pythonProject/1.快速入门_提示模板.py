from langchain.prompts.chat import (
    ChatPromptTemplate,# 定义用户输入
    SystemMessagePromptTemplate,# 定义AI角色
    HumanMessagePromptTemplate,# 多个消息组成对话
)
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo",  # 支持的模型
    api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",
    base_url="https://api.chatanywhere.tech/v1"
)
template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

message = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="translate thisI love programming."#尽量用同一种语言
)
chat_response = chat_model.predict_messages(message,temperature = 0.7)
print(chat_response.content)