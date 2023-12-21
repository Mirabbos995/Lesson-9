
# Lesson 6

from repo.lesson9 import b , integer
from misol.misol3 import dictionary , people
from misol.misol4 import countries

print(b,dictionary(),countries(), integer(), people())


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



numbers = [45,55,60,37,100,105,220]
numbers[0],numbers[3]=numbers[3],numbers[0]
print(numbers)






         # Lesson 5
def name():
    names = ["Ali","Vali","Hasan","Husan","Olim"]          # 1- misol
    for name in names:
        if name == "Ali":
            print(f"Salom {name}")
        elif name == "Vali":
            print(f"Salom {name}")
        elif name == "Hasan":
            print(f"Salom {name}")
        elif name == "Husan":
            print(f"Salom {name}")
        elif name == "Olim":
            print(f"Salom {name}")
    print(f"Kod {len(names)} marta qaytarilgan")
name()


