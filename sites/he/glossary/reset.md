# Reset (איפוס מצב המאגר)

**הגדרה קצרה:** פעולה ב-Git המאפשרת לחזור למצב קודם של המאגר, על ידי איפוס ה-HEAD, אזור העבודה (working directory) ו/או אזור ההכנה (staging area) לנקודה ספציפית בהיסטוריה.

## הסבר מורחב

`Reset` (איפוס מצב המאגר) הוא כלי חזק ב-Git שמאפשר לחזור למצב קודם של המאגר. יש שלושה סוגים עיקריים של reset:

1. **Soft Reset** (`--soft`): איפוס ה-HEAD בלבד, שומר שינויים ב-staging area
2. **Mixed Reset** (`--mixed`, ברירת מחדל): איפוס HEAD ו-staging area, שומר שינויים ב-working directory
3. **Hard Reset** (`--hard`): איפוס מלא - HEAD, staging area ו-working directory

היתרונות העיקריים של **Reset** הם:
* **בטיחות:** מאפשר לחזור למצב קודם ללא איבוד מידע.
* **גמישות:** שלושה סוגי reset שונים למצבים שונים.
* **ניקוי:** מאפשר לנקות שינויים לא רצויים.
* **שליטה:** מאפשר לעצב מחדש את ההיסטוריה.

**דוגמאות לשימוש נפוץ:**
* ביטול התחייבות אחרונה עם שמירת השינויים.
* ניקוי staging area לפני commit חדש.
* חזרה למצב נקי לפני ניסוי.
* ביטול merge או rebase כושל.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# reset soft - איפוס HEAD בלבד, שומר שינויים ב-staging area
git reset --soft HEAD~1

# reset mixed (ברירת מחדל) - איפוס HEAD ו-staging area
git reset HEAD~1
git reset --mixed HEAD~1

# reset hard - איפוס מלא, מסיר כל השינויים
git reset --hard HEAD~1

# reset לזיהוי ספציפי
git reset --hard abc1234

# reset של קובץ ספציפי
git reset HEAD file.txt

# reset של קובץ ספציפי עם hard
git reset --hard HEAD file.txt

# reset לזיהוי מרוחק
git reset --hard origin/main

# reset עם שמירת שינויים כ-stash
git reset --soft HEAD~1 && git stash

# reset של staging area בלבד
git reset

# reset עם הודעה על השינויים
git reset --hard HEAD~1 --quiet

# reset עם אימות
git reset --hard HEAD~1 --verify-signatures
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# reset בסיסי
def soft_reset(repo, commit_hash):
    """ביצוע soft reset - איפוס HEAD בלבד"""
    try:
        repo.git.reset('--soft', commit_hash)
        print(f"Soft reset ל-{commit_hash} הושלם בהצלחה")
        return True
    except Exception as e:
        print(f"שגיאה ב-soft reset: {e}")
        return False

def mixed_reset(repo, commit_hash):
    """ביצוע mixed reset - איפוס HEAD ו-staging area"""
    try:
        repo.git.reset('--mixed', commit_hash)
        print(f"Mixed reset ל-{commit_hash} הושלם בהצלחה")
        return True
    except Exception as e:
        print(f"שגיאה ב-mixed reset: {e}")
        return False

def hard_reset(repo, commit_hash):
    """ביצוע hard reset - איפוס מלא"""
    try:
        repo.git.reset('--hard', commit_hash)
        print(f"Hard reset ל-{commit_hash} הושלם בהצלחה")
        return True
    except Exception as e:
        print(f"שגיאה ב-hard reset: {e}")
        return False

# reset של קובץ ספציפי
def reset_file(repo, file_path, hard=False):
    """איפוס קובץ ספציפי"""
    try:
        if hard:
            repo.git.reset('--hard', 'HEAD', '--', file_path)
        else:
            repo.git.reset('HEAD', '--', file_path)
        print(f"Reset של {file_path} הושלם")
        return True
    except Exception as e:
        print(f"שגיאה ב-reset של {file_path}: {e}")
        return False

# בדיקת מצב לפני ואחרי reset
def check_reset_status(repo, commit_hash, reset_type='mixed'):
    """בדיקת מצב המאגר לפני ואחרי reset"""
    print(f"מצב לפני {reset_type} reset:")
    print(f"HEAD: {repo.head.commit.hexsha[:8]}")
    print(f"Staging area: {len(repo.index.diff('HEAD'))} שינויים")
    print(f"Working directory: {len(repo.untracked_files)} קבצים לא מנוהלים")
    
    try:
        # ביצוע reset
        if reset_type == 'soft':
            repo.git.reset('--soft', commit_hash)
        elif reset_type == 'hard':
            repo.git.reset('--hard', commit_hash)
        else:
            repo.git.reset('--mixed', commit_hash)
        
        print(f"\nמצב אחרי {reset_type} reset:")
        print(f"HEAD: {repo.head.commit.hexsha[:8]}")
        print(f"Staging area: {len(repo.index.diff('HEAD'))} שינויים")
        print(f"Working directory: {len(repo.untracked_files)} קבצים לא מנוהלים")
        
    except Exception as e:
        print(f"שגיאה ב-reset: {e}")

# reset עם גיבוי
def safe_reset(repo, commit_hash, reset_type='mixed'):
    """ביצוע reset בטוח עם גיבוי"""
    try:
        # יצירת ענף גיבוי
        backup_branch = f"backup-{repo.head.commit.hexsha[:8]}"
        repo.git.checkout('-b', backup_branch)
        
        # חזרה לענף המקורי
        repo.git.checkout('-')
        
        # ביצוע reset
        if reset_type == 'soft':
            repo.git.reset('--soft', commit_hash)
        elif reset_type == 'hard':
            repo.git.reset('--hard', commit_hash)
        else:
            repo.git.reset('--mixed', commit_hash)
        
        print(f"Reset בטוח הושלם. גיבוי נשמר בענף {backup_branch}")
        return True
        
    except Exception as e:
        print(f"שגיאה ב-reset בטוח: {e}")
        return False

# דוגמה לשימוש
if __name__ == "__main__":
    # בדיקת התחייבויות אחרונות
    print("התחייבויות אחרונות:")
    for commit in repo.iter_commits('HEAD', max_count=5):
        print(f"  {commit.hexsha[:8]} - {commit.message.strip()}")
    
    # דוגמה: ביטול התחייבות אחרונה עם שמירת שינויים
    last_commit = repo.head.commit.parents[0].hexsha
    if soft_reset(repo, last_commit):
        print("התחייבות אחרונה בוטלה, השינויים נשמרו ב-staging area")
    
    # דוגמה: ניקוי staging area
    if mixed_reset(repo, 'HEAD'):
        print("Staging area נוקתה")
    
    # דוגמה: reset מלא למצב נקי
    if hard_reset(repo, 'HEAD'):
        print("מאגר אופס למצב נקי")
```

## מונחים קשורים

* [Commit (התחייבות)](./commit.md)
* [HEAD (ראש המאגר)](./head.md)
* [Staging Area (אזור ההכנה)](./staging.md)
* [Working Directory (אזור העבודה)](./working-directory.md)
* [Stash (שמירה זמנית)](./stash.md)

## מקורות מידע נוספים

* [תיעוד Git על git reset](https://git-scm.com/docs/git-reset)
* [Git Reset Tutorial](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.reset)
* [Understanding Git Reset](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified#_git_reset) 