import random
from typing import List


def main():
    options: List[str] = ["rock", "paper", "scissors"]
    while True:
        player: str = input("Input your option(r, p or s): ")
        computer: str = random.choice(options)
        if not input_valid(player):
            continue
        if player == "r":
            player = options[0]
        if player == "p":
            player = options[1]
        if player == "s":
            player = options[2]
        print(f"Computer picked: {computer}")
        rps_game(computer, player)
        again: str = input("Do you want to play again(yes or no)?")
        if again == "no":
            break



def rps_game(computer: str, player: str):
    if computer == player:
        print(f"The game is tied, both players picked the same option: {computer}!")
    if computer == "rock" and player == "paper":
        print(f"Player wins, you picked {player} and computer picked {computer}!")
    if computer == "scissors" and player == "rock":
        print(f"Player wins, you picked {player} and computer picked {computer}!")
    if computer == "rock" and player == "scissors":
        print(f"Computer wins, you picked {player} and computer picked {computer}!")
    if computer == "scissors" and player == "paper":
        print(f"Computer wins, you picked {player} and computer picked {computer}!")






def input_valid(player: str) -> bool:
    if player.isnumeric():
        print("Your input can't be a number, it needs to be one of the options in the bracket(r, p or s)! Pick again!")
        return False
    if player != "r" and player != "p" and player != "s":
        print("This is not one of the options! Pick again!")
        return False
    return True





main()