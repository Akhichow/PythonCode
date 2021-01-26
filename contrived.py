numbers = [7, 42, 30, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # Reject the numbers
        print("The numbers are unacceptable")
        break
else:
    print("All values are acceptable")