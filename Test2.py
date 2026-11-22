import random

secret_number = random.randint(1, 50)

print("Hello, lets play a game called guess the number!")
guess = int(input("Guess: "))
distance = abs(guess - secret_number)
lives = 5

while guess != secret_number and lives > 0:
    if guess < 1 or guess > 50:
        print("Invalid guess! Please enter a number between 1 and 50.")
        guess = int(input("Guess: "))
        distance = abs(guess - secret_number)
        continue
        
    if distance < 5:
        print("Super hot!")
    elif distance >= 5 and distance < 15:
        print("Warm")
    elif distance >= 15 and distance < 25:
        print("Cold!")
    else:
        print("Freezing cold")
    
    lives = lives - 1
    print(f"You have {lives} lives left!")
    
    if lives > 0:
        guess = int(input("Guess: "))
        distance = abs(guess - secret_number)

if guess == secret_number:
    print("You Win!")
else:
    print("No more lives left!")
    print(f"The number was {secret_number}")



