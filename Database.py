from User import User


class Database():
    # Constructor given a user_list.
    def __init__(self, user_list):
        self.user_list = user_list
        self.file_name = "Master.csv"

    # Create's a CSV file that stores user information
    def create_file(self):
        file = open(self.file_name, "w")
        header = "First Name,Last Name,Email,Phone Number,Permissions(Email-Phone-Announcement-Rent-Admin)"
        file.write(header + '\n')
        for user in self.user_list:
            file.write(user.first_name + ',' + user.last_name + ',' + user.email + ',' + user.phone_number + ','
                       + user.permissions + "\n")
        file.close()
        return file

    # Add a user to the database.
    def add_user(self, user):
        self.user_list.append(user)
        file = open(self.file_name, "w")
        file.write(user.first_name + ',' + user.last_name + ',' + user.email + ',' + user.phone_number + ','
                   + user.permissions + "\n")
        file.close()

    # Remove a user by removing them from list and overwriting file.
    def remove_user(self, user):
        self.user_list.remove(user)
        self.create_file()

    # Access the current list of users.
    def get_user_list(self):
        return self.user_list

    # Print the current list of users.
    def print_user_list(self):
        for user in self.user_list:
            print(str(user))

    # Returns a list of user emails
    def get_email_list(self):
        email_list = []
        for user in self.user_list:
            if user.permissions[0] == '1':
                email_list.append(user.email)
        return email_list

    # Returns a list of phone numbers of users
    def get_msg_list(self):
        msg_list = []
        for user in self.user_list:
            if user.permissions[1] == '1':
                msg_list.append(user.phone_number)
        return msg_list

    # Returns a String representing the data in a readable format.
    def __str__(self):
        header = "First Name        Last Name       Email                       Phone Number        " \
                 "Permissions(Email-Phone-Announcement-Rent-Admin)\n"
        output = header + '_' * (len(header) - 1) +'\n'
        for user in self.user_list:
            output += '{:<18}{:<16}{:<28}{:<20}{:<5}'.format(user.first_name,user.last_name,user.email
                                                            ,user.phone_number,user.permissions)
            output += '\n'
        return output