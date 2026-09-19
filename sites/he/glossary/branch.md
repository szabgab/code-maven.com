# Branch (ענף)

**הגדרה קצרה:** ענף הוא קו פיתוח עצמאי במאגר קוד (repository) במערכת ניהול גרסאות כמו **Git**. כל ענף מאפשר לבצע שינויים, פיתוחים או ניסויים מבלי להשפיע על הקוד הראשי (לרוב master/main).

## הסבר מורחב

`Branch` (ענף) הוא כלי מרכזי בעבודה עם Git. כל ענף הוא למעשה הצבעה (pointer) להיסטוריית התחייבויות (commits) נפרדת, שמאפשרת פיתוח במקביל למספר כיוונים. נהוג ליצור ענפים חדשים עבור פיצ'רים, תיקוני באגים, ניסויים או גרסאות שונות של הפרויקט. כאשר העבודה בענף מסתיימת, ניתן למזג (merge) אותו חזרה לענף הראשי או לכל ענף אחר.

היתרונות העיקריים של **Branch** הם:
* **פיתוח במקביל:** מספר מפתחים/ות יכולים לעבוד על פיצ'רים שונים מבלי להפריע זה לזו.
* **ניסוי וטעייה:** ניתן לבדוק רעיונות חדשים מבלי לסכן את הקוד היציב.
* **ניהול גרסאות:** מאפשר לנהל גרסאות שונות של הפרויקט (למשל, גרסת פיתוח מול גרסת ייצור).

**דוגמאות לשימוש נפוץ:**
* יצירת ענף חדש עבור פיצ'ר: `git checkout -b feature/login`
* עבודה על תיקון באג בענף נפרד.
* מיזוג (merge) של ענף הפיצ'ר לענף הראשי לאחר סיום הפיתוח.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# יצירת ענף חדש ומעבר אליו
git checkout -b feature/login

# מעבר לענף קיים
git checkout main

# מחיקת ענף מקומי
git branch -d feature/login
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
repo = Repo('my_repo')
# יצירת ענף חדש
new_branch = repo.create_head('feature/login')
# מעבר לענף החדש
new_branch.checkout()
# מעבר לענף קיים
repo.heads.main.checkout()
# מחיקת ענף (דרך git)
repo.git.branch('-d', 'feature/login')
```

## מונחים קשורים

* [Repository (מאגר קוד)](./repository.md)
* [Commit (התחייבות)](./commit.md)
* [Merge (מיזוג)](./merge.md)
* [Pull Request (בקשת משיכה)](./pull-request.md)

## מקורות מידע נוספים

* [תיעוד Git על Branches](https://git-scm.com/book/he/v2/%D7%91%D7%A1%D7%99%D7%A1-%D7%94-Git-%D7%A2%D7%A0%D7%A4%D7%99%D7%9D-%D7%91%D7%92%D7%99%D7%98)
* [תיעוד GitHub על Branches](https://docs.github.com/en/get-started/quickstart/github-glossary#branch) 