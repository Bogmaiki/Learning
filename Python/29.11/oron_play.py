print('********* oron play *************')
import random

def play_oron():
    num1 = random.randrange(1, 11)
    num2 = random.randrange(1, 11)
    user_sum = int(input(str(num1) + " + " +  str(num2) + " = "))
    if(user_sum == num1+num2):
        print('10 points')
        return True
    else:
        print('TRY again')
        return False

play_oron()