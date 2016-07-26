while True:
    x = (int(input("Enter a number: ")))
    y = (input("Convert to bin, hex, or oct?"))
    print(y)
    if y == ("bin"):
        print (bin(x))
    elif y== ("hex"):
        print (hex(x))
    elif y== ("oct"):
        print (oct(x))
    else:
        break
