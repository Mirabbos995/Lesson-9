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