#hangman games
import random

hangman = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|-
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |+
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
"""]
#function returns a random name
def choice_word():
    human_names = ["Karen", "Aram", "Sergey", "Gaspar", "Valod"]
    rand_human = random.choice(human_names)
    return rand_human

#function returns whether you won or lost 
def logic_game(list_board):
    print("Welcome to the Hangman game, guess the names of Armenian men")
    word = choice_word()
    len_word = "-" * len(word)
    wrong_answer = 11
    k = -1
    while "-" in len_word:
        guess = input('Enter a letter: ')
        word_re = ""
        for i in range(len(word)):
            if guess == word[i].lower():
                word_re += word[i]
            else:
                word_re += len_word[i]
        len_word= word_re
        print(len_word)
        if guess.lower() not in word.lower():
            wrong_answer -= 1
            k += 1
            print(list_board[k].strip())
            print("wrong answer,try to reason more correctly")
        elif "-" not in len_word:
            return "You win,the correct answer-",len_word
        if wrong_answer == 0:
            return "Game over,the correct answer-",word
print(logic_game(hangman))

