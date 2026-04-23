from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
# 常用上面这种
# from langchain.chat_models import ChatOpenAI
from numpy.f2py.crackfortran import verbose
import my_API
chat_model = my_API.chat_model
# 这是from_messages 消息队列{系统信息、用户信息、AI信息}
# system_template = "你是一个讲笑话小能手，我给你一个关键词，你根据这个关键词，给出一个笑话"
# system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
# human_template = "关键词：{keyword}"
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# prompt = ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])
# model = chat_model
# output_parser = StrOutputParser()
# chain = prompt | model | output_parser
# output_message = chain.invoke({"keyword":"北京"})
# print(output_message)

# 这是from_template 单一字符串模板
template = "你是一个讲笑话小能手，我给你一个关键词，你根据这个关键词，给出一个笑话：{keyword}"
prompt = ChatPromptTemplate.from_template(template)
model = chat_model
output_parser = StrOutputParser()
chain = prompt | model | output_parser
output_message = (chain | output_parser).invoke({"keyword":"北京"})# 查看某一个组件输出
print(output_message)