import json

def handler(req, res):
    # 这是一个测试接口，用来确认 Vercel 能跑通 Python
    return res.status(200).json({"message": "Hello from Python! Robot is alive!"})
