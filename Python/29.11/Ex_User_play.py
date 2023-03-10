user = ['gal@hackeru.co.il', 'gal123456', False ]

def info():
    for i in user:
        print(i)

def login():
    username = input('Enter email / username')
    password = input('Enter password')
    if username == user[0] and password == user[1]:
        user[2] = True
        print("המשתמש התחבר בהצלחה")
        return True
    else:
        print('שם המשתמש או הסיסמה אינם נכונים')
        return False

def logout():
    username = input('Enter email / username')
    password = input('Enter password')
    if username == user[0] and password == user[1]:
        user[2] = False
        print("המשתמש התנתק בהצלחה")
        return True
    else:
        print('שם המשתמש או הסיסמה אינם נכונים')
        return False

def change_password():
    username = input('Enter email / username')
    password = input('Enter password')
    if username == user[0] and password == user[1]:
        new_password_1 = input("Enter new password")
        new_password_2 = input("Enter new re-password")
        if new_password_1 == new_password_2:
            print("הסיסמה עודכנה בהצלחה")
            user[1] = new_password_1
            return True
        else:
            print('הסיסמאות אינן תואמות')
            return False
    else:
        print('שם המשתמש או הסיסמה אינם נכונים')
        return False

def get_options():
    op = input('****** Enter Option ****** \n '
               '1 - login | 2 - logout | 3 - change_password | 100 - print \n >>>')
    if op == '1':
        login()
    elif op == '2':
        logout()
    elif op == '3':
        change_password()
    elif op == '100':
        info()
    get_options()


get_options()