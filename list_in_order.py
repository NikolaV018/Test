from typing import List

def main():
    first_list: List = []
    while True:
        numbers: int = int(input("Input numbers for your list: "))
        if numbers == -1:
            break
        first_list.append(numbers)



    first_list.sort()
    print(first_list)

    #final_list = order_list(first_list)
    #print(final_list)




def order_list(unordered: List[int]) -> List[int]:
    min: int = unordered[0]
    p: int = 0
    new_list: List = []
    for p in range(5):
        for number in unordered:
            if number < min:
                min = number
        new_list.append(min)
        unordered.remove(min)
        if len(unordered) != 0:
            min = unordered[0]



    return new_list








main()
