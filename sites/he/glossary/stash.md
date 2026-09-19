 # Stash (שמירה זמנית)

**הגדרה קצרה:** פעולה ב-Git המאפשרת לשמור שינויים זמניים (uncommitted changes) בצד, כדי לנקות את אזור העבודה (working directory) ולאפשר מעבר לענף אחר או ביצוע פעולות אחרות, ולאחר מכן להחזיר את השינויים.

## הסבר מורחב

`Stash` (שמירה זמנית) הוא כלי שימושי ב-Git כאשר יש לך שינויים שעדיין לא התחייבת אליהם, ואתה צריך לעבור לענף אחר או לבצע פעולה אחרת. במקום לבצע commit לא מוכן או לאבד את השינויים, Git מאפשר לך לשמור אותם זמנית ב"מחסנית" (stash).

היתרונות העיקריים של **Stash** הם:
* **גמישות בעבודה:** מאפשר מעבר מהיר בין ענפים ללא איבוד עבודה.
* **ניקוי אזור העבודה:** מאפשר לבצע פעולות Git אחרות על מאגר נקי.
* **שמירה זמנית:** שומר שינויים ללא יצירת commit רשמי.
* **ניהול שינויים:** מאפשר לחזור לשינויים מאוחר יותר.

**דוגמאות לשימוש נפוץ:**
* כאשר יש שינויים לא מוכנים ואתה צריך לעבור לענף אחר לתיקון דחוף.
* כאשר אתה רוצה לבצע pull או merge על מאגר נקי.
* כאשר אתה רוצה לשמור עבודה זמנית לפני ניסוי או שינוי גדול.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# שמירה זמנית של כל השינויים
git stash

# שמירה זמנית עם הודעה מתארת
git stash push -m "עבודה על פיצ'ר חדש"

# הצגת רשימת השמירות הזמניות
git stash list

# החזרת השמירה הזמנית האחרונה
git stash pop

# החזרת שמירה זמנית ספציפית
git stash apply stash@{1}

# הצגת תוכן השמירה הזמנית
git stash show stash@{0}

# הצגת diff של השמירה הזמנית
git stash show -p stash@{0}

# מחיקת שמירה זמנית
git stash drop stash@{0}

# מחיקת כל השמירות הזמניות
git stash clear

# שמירה זמנית של קבצים ספציפיים
git stash push file1.txt file2.txt

# שמירה זמנית כולל קבצים לא מנוהלים (untracked)
git stash -u
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# שמירה זמנית של שינויים
stash = repo.git.stash()

# שמירה זמנית עם הודעה
stash = repo.git.stash('push', '-m', 'עבודה על פיצ\'ר חדש')

# הצגת רשימת השמירות הזמניות
stash_list = repo.git.stash('list')
print("רשימת שמירות זמניות:")
for line in stash_list.split('\n'):
    if line.strip():
        print(f"  {line}")

# החזרת השמירה הזמנית האחרונה
repo.git.stash('pop')

# החזרת שמירה זמנית ספציפית
repo.git.stash('apply', 'stash@{1}')

# בדיקת מצב המאגר לפני ואחרי stash
print("מצב לפני stash:")
print(repo.git.status())

# שמירה זמנית
repo.git.stash()

print("מצב אחרי stash:")
print(repo.git.status())

# החזרת השמירה הזמנית
repo.git.stash('pop')

print("מצב אחרי החזרת stash:")
print(repo.git.status())
```

## מונחים קשורים

* [Commit (התחייבות)](./commit.md)
* [Branch (ענף)](./branch.md)
* [Checkout (מעבר)](./checkout.md)
* [Status (מצב)](./status.md)
* [Diff (הבדלים)](./diff.md)

## מקורות מידע נוספים

* [תיעוד Git על git stash](https://git-scm.com/docs/git-stash)
* [Git Stash Tutorial](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.stash)