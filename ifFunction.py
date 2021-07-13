# num = 100
#
# if num >= 100:
#     print(num, "is GREATER than 100.")
# else:
#     print(num, "is LESS than 100.")

num = int(input("Enter Marks: "))

if 100 >= num >= 0:
    if num >= 75:
        print("Grade: A")
    elif num >= 65:
        print("Grade: B")
    elif num >= 50:
        print("Grade: C")
    elif num >= 35:
        print("Grade: S")
    else:
        print("FAIL!")
else:
    print("INVALID MARKS!")
