import random

flag = True
while flag:
    num = input("type a number for an upper bound: ")
    if num.isdigit():
        print("lets play")
        num = int(num)
        flag = False
    else:
        print("invalid input try again")

secret = random.randint(1,num)

guess = None
count = 0

while guess != secret:

    guess = input("guess the number please (between 1 and " + str(num) +":")

    if guess.isdigit():
        guess = int(guess)
        if guess == secret:
            print("you're right!")
        else:
            print("wrong number please try again")
            count+=1
            print("you have tried " + str(count) + " times. Out of 5 guesses you have " + str(5-count) + " tries left")
            if count== 5:
                break
    else:
        print("invalid input try again")