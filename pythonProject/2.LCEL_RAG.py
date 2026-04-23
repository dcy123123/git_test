# 基于向量检索的问答系统
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai.embeddings import OpenAIEmbeddings
import my_API

chat_model = my_API.chat_model
texts = ["harrison worked at kensho", "bears like to eat honey"]
embeddings = OpenAIEmbeddings(
    openai_api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",  # 替换为你的真实 API Key
    openai_api_base="https://api.chatanywhere.tech/v1"  # 可选，默认是 OpenAI 官方端点
)
vectorstore = DocArrayInMemorySearch.from_texts(
    texts = texts,# 存储的文本
    embedding=embeddings, # 将文本转成向量
)
retriever = vectorstore.as_retriever() # 将向量数据库转层检索器
# 提示词模板
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = chat_model
output_parser = StrOutputParser()
setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}# 直接传递问题
)
chain =  setup_and_retrieval |prompt | model | output_parser
output_message = chain.invoke("where dose bear like eat?")
print(output_message)