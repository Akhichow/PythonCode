option = "-"
while True:
    if option in range(1, 7):
        print("You have chosen option {}".format(option))
        print("What else would you like to do? ")
        option = int(input())
    else:
        option = int(input("Please choose one of the options below :\n"
                           "1. Go Swimming\n"
                           "2. Go Trekking\n"
                           "3. Go Shopping\n"
                           "4. Go Skiing\n"
                           "5. Go Clubbing\n"
                           "6. Stay Home\n"
                           "0. Exit\n"))
    if option == 0:
        print("You are quitting")
        break
