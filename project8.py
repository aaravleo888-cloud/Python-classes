# GROCERY COST COMPARISON TOOL
print("=== GROCERY COST COMPARISON TOOL ===")

# ---------- PART 1: what did this week's shop cost per person? ----------
rice_price = 16
milk_price = 8
fruit_price = 4
number_of_baskets = 2
family_members = 5
# parentheses make the addition happen before * and /
cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members
print("Cost per person:", cost_per_person)

# ---------- PART 2: can the items be shared equally? ----------
total_items = int(input("Enter the total number of grocery items: "))
people = int(input("Enter the number of people sharing them (1 or more): "))
if total_items % people == 0:
    print(total_items, "items divide equally among", people, "people.")
else:
    print(total_items, "items do not divide equally among", people, "people -", total_items % people, "left over.")

# ---------- PART 3: compare with three stores ----------
weekly_average = 72.5          # given: the corrected weekly average
store_a_average = 70
store_b_average = 75
store_c_average = 80
if weekly_average < store_a_average and weekly_average < store_b_average and weekly_average < store_c_average:
    verdict = "cheaper than all three stores"
elif weekly_average > store_a_average and weekly_average > store_b_average and weekly_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"

print("\n=== SUMMARY ===")
print("Cost per person this week:", cost_per_person)
print("Weekly average           :", weekly_average)
print("Verdict                  :", verdict)
