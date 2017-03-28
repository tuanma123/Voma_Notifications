from flask import Flask, request
from twilio import twiml
import Commands
import sys
import Database
app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    print("Before\n")
    print Database.print_database_by_row()
    number = request.form['From']
    body = request.form['Body']
    resp = twiml.Response()
    reply = Commands.get_reply_phone(body,number)
    resp.message(reply)

    print("After\n")
    print Database.print_database_by_row()
    print(str(number))
    return str(resp)



if __name__ == '__main__':
    app.run()
