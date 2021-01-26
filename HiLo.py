low = 1
high = 1000

print("Please think of a number between 1 and {}".format(high))
input("Press ENTER to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c is my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess Higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 greater than the guess
        high = guess - 1
    elif high_low == "c":
        # Guessed correctly
        print("I got it correct in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    guesses += 1
else:
    print("You have guessed the correct number {}".format(low))
    print("You got in {} guesses".format(guesses))
