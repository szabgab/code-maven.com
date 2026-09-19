 # History (היסטוריה)

**הגדרה קצרה:** רשימה מסודרת של כל ההתחייבויות (commits) במאגר Git, המציגה את התפתחות הפרויקט לאורך זמן.

## הסבר מורחב

`History` (היסטוריה) היא הרשימה המלאה של כל ההתחייבויות במאגר, מסודרות בסדר כרונולוגי. כל התחייבות מכילה מידע על השינויים שנעשו, מי עשה אותם, ומתי.

**דוגמאות לשימוש נפוץ:**
* מעקב אחר התפתחות הפרויקט
* מציאת מתי הוכנס באג
* הבנת מי עבד על מה
* חזרה לגרסה קודמת

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת היסטוריה בסיסית
git log

# הצגת היסטוריה בקיצור
git log --oneline

# הצגת היסטוריה עם גרף
git log --graph --oneline

# הצגת היסטוריה של קובץ
git log -- file.txt

# הצגת היסטוריה של מפתח
git log --author="שם"

# הצגת היסטוריה לפי תאריך
git log --since="2023-01-01"

# הצגת היסטוריה עם מספר מוגבל
git log -n 10
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo

repo = Repo('my_repo')

# הצגת היסטוריה בסיסית
def show_history(repo, max_count=10):
    for commit in repo.iter_commits('HEAD', max_count=max_count):
        print(f"{commit.hexsha[:8]} - {commit.message.strip()}")

# הצגת היסטוריה של קובץ
def show_file_history(repo, file_path):
    for commit in repo.iter_commits('HEAD', paths=file_path):
        print(f"{commit.hexsha[:8]} - {commit.message.strip()}")

# חיפוש בהיסטוריה
def search_history(repo, search_term):
    for commit in repo.iter_commits('HEAD'):
        if search_term in commit.message:
            print(f"{commit.hexsha[:8]} - {commit.message.strip()}")

show_history(repo, 5)
```

## מונחים קשורים

* [Log (היסטוריה)](./log.md)
* [Commit (התחייבות)](./commit.md)
* [Branch (ענף)](./branch.md)

## מקורות מידע נוספים

* [תיעוד Git על git log](https://git-scm.com/docs/git-log)