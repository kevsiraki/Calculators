while True:

    import math

    print("Below, input a list of numbers you would like to calculate the mean of (use one space for each integer or float): ")

    lst = list(map(float,input().split())) #the list(input #s)

    def average(lst): return sum(lst) * 1.0 / len(lst)
    avg = average(lst) #the function for mean/average

    print ("The mean/average of your input is: ")
    print (avg)

    variance = list(map(lambda x: (x - avg)**2, lst))
    qst1 = input("Would you like to calculate the variance of your input?")
    #variance(in list form and also the average of the list)
    print (qst1)

    if qst1 == ("yes"):
        print (variance)
    print ("The avergage of the variance is:")
    print (average(variance))
    print ("Just for future reference, variance is calculated by having each number in a list subtracted by the mean, then squaring each difference, and then finally, finding the average of the squared numbers.")

    standard_deviation = (math.sqrt(average(variance)))
     #standard deviation
    qst2 =  (input("Would you like to find out the standard deviation of your list?"))
    print (qst2)

    if qst2 == ("yes"):
        print ("The standard deviation is: ")
        print (standard_deviation)

    elif qst2 == ("no"):
        print ("If you would like to find it by yourself, the formula for standard deviation is variance squared.")#standard deviation formula, in short, is variance^2

    elif qst2 == 'r':
        break
