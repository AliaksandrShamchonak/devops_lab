y = int(input("Input a leap year between 1900 and 10^5: "))
if y in range(1900, 10**5):
    if y % 4:
        print("false")
    elif y % 100 == 0 and y % 400:
        print("false")
    else:
        print("true")
else:
    print("false")
