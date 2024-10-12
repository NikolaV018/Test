from typing import List


def main():
    print('Game explanation!\nIn this game one player input a word and another tries to guess the letters in the word, if he guesses correct,\nthey appear on the line, the player can make up to 7 mistakes, if he misses one more time, the game is over!\n')
    game()


def game():
    counter: int = 0
    words_used: List[str] = []
    while True:
        counter +=1
        mistake: int = 0
        guess_words: List[str] = []
        while True:
            solution_word: str = input("Type the solution word for the hangman game: ").lower()
            if not validate_word(solution_word):
                continue
            words_used.append(solution_word)
            break
        for i in range(20):
            print("")
        guess: List[str] = []
        for i in solution_word:
            guess.append("_")
        while True:
            print_as_string(guess)
            letter: str = input("\nType a letter to check: ").lower()
            if not validate_letter(letter):
                continue
            if not letter in solution_word:
                if letter in guess:
                    print("You have already used this letter, try again!")
                    continue
                if not letter in guess:
                    if not letter in guess_words:
                        guess_words.append(letter)
                        mistake += 1
                        hangman_dude(mistake)
                print("You have made this many mistakes:", mistake)
                print("You used this letters:", guess_words)
                if mistake == 8:
                    print("You have lost!!!!!")
                    again: str = input("Do you want to play again(Y/N)? ").lower()
                    if again == "n":
                        return False
                continue
            if letter in solution_word:
                check_letter(solution_word, letter, guess)
                if not "_" in guess:
                    end = "".join(guess)
                    print("You have guessed the right word, the word is:", end)
                    again2: str = input("Do you want to play again(Y/N)? ").lower()
                    if again2 == "n":
                        return False

                    break
                continue
        print("You have played this many games:", counter)
        print("Words used so far were:", words_used)




def validate_word(word: str) -> bool:
    if len(word) < 2 or len(word) > 15:
        print("Your input is not the right size!")
        return False
    for i in word:
        if i.isnumeric():
            print("Your input cannot have any numbers!")
            return False
    return True

def validate_letter(letter: str) -> bool:
    if len(letter) > 1:
        print("Your input can only be a single letter!")
        return False
    for i in letter:
        if i.isnumeric():
            print("Your input cannot have any numbers!")
            return False
    return True

def check_letter(word: str, letter: str, solution: List[str]) -> List[str]:
    for i, char in enumerate(word):
        if char == letter:
            solution[i] = letter

    return solution
def print_as_string(solution: List[str]) -> None:
    for i in solution:
        print(i + " ", end= "")



def hangman_dude(mistakes: int) -> None:
    if mistakes == 1:
        print("    |\n    |")
    if mistakes == 2:
        print(" ____\n     |\n     |\n     |\n     |")
    if mistakes == 3:
        print(" ____\n     |\n  0  |\n     |\n     |")
    if mistakes == 4:
        print(" ____\n     |\n 0   |\n |   |\n     |")
    if mistakes == 5:
        print(" ____\n     |\n  0  |\n  |  |\n   \\ |")
    if mistakes == 5:
        print(" ____\n    |\n 0  |\n |  |\n /\\ |")
    if mistakes == 6:
        print(" ____\n     |\n  0  |\n  |\\ |\n  /\\ |")
    if mistakes == 7:
        print(" ____\n     |\n  0  |\n /|\\ |\n  /\\ |")
    if mistakes == 8:
        print(" ____\n  |  |\n  0  |\n /|\\ |\n  /\\ |")



















main()