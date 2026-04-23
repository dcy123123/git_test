from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo",  # 支持的模型
    api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",
    base_url="https://api.chatanywhere.tech/v1"
)
class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")
template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chain = LLMChain(
    llm=chat_model,
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser()
)
# chain = LLMChain(
#     llm=chat_model,
#     prompt=chat_prompt
# )
output_message = chain.run("places")
print(output_message)
