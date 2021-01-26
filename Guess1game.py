import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO:Remove after testing
guess = 0   #initialize
print("Please guess a number between 1 and {}: ".format(highest))


# if guess == answer:
#     print("You got it in the first try")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     else:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You got it correctly in the second try")
#     else:
#         print("You've exhausted your attempts")

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("See you later alligator")
        break
    if guess == answer:
        print("Guessed it correctly")
        break
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
    # guess = int(input())
    # if guess == answer:
    #     print("You got it correctly now")
    #     break


