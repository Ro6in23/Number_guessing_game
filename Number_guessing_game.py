import random

# Function to calculate number of attempts
def calc_attempts(lvl):
    global attempts
    if lvl == "easy":
        attempts =10
    elif lvl == "hard":
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

logo = """
           _____                       _   _                                  _               
          / ____|                     | | | |                                | |              
         | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
         | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
         | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
          \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                         
"""

print(logo)
# Choosing random number between 1 and 100
print("Welcome to the Number Guessing Game!")
final_num = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
attempts = 0
level = input("Choose the difficulty level. Type 'easy' or 'hard': ").lower()
calc_attempts(level)
while attempts:
    guess = int(input("Make a guess: "))
    if guess == final_num:
        print(f"You got it! The answer was {guess}.")
        break
    elif guess > final_num:
        attempts-=1
        print(f"Too high.\nGuess again")
        print(f"You have {attempts} attempts remaining")
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
    else:
        attempts-=1
        print(f"Too low.\nGuess again")
        print(f"You have {attempts} attempts remaining")
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")






