
# Lesson 6
def countries():
    countries = {      # 4-misol
        "AQSH ": "WASHINGTON",
        "ITALIYA ": "RIM",
        "MALAYZIYA ": "SINGAPUR",
        "O'ZBEKISTON ": " ASHKENT",
        "QIRG'IZISTON ": "BISHKEK",
        "ROSSIYA ": "MOSKVA",
        "SINGAPUR": "KUALA-LUMPUR",
        "TOJIKISTON": "DUSHENBE"
    }

    for key, value in sorted(countries.items()):
        print(key, value)
countries()