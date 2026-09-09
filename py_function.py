# ============================================
# 📘 PYTHON KONSPEKTI — "FUNCTIONS (Funksiyalar)"
# ============================================

# ============================================
# 🎯 DARS MAQSADI
# ============================================
# Ushbu darsda Python'dagi funksiyalar haqida:
# - DEFINE vs CALL (yaratish va chaqirish)
# - Parametr vs Argument
# - Keyword & default arguments
# - Scope (ko'lam)


# ============================================
# 1️⃣ DEFINE vs CALL (Funksiyani yaratish va chaqirish)
# ============================================

print(" === DEFINE vs CALL ===== ")

# 📌 Tushuncha:
# Funksiya - qayta ishlatiladigan kod bloki
# Python'da {} o'rniga indentation (bo'sh joy) ishlatiladi

# Built-in funksiyalar: print(), type(), input(), len() va boshqalar

# -------------------- DEFINE (Yaratish) --------------------
def greet(a):
    print(f"How do you do, {a}")

def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

# -------------------- CALL (Chaqirish) --------------------
# greet() funksiyasini chaqiramiz (hech narsa qaytarmaydi - None)
result1 = greet('Martin')
print("result1:", result1)   # None chiqadi

# greeting() funksiyasini chaqiramiz (qiymat qaytaradi)
result2 = greeting("Justin")
print("result2:", result2)   # "Hi Justin" chiqadi

# 📌 Muhim farq:
# greet() - print() ishlatadi, lekin return qilmaydi -> natija None
# greeting() - return ishlatadi -> natijani o'zgaruvchiga saqlash mumkin


# ============================================
# 2️⃣ PARAMETR vs ARGUMENT
# ============================================

# 📌 Tushuncha:
# Parametr - funksiyani yaratishda ishlatiladigan o'zgaruvchi (placeholder)
# Argument - funksiyani chaqirishda beriladigan haqiqiy qiymat

# Yuqoridagi misolda:
# greet(a) dagi 'a' - PARAMETR
# greet('Martin') dagi 'Martin' - ARGUMENT

# greeting(b) dagi 'b' - PARAMETR
# greeting("Justin") dagi "Justin" - ARGUMENT


# ============================================
# 3️⃣ KEYWORD & DEFAULT ARGUMENTS
# ============================================

print(" ===== Keyword & default arguments ===== ")

# -------------------- DEFAULT ARGUMENTS --------------------
# Parametrga standart qiymat berish mumkin

# DEFINE
def give_greet(name, age=22):        # age - default argument (standart qiymat 22)
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

# -------------------- CALL --------------------
# Keyword argumentlar bilan chaqirish (tartib muhim emas)
result3 = give_greet(name="Justin", age=28)   # name="Justin" va age=28 - KEYWORD ARGUMENTLAR
print("result3:", result3)   # Hi Justin, you are 28 years old!

# Positional argument va default argument
result4 = give_greet("John")   # "John" - positional argument, age default (22) ishlaydi
print("result4:", result4)     # Hi John, you are 22 years old!

# 📌 Eslatma: 
# - Default argumentlar har doim PARAMETRLARNING OXIRIDA kelishi kerak
# - Keyword argumentlar positional argumentlardan KEYIN kelishi kerak


# ============================================
# 4️⃣ SCOPE (O'zgaruvchilar ko'lami)
# ============================================

print(" ===== Scope ===== ")

# 📌 Tushuncha:
# Scope - o'zgaruvchi qayerda mavjud va qayerda ishlatilishi mumkinligi

b = 100   # GLOBAL o'zgaruvchi (3-bosqich)

# -------------------- LOCAL vs GLOBAL --------------------
# DEFINE
def calculate(a):   # a - LOCAL parametr (2-bosqich)
    c = a * b       # c - LOCAL o'zgaruvchi, b - GLOBAL o'zgaruvchi (1-bosqich)
    print(f"the c value: {c}")

# CALL
calculate(5)   # 5 - ARGUMENT, natija: 5 * 100 = 500

# 📌 Tushuntirish:
# 1. c = a * b -> a=5 (local), b=100 (global)
# 2. Natija: c = 5 * 100 = 500
# 3. print() orqali c ning qiymati chiqariladi

# -------------------- Scope qoidalari --------------------
# 1. Funksiya ichidagi o'zgaruvchilar LOCAL (faqat funksiya ichida mavjud)
# 2. Funksiyadan tashqaridagi o'zgaruvchilar GLOBAL (hamma joyda mavjud)
# 3. Funksiya ichida global o'zgaruvchini o'qish mumkin
# 4. Funksiya ichida global o'zgaruvchini o'zgartirish uchun 'global' kalit so'zi kerak

# Misol:
x = 50   # GLOBAL

def test_scope():
    y = 30   # LOCAL
    print("Global x:", x)   # Globalga kirish mumkin
    print("Local y:", y)

test_scope()
# print(y)   # ❌ XATO! y funksiyadan tashqarida mavjud emas


# ============================================
# ✅ XULOSA (Qisqacha eslatma)
# ============================================

# 📌 1. DEFINE - funksiyani yaratish, CALL - chaqirish
# 📌 2. Parametr - funksiyadagi placeholder, Argument - haqiqiy qiymat
# 📌 3. Default argument - standart qiymat, Keyword argument - nom bilan chaqirish
# 📌 4. Local scope - funksiya ichi, Global scope - butun dastur
# 📌 5. return - qiymat qaytaradi, printsiz return bo'lsa -> None
