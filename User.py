class User():

    def __init__(self,first_name, last_name, email, phone_number, permissions):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.permissions = permissions

    def change_email(self, new_email):
        self.email = new_email

    def change_phone_number(self,new_phone_number):
        self.phone_number = new_phone_number

    def change_permission(self, new_permissions):
        self.permissions = new_permissions

    def change_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def is_admin(self):
        return self.permissions[4] == 1

    def can_send_announcements(self):
        return self.permissions[2] == 1

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.phone_number + ' ' + self.permissions