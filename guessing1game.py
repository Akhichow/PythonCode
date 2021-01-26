answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done champ")
#     else:
#         print("You've exhausted all options")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done champ")
#     else:
#         print("You've exhausted all options")
# else:
#     print("Well done champ")

# if guess != answer:
#     if guess > answer:
#         print("Please guess lower")
#     else:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done champ")
#     else:
#         print("You've exhausted all options")
# else:
#     print("Well done champ")

if guess == answer:
    print("Well done champ")
else:
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done champ")
    else:
        print("You've exhausted all options")