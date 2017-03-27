from UserInfo import twilio_phone_number, twilio_auth_token, twilio_id, email_username, email_password


import Database
from User import User
from Spammer import Spammer
import Timing

def main():
    spam = Spammer(twilio_id, twilio_auth_token, twilio_phone_number, email_username, email_password)
    print("This application is based on a 24-hour clock.")
    hour = int(raw_input("Please enter the hour you would like to send messages."))
    minute = int(raw_input("Please enter the minute you would like to send messages"))
    while True :
        #if(count == 0) :
        spam.automated_messages(hour,minute)
        Timing.sleep_every_x_seconds(15)

        #count+=1

main()
