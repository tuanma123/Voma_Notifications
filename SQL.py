import _sqlite3

connection = _sqlite3.connect("Master.db")
connection.text_factory = str
cursor = connection.cursor()

def create_table ():
    cursor.execute("CREATE TABLE IF NOT EXISTS users(firstName TEXT, lastName TEXT, email TEXT, phoneNumber INT, "
                   "permissions INT)")

def insert_table_entry(first_name, last_name, email, phone_number, permissions):
    cursor.execute("INSERT INTO users (firstName, lastName, email, phoneNumber, permissions) VALUES (?, ?, ?, ?, ?)",
                   (first_name, last_name, email, phone_number, permissions))
    connection.commit()

def print_database_by_row():
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print (str(row))

def close_sql():
    cursor.close()
    connection.close()


insert_table_entry("Tuan", "Maa", "Tjsdfs", 234234, "1010101")
print_database_by_row()
close_sql()