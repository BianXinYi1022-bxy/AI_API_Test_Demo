# AI_API_Test_Demo

本项目是一个基于大模型的 API 自动化测试轻量级 Demo。

## 🎯 项目背景
为了提升接口测试的效率，探索“AI + 测试”的落地场景，本项目通过调用大模型 API，自动根据接口文档生成测试用例，并结合 Pytest 框架实现接口自动化执行与断言校验。

## 🛠️ 技术栈
*   编程语言：Python
*   测试框架：Pytest
*   接口请求：Requests
*   AI 能力：调用大模型 API (Prompt 工程)

## 🚀 核心功能
1.  **AI 辅助用例生成**：通过 Prompt 约束，让大模型输出标准的 JSON 格式测试用例。
2.  **数据驱动测试 (DDT)**：读取生成的 JSON 文件，通过 Pytest 的参数化装饰器批量执行用例。
3.  **结果断言**：验证 HTTP 状态码及接口返回字段。

## 💻 运行方式
1. 安装依赖：`pip install pytest requests openai`
2. 运行脚本：`pytest test_api.py -s`
