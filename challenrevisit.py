# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:\n"
#               "1.Learn Python \n"
#               "2.Learn Java \n"
#               "3.Go Swimming \n"
#               "4.Have Dinner \n"
#               "5.Go to bed \n"
#               "0.Exit")
#     choice = input()

for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)