═══════════════════════════════════════════════════════════════
GIT — TO‘LIQ QO‘LLANMA
═══════════════════════════════════════════════════════════════

═══════════════════════════════════════════════════════════════

1. KONFIGURATSIYA (SOZLASH)
   ═══════════════════════════════════════════════════════════════

git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"
git config --list
git config --global core.editor "code --wait"

═══════════════════════════════════════════════════════════════ 2. BOSHLASH
═══════════════════════════════════════════════════════════════

git init # Yangi repo
git clone https://github.com/... # Nusxalash

═══════════════════════════════════════════════════════════════ 3. HOLAT VA O'ZGARISHLAR
═══════════════════════════════════════════════════════════════

git status # Holat
git status -s # Qisqa holat
git diff # O'zgarishlar
git diff --staged # Stage dagi o'zgarishlar

═══════════════════════════════════════════════════════════════ 4. FAYLLARNI QO'SHISH
═══════════════════════════════════════════════════════════════

git add . # Barcha fayllar
git add index.html # Bitta fayl
git add src/ # Papka

═══════════════════════════════════════════════════════════════ 5. SAQLASH (COMMIT)
═══════════════════════════════════════════════════════════════

git commit -m "Xabar" # Commit
git commit -am "Xabar" # Add + Commit
git commit --amend -m "Yangi" # Tahrirlash

═══════════════════════════════════════════════════════════════ 6. REMOTE
═══════════════════════════════════════════════════════════════

git remote add origin URL # Remote qo'shish
git remote -v # Ko'rish
git remote remove origin # O'chirish
git remote rename origin upstream # Nom o'zgartirish

═══════════════════════════════════════════════════════════════ 7. YUKLASH VA YANGILASH
═══════════════════════════════════════════════════════════════

git push origin main # Yuklash
git push -u origin main # Birinchi marta
git pull origin main # Yangilash
git fetch origin # O'zgarishlarni olish

═══════════════════════════════════════════════════════════════ 8. BRANCH (SHOXCHALAR)
═══════════════════════════════════════════════════════════════

git branch # Ko'rish
git branch new-feature # Yaratish
git checkout new-feature # O'tish
git checkout -b new-feature # Yaratish + o'tish
git branch -d new-feature # O'chirish
git branch -m eski yangi # Nom o'zgartirish

═══════════════════════════════════════════════════════════════ 9. MERGE (BIRLASHTIRISH)
═══════════════════════════════════════════════════════════════

git checkout main
git merge new-feature # Birlashtirish
git merge --abort # Bekor qilish
git merge --squash new-feature # Squash

═══════════════════════════════════════════════════════════════ 10. TARIX (LOG)
═══════════════════════════════════════════════════════════════

git log # To'liq
git log --oneline # Qisqa
git log --graph --oneline --all # Grafik
git log -5 # Oxirgi 5 ta
git log --author="Ism" # Muallif
git log --grep="xatolik" # Qidiruv

═══════════════════════════════════════════════════════════════ 11. RESET (BEKOR QILISH)
═══════════════════════════════════════════════════════════════

git reset HEAD index.html # Stage dan olib tashlash
git reset --soft HEAD~1 # Commit bekor (o'zgarish saqlanadi)
git reset --hard HEAD~1 # Commit bekor (o'zgarish o'chadi)
git reset --hard commit_id # Commit ga qaytish

═══════════════════════════════════════════════════════════════ 12. STASH (YASHIRISH)
═══════════════════════════════════════════════════════════════

git stash # Yashirish
git stash list # Ko'rish
git stash pop # Qaytarish
git stash apply # Qaytarish (saqlab)
git stash drop # O'chirish
git stash clear # Hammasini o'chirish

═══════════════════════════════════════════════════════════════ 13. REVERT (QAYTARISH)
═══════════════════════════════════════════════════════════════

git revert commit_id # Commit ni qaytarish
git revert --abort # Bekor qilish

═══════════════════════════════════════════════════════════════ 14. TAG (TEPLAR)
═══════════════════════════════════════════════════════════════

git tag v1.0.0 # Yaratish
git push origin v1.0.0 # Yuklash
git push --tags # Barcha taglar
git tag # Ko'rish
git tag -d v1.0.0 # O'chirish

═══════════════════════════════════════════════════════════════ 15. SUBMODULE
═══════════════════════════════════════════════════════════════

git submodule add URL # Qo'shish
git submodule update --init # Yangilash
git submodule status # Ko'rish

═══════════════════════════════════════════════════════════════ 16. HAMMA KAMANDALAR JADVALI
═══════════════════════════════════════════════════════════════

git config Sozlash
git init Repo yaratish
git clone Nusxalash
git status Holat
git diff O'zgarishlar
git add Fayl qo'shish
git commit Saqlash
git remote Remote boshqarish
git push Yuklash
git pull Yangilash
git fetch O'zgarishlarni olish
git branch Branch boshqarish
git checkout Branch ga o'tish
git switch Branch ga o'tish
git merge Birlashtirish
git log Tarix
git reset Bekor qilish
git stash Yashirish
git revert Qaytarish
git tag Teplar
git submodule Submodule

═══════════════════════════════════════════════════════════════ 17. TEZKOR BUYRUQLAR
═══════════════════════════════════════════════════════════════

git status # Holat
git add . && git commit -m "xabar" # Add + Commit
git push origin main # Yuklash
git pull origin main # Yangilash
git log --oneline --graph # Tarix

═══════════════════════════════════════════════════════════════ 18. XATOLIKLAR VA YECHIMLAR
═══════════════════════════════════════════════════════════════

not a git repository → git init
Please tell me who you are → git config --global user.name "Ism"
Permission denied → SSH kalit yoki token
Merge conflict → Faylni qo'lda tuzatish

19. MUHIM ESLATMA
    ═══════════════════════════════════════════════════════════════

Har bir loyiha uchun alohida Git!
cd loyiha1
git init
git remote add origin https://github.com/username/repo1.git

cd ../loyiha2
git init
git remote add origin https://github.com/username/repo2.git

═══════════════════════════════════════════════════════════════ 20. FOYDALI MANBALAR
═══════════════════════════════════════════════════════════════

Git Documentation: https://git-scm.com/doc
GitHub Docs: https://docs.github.com/en/get-started
Pro Git Book: https://git-scm.com/book/en/v2

═══════════════════════════════════════════════════════════════
📅 2026 | GIT QO'LLANMA BY IRON
═══════════════════════════════════════════════════════════════
