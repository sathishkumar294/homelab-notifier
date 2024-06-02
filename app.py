from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")

if BOT_TOKEN is "":
    exit()

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage" 

def notify_telegram(message):
    response = requests.post(telegram_url, json={
        "chat_id": BOT_CHAT_ID,
        "text": message
    })
    return response.status_code, response.text

@app.route("/notify", methods=["POST"])
def handle_request():
    data = request.json

    message = data.get("message")

    status_code, response_text = notify_telegram(message)

    return jsonify({
        "status_code": status_code,
        "response": response_text
    }), status_code

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
