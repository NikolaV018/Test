from typing import List, Dict


def main():
    menu: Dict[str, str]= {
        "hot dog": "150 dinars",
        "pizza": "650 dinars",
        "pao de queijo": "50 dinars",
    }
    while True:
        while True:
            do_you_want: str = input("Do you want to add a new item?(y/n) ").lower()
            if do_you_want == "y":
                break
            if do_you_want == "n":
                print(menu)
                break
        new_item = item()
        new_item_price = price_of_item()
        menu[new_item] = new_item_price + " dinars"
        print(menu)
        again: str = input("Do you want to add another item?(y/n) ")
        if again == "y":
            continue
        break

def item() -> str:
    while True:
        new_item: str = input("What item do you want to add to the menu? ").lower()
        if not item_val(new_item):
            continue
        break
    return new_item

def price_of_item() -> str:
    while True:
        new_item_price: str = input("What is the price of the new item? ")
        if not price_val(new_item_price):
            continue
        break
    return  new_item_price

def item_val(new_item: str) -> bool:
    if new_item.isnumeric():
        print("The item should not be a number!")
        return False
    return True

def price_val(new_item_price: str) -> bool:
    if not new_item_price.isnumeric():
        print("The price must be a number!")
        return False
    return True

main()