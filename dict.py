from typing import List

class Users:
    username: str
    email: str
    password: str
    age: int

    def __init__(self, username: str, email: str, password: str, age: int):
        self.username = username
        self.email = email
        self.password = password
        self.age = age

    def __str__(self):
        return f"{self.email} + {self.password}"

def main():


    list_of_users : List[Users] = [
        Users(username="marcopolo", email="marco.polo123@gmail.com", password="marco123", age=25),
        Users(username="breno321", email="breno123@hotmail.com", password="isadora", age=23),
        Users(username="johnnyw", email="johnnyw@gmail.com", password="drink1", age=44),

    ]
    search: str = input("Search by username: ")
    person = find_person(search, list_of_users)
    print(person)


def find_person(name: str, list_of_users: List[Users]) -> Users | None:
    holder: str = ""
    for person in list_of_users:
        if person.username == name:
            return person
    return None







main()