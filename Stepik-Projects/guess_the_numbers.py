from random import *

num_run = randint(1, 100)
num_user = int(input())
while num_user != num_run:
    if num_user > num_run:
        print("Too many, please try again")
    else:
        print("Too little, try again")
    num_user = int(input())
else:
    print("You guessed right, congratulations!")
