# Python conditions (if/elif/else)
acquired_marks = 88
pass_marks = 33

if acquired_marks >= pass_marks:
    print("Passed")

else:
    print("Failed")


# Check even / odd number
num = 5

if num % 2 == 0:
    print(num, "is an even number!")

else:
    print(num, "is an odd number!")


# Define Grade by Marks
if acquired_marks >= 80:
    print("A+")

elif acquired_marks >= 70:
    print("A")

elif acquired_marks >= 60:
    print("A-")

elif acquired_marks >= 50:
    print("B")

elif acquired_marks >= 40:
    print("C")

elif acquired_marks >= 33:
    print("D")

else:
    print("F")
