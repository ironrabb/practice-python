# ============================================
# 📘 PYTHON KONSPEKTI — "OBJECTS (Obyektlar)"
# ============================================

# ============================================
# 🎯 DARS MAQSADI
# ============================================
# Ushbu darsda Python'dagi obyektlar haqida:
# - (1) What is object (Obyekt nima?)
# - (2) Iterable objects & RANGE
# - (3) DICTIONARY (Lug'at)
# - (4) Error handling system (Xatoliklarni boshqarish)


# ============================================
# 📦 IMPORT (Paket/Modul)
# ============================================

import array   # package/module
import math


# ============================================
# 1️⃣ WHAT IS OBJECT (Obyekt nima?)
# ============================================

print(" ===== What is object ==== ")

# 📌 Tushuncha:
# Obyekt - state (holat) va method (metod) xususiyatlariga ega
# Python'da HAMMA NARSA obyekt!

# Turli obyektlarning turlarini ko'ramiz:
print(type('Hello World!'))   # <class 'str'>
print(type(100))              # <class 'int'>
print(type(True))             # <class 'bool'>
print(type(array))            # <class 'module'>
print(type(math))             # <class 'module'>

# -------------------- IMPORT usullari --------------------
from math import ceil   # faqat bitta method kerak bo'lganda

# 📌 Paradigm (Dasturlash paradigmalari):
# - Functional Programming (Funksional dasturlash)
# - OOP (Object-Oriented Programming)

# 📌 OOP 4 CONCEPTS (OOP ning 4 asosiy tushunchasi):
# 1. Abstraction (Mavhumlashtirish)
# 2. Encapsulation (Inkapsulyatsiya)
# 3. Inheritance (Meros olish)
# 4. Polymorphism (Polimorfizm)

# -------------------- CALL (Chaqirish) --------------------
result1 = math.ceil(97.7)   # math moduli orqali chaqirish
print("result1:", result1)  # 98

result2 = ceil(98.7)        # to'g'ridan-to'g'ri import qilingan funksiya
print("result2:", result2)  # 99

# 📌 Eslatma: 
# math.ceil() - modul orqali chaqirish
# ceil() - to'g'ridan-to'g'ri import qilingan funksiya


# ============================================
# 4️⃣ ERROR HANDLING SYSTEM (Xatoliklarni boshqarish)
# ============================================

print(" == Error handling system ===== ")

# -------------------- DICTIONARY yaratish --------------------
car_dict = dict(name="Tayota", year=2026, electric=True)

# -------------------- TRY-EXCEPT-ELSE-FINALLY --------------------
try:
    print("passed here")
    a = car_dict.speed          # ← 1-xato: AttributeError
    result = car_dict["origin"] # ← 2-xato: KeyError (yetib bormaydi!)
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:   # exception errori hamma errorni ushlaydi
    print("No speed found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")

# 📌 Tushuntirish:
# try        -> Xato bo'lishi mumkin bo'lgan kod
# except     -> Xatoni ushlash va boshqarish
# else       -> Xato bo'lmasa ishlaydigan kod
# finally    -> Har qanday holatda ham ishlaydigan kod (tozalash uchun)

# 📌 Xatolar turlari:
# AttributeError -> Obyektda mavjud bo'lmagan xususiyatga murojaat
# KeyError       -> Lug'atda mavjud bo'lmagan kalitga murojaat


# ============================================
# ✅ XULOSA (Qisqacha eslatma)
# ============================================

# 📌 1. Obyekt - state va methodga ega, Python'da hamma narsa obyekt
# 📌 2. Iterable objects - takrorlanuvchi obyektlar (list, tuple, range)
# 📌 3. Dictionary - kalit-qiymat juftliklari to'plami
# 📌 4. Error handling - try/except/else/finally orqali xatolarni boshqarish
# 📌 5. OOP 4 CONCEPTS - Abstraction, Encapsulation, Inheritance, Polymorphism
