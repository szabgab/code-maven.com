 # Staging Area (אזור ההכנה)

**הגדרה קצרה:** אזור ביניים ב-Git שבו נשמרים השינויים שהוכנו ל-commit, לפני שהם נשמרים בהיסטוריה של המאגר.

## הסבר מורחב

`Staging Area` (אזור ההכנה) הוא אזור זמני שבו אתה מכין שינויים לפני commit. זה מאפשר לך לבחור בדיוק איזה שינויים לכלול ב-commit הבא, גם אם יש לך שינויים רבים בקבצים שונים.

**דוגמאות לשימוש נפוץ:**
* הכנת קבצים ל-commit
* בחירת שינויים ספציפיים
* בדיקת מה ייכלל ב-commit
* ניקוי staging area

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הוספת קובץ ל-staging area
git add file.txt

# הוספת כל השינויים
git add .

# הוספת קבצים לפי pattern
git add *.js

# הסרת קובץ מ-staging area
git reset HEAD file.txt

# הצגת מה ב-staging area
git diff --staged

# ניקוי staging area
git reset
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo

repo = Repo('my_repo')

# בדיקת staging area
def check_staging_area(repo):
    staged_files = repo.index.diff('HEAD')
    print(f"קבצים ב-staging area: {len(staged_files)}")
    
    for diff in staged_files:
        print(f"  {diff.a_path}")

# הוספת קובץ ל-staging area
def stage_file(repo, file_path):
    repo.index.add([file_path])
    print(f"נוסף {file_path} ל-staging area")

check_staging_area(repo)
```

## מונחים קשורים

* [Add (הוספה)](./add.md)
* [Commit (התחייבות)](./commit.md)
* [Reset (איפוס)](./reset.md)

## מקורות מידע נוספים

* [תיעוד Git על Staging Area](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)