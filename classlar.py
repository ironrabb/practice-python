

# ============================================
# 🎯 DARS MAQSADI
# ============================================
# Ushbu darsda Python'dagi klasslar haqida:
# - (1) What is class (Klass nima?)
# - (2) Ordinary vs Static properties
# - (3) Special/Magic methods


# ============================================
# 1️⃣ WHAT IS CLASS (Klass nima?)
# ============================================

print(" ===== What is class ==== ")

# 📌 Tushuncha:
# Class - blueprint (andoza) obyekt yaratish uchun!
# Struktura: state (holat) > constructor (konstruktor) > method (metod)

class Person:
    # ============================================================
    # 1. CLASS STATE (xususiyat)
    # ============================================================
    message = "class state property"

    # ============================================================
    # 2. CONSTRUCTOR (__init__)
    # ============================================================
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ============================================================
    # 3. METHODS (metodlar)
    # ============================================================
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


# -------------------- OBYEKT YARATISH --------------------
person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# -------------------- ORDINARY STATE (oddiy xususiyat) --------------------
print("person1.name:", person1.name)   # Justin

# -------------------- ORDINARY METHOD (oddiy metod) --------------------
person1.introduce()   # Justin says: How do you do!
person2.say_age()     # Martin says I am 35!


# ============================================
# 2️⃣ ORDINARY vs STATIC PROPERTIES
# ============================================

print(" ==== ordinary vs static properties===")

# -------------------- STATIC STATE (statik xususiyat) --------------------
# Classga tegishli, obyektga emas
new_message = Person.message
print("new_message:", new_message)   # class state property

# -------------------- STATIC METHOD (statik metod) --------------------
# @classmethod dekoratori bilan yaratiladi
# Class orqali chaqiriladi, obyekt kerak emas
Person.explain()   # static method property executed!

# 📌 Farqi:
# Ordinary (oddiy)  -> obyektga tegishli (self orqali)
# Static (statik)   -> classga tegishli (cls orqali yoki klass nomi bilan)


# ============================================
# 3️⃣ SPECIAL/MAGIC METHODS
# ============================================

print(" ===== special/magic methods===== ")

# 📌 Tushuncha:
# Magic methods - Python'ning eng ko'p ishlatiladigan special metodlari

# -------------------- Asosiy magic metodlar --------------------
# __init__     -> Konstruktor (obyekt yaratilganda ishlaydi)
# __new__      -> Obyekt yaratishdan oldin ishlaydi
# __str__      -> print() yoki str() chaqirilganda ishlaydi
# __call__     -> Obyektni funksiya kabi chaqirganda ishlaydi
# __getitem__  -> Obyektdan element olishda ishlaydi

class Car:
    # ============================================================
    # 1. CLASS STATE
    # ============================================================
    description = "This class makes cars"

    # ============================================================
    # 2. CONSTRUCTOR (__new__ va __init__)
    # ============================================================
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # ============================================================
    # 3. METHODS
    # ============================================================
    def start_engine(self):
        print(f"The {self.name} started engine!")

    def stop_engine(self):
        print(f"The {self.name} stopped engine!")

    # ============================================================
    # 4. MAGIC METHODS (2 ta pastki chiziq!)
    # ============================================================
    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")


# -------------------- OBYEKT YARATISH --------------------
my_car = Car("Ferrari", 2025)
my_car.start_engine()   # The Ferrari started engine!
my_car.stop_engine()    # The Ferrari stopped engine!

print(" ----- ")

your_car = Car("Toyota", 2026)
print(your_car)   # __str__ avtomatik chaqiriladi -> Toyota was produced in 2026 year!
your_car()        # __call__ avtomatik chaqiriladi -> Object called as function!

# 📌 Tushuntirish:
# __new__   -> Obyekt yaratishdan OLDIN ishlaydi (birinchi bo'lib)
# __init__  -> Obyekt yaratilgandan KEYIN ishlaydi (state o'rnatish)
# __str__   -> print(obyekt) yoki str(obyekt) chaqirilganda avtomatik ishlaydi
# __call__  -> obyekt() ko'rinishida chaqirilganda avtomatik ishlaydi


# ============================================
# ✅ XULOSA (Qisqacha eslatma)
# ============================================

# 📌 1. Class - obyekt yaratish uchun andoza (blueprint)
# 📌 2. Struktura: class state > constructor > methods
# 📌 3. __init__ - konstruktor, obyekt yaratilganda ishlaydi
# 📌 4. self - obyektning o'ziga murojaat
# 📌 5. cls - classning o'ziga murojaat (@classmethod)
# 📌 6. Ordinary vs Static:
#       - Ordinary: obyektga tegishli (self)
#       - Static: classga tegishli (cls yoki klass nomi)
# 📌 7. Magic methods: __init__, __new__, __str__, __call__, __getitem__
# 📌 8. __str__ - print() da avtomatik ishlaydi
# 📌 9. __call__ - obyektni funksiya kabi chaqirganda ishlaydi

