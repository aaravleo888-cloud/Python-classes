# Holiday planner 
print("===== WELCOME TO HOLIDAY PLANNER =====")
print("Step 1: Pick your trip ")
print("1 - Beach")
print(" 2 - Camping")
choice = int(input("Choose (1,2)"))

if choice == 1:
    print("Step 2: Pick your hotel/motel location")
    print("1 - near beach")
    print("2 - near lighthouse")
    choice = int(input("Choose (1,2)"))
    if choice == 1:
        print("Best plan:")
        print("Surfing, chilling or swimming")
    else:
        print("Best plan:")
        print("Explore lighthouse, rest at hotel/motel or check out a food place")
elif choice == 2:
    print("Step 2: Pick your camping location ")
    print("1 - near lake")
    print("2 - near river")
    choice = int(input("Choose (1,2)"))
    if choice == 1:
        print("Best plan:")
        print("Explore lake, stay in camp, make campfire")
    else:
        print("Best plan:")
        print("Explore river, stay in camp, go boating")
else:
    print("Invalid choice, pick 1 or 2 only")

print()
print(" Enjoy your trip ")
print()

