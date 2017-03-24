import Database
from User import User

tuan = User("Tuan", "Ma", "tuanma123@gmail.com", 4259705093, "11111","11111111")
tuan2 = User("Tuan", "Mama", "tuanma@cs.washington.edu", 4259705093, "11111", "111111")


Database.create_table()
Database.insert_user_object(tuan)
Database.insert_user("Sample","User","sample@gmail.com",4259005092,"10110","000000000")
Database.print_database_by_row()
print("#" * 50)
Database.update_user(tuan, tuan2)
Database.print_database_by_row()
print ("#"*50)
Database.delete_user("Sample", "User")
Database.print_database_by_row()
Database.clear_table()
