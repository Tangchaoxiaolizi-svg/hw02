import requests
import json

# ===== 火山引擎配置 =====
url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
API_KEY = "8cc39034-d771-443f-977c-651f68885029"  # 你的API Key
model = "ep-20260313200444-q2fgq"  # 你的接入点ID
# ======================

def chat_with_deepseek(user_input):
    """调用DeepSeek API，返回回复内容"""
    
    # 设置请求头
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 设置请求数据
    data = {
        "model": model,  # ⚠️ 这里改成用上面定义的model变量
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        # 发送请求
        print(" 正在思考...", end="", flush=True)
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        # 解析返回结果
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return reply
        
    except requests.exceptions.Timeout:
        return "请求超时，请检查网络"
    except requests.exceptions.ConnectionError:
        return "网络连接失败，请检查网络"
    except Exception as e:
        return f"出错了：{str(e)}"

def main():
    """主程序"""
    print("=" * 50)
    print("🤖 DeepSeek 聊天机器人")
    print("=" * 50)
    print("💡 输入你想说的话，按回车发送")
    print("💡 输入 'exit' 或 'quit' 退出")
    print("-" * 50)
    
    while True:
        user_input = input("\n👤 你: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("👋 再见！")
            break
        
        reply = chat_with_deepseek(user_input)
        print(f"🤖 DeepSeek: {reply}")

if __name__ == "__main__":
    main()