import imaplib
from UserInfo import email_username, email_password
import poplib
import re
import email
from Spammer import Spammer
from email.parser import Parser
from UserInfo import twilio_phone_number, twilio_auth_token, twilio_id, email_username, email_password
spam = Spammer(twilio_id, twilio_auth_token, twilio_phone_number, email_username, email_password)
import Timing
import Database

def parse_information(info):
    char_list = list(info)
    parsed_info = ""
    open = False
    for char in char_list:
        if open and not char == ">":
            parsed_info += char
        if char == "<":
            open = True
    return parsed_info


parser = Parser()
mailbox = poplib.POP3_SSL('pop.googlemail.com', '995')
mailbox.user(email_username)
mailbox.pass_(email_password)

def test(string):
    print(string)
    print Database.print_database_by_row()

while(True):
    try:
        raw_email = b"\n".join(mailbox.retr(1)[1])
        parsed_email = parser.parsestr(raw_email)
        from_user = parse_information(parsed_email.get('From'))
        valid_user = Database.verify_email(from_user)
        subject = parsed_email.get('Subject').lower()
        is_admin = Database.is_admin(from_user)
        body = ""
        print valid_user
        if parsed_email.is_multipart():
            for payload in parsed_email.get_payload():
                body += str(payload.get_payload()) + " "
        else:
            body += str(parsed_email.get_payload()) + " "

        message_tokens = body.split(" ")
        if "paid" in subject and valid_user:
            test("Before")
            Database.update_rent(email)
            msg = "Thank you for your payment"
            test("After")

        elif "announce" in subject and valid_user and Database.announcement_enabled(from_user):
            test("Before")
            preference_list = Database.get_preference_list()
            email_list = preference_list[0]
            phone_list = preference_list[1]
            name = Database.get_name(from_user)
            msg = ' '.join(body[1:])
            for email in email_list:
                spam.send_email(email, "Voma Notifications: Announcement by " + name, msg)
            for number in phone_list:
                spam.send_text(number, msg)

            msg = "Announcement has been sent"
            test("After")

        elif "emailon" in subject and valid_user:
            test("Before")

            Database.update_email_preference(from_user, 1)
            msg = "Email Notifications has been turned on"
            test("After")

        elif "emailoff" in subject and valid_user:
            test("Before")
            Database.update_email_preference(from_user, 0)
            msg = "Email Notifications has been turned off"
            test("After")

        elif "phoneon" in subject and valid_user:
            test("Before")
            Database.update_phone_preference(from_user, 1)
            msg = "Phone Notifications has been turned on"
            test("After")

        elif "phoneoff" in subject and valid_user:
            test("Before")
            Database.update_phone_preference(from_user, 0)
            msg = "Phone Notifications has been turned off"
            test("After")

        elif "report" in subject and valid_user and is_admin:
            test("Before")
            msg = Database.get_rent_report()
            test("After")

        elif "history" in subject and valid_user:
            test("Before")
            msg =  Database.get_rent_history(from_user)
            test("After")

        spam.send_email(from_user, "Voma_Notifications Command: " + subject, msg)


    except:
        print("No new messages")

    Timing.sleep_every_x_seconds(30)