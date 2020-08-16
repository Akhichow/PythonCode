print("The prime numbers between 1 and 100 are:")
for Number in range(1,101):     #gives a range from 1 to 100 & 101 is not included
    count = 0
    if Number > 1:  #Omit 1 as 1 is neither prime nor composite
        for i in range(2,Number):   #Total range is to divide from 2 till that number - can also be number//2 + 1
            if (Number%i) == 0:
                count=count+1       #Increment count if it's divisible

    if (count == 0 and Number!=1):      #Check count & number greater than 1
        print(Number,end=" ")           #Print Number with a gap
