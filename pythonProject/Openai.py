# 这种是直接远程调用OpenAI模型
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-CnM7il5KwotDSAfBPFbMDDBQFG6rWP6FJRw50IXv7d7bXkXE",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.org/v1"
)

history = [
    {"role": "system", "content": "你是一个乐于助人的助手"}
]

while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
        temperature=0.7
    )

    ai_response = response.choices[0].message.content
    print("AI:", ai_response)
    history.append({"role": "assistant", "content": ai_response})