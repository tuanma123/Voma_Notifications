from User import User

file_name = "Master.csv"


def create_file(users):
    file = open(file_name,"w")
    header = "First Name,Last Name,Email,Phone Number,Permissions(Email,Phone,Announcement,Rent,Admin)"
    file.write(header + '\n')
    for user in users:
        file.write(user.first_name + ',' + user.last_name + ',' + user.email + ',' + user.phone_number + ','
                   + user.permissions + "\n")
    file.close()
    return file


def get_user_list():
    user_list = []

    with open(file_name, "r") as lines:
        counter = 0
        for line in lines:
            if counter > 0:
                user_list.append(create_user_from_string(line))
            counter += 1
    return user_list


def create_user_from_string(string):
    fields = string.split(",")
    user = User(fields[0], fields[1], fields[2], fields[3], fields[4])
    return user