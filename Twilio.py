from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

@app.route('/TuansPage/overwatchaccount', methods=['POST'])
def sms():
    number = request.form['From']
    body = request.form['Body']
    resp = twiml.Response()
    resp.message(body)
    if body == "add 4" :
        list.append(4)

    print(list)

    return str(resp)

@app.route('/TuansPages')
def tuans_page():
    return "Tuan is super cool"

if __name__ == '__main__':
    app.run()
