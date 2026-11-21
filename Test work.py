import random
secret_number = random.randint(1,50)
lives = 5
guess = 0
distance = abs(secret_number - guess)

while lives > 0:
    guess = input("Guess!")
    distance = abs(secret_number - guess)
    if distance <= 10:
        print("Hot")
        lives -= 1
    elif distance > 10 and distance <= 20:
        print("Warm")
        lives -= 1
    elif distance > 20 and distance <= 30:
        print("Cold")
        lives -= 1
    else:
        print('ice cold')
        lives -= 1

    if guess == secret_number:
        print("You win!")

    if lives == 0:
        print("You lost!")
        print(f"The number was {secret_number}") 
