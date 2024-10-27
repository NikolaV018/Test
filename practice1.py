from re import search
from typing import List


def main():
    nbr_list: List[int] = [4, 12, 3, 5, 12, 3, 45, 2, 12, 5 ,6 , 8]
    number: str = input("Input a number: ")
    if pos_ver(number):
        num = int(number)
    positions: List[int] = position(num,nbr_list)
    print(f"Your number is this position/positions = {positions}!")
    counter: int = count_repeat(num, nbr_list)
    print(f"Your number repeats {counter} this many times!")
    sum_of_numbers: int = sum(nbr_list)
    print(f"Sum of all repeating numbers on the list is {sum_of_numbers}")

def position(number: int,nbr_list: List[int]) -> List[int]:
    positions: List[int] = []
    for i, item in enumerate(nbr_list):
        if number == item:
            positions.append(i)
    return positions

def count_repeat(number: int, nbr_list: List[int]) -> int:
    counter = 0
    for i in nbr_list:
        if number == i:
            counter += 1
    return counter

def sum(nbr_list: List[int]) -> int:
    sum_numbers: int = 0
    for i in nbr_list:
        counter = 0
        for n in nbr_list:
            if i == n:
                counter += 1
            if counter > 1:
                sum_numbers += i
                break
    return sum_numbers

def pos_ver(search: str) -> bool:
    while True:
        if not search.isnumeric():
            print("You need to input a number!")
            return False
        if 0 > int(search) or int(search) > 100:
            print("Your number needs to be between 0 and 100!")
            return False
        return True






main()