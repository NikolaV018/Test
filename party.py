from typing import List

def main():
    party_list: List[str] = ["Fernadno", "Ana", "David", "Elisa", "Mario", "Breno"]
    did_breno_try: bool = False
    underage_counter: int = 0
    money_made: int = 0
    women: int = 0
    men: int = 0
    tall_ppl: int = 0
    while True:
        party_req(party_list, underage_counter, did_breno_try, money_made, women, men, tall_ppl)
        more_people: str = input("Are there more people(y/n)? ")
        if not more_people == "y":
            break

    people: int = women + men

    print("Did Breno try to enter:", did_breno_try)
    print("How many underaged people tried to enter:", underage_counter)
    print("How much money was made:", money_made)
    print("There were this many women trying to enter:", women)
    print("There were this many men trying to enter:", men)
    print("There were this many people trying to enter:", people)
    print("There were this many people over 2 meters trying to enter:", tall_ppl)



def party_req(party_list: List[str], underage_counter: int, did_breno_try: bool, money_made: int, women: int, men: int, tall_ppl: int) -> bool:
    while True:
        name: str = input("Input your username: ")
        if name.lower() == "breno":
            did_breno_try = True
            return False
        if not validate_name(name):
            continue
        if not name_in_list(name,party_list):
            return False
        break

    while True:
        age: str = input("Input your age: ")
        if not validete_age(age):
            continue
        if int(age) < 18:
            underage_counter += 1
            print("You must be over 18 to enter the party!")
            return False
        break

    while True:
        gender: str = input("Enter your gender(m/f): ")
        if not validate_gender(gender):
            continue
        if gender.lower() == "m":
            print("You have to pay 25 dollars!")
            money_made += 25
            men += 1
        if gender.lower() == "f":
            women += 1
        break

    while True:
        height: str = input("Enter your height: ")
        if not validate_height(height):
            continue
        if gender == "m" and float(height) < 1.6:
            return False
        if float(height) > 2:
            tall_ppl += 1
        break
    return True


def name_in_list(name: str, name_list: List[str]) -> bool:
    if not name in name_list:
        print("Your name is not on the list!")
        return False
    return True


def validate_name(name: str) -> bool:
        if name.isnumeric():
            print("Your input needs to be a string!")
            return False
        if len(name) < 3 or len(name) > 10:
            print("Your input is not the right size!")
            return False
        for i in name:
            if i.isnumeric():
                print("Your input cannot have any numbers!")
                return False
        return True

def validete_age(age: str) -> bool:
    if not age.isnumeric():
        print("Your input is not a number!")
        return False
    if int(age) < 0 or int(age) > 119:
        print("Not a valid age number!")
        return False
    return True

def validate_gender(gender: str) -> bool:
    if gender.lower() == "f":
        print("This person is a female!")
        return True
    if gender.lower() == "m":
        print("This person is a male!")
        return True
    return False

def validate_height(height: str) -> bool:
    if not is_float(height):
        print("Your input needs to be a float number!")
        return False
    if float(height) < 1.5 or float(height) > 5:
        return False
    return True


def is_float(string: str) -> bool:
    split_string = string.split('.')
    if len(split_string) > 2:
        return False
    if len(split_string) < 2:
        return False
    if not split_string[0].isnumeric():
        return False
    if not split_string[1].isnumeric():
        return False
    return True
















main()