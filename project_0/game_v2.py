"""
Game "Guess the number" 
Computer makes and guesses numbers by itself
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guesses the number

    Args:
        number (int, optional): The made number. Defaults to 1.

    Returns:
        int: Attemptes amount
    """
    count = 0
    
    while True:
        count += 1
        # supposed number
        predict_number = np.random.randint(1,  101)
        # Exit from loop
        if number == predict_number:
            break
    
    return count

def score_game(random_predict) -> int:
    """Amount of attempts to guess in average for 1000 sets
    
    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Average attempts amount 
    """
    count_ls = []
    # fix the seed for reproduceability
    np.random.seed(1)
    # a list of guessed numbers
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses number in average of {score} attempts')

# Run
if __name__ == "__main__":
    score_game(random_predict)