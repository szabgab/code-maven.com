 # Add (הוספה)

**הגדרה קצרה:** פקודה ב-Git שמעבירה קבצים או שינויים מאזור העבודה (working directory) לאזור ההכנה (staging area), כדי להכין אותם ל-commit.

## הסבר מורחב

`Add` (הוספה) היא הפקודה שמעבירה שינויים מאזור העבודה לאזור ההכנה. זה השלב הראשון בתהליך ה-commit, שבו אתה בוחר איזה שינויים לכלול ב-commit הבא.

**דוגמאות לשימוש נפוץ:**
* הוספת קבצים חדשים למעקב
* הכנת שינויים ל-commit
* הוספת קבצים לפי סוג או מיקום
* הוספת כל השינויים בבת אחת

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הוספת קובץ ספציפי
git add file.txt

# הוספת כל השינויים
git add .

# הוספת קבצים לפי סיומת
git add *.js
git add *.py

# הוספת קבצים בתיקיה
git add src/

# הוספת קבצים עם pattern
git add "*.{js,css,html}"

# הוספת קבצים אינטראקטיבית
git add -i

# הוספת קבצים עם patch
git add -p

# הוספת קבצים עם אימות
git add --dry-run file.txt
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo

repo = Repo('my_repo')

# הוספת קובץ
def add_file(repo, file_path):
    repo.index.add([file_path])
    print(f"נוסף {file_path}")

# הוספת כל השינויים
def add_all(repo):
    repo.index.add('*')
    print("נוספו כל השינויים")

# הוספת קבצים לפי pattern
def add_pattern(repo, pattern):
    repo.index.add(pattern)
    print(f"נוספו קבצים לפי {pattern}")

# בדיקת מה נוסף
def check_added(repo):
    staged = repo.index.diff('HEAD')
    print(f"קבצים שהוכנו: {len(staged)}")
    for diff in staged:
        print(f"  {diff.a_path}")

add_file(repo, "new_file.txt")
check_added(repo)
```

## מונחים קשורים

* [Staging Area (אזור ההכנה)](./staging.md)
* [Commit (התחייבות)](./commit.md)
* [Status (מצב)](./status.md)

## מקורות מידע נוספים

* [תיעוד Git על git add](https://git-scm.com/docs/git-add)