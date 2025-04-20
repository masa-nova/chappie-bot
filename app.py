from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "チャッピーBot 動いてるよ！"

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.json['events'][0]
    user_message = event['message']['text']
    print(f"User said: {user_message}")  # テスト用ログ

    return {
        "replyToken": event['replyToken'],
        "messages": [{
            "type": "text",
            "text": "やっほー🌟チャッピーだよ！"  # 固定返信
        }]
    }

if __name__ == "__main__":
    app.run()