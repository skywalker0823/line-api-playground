import dotenv, os, requests, json

dotenv.load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv('Test_Access_Token')

class Line_API:
    def __init__(self):
        self.base_url = "https://api.line.me/v2/bot/message/"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
        }
        self.data_set = {"messages": []}
    
    def reply_message(self, reply_token=None, text=None):
        text = input("Enter your message: ")
        reply_token = input("Enter reply token: ")
        self.data_set["replyToken"] = reply_token
        self.data_set["messages"].append({
            "type": "text",
            "text": text
        })
        response = requests.post(self.base_url+"reply", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def broadcast_message(self, text=None):
        text = input("Enter your message: ")
        self.data_set["messages"].append({
            "type": "text",
            "text": text
        })
        response = requests.post(self.base_url+"broadcast", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def broadcast_image(self, image_url=None):
        image_url = input("Enter image url: ")
        self.data_set["messages"].append({
            "type": "image",
            "originalContentUrl": image_url,
            "previewImageUrl": image_url
        })
        response = requests.post(self.base_url+"broadcast", data=json.dumps(self.data_set), headers=self.headers)
        self.resulter(response)

    def push_message(self, text=None, user_id=None):
        text = input("Enter your message: ")
        user_id = input("Enter user id: ")
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
        date = input("Enter date(YYYYMMDD): ")
        response = requests.get(self.base_url+f"delivery/broadcast?date={date}", headers=self.headers)
        self.resulter(response)
        print(response.json())
    
    def flex_message(self):
        data = None
        with open("flex_example.json", "r") as file:
            data = json.load(file)
        data_set = {
            "messages": [
                {
                    "type": "flex",
                    "altText": "Flex Message",
                    "contents": data
                }
            ]
        }
        response = requests.post(self.base_url+"broadcast", headers=self.headers, data=json.dumps(data_set))
        self.resulter(response)
        print(response.json())

    def resulter(self, response):
        if response.status_code != 200:
            print("Error broadcasting message: ", response.status_code, response.text)
        else:
            print("\nMessage broadcasted successfully! = w =\n")
            
    
    def quit(self):
        print("Good bye")
        exit(0)

    def invalid(self):
        print("Invalid selection")
        pass

def run():
    line = Line_API()
    options = {
        "1": line.broadcast_message,
        "2": line.push_message,
        "3": line.reply_message,
        "4": line.get_quota,
        "5": line.get_broadcast_count,
        "6": line.broadcast_image,
        "7": line.flex_message,
        "q": line.quit,
        "Q": line.quit
    }
    while True:
        select = input(
            """
                Enter your selection:
                    1. broadcast(This will send message to all users)
                    2. push(Send message to specific user)
                    3. reply(Send message by a replyToken)
                    4. get quota
                    5. get broacast count
                    6. broadcast image
                    7. flex message
                    Q/q. Quit\n
            """
        )
        options.get(select, line.invalid)()

if __name__ == "__main__":
    run()