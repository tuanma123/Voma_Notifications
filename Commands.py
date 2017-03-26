import Database
legal_commands = {"paid", "annouce", "emailon", "emailoff", "phoneon", "phoneoff", "utility","history"}
legal_admin_commands = {"nuke","report","setutility"}
all_commands = legal_admin_commands | legal_commands


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
        Database.update_rent_phone(phone_number)
        msg = "Thank you for your payment"
    elif "announce" in command.lower():
        msg = "Announcement by " + str(Database.get_name_phone(phone_number)) + "\n" + \
              ' '.join(message_tokens[1:])
    elif "emailon" in command.lower():
        Database.update_permissions_email(phone_number)
        msg = "Messaging has been turned on"
    elif "phoneon" in command:
        Database.update_permissions_phone(phone_number)
    elif "history" in command:
        return None
    return msg


print(get_reply_phone("announce Hello world I am testing this new product", "12065793508"))
