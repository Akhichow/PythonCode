name = input("What is your name? ")
age = int(input("What is your age, {0}? ".format(name)))
# print("Hi Akhil, you are {0} years old".format(age))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry yoda, you will die now")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
