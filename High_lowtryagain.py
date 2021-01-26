low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to begin")

guess = 1
guesses = 0
while low != high:
    # print("\t Guessing in the range of {} and {}".format(low,high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Is your guess higher or lower?"
                     " Please press h for higher, l for lower and c for correct"
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("You had guessed {}. I got it in {} guesses".format(guess, guesses))
        break
    else:
        print("Please enter h,l or c ONLY")
        guesses -= 1

    guesses += 1
else:
    print("You had guessed {}. I got it in {} guesses".format(low, guesses))
