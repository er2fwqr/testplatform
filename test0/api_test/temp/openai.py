import openai

# 设置 OpenAI 的 API Key
openai.api_key = "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"

# 询问您想聊什么
question = input("What would you like to talk about? ")

# 调用 OpenAI 的 API，获取回答
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question,
    max_tokens=1024,
    n=1,
    temperature=0.5,
)

# 输出回答
print(response["choices"][0]["text"])