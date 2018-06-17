import requests
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    jsonContent = request.json
    telegramAPI = 'https://api.telegram.org/' + jsonContent['telegramToken']
    telegramApiRequest = requests.post(telegramAPI, json={
        'chat_id': jsonContent['chatId'],
        'text': jsonContent['text']
    })
    return '', telegramApiRequest.status_code

if __name__ == '__main__':
    print 'Start'
    app.run(host='0.0.0.0', port=5010)
