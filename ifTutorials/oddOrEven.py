num = int(input("Enter a Number: "))

printString = "{} is {} Number."

if (num % 2) == 0:
    print(printString.format(num, "Even"))
else:
    print(printString.format(num, "Odd"))
