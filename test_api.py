import json
import pytest
import requests

# 1. 读取由大模型生成的测试用例 (数据驱动测试 DDT)
# 这里我们先手动模拟一个 json 数据，防止没有实际文件报错
MOCK_CASES = [
    {"case_name": "正常登录", "username": "admin", "password": "123456", "expected_code": 200},
    {"case_name": "密码错误", "username": "admin", "password": "wrong", "expected_code": 400}
]

def get_cases():
    try:
        with open("test_cases.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到本地JSON文件，使用 Mock 数据执行...")
        return MOCK_CASES

# 2. 使用 pytest 的参数化装饰器，将用例注入到测试函数中
@pytest.mark.parametrize("case", get_cases())
def test_login_api(case):
    print(f"\n正在执行用例: {case['case_name']}")
    
    # 这里为了演示，使用公共测试接口 httpbin.org 模拟 POST 请求
    # 实际业务中，这里应该替换为你们公司真实的登录接口 URL
    url = "https://httpbin.org/post" 
    
    payload = {
        "username": case["username"],
        "password": case["password"]
    }
    
    # 发送 HTTP 请求
    response = requests.post(url, json=payload)
    
    # 3. 结果断言与校验
    # 校验 HTTP 状态码是否为 200 (请求成功)
    assert response.status_code == 200
    
    # 如果要校验业务返回码 (比如 code=200 或 400)，可以解开下面这行注释
    # assert response.json()['json']['expected_code'] == case['expected_code'] 
    
    print(f"✅ 用例 [{case['case_name']}] 执行通过")

# 运行方式：在终端输入 pytest test_api.py -s
