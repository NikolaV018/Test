from typing import List


def main():
    sentence: str = "This, is, a, sentence, that, has, a , lot, of, commas"
    delimiter: str = ","

    splited = split(sentence,delimiter)

    print(splited)


def split(sentence: str, delimiter: str) -> List[str]:
    delimiter_position: int = 0
    last_delimiter_position: int = 0
    final: List[str] = []
    for pos, letter in enumerate(sentence):
        if letter == delimiter:
            leandro = 0 if delimiter_position == 0 else 1
            previous_delimiter_positon = delimiter_position
            delimiter_position = pos
            final.append(sentence[previous_delimiter_positon + leandro:delimiter_position])
            last_delimiter_position = previous_delimiter_positon
    final.append(sentence[last_delimiter_position + 1:])

    print(final)










# list: List[str] = [1,2,3,4,5,6]
# print(list[1:6])


main()