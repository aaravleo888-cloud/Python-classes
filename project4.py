print("Hello, time to calculate the teams points")

# Assign the teams a score
team1 = 120
team2 = 145
team3 = 170
team4 = 195
team5 = 220

# Find the average of 5 teams points
total = team1 + team2 + team3 + team4 + team5
average = total/5

print("Sum of the points of the 5 teams:", total)
print("Average of the 5 teams:", average)

# Calculate the task earnings
earnings_per_tasks = 25
earnings = total * earnings_per_tasks
print("Total earnings   :", earnings)

# Divide the tasks
total_tasks = total // 30
leftovers   = total % 30

print("tasks fully completed :", total_tasks)
print("tasks not fully completed:", leftovers)

# Compare last class with today
last_class = 780

print("Better than last class?", total > last_class)
print("Same as last class?", total == last_class)
print("Neater than last class?", total>= last_class)

# A bonus task adds 30 points
total += 30 
print("After bonus task", total,"points")

# A Half completed task subtracts 15 point
total -= 15
print("After Incomplete task", total,"points")

# Total task completed 
total //= 30
print("Total tasks completed:", total)