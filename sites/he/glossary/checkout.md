 # Checkout (מעבר)

**הגדרה קצרה:** פעולה ב-Git המאפשרת לעבור בין ענפים שונים, התחייבויות שונות או קבצים ספציפיים, תוך עדכון אזור העבודה (working directory) למצב הרצוי.

## הסבר מורחב

`Checkout` (מעבר) הוא אחד הפקודות הבסיסיות והחשובות ביותר ב-Git. היא מאפשרת לך לעבור בין מצבים שונים במאגר:

1. **מעבר לענף אחר** - שינוי הענף הפעיל
2. **מעבר להתחייבות ספציפית** - חזרה לנקודה בהיסטוריה
3. **מעבר לקובץ ספציפי** - שחזור קובץ לגרסה קודמת
4. **יצירת ענף חדש** - יצירת ענף חדש ומעבר אליו

היתרונות העיקריים של **Checkout** הם:
* **גמישות:** מאפשר מעבר מהיר בין מצבים שונים במאגר.
* **בטיחות:** שומר על שינויים לא מוכנים (אם אפשר).
* **נוחות:** מאפשר לבדוק קוד ללא שינוי הענף הפעיל.
* **יצירתיות:** מאפשר ליצור ענפים חדשים בקלות.

**דוגמאות לשימוש נפוץ:**
* מעבר לענף אחר כדי לעבוד על פיצ'ר חדש.
* חזרה להתחייבות קודמת כדי לבדוק קוד.
* יצירת ענף חדש מתוך ענף קיים.
* שחזור קובץ לגרסה קודמת.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# מעבר לענף קיים
git checkout main
git checkout develop
git checkout feature/new-feature

# יצירת ענף חדש ומעבר אליו
git checkout -b feature/new-feature
git checkout -b hotfix/bug-fix main

# מעבר להתחייבות ספציפית
git checkout abc1234
git checkout HEAD~1

# מעבר לקובץ ספציפי (שחזור לגרסה אחרונה)
git checkout HEAD -- file.txt
git checkout HEAD -- src/

# מעבר לקובץ מהתחייבות ספציפית
git checkout abc1234 -- file.txt

# מעבר לענף מרוחק
git checkout -b local-branch origin/remote-branch

# מעבר לענף עם מעקב אחרי ענף מרוחק
git checkout --track origin/feature-branch

# מעבר לענף אחר עם שמירת שינויים
git checkout -m feature-branch

# מעבר לענף אחר עם stash אוטומטי
git checkout -m feature-branch && git stash

# מעבר לענף אחר עם commit אוטומטי
git checkout -m feature-branch && git commit -m "WIP"

# בדיקת ענף נוכחי
git checkout --show-current

# מעבר לענף אחר עם אימות
git checkout --verify-signatures main
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# מעבר לענף קיים
def checkout_branch(repo, branch_name):
    """מעבר לענף קיים"""
    try:
        repo.git.checkout(branch_name)
        print(f"עברת לענף {branch_name}")
        return True
    except Exception as e:
        print(f"שגיאה במעבר לענף {branch_name}: {e}")
        return False

# יצירת ענף חדש ומעבר אליו
def create_and_checkout_branch(repo, new_branch, base_branch='HEAD'):
    """יצירת ענף חדש ומעבר אליו"""
    try:
        repo.git.checkout('-b', new_branch, base_branch)
        print(f"נוצר ענף חדש {new_branch} ועברת אליו")
        return True
    except Exception as e:
        print(f"שגיאה ביצירת ענף {new_branch}: {e}")
        return False

# מעבר להתחייבות ספציפית
def checkout_commit(repo, commit_hash):
    """מעבר להתחייבות ספציפית"""
    try:
        repo.git.checkout(commit_hash)
        print(f"עברת להתחייבות {commit_hash[:8]}")
        return True
    except Exception as e:
        print(f"שגיאה במעבר להתחייבות {commit_hash}: {e}")
        return False

# שחזור קובץ לגרסה אחרונה
def restore_file(repo, file_path):
    """שחזור קובץ לגרסה אחרונה"""
    try:
        repo.git.checkout('HEAD', '--', file_path)
        print(f"קובץ {file_path} שוחזר לגרסה אחרונה")
        return True
    except Exception as e:
        print(f"שגיאה בשחזור {file_path}: {e}")
        return False

# מעבר לענף עם שמירת שינויים
def safe_checkout(repo, branch_name):
    """מעבר בטוח לענף עם שמירת שינויים"""
    try:
        # בדיקה אם יש שינויים לא מוכנים
        if repo.is_dirty():
            print("יש שינויים לא מוכנים, שומר כ-stash...")
            repo.git.stash()
            repo.git.checkout(branch_name)
            print(f"עברת לענף {branch_name}, השינויים נשמרו ב-stash")
        else:
            repo.git.checkout(branch_name)
            print(f"עברת לענף {branch_name}")
        return True
    except Exception as e:
        print(f"שגיאה במעבר בטוח: {e}")
        return False

# בדיקת ענפים זמינים
def list_branches(repo):
    """הצגת רשימת ענפים זמינים"""
    branches = []
    for branch in repo.branches:
        branches.append(branch.name)
    
    print("ענפים זמינים:")
    for branch in branches:
        if branch == repo.active_branch.name:
            print(f"  * {branch} (נוכחי)")
        else:
            print(f"    {branch}")
    
    return branches

# מעבר לענף מרוחק
def checkout_remote_branch(repo, remote_branch):
    """מעבר לענף מרוחק"""
    try:
        # יצירת ענף מקומי עם מעקב אחרי הענף המרוחק
        local_branch = remote_branch.replace('origin/', '')
        repo.git.checkout('-b', local_branch, remote_branch)
        print(f"עברת לענף מרוחק {remote_branch} כענף מקומי {local_branch}")
        return True
    except Exception as e:
        print(f"שגיאה במעבר לענף מרוחק {remote_branch}: {e}")
        return False

# דוגמה לשימוש
if __name__ == "__main__":
    # הצגת ענף נוכחי
    current_branch = repo.active_branch.name
    print(f"ענף נוכחי: {current_branch}")
    
    # הצגת ענפים זמינים
    available_branches = list_branches(repo)
    
    # דוגמה: יצירת ענף חדש
    new_feature = "feature/user-authentication"
    if create_and_checkout_branch(repo, new_feature):
        print(f"עובד על פיצ'ר חדש: {new_feature}")
    
    # דוגמה: שחזור קובץ
    if restore_file(repo, "config.json"):
        print("קובץ config.json שוחזר")
    
    # דוגמה: מעבר בטוח לענף אחר
    if safe_checkout(repo, "main"):
        print("חזרת לענף main")
```

## מונחים קשורים

* [Branch (ענף)](./branch.md)
* [Commit (התחייבות)](./commit.md)
* [HEAD (ראש המאגר)](./head.md)
* [Working Directory (אזור העבודה)](./working-directory.md)
* [Stash (שמירה זמנית)](./stash.md)

## מקורות מידע נוספים

* [תיעוד Git על git checkout](https://git-scm.com/docs/git-checkout)
* [Git Checkout Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.checkout)
* [Understanding Git Checkout](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_branching)