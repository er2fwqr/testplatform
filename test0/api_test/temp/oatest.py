import requests

# 定义 API 的地址
API_URL = "https://api.openai.com/v1/engines/davinci/completions"

# 定义一个用于获取用户输入的函数
def get_input():
    # 获取用户输入
    user_input = input("请输入你想对我说的话：")
    # 返回用户输入
    return user_input

# 定义一个用于响应用户输入的函数
def respond(user_input):
    # 构造请求数据
    data = {
        "prompt": user_input,
        "max_tokens": 256,
        "temperature": 0.5,
    }
    # 发送请求
    response = requests.post(API_URL, json=data)
    # 解析响应
    response_data = response.json()
    # 获取响应文本
    response_text = response_data["choices"][0]["text"]
    # 返回响应文本
    return response_text

# 循环进行对话
while True:
    # 获取用户输入
    user_input = get_input()
    print(respond(user_input))