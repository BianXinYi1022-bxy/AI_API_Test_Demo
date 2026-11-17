import json
# 导入 openai 库以调用大模型 API
# 安装方式：pip install openai
from openai import OpenAI 

# 初始化客户端 (这里以兼容 OpenAI 格式的国内大模型为例，如 DeepSeek 或 阿里通义千问)
# 实际使用时需要替换为你自己的 API_KEY
client = OpenAI(
    api_key="your_api_key_here", 
    base_url="https://api.deepseek.com" # 示例 base_url
)

# 模拟一段接口文档输入（需求分析）
api_doc = """
接口地址：/api/login
请求方式：POST
请求参数：username (必填), password (必填)
成功返回：code=200, msg="success"
失败返回：code=400, msg="用户名或密码错误"
"""

# 核心：Prompt 工程。强制大模型输出标准的 JSON 格式，方便后续代码解析
prompt = f"""
请根据以下接口文档，生成3条测试用例（包含正常、异常情况）。
请严格以 JSON 数组格式输出，不要输出任何其他废话。
JSON 格式要求：
[
  {{"case_name": "用例名", "username": "账号", "password": "密码", "expected_code": 期望返回码}}
]

接口文档：
{api_doc}
"""

def generate_test_cases():
    print("正在调用大模型生成测试用例...")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # 获取 AI 生成的 JSON 字符串
    cases_text = response.choices[0].message.content
    print("AI 生成的用例：\n", cases_text)
    
    # 将用例保存到本地 JSON 文件，供 test_api.py 读取执行
    with open("test_cases.json", "w", encoding="utf-8") as f:
        f.write(cases_text)
    print("用例已保存至 test_cases.json")

if __name__ == "__main__":
    generate_test_cases()
