from models.user import User
from typing import Dict



database_users = Dict[str,User]

database_users = {

    "Samuel": User(**{
                     "name":"Eduard",
                     "passw":"M123",
                     "email":"samuE@gmail.com",
                     "username":"Sam"  })
                        ,

   "Johny": User(**{
                    "name":"Eduardo",
                    "passw":"E123",
                    "email":"johnye@gmail.com",
                    "username":"Johnyq"  }), 
                                                                        

}

def get_user(username:str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def set_user(user_in_db: User):
    database_users[user_in_db.username] = user_in_db
    return user_in_db 