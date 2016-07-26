while True:

    import math
    import os

    """Calculator!"""


    #pi
    pi = (math. pi)

    #add, mult, divide, minus

    print ("1: Addition:")
    def add(x, y):
        return (x + y)

    print ("2: Subtraction:")
    def sub(x, y):
        return (x - y)

    print ("3: Multiplication:")
    def mult(x, y):
        return (x * y)

    print ("4: Division:")
    def div(x, y):
        return (x / y)

    #sohcahtoa radian calculations

    print ("5: Sine:")
    def sin(o):
        return (math. sin(o))

    print ("6: Cosine:")
    def cos(o):
        return (math. cos(0))

    print ("7: Tangent:")
    def tan(o):
        return (math. tan(o))

    # sqrt/powers

    print  ("8: Square Root:")
    def sqrt(x):
        return (math. sqrt(x))
    print ("9: Powers:")
    def sqr(x):
        return (x ** 2)

    #userinput

    opt = (input("Choose which operation you would like(enter a number 1 - 9)."))

    #userresponse

    if opt == '1':
        f1 = float(input("First number here: "))
        f2 = float(input("Second number here: "))
        print(add(f1, f2))

    elif opt == '2':
        f47754 = float(input("First number here: "))
        f24354 = float(input("Second number here: "))
        print(sub(f47754, f24354))

    elif opt == '3':
        f1877 = float(input("First number here: "))
        f2345 = float(input("Second number here: "))
        print(mult(f1877, f2345))

    elif opt == '4':
        fl45343 = float(input("First number here: "))
        f24354353 = float(input("Second number here: "))
        print(div(fl45343, f24354353))

    elif opt == '5':
        f3 = float(input("Enter a radian measure: "))
        print(math.sin(f3))

    elif opt == '6':
        f97 = float(input("Enter a radian measure: "))
        print(math. cos(f97))

    elif opt == '7':
        f464 = float(input("Enter a radian measure: "))
        print(math. tan(464))

    elif opt == '8':
        f098 = float(input("Enter a number that you wish to find the sqare root of: "))
        print(math. sqrt(f098))

    elif opt == '9':
        f043 = float(input("Enter the coefficient: "))
        f076 = float(input("Enter the exponent: "))
        print (f043 ** f076)

    elif opt == 'r':
        break
        






         

