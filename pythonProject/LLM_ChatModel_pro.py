# 需要启动ollama
# 这种格式是Langchain开发的通用模板
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool, AgentType, initialize_agent
from langchain_community.chat_models import ChatOllama  # 使用 Ollama 的接口

# 1. 初始化本地 Ollama 的 DeepSeek 模型
chat = ChatOllama(
    model="deepseek-r1:1.5b",  # 本地 Ollama 模型名称
    temperature=0.7 # 控制输出的随机性程度 ->0输出保守 ->高 输出丰富但可能不准确
)

# 2. 内存初始化
# 自动保存对话历史
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 3. 提示模板
# 三层结构：
# 指令系统：设定AI角色和回答规范
# 历史对话：动态插入记忆对话
# 用户输入：Input
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个物理学家助手，用中文回答且不超过30字"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 4. 工具设置
search = DuckDuckGoSearchRun()# 联网搜索工具
tools = [
    Tool(name="search", func=search.run, description="联网搜索最新信息")
]

# 5. 构建链
# |管道操作符 数据从左往右
chain = (
    prompt
    | chat.bind()#语言模型生成
    | {"output": StrOutputParser()}# 输出解析，包装成字典结构
)

# 6. 创建Agent
agent = initialize_agent(
    tools=tools,# 代理使用工具
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    llm=chat,# 指定聊天核心模型
    verbose=True,# 调试信息 类似深度思考的过程
    handle_parsing_errors=True# 当代理输出不符合预期格式时的处理
)

# 7. 格式化输出函数
def format_output(output):
    text = output['output']
    formatted_text = text.replace("，", "，\n").replace("。", "。\n")
    return formatted_text

# 测试
result = agent.invoke({"input": "解释量子力学"})
print(format_output(result))