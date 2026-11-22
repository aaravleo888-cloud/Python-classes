#  ========================================
#   Power calculator
# =========================================

print("Power calculator")

base = int(input("A Base value: "))
expo = int(input("The Power of number: "))
total = 1

for i in range(1, expo + 1):
    total = total * base
    print(f"Step {i}  total = {total}")

print(f"Final answer for your equation: {total} ")



