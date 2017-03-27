import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import TwilioRestClient
import Database
import Timing

particles = (",", ".", "?", "!")


def parse_message(file_path):
    text = open(file_path, "r")
    line_list = []
    for line in text:
        line = line.replace("findStr", "replaceStr")
        line_list.append(line.strip().split(" "))
    return line_list


def construct_token_string(file_string_list, token_map):
    result = ""
    # Go through the entire list of sentences
    for string_list in file_string_list:
        # If the list is empty, its just a line feed
        if string_list == ['']:
            result += '\n'
        else:
            # Go through every word of a non empty sentence
            for string in string_list:
                # If the word is a token as defined by the opening bracket.
                if string[0] == "[":
                    # Remove all grammer particles such as periods and commas.
                    string_remove = string
                    for particle in particles:
                        string_remove = string_remove.replace(particle, "")
                    # Check if the token is in the token map.
                    # If so replace it with the matching value from the token map.
                    if string_remove in token_map:
                        string = string.replace(string_remove, token_map[string_remove])
                        result += string + " "
                    else:
                        result += string + " "
                else:
                    result += string + " "
    return result


class Spammer():
    def __init__(self, twilio_sid, twilio_auth_token, twilio_number, email_address, email_password):
        self.twilio_sid = twilio_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_number = twilio_number
        self.email_address = email_address
        self.email_password = email_password

    def send_text(self, to_number, body):
        """

        :param to_number:
        :param body:
        :return:
        """
        client = TwilioRestClient(self.twilio_sid, self.twilio_auth_token)
        client.messages.create(to=to_number, from_=self.twilio_number, body=body)

    def send_email(self, to_address, subject, body):
        """

        :param to_address:
        :param subject:
        :param body:
        :return:
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_address
        msg['Subject'] = subject

        body = body
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email_address, self.email_password)
        text = msg.as_string()
        server.sendmail(self.email_address, to_address, text)
        server.quit()
        print("message sent")


    def send_email_to_users(self, subject, body):
        user_list = Database.get_user_list()
        for user in user_list:
            pass

    def send_text_to_users(self, body):
        for phone_number in Database.get_phone_list():
            self.send_text(phone_number, body)

    def send_messages_based_on_preferences(self, user, message):
        if user.permissions[0] == "1":
            self.send_email(user.email,"AUTOMATED MESSAGE", message)
        if user.permissions[1] == "1":
            self.send_text(user.phone_number, message)



    def automated_messages(self, hour, minute):
        """

        :param time_of_day: Based on 24 hour clock. Tuple: ( Hour , Minute )
        :return:
        """
        now = datetime.datetime.now()
        days_left = Timing.days_left_in_month(now.month, now.day, Timing.is_leap_year(now.year))
        if days_left == 6 and now.hour == hour and now.minute == minute:
            print("Entered here")
            for user in Database.get_user_list():
                if user.rent[now.month-1] == "0":
                    #NOTE: IMPLEMENT AN UTILITY VARIABLE
                    message_map = {"[NAME]" : user.first_name + " " + user.last_name, "[PRICE]" : "$600.00"}
                    message_list = parse_message("/media/tonyvo/VO/Programming/git-repos/Voma_Notifications/Messages/7DayWarning.mv")
                    message = construct_token_string(message_list, message_map)
                    self.send_messages_based_on_preferences(user, message)
        elif days_left == 4 and now.hour == hour and now.minute == minute:
            for user in Database.get_user_list():
                if user.rent[now.month-1] == 0:
                    #NOTE: IMPLEMENT AN UTILITY VARIABLE
                    message_map = {"[NAME]" : user.first_name + user.last_name, "[PRICE]" : "$600.00"}
                    message_list = parse_message("/media/tonyvo/VO/Programming/git-repos/Voma_Notifications/Messages/4DayWarning.mv")
                    message = construct_token_string(message_list, message_map)
                    self.send_messages_based_on_preferences(user, message)

        elif days_left == 2 and now.hour== hour and now.minute == minute:
            for user in Database.get_user_list():
                if user.rent[now.month-1] == 0:
                    #NOTE: IMPLEMENT AN UTILITY VARIABLE
                    message_map = {"[NAME]" : user.first_name + user.last_name, "[PRICE]" : "$600.00"}
                    message_list = parse_message("/media/tonyvo/VO/Programming/git-repos/Voma_Notifications/Messages/2DayWarning.mv")
                    message = construct_token_string(message_list, message_map)
                    self.send_messages_based_on_preferences(user, message)
