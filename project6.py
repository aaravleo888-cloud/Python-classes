# Welcome to the pool!!!!!!
print("Before you enter we have to do a few checks")
age = int(input("How old are you?"))
swim = input("Can you swim? (yes/no)")
adult = input("Do you have an adult with you? (yes/no)")

if age < 4 and age <= 17 and adult != "yes":
    print("You need an adult")
elif age < 4 and age <= 17 and adult == "yes":
    print("Nice but make sure to stay with your adult")
elif age > 18 and not swim == "yes":
    print("Make sure to stay at the shallow end")
elif age > 18 and swim == "yes":
    print("You are all good to go!")
elif age > 80 and swim == "yes":
    print("You are all good to go but please be careful")
elif age > 80 and swim != "no":
    print("Sorry but I don't recommend entering")
elif age > 150:
    print("Type the correct age ")
else:
    print("Type the corrct info")

print("Enjoy!")