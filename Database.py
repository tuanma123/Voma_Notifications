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


def get_user(first_name, last_name):
    """
    Prints all users whose first and last name match the parameters.

    :param first_name: First name of the search query.
    :param last_name: Last name of the search query.
    :return: Void.
    """
    cursor.execute("SELECT * FROM users WHERE firstName=? AND lastName=?", (first_name, last_name))
    for row in cursor.fetchall():
        print(str(row))


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
    """ Gets a mailing list for all of our users.

    :return: A list of all our users' emails.
    """
    email_list = []
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        email_list.append(row[2])
    return get_user_list()


def get_phone_list():
    """ Gets a  phone mailing list for all of our users.

    :return: A list of all our users's phone numbers.
    """
    phone_list = []
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        phone_list.append(row[3])
    return phone_list


def clear_table():
    """ Clears the entire users table.

    :return: Void.
    """
    cursor.execute("DELETE FROM users")
    connection.commit()


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


def update_user(old_user, new_user):
    """ Updates the data for a user.

    :param old_user: The old user information.
    :param new_user:  The new user information.
    :return: Void.
    """
    #cursor.execute("SELECT * FROM users")
    cursor.execute("UPDATE users  SET firstName=?, lastName=?, email=?, phoneNumber=?, permissions=?, rent=? WHERE firstName=? "
                   "AND lastName=?",(new_user.first_name, new_user.last_name, new_user.email, new_user.phone_number,
                                     new_user.permissions, new_user.rent, old_user.first_name, old_user.last_name))
    connection.commit()

def verify_phone_number(phone_number):
    cursor.execute("SELECT * FROM users where phoneNumber=?", (phone_number))
    result = cursor.fetchall()
    return len(result) > 0


def verify_email(email):
    cursor.execute("SELECT * FROM users WHERE email=?", email)
    result = cursor.fetchall()
    return len(result) > 0


def is_admin(email="", phone_number=""):
    if not email == "":
        cursor.execute("SELECT * FROM users WHERE email=?", email)
        return cursor.fetchall()[0][2] == 1
    else:
        cursor.execute("SELECT * FROM users WHERE phoneNumber=?", (phone_number))
        return cursor.fetchall()[0][3] == 1


def print_database_by_row():
    """ Prints the entire database, verbatim, row by row.

    :return: Void.
    """
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print (str(row))


def close_sql():
    """

    :return:
    """
    cursor.close()
    connection.close()