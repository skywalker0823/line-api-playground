# Fast API with Line Messaging API and Webhook
from fastapi import FastAPI, Request, Response, status
import dotenv, os

dotenv.load_dotenv()

app = FastAPI()

CHANNEL_ACCESS_TOKEN = os.getenv('Test_Access_Token')

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Webhook 環節
# 1. 設定好ngrok 或是地址後 在Line Developer 以下用來測試是否成功
@app.post("/webhook")
async def webhook(request: Request, response: Response):
    data = await request.json()
    print(data)
    return "OK"