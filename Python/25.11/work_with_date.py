import datetime

time = datetime.datetime.now()
print(time)
print(type(time))
print(time.day)
print(time.month)
print(time.year)
print(time.hour)
print(time.minute)
print(time.second)
print(time.strftime("%A"))

birthday = datetime.datetime(1983, 10, 19)
print("birthday >>", birthday.strftime("%A"))
