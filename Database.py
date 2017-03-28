import _sqlite3
from User import User

connection = _sqlite3.connect("Master.db")
connection.text_factory = str
cursor = connection.cursor()


def create_table ():
    """ Creates a table named users

    :return: Void.
    """
    cursor.execute("CREATE TABLE IF NOT EXISTS users(firstName TEXT, lastName TEXT, email TEXT, phoneNumber TEXT, "
                   "permissions TEXT, rent TEXT)")


# Determine if given information is a type of phone number or email address
def determine_phone_or_email(string) :
    if ".com" in string or ".edu" in string:
        return "email"
    else:
        return "phoneNumber"


# Inserting Users_______________________________________________________________________________________________________
def insert_user(first_name, last_name, email, phone_number, permissions, rent):
    """ Insert a new user into the database based on parameters.

    Permissions field is a binary number that is interpreted to determine execution of other programs.

    :param first_name: First name of the new user.
    :param last_name: Last name of the new user.
    :param permissions: The permissions settings for the new user.
    :param email: Email of the new user.
    :param phone_number: Phone number of the new user.
    :return: Void.
    """
    cursor.execute("INSERT INTO users (firstName, lastName, email, phoneNumber, permissions, rent) VALUES "
                   "(?, ?, ?, ?, ?, ?)", (first_name, last_name, email, phone_number, permissions, rent))
    connection.commit()


def insert_user_object(user):
    """ Inserts a new user into the database based on a User object. Simply calls insert_user method using the parameter's
    fields.

    :param user: User object. The fields of this object are used to enter a new user into the system.
    :return: Void.
    """
    insert_user(user.first_name, user.last_name, user.email, user.phone_number, user.permissions, user.rent)


def insert_user_list(user_list):
    """ Inserts a whole list of users into the database. Iterates through the list of users and calls the insert user
    method.

    :param user_list: The list of users to insert.
    :return: Void.
    """
    for user in user_list:
        insert_user_object(user)


# Deleting Users________________________________________________________________________________________________________
def delete_user(first_name, last_name):
    """ Deletes all users who's first name and last name match the parameters.

    :param first_name: First name to the user to be deleted.
    :param last_name:  Last name of the user to be deleted.
    :return: Void.
    """
    cursor.execute("DELETE FROM users WHERE firstName=? AND lastName=?", (first_name, last_name))
    connection.commit()


def delete_user_object(user):
    """ Deletes all users based on a User object input. Calls the delete_user method using the object's fields.

    :param user: The user to be deleted.
    :return: Void.
    """
    delete_user(user.first_name, user.last_name)


# Verifying Users and Checking admin status_____________________________________________________________________________

def verify_phone_number(phone_number):
    """ Verify that  user is in the database based on phone number

    :param phone_number: The user's phone number
    :return: True or false depending if user is in the database or not.
    """
    cursor.execute("SELECT * FROM users WHERE phoneNumber=?", (phone_number,))
    result = cursor.fetchall()
    return len(result) > 0


def verify_email(email):
    """ Verify that  user is in the database based on email

        :param phone_number: The user's email address.
        :return: True or false depending if user is in the database or not.
        """

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    result = cursor.fetchall()
    return len(result) > 0


def is_admin(information):
    user = get_user(information)
    return user.permissions[4] == "1"


def announcement_enabled(information):
    user = get_user(information)
    return user.permissions[2] == "1"


def get_user(first_name, last_name):
    """
    Prints all users whose first and last name match the parameters.

    :param first_name: First name of the search query.
    :param last_name: Last name of the search query.
    :return: Void.
    """
    cursor.execute(
        "SELECT * FROM users WHERE firstName=? AND lastName=?", (first_name, last_name))
    for row in cursor.fetchall():
        print(str(row))


# Retrieving User Information___________________________________________________________________________________________

def get_user_list():
    """ Returns a list of all our users as User objects.

    :return: A list of our users.
    """
    user_list = []
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        user_list.append(User(row[0], row[1], row[2], row[3], row[4], row[5]))
    return user_list


def get_email_list():
    """ Gets a mailing list for ALL of our users.

    :return: A list of all our users' emails.
    """
    email_list = []
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        email_list.append(row[2])
    return get_user_list()


def get_user(information):
    location = determine_phone_or_email(information) + "=?"
    cursor.execute("SELECT * FROM users WHERE " + location, (information,))
    user_info = cursor.fetchone()
    if user_info:
        user = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5])
        return user


def get_rent_report():
    rent_list = []
    user_list = get_user_list()
    for user in user_list:
        rent_list.append(user.first_name + " " + user.last_name + ": " + user.rent)

    user_string = "\n"
    for string in rent_list:
        user_string += string + "\n"

    return user_string


def get_rent_history(information):
    user = get_user(information)
    return user.rent


def get_phone_list():
    """ Gets a  phone mailing list for ALL of our users.

    :return: A list of all our users's phone numbers.
    """
    phone_list = []
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        phone_list.append(row[3])
    return phone_list


def get_preference_list():
    """ Gets a list of all users preferable way of retrieving messages.
    [ [email list] , [phone_list] ]
    :return: Returns a 2D list where the first list contains the email list and second contains phone list
    """
    phone_list = []
    email_list = []
    user_list = get_user_list()
    for user in user_list:
        if user.permissions[0] == "1":
            email_list.append(user.email)
        if user.permissions[1] == "1":
            phone_list.append(user.phone_number)
    return [email_list, phone_list]


def get_name(information) :
    user = get_user(information)
    return user.first_name + " " + user.last_name

# Updating User Information_____________________________________________________________________________________________


# Update Users email given old and new email.
def update_email(old_email, new_email):
    cursor.execute("UPDATE users SET email=? WHERE email=?", (new_email, old_email))


# Update users phone number given old and new phone number
def update_phone_number(old_number, new_number):
    cursor.execute("UPDATE users SET phoneNumber=? WHERE phoneNumber=?", (new_number, old_number))
    connection.commit()


def update_user(old_user, new_user):
    """ Updates the data for a user.

    :param old_user: The old user information.
    :param new_user:  The new user information.
    :return: Void.
    """
    cursor.execute("UPDATE users  SET firstName=?, lastName=?, email=?, phoneNumber=?, permissions=?, rent=? WHERE firstName=? "
                   "AND lastName=?",(new_user.first_name, new_user.last_name, new_user.email, new_user.phone_number,
                                     new_user.permissions, new_user.rent, old_user.first_name, old_user.last_name))
    connection.commit()


def update_rent(information):
    """ Updates the persons rent by one given their email address.

    :param information: The user's email address.
    :return: Void
    """
    info_type = determine_phone_or_email(information)
    location = info_type + "=?"
    cursor.execute("SELECT * FROM users WHERE " + location, (information,))
    current_rent = cursor.fetchone()
    if current_rent:
        current_rent = current_rent[5]
        current_rent_list = list(current_rent)
        for x in current_rent_list :
            if x == "0":
                pos_x = current_rent.index(x)
                current_rent_list[pos_x] = "1"
                break
        new_rent = ''.join(current_rent_list)
        cursor.execute("UPDATE users SET rent=? WHERE rent=? AND " + location, (new_rent, current_rent,information))
        connection.commit()


#  Updates a users permissions and turns on email notifications.
def update_email_preference(information, number):
    info_type = determine_phone_or_email(information)
    location = info_type + "=?"
    cursor.execute("SELECT * FROM users WHERE " + location, (information,))
    check = cursor.fetchone()
    if check:
        permissions = check[4]
        indexing = list(permissions)
        indexing[0] = str(number)
        new_permissions = ''.join(indexing)
        cursor.execute("UPDATE users SET permissions=? WHERE permissions=? AND " + location,
                       (new_permissions, permissions, information))
        connection.commit()


# Updates a users permissions and turns on phone notifications.
def update_phone_preference(information, number):
    info_type = determine_phone_or_email(information)
    location = info_type + "=?"
    cursor.execute("SELECT * FROM users WHERE " + location, (information,))
    check = cursor.fetchone()
    if check:
        permissions = check[4]
        indexing = list(permissions)
        indexing[1] = str(number)
        new_permissions = ''.join(indexing)
        cursor.execute("UPDATE users SET permissions=? WHERE permissions=? AND " + location,
                       (new_permissions, permissions, information))
        connection.commit()


# Viewing the table_____________________________________________________________________________________________________
def print_database_by_row():
    """ Prints the entire database, verbatim, row by row.

    :return: Void.
    """
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print (str(row))


# Clearing and Closing the table________________________________________________________________________________________
def clear_table():
    cursor.execute("DELETE FROM users")
    connection.commit()


def close_sql():
    cursor.close()
    connection.close()
