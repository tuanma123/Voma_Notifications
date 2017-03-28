from UserInfo import twilio_phone_number, twilio_auth_token, twilio_id, email_username, email_password
from Spammer import Spammer
import Database
legal_commands = {"paid", "annouce", "emailon", "emailoff", "phoneon", "phoneoff", "utility","history"}
legal_admin_commands = {"nuke","report","setutility"}
all_commands = legal_admin_commands | legal_commands
spam = Spammer(twilio_id, twilio_auth_token, twilio_phone_number, email_username, email_password)


def legal_command(reply):
    return reply.split(" ")[0] in all_commands


def get_reply_phone(message_received, phone_number):
    Database.print_database_by_row()
    message_tokens = message_received.split(" ")
    command = message_tokens[0]
    is_member = Database.verify_phone_number(phone_number)
    is_admin = Database.is_admin_phone(phone_number)
    msg = ""
    if "paid" in command.lower():
        Database.update_rent_by_phone(phone_number)
        msg = "Thank you for your payment"

    elif "announce" in command.lower() and is_member and Database.announcement_enabled_phone(phone_number):
        msg = "Announcement by " + str(Database.get_name_phone(phone_number)) + "\n" + \
              ' '.join(message_tokens[1:])
        preference_list = Database.get_preference_list()
        email_list = preference_list[0]
        phone_list = preference_list[1]
        for email in email_list:
            spam.send_email(email, "Announcement", msg)
        for number in phone_list:
            spam.send_text(number, msg)
        return "Announcement has been sent"

    elif "emailon" in command.lower() and is_member:
        Database.update_permissions_email(phone_number, 1)
        msg = "Email Notifications has been turned on"

    elif "emailoff" in command.lower() and is_member:
        Database.update_permissions_email(phone_number, 0)
        msg = "Email Notifications has been turned off"

    elif "phoneon" in command and is_member:
        Database.update_permissions_phone(phone_number, 1)
        msg = "Phone Notifications has been turned on"

    elif "phoneoff" in command and is_member:
        Database.update_permissions_phone(phone_number, 0)
        msg = "Phone Notifications has been turned off"

    elif "report" in command and is_member and is_admin:
        print("Data is: "+ str(Database.get_rent_report()))
        return Database.get_rent_report()

    elif "history" in command and is_member:
        return Database.get_rent_history(phone_number)
    return msg
