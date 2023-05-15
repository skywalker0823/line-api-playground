# Line API playground
希望能夠透過這個專案，可以更快速的了解 Line API 的使用方式。

## 設置
1. 申請 https://developers.line.biz/console/ 的帳號，你要建立一個 Channel後 取得 `Channel access token` 這裡不多說明，請參考 https://developers.line.biz/en/docs/messaging-api/getting-started/
2. git clone https://github.com/skywalker0823/line-api-playground.git && cd line-api-playground
3. cp .env.example .env
4. 修改 .env 的內容，填入你的 `Channel access token`
5. pip install -r requirements.txt

## main.py
測試回應 webhook 事件
1. uvicorn main:app --reload --port 5000
2. (Open another terminal)ngrok http 5000
3. 將 ngrok 給的連結填入 https://developers.line.biz/console/channel/{你的CHANNEL}/messaging-api 的 Webhook URL 並測試

## broadcast.py
測試message API的各項基本功能
1. python3 broadcast.py

