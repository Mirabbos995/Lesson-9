 # Lesson 6

b = input("Please enter a country: ")                # 2-misol

def country():
    a = {
        "O'ZBEKISTON": 'Tashkent',
        'AQSH': 'Washington D.C.',
        'BRITANYA': 'London',
        "FRANSIYA": 'Paris',
        'GERMANIYA': 'Berlin',
        'KANADA': 'Ottava',
        'AUTRALIA': 'Kanberra',
    }

    if b in a:
        print(f"The capital of {b} is {a[b]}.")
    else:
        print("Error")
country()



#Lesson 5
def integer():
    a = [11,13,17,19,23,29,31,37,41,43,47,49,51,53,57,59,61,67,71,73,77,79,83,89,91,97] # 2-misol
    for b in a:
        cube = b**3
        print(cube)
integer()

