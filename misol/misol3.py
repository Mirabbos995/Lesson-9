
# Lesson 6

def dictionary():
    dictionary = {                  # 3-misol
        "Issubset -": "Agar a obyektdagi elementlar b obyektrida bo’lsa True , bo’lmasa False.",
        "Float -": "O'nik son",
        "For -": "Biror amalni qayta qaytabajarish tsikli",
        "Integer -": "Butun son",
        "Boolean -": "mantiqiy qiymat",
        "Append -": "Elementlarni oxiriga tushuradigan method",
        "Insert -": "Elementlarni index orqali hoxlagan joyiga tushuradi",
        "Range -": "Faqat integer bilan ishlaydi",
        "Delete -": "Elementlarni index orqali o'chiradi",
        "Print -": "Konsolga chiqari berish uchun ishlatiladi"
        }
    for key, value in sorted(dictionary.items()):
        print(key, value)
dictionary()


# Lesson 5
def people():
    a = int(input("Bugun necha kishi bilan suhbaylashdingiz: "))
    x = str(input("1-suhbatlashgan odamingiz kim edi: "))
    y = str(input("2-suhbatlashgan odamingiz kim edi: "))
    z = str(input("3-suhbatlashgan odamingiz kim edi: "))
    items = [x, y, z]
    for x in items:
        print(items)
people()