import data
users = data.all_users
print(user)


def login(username,password):
    print("into func login")
    for user in users:
        # print(user)
        if user["username"] == username and user["password"] == password:
            user["isLogin"] = True
            return user
    return False








userLogin = login('dani', 'dani123')
print(userLogin)

userLogin['points'] = 100
print(userLogin)

