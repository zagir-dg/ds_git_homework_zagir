"""
Game "Guess the number" 

"""

import numpy as np

# We are making a number
number = np.random.randint(1, 101)

# Number of guessing attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number has to be lower")
    elif predict_number < number:
        print("The number has to be higher")
    else:
        print(f"You've guessed the number! This number = {number}, {count} attempts were spent")
        # End of the game, exit from loop
        break