# Python program to illustrate the use

# Of 'is' identify operator

"""
x = 5

if (type(x) is int):

    print("True")

else:

    print("False")

x = 5.5



if (type(x) is not float):

    print("True")
else:

    print("False")


x = 20

y = 20

if (x is y):
    print("x & y SAME identity")


y = 30
if (x is not y):

    print("x & y have different identity")
"""

"""a = 10 #  binary number of 10: 1010

b = -10 # binary number of -10: -1010


# Prints bitwise right shift operators

print("a >> 1 =", a >> 1)

print("b >> 1=", b >> 1)


a = 5 # binary number of 5: 0101

b = -10


# Print bitwise left shift operators

print("a << 1=", a << 1)

print("b << 1=", b << 1)"""

print("Enter marks Obatined in 5 Subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive= int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot/5)

validRange = range(0,101)

if avg not in validRange:
    print("Invalid Input")

elif avg in range(91,101):
    print("Your Grade is A1")
elif avg in range(81,91):
    print("Your Grade is A2")
elif avg in range(71, 81):
    print("Your Grade is B1")
elif avg in range(61,71):
    print("Your Grade is B2")
elif avg in range(51, 61):
    print("Your Grade is C1")
elif avg in range(41,51):
    print("Your Grade is C2")
elif avg in range(33,41):
    print("Your Grade is D")
elif avg in range(21,33):
    print("Your Grade is E1")
elif avg in range(0,21):
    print("Your Grade is E2")