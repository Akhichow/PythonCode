name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# if age >= 18 and age < 30:
if 18 <= age <= 30:
    print("Welcome to the 18-30 party,{}".format(name))
elif age < 18:
    print("Please wait for {} years".format(18-age))
else:
    print("You missed it {} years ago".format(age-30))
