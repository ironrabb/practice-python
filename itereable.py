# ============================================
# 1️⃣ ITERABLE OBJECTS & RANGE
# ============================================

print(" ===== Iterable objects & RANGE========")

# 📌 Tushuncha:
# Iterable objects - takrorlanuvchi (aylanib o'tish mumkin bo'lgan) obyektlar

# -------------------- Iterable objectlar ro'yxati --------------------
# string, dict, tuple, list, range, map, filter

# -------------------- RANGE obyekti --------------------
range_obj = range(3)
print("range_obj:", range_obj)   # range(0, 3)

# -------------------- STRING ustida iteratsiya --------------------
for letter in "MIT":
    print(f"the letter: {letter}")
# Natija:
# the letter: M
# the letter: I
# the letter: T

# -------------------- RANGE ustida iteratsiya --------------------
for ele in range_obj:
    print(f"the element: {ele}")
# Natija:
# the element: 0
# the element: 1
# the element: 2

# 📌 Eslatma:
# range(3) -> 0, 1, 2 (3 kirmaydi)
# range(start, stop, step) ko'rinishida ham ishlatiladi


# ============================================
# 2️⃣ DICTIONARY (Lug'at)
# ============================================

print(" ===== DICTIONARY ===== ")

# 📌 Tushuncha:
# Dictionary - JSON obyektiga o'xshash, kalit-qiymat juftliklari to'plami

# -------------------- Dictionary yaratishning 2 usuli --------------------
# 1-usul: {} bilan
person = {"name": "Justin", "age": 25, "single": True}

# 2-usul: dict() funksiyasi bilan
person_obj = dict(name="Justin", age=25, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# -------------------- get() metodi --------------------
# get() - xavfsiz qiymat olish usuli (xato bo'lsa None qaytaradi)

# name = person_obj["name"]      # Bu usul xato bo'lsa KeyError beradi
name = person_obj.get("name")    # Bu usul xavfsiz
hobby = person_obj.get("hobby")  # Mavjud bo'lmagan kalit -> None
balance = person_obj.get("balance", 0)  # Default qiymat bilan -> 0

print(f"the name: {name}, hobby: {hobby} and balance: {balance}")
# Natija: the name: Justin, hobby: None and balance: 0

# -------------------- del - elementni o'chirish --------------------
del person_obj["single"]   # "single" kalitini o'chiramiz

# -------------------- Dictionary ustida iteratsiya --------------------
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}")
# Natija:
# the key: name => value Justin
# the key: age => value 25

# 📌 Eslatma:
# get() metodi - xavfsiz, chunki mavjud bo'lmagan kalitda xato bermaydi
# [] bilan murojaat - mavjud bo'lmagan kalitda KeyError beradi
# del - kalitni va uning qiymatini o'chiradi


# ============================================
# ✅ XULOSA (Qisqacha eslatma)
# ============================================

# 📌 1. Iterable objects - takrorlanuvchi obyektlar
#       (string, dict, tuple, list, range, map, filter)
# 📌 2. RANGE - sonlar ketma-ketligini yaratadi (range(3) -> 0, 1, 2)
# 📌 3. DICTIONARY - kalit-qiymat juftliklari to'plami
# 📌 4. get() - xavfsiz qiymat olish usuli (default qiymat bilan)
# 📌 5. del - dictionary elementini o'chirish
# 📌 6. for loop - iterable objectlar ustida aylanish uchun
