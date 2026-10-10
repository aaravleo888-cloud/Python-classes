# =========================================================
# Farm harvest calculator
# =========================================================

# --- Assignment operator (=) ---
# store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 34
field3 = 200
field4 = 57
field5 = 99

# --- Arithmetic operators (+, -, *, /)---
# Calculate total and average harvest
total    = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest     :", total, "kg")
print("Average per field :", average, "kg")

# Price per kg is 15 rupees - calculate total earnings 
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings    : Rs.", earnings)

# --- Floor division (//) and modulus (%) ---
# Pack the harvest into bags of 25 kg each
bags     = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain     :", leftover, "kg")

# --- Comparision operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

# --- Assignment operators (+=, -=) ---
# A bonus field adds 30 kgs to the total
total += 30
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed  :", bags)