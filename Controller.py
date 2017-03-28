from UserInfo import twilio_phone_number, twilio_auth_token, twilio_id, email_username, email_password
from Spammer import Spammer
from User import User
import Timing
import Database
Database.clear_table()
Database.create_table()
tuan = User("Tuan", "Ma", "tuanma123@gmail.com", "+14259705093", "11111", "100000000000")
tony = User("Tony", "Vo", "tonyt.vo22@gmail.com", "+12065793508", "11101", "100000000000")
Database.insert_user_object(tuan)
Database.insert_user_object(tony)
Database.print_database_by_row()
Database.connection.commit()
print(Database.get_name("tonyt.vo22@gmail.com"))

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
