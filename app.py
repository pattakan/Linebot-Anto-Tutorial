from flask import Flask, request
import antolib
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

line_bot_api = LineBotApi('644ed89ce4624ca42b092bdc97e0cc3f')
handler = WebhookHandler('m/7GjPv6Vh0Dsm55pefeamrwLcp3GIHIb3r8fYesY4ij0ZBSQ98Ao0llb4+hxQK9HorjP8yQHhXiMzFKcQ9NePdpfNPrOtNQ80soelANbDAIN7s+tJb2lWjeCOqDoOZ28ROq3wfIqI/4MbZGjbEr0QdB04t89/1O/w1cDnyilFU=')

app = Flask(__name__)

# username of anto.io account
user = 'pattakan'
# key of permission, generated on control panel anto.io
key = 'kZwWNRjizWPMXf35chBmbAb8yrNg258MILpM5BYw'
# your default thing.
thing = 'myDevice'

anto = antolib.Anto(user, key, thing)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text="Turn Off channel1"))
     if(message == 'channel1 on'):
        anto.pub('myChannel1', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On channel1"))
    elif(message == 'channel1 off'):
        anto.pub('myChannel1', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off channel1"))
    elif(message == 'channel2 on'):
        anto.pub('myChannel2', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On channel2"))
    elif(message == 'channel2 off'):
        anto.pub('myChannel2', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off channel2"))
    elif(message == 'channel3 on'):
        anto.pub('myChannel3', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On channel3"))
    elif(message == 'channel3 off'):
        anto.pub('myChannel3', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off channel3"))
    elif(message == 'channel4 on'):
        anto.pub('myChannel4', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On channel4"))
    elif(message == 'channel4 off'):
        anto.pub('myChannel4', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off channel4"))
if __name__ == "__main__":
    anto.mqtt.connect()
    app.run(debug=True)
