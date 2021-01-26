import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: REMOVE AFTER TESTING
print("Please guess a number between 1 and {}:".format(highest))
guess = 0  # initialise to any number that doesn't equal to an answer
tries = 0

while guess != answer and tries < 10:
    tries = tries + 1
    guess = int(input())
    if guess == 0:
        print("You have quit")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        else:  # guess must be greater than answer
            print("Please guess higher")

if tries == 10:
    print("Sorry you have exhausted {} tries".format(tries))

# guess = int(input())
# if guess == answer:
#     print("Well done")
# else:
#     print("Sorry, please try again")

# if guess == answer:
#     print("Well done bitch")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     else: # guess must be greater than answer
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Sorry, please try again")
