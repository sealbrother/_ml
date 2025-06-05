import ollama

response = ollama.chat(model='llama3:8b', messages=[
    {'role': 'user', 'content': '請幫我解釋牛頓第三運動定律'},
])

output = response['message']['content']

print("="*50)
print("回應內容：")
print(output)

# model='llama3:8b'：你可以使用你本地下載的模型名稱，如 llama3:8b 或 llama3.2:3b

# messages=[]：這是標準的 chat history 格式，可以模擬 ChatGPT 對話。

# response['message']['content']：取得回應內容。