from repo.lesson9 import b
from misol.misol3 import dictionary
from misol.misol4 import countries

print(b,dictionary(),countries())


a = input("Enter the first food: ")                # 1-misol
b = input("Enter the second food: ")
d = input("Enter the third food: ")

def menu():
    menu = {
        "Osh": "20000",
        "Manti": "30000",
        "Non": "3000",
        "SHo'rva": "25000",
        "Norin": "35000",
        "Kabob": "25000",
        "Mastava": "20000"
        }
    for food in a,b,d:
        if food in menu:
            print(f"The price of {food} is {menu[food]} sum.")
        else:
            print("We do not have such a food.")
menu()





