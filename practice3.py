from typing import List, Tuple


def main():
    lists: List[List[int]] = [[2, 5, 15], [1, 4, 6], [10, 11, 12]]

    for i in lists[0]:
        highest1= 0
        if i > highest1:
            highest1 = i

    print(f"Highest number in the first position of the list is {highest1}!")

    for i in lists[1]:
        highest2= 0
        if i > highest2:
            highest2 = i

    print(f"Highest number in the first position of the list is {highest2}!")

    for i in lists[2]:
        highest3= 0
        if i > highest3:
            highest3 = i

    print(f"Highest number in the first position of the list is {highest3}!")

    if highest1 > highest2 and highest1 > highest3:
        print(f"The highest number in all of the lists is from the list in the first position and is number {highest1}!!")

    elif highest2 > highest1 and highest2 > highest3:
        print(f"The highest number in all of the lists is from the list in the second position and is number {highest2}!!")

    else:
        print(f"The highest number in all of the lists is from the list in the third position and is number {highest3}!!")



def main2():
    lists: List[List[int]] = [[2, 5, 15], [1, 4, 6], [10, 11, 12],[14, 11, 20],[10, -100, -12],[45, 11, 2]]
    high_number, high_list = highest_number_of_list_of_lists(lists)
    print(f"The highest number on all of the lists is {high_number} and it is on the list number {high_list + 1}!")


def highest_number_of_list_of_lists(lists: List[List[int]]) -> Tuple[int, int]:
    high_number: List[int] = []
    for list in lists:
        highest = 0
        for i in list:
            if i > highest:
                highest = i
        high_number.append(highest)
    biggest_number: int = 0
    for i in high_number:
        if i > biggest_number:
            biggest_number = i
    big_number_list: int = high_number.index(biggest_number)
    return biggest_number, big_number_list


main2()















