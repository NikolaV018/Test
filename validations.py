def main():
    while True:
        age: str = input("Input your age: ")
        if not validete_age(age) :
            continue
        break
    print("Your age is", age)

    while True:
        name: str = input("Input your username: ")
        if not validate_name(name):
            continue
        break
    print("Your username is", name)

    while True:
        height: str = input("Input your height(meters): ")
        if not validate_height(height):
            continue
        break
    print("Your height is", height, "meters!")




def validete_age(age: str) -> bool :
    if not age.isnumeric():
        print("Your input is not a number!")
        return False
    if int(age) < 0 or int(age) > 119:
        print("Not a valid age number!")
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