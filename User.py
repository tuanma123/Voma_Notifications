class User():

    def __init__(self,first_name, last_name, email, phone_number, permissions, rent):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.permissions = permissions
        self.rent = rent

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

    def update_rent(self):
        for x in range(0, len(self.permissions)):
            if self.permissions[x] == 0:
                self.permissions[x] = 1
                return True
        return False

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' \
               + self.phone_number + ' ' + self.permissions
