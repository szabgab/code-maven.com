# Clone (שכפול)

**הגדרה קצרה:** פעולה במערכת ניהול הגרסאות **Git** ובפלטפורמות כמו **GitHub**, שבה נוצרת העתקה מלאה של מאגר קוד (**repository**) מהמיקום המקורי (לרוב מהשרת) אל המחשב המקומי של המשתמש.

## הסבר מורחב

`Clone` (שכפול) הוא אחד הצעדים הראשונים שמבצע מפתח שרוצה לעבוד עם פרויקט קיים ב-Git. כאשר מבצעים `git clone`, נוצרת תיקיה חדשה במחשב המקומי, המכילה את כל קבצי המאגר, ההיסטוריה המלאה של השינויים, וההגדרות של המאגר המקורי (כולל כתובת ה-remote).

היתרונות העיקריים של **Clone** הם:
* **עבודה לא מקוונת:** מאפשר למפתחים לעבוד על הקוד במחשב האישי, גם ללא חיבור לאינטרנט.
* **גישה להיסטוריה:** כל ההיסטוריה של המאגר זמינה, כולל כל הענפים והתחייבויות.
* **שיתוף פעולה:** ניתן לבצע שינויים מקומיים, ליצור ענפים חדשים, ולדחוף אותם חזרה למאגר המקורי (אם יש הרשאות).

**דוגמאות לשימוש נפוץ:**
* כאשר רוצים להתחיל לעבוד על פרויקט קיים מהאינטרנט.
* כאשר רוצים לבדוק קוד של פרויקט לפני שמבצעים בו שינויים.
* כאשר רוצים לבצע שינויים ולתרום אותם חזרה באמצעות Pull Request.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# שכפול בסיסי של מאגר קוד
git clone https://github.com/USERNAME/REPO.git

# שכפול לתיקיה ספציפית
git clone https://github.com/USERNAME/REPO.git my_project_folder

# שכפול ענף ספציפי
git clone -b develop https://github.com/USERNAME/REPO.git

# שכפול רדוד (ללא היסטוריה)
git clone --depth 1 https://github.com/USERNAME/REPO.git

# שכפול עם תת-מודולים
git clone --recursive https://github.com/USERNAME/REPO.git
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

# שכפול בסיסי
repo = Repo.clone_from('https://github.com/USERNAME/REPO.git', 'local_folder')

# שכפול עם הגדרות נוספות
repo = Repo.clone_from(
    'https://github.com/USERNAME/REPO.git',
    'local_folder',
    branch='develop',        # שכפול ענף ספציפי
    depth=1,                # שכפול רדוד
    recursive=True          # כולל תת-מודולים
)

# בדיקת סטטוס אחרי השכפול
print(f"Active branch: {repo.active_branch}")
print(f"Working dir: {repo.working_dir}")

# הצגת רשימת הקבצים במאגר
for root, dirs, files in os.walk(repo.working_dir):
    print(f"\nDirectory: {root}")
    for file in files:
        print(f"  {file}")
```

## מונחים קשורים

* [Repository (מאגר קוד)](./repository.md)
* [Fork (מזלג)](./fork.md)
* [Pull Request (בקשת משיכה)](./pull-request.md)
* [Branch (ענף)](./branch.md)

## מקורות מידע נוספים

* [תיעוד Git על git clone](https://git-scm.com/docs/git-clone)
* [תיעוד GitHub על Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.repo.base.Repo.clone_from)
