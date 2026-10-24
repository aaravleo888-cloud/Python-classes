# Ask how much homework you have
homework = int(input("How many minutes of homework do you have?:"))

# Decide if it is a long or a short session of homework
if homework > 60:
    print("It is a long session today.")
    print("Good luck!")
else:
    print("It is a short session today.")
    print("Finish quick!, You got this!")

# Ask if there is a test coming up
test = input("Is there a test coming up(yes/no)?:")

# Tell to do extra studys if there is a test coming up and if there is no test, there get free time 
if test == "yes":
    print("You should practice more.")
else:
    print("Alright, you don't need to study but your choice")

free_time = ("yes" or "no")

if test == "yes":
    free_time = "no"
else:
    free_time = "yes"
print("Alright, your day is planned\n")
print("------Day planner------")
print("Homework minutes", homework)
print("Test coming?", test)
print("Free time?", free_time)
print("Good luck!")
print("-----------------------")