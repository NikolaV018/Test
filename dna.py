def main():
    a_counter = 0
    c_counter = 0
    g_counter = 0
    t_counter = 0
    while True:
        dna: str = input("Input your dna string: ").lower()
        if dna_very(dna) == False:
            continue
        break
    for letter in dna:
        if letter == "a":
            a_counter += 1
        if letter == "c":
            c_counter += 1
        if letter == "g":
            g_counter += 1
        if letter == "t":
            t_counter += 1
        else:
            continue
    print(f"There are {a_counter} times letter A appears in this DNA!")
    print(f"There are {c_counter} times letter C appears in this DNA!")
    print(f"There are {g_counter} times letter G appears in this DNA!")
    print(f"There are {t_counter} times letter T appears in this DNA!")



def dna_very(dna: str) -> bool:
    if len(dna) > 1000:
        print("Your input is too long!!!")
        return False
    for i in dna:
        if i.isnumeric():
            print("Your input cannot have any numbers!")
            return False










main()