import dotenv, os, requests, json

dotenv.load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv('Test_Access_Token')

options = {
    "1": "broadcast",
    "2": "push",
    "3": "reply"
}

class Line_API:
    def __init__(self):
        self.base_url = "https://api.line.me/v2/bot/message/"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
        }
        self.data_set = {"messages": []}
    
    def reply_message(self, reply_token=None, text=None):
        self.data_set["replyToken"] = reply_token
        self.data_set["messages"].append({
            "type": "text",
            "text": text
        })
        response = requests.post(self.base_url+"reply", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def broadcast_message(self, text=None):
        self.data_set["messages"].append({
            "type": "text",
            "text": text
        })
        response = requests.post(self.base_url+"broadcast", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def push_message(self, text=None, user_id=None):
        self.data_set["to"] = user_id
        self.data_set["messages"].append({
            "type": "text",
            "text": text
        })
        response = requests.post(self.base_url+"push", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def get_quota(self):
        response = requests.get(self.base_url+"quota", headers=self.headers)
        self.resulter(response)
        print(response.json())
    
    def get_broadcast_count(self, date=None):
        self.date = date
        response = requests.get(self.base_url+f"delivery/broadcast?date={self.date}", headers=self.headers)
        self.resulter(response)
        print(response.json())

    def resulter(self, response):
        if response.status_code != 200:
            print("Error broadcasting message: ", response.status_code, response.text)
        else:
            print("\nMessage broadcasted successfully!\n")
    



def run():
    while True:
        line = Line_API()
        select = input(
            """
                Enter your selection:
                    1. broadcast(This will send message to all users)
                    2. push(Send message to specific user)
                    3. reply(Send message by a replyToken)
                    4. get quota
                    5. get broacast count
                    Q. Quit\n
            """
        )
        if select == "1":
            inputer = input("Enter your message: ")
            line.broadcast_message(inputer)
        elif select == "2":
            inputer = input("Enter your message: ")
            user_id = input("Enter user id: ")
            line.push_message(inputer, user_id)
        elif select == "3":
            inputer = input("Enter your message: ")
            reply_token = input("Enter reply token: ")
            line.reply_message(reply_token, inputer)
        elif select == "4":
            line.get_quota()
        elif select == "5":
            date = input("Enter date(YYYYMMDD): ")
            line.get_broadcast_count(date)
        elif select == "q" or select == "Q":
            print("Good bye")
            break
        else:
            print("Wrong selection!")
            pass



if __name__ == "__main__":
    run()