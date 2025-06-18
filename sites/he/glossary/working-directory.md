# Working Directory (אזור העבודה)

**הגדרה קצרה:** התיקיה במערכת הקבצים שבה אתה עובד כרגע, המכילה את כל הקבצים הנוכחיים של המאגר ואת השינויים שעשית.

## הסבר מורחב

`Working Directory` (אזור העבודה) הוא התיקיה במחשב שלך שבה נמצאים כל הקבצים של המאגר. זה המקום שבו אתה עורך קבצים, מוסיף קבצים חדשים, או מוחק קבצים קיימים.

**דוגמאות לשימוש נפוץ:**
* עריכת קבצים קיימים
* הוספת קבצים חדשים
* מחיקת קבצים
* בדיקת מצב השינויים

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת תוכן אזור העבודה
ls -la

# בדיקת מצב השינויים
git status

# הצגת הבדלים באזור העבודה
git diff

# ניקוי אזור העבודה (זהירות!)
git clean -fd
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# בדיקת אזור העבודה
def check_working_directory(repo):
    print(f"אזור העבודה: {repo.working_dir}")
    print(f"קבצים שעברו שינויים: {len(repo.untracked_files)}")
    
    # הצגת קבצים לא מנוהלים
    for file in repo.untracked_files:
        print(f"  לא מנוהל: {file}")

check_working_directory(repo)
```

## מונחים קשורים

* [Staging Area (אזור ההכנה)](./staging.md)
* [Status (מצב)](./status.md)
* [Diff (הבדלים)](./diff.md)

## מקורות מידע נוספים

* [תיעוד Git על Working Directory](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) 