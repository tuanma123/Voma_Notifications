import Database
from User import User
from Spammer import Spammer
import Timing
import Twilio
import datetime

def main():
    spam = initial_setup()
    print("This application is based on a 24-hour clock.")
    hour = int(raw_input("Please enter the hour you would like to send messages."))
    minute = int(raw_input("Please enter the minute you would like to send messages"))
    while True :
        #if(count == 0) :
        spam.automated_messages(hour,minute)
        Timing.sleep_every_x_seconds(15)

        #count+=1


def initial_setup():
    email_username = raw_input('Please enter a valid Google email address.')
    email_password = raw_input("Please enter the corresponding Google email account password.")
    twilio_id = raw_input("Please enter a valid Twilio ID.")
    twilio_auth_token = raw_input("Please enter the corresponding Twilio authentication token.")
    twilio_phone_number = raw_input("Please enter the corressponding Twilio phone number.")

    email_username = "spamslamjamuw@gmail.com"
    email_password = "pleasehackme"
    twilio_id = "ACd2c7cb9040bb920dbb196efbd6af7df7"
    twilio_auth_token = "5efc50b214eb7a96361f046f0b4e9b8f"
    twilio_phone_number = "+12069224468"
    return Spammer(twilio_id, twilio_auth_token, twilio_phone_number, email_username, email_password)

main()