from langchain.schema import BaseOutputParser
class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")
message = CommaSeparatedListOutputParser().parse("hi, bye")
print(message)