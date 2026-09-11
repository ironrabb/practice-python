# ============================================
# 📘 PYTHON KONSPEKTI — "Objektdagi hamma narsa"
# ============================================

# ============================================
# 1️⃣ PYTHONDA HAMMA NARSA OBJEKT
# ============================================

message = "pythonda hamma narsa ibject sifatida qaraladi"
print(message)

result = type(message)
print(result)   # <class 'str'>

# 📌 Tushuncha:
# Har bir maʼlumot (son, matn, roʻyxat, funksiya) — bu obyekt.
# type() funksiyasi obyektning turini koʻrsatadi.


# ============================================
# 2️⃣ O'RNATILGAN (BUILT-IN) VOSITALAR
# ============================================

# Python’da uchta asosiy oʻrnatilgan vosita mavjud:
# TYPES (turlar)      -> int, float, str, list, dict
# FUNCTIONS (funksiyalar) -> print(), len(), input(), type()
# CONSTANTS (doimiylar)   -> True, False, None

print(dir(__builtins__))   # Barcha o'rnatilgan vositalarni ko'rsatadi


# ============================================
# 3️⃣ MATN (STRING) METODLARI
# ============================================

# Asosiy metodlar roʻyxati:
# upper(), lower(), title(), capitalize(), count(), find(), index(),
# isalnum(), isalpha(), isdigit(), islower(), isupper(), split(), join()

course = "ai python fulstack"

# title() — har bir so'zni bosh harf bilan yozadi
result = course.title()
print(f"the result (2): {result}")   # Ai Python Fulstack

# upper() — hammasini katta harfga o'zgartiradi
result = course.upper()
print(f"the result (3): {result}")   # AI PYTHON FULSTACK

# replace() — so'zni almashtiradi
result = course.replace("fulstack", "masterclass")
print(f"the result (4): {result}")   # ai python masterclass

# 📌 f-string (f"...") — matn ichida {o‘zgaruvchi} yozib, uning qiymatini chiqarish usuli.


# ============================================
# 4️⃣ BOOLEAN METODLAR VA INPUT
# ============================================

# Foydalanuvchidan maʼlumot olish:
y = input("enter your name for y: ")
print(y)

# Matn ustida tekshirish metodlari:
# isalnum() -> Faqat harf va raqamlardan tashkil topganmi?
# isalpha() -> Faqat harflardan tashkil topganmi?
# isdigit() -> Faqat raqamlardan tashkil topganmi?

result = y.isalnum()
print(f"the input is alphanumeric?: {result}")

result = y.isalpha()
print(f"the input is alphabetic?: {result}")

result = y.isdigit()
print(f"the input is numeric?: {result}")


# ============================================
# 5️⃣ TRUTHY VA FALSY QIYMATLAR
# ============================================

# Python’da har bir qiymat True yoki False deb baholanadi.

# FALSY (yolg‘on)     | TRUTHY (rost)
# --------------------|-------------------------------
# False               | True
# 0, 0.0              | Har qanday 0 dan farqli son
# "" (bo‘sh matn)     | "mit", "hello"
# [] (bo‘sh ro‘yxat)  | To‘ldirilgan ro‘yxat
# {} (bo‘sh lug‘at)   | To‘ldirilgan lug‘at
# None                | -

test_falsy = "" or False or None or 0 or 100
print("the falsy :", bool(test_falsy))   # True (chunki 100 truthy)

test_truthy = "mit"
print("test_truthy", bool(test_truthy))  # True

# 📌 Eslatma: or operatorida birinchi truthy qiymat tanlanadi.
# Yuqoridagi misolda 100 truthy bo‘lgani uchun natija True chiqadi.


# ============================================
# ✅ XULOSA (Qisqacha eslatma)
# ============================================

# NIMA O‘RGANDIK?     | QISQA IZOH
# --------------------|-----------------------------------
# Objekt              | Har bir maʼlumot obyekt
# type()              | Obyekt turini aniqlaydi
# Metodlar            | Obyektga bog‘liq funksiyalar (masalan, upper())
# Input               | Foydalanuvchidan maʼlumot olish
# Truthy/Falsy        | Har bir qiymat mantiqiy qiymatga ega

