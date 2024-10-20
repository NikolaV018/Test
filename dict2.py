from typing import List, Dict


def main():
    name_list: List[str] = ["Breno", "Nikola","Elisa","Isadora"]
    name_plus_age_list: List[str] = ["Breno+23", "Nikola+27", "Elisa+23", "Nikola+22", "Isadora+22", "Elisa+26", "Elisa+20"]

    search(name_list, name_plus_age_list)




def search(list1: List[str],list2: List[str]) -> None:
    answer: Dict[str, str] = {}
    for name in list2:
        x = name.split("+")
        if x[0] in list1:
            answer[x[0]] = x[1]

    print(answer)

main()