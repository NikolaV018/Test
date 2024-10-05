def main():
    nbr: int = int(input("How many lines: "))
    pyramid(nbr)

def pyramid(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            if j != i:
                print(i, end="")
            elif j == i:
                print(i)





main()

