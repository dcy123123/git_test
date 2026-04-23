from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo",  # 支持的模型
    api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",
    base_url="https://api.chatanywhere.tech/v1",
    verbose = True
)