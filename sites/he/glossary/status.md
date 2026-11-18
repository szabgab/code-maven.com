 # Status (בדיקת מצב המאגר)

**הגדרה קצרה:** פקודה ב-Git המציגה את המצב הנוכחי של המאגר, כולל מידע על קבצים שעברו שינויים, קבצים שהוכנו ל-commit, וקבצים שלא מנוהלים על ידי Git.

## הסבר מורחב

`Status` (בדיקת מצב המאגר) הוא אחד הפקודות החשובות ביותר ב-Git שמאפשרת לך לראות את המצב הנוכחי של המאגר. הפקודה מציגה מידע על:

* **קבצים שעברו שינויים** (modified files)
* **קבצים שהוכנו ל-commit** (staged files)
* **קבצים שלא מנוהלים** (untracked files)
* **קבצים שנמחקו** (deleted files)
* **ענף נוכחי** (current branch)
* **מצב ביחס לענף מרוחק** (ahead/behind)

היתרונות העיקריים של **Status** הם:
* **סקירה מהירה:** מאפשר לראות במבט אחד מה השתנה במאגר.
* **תכנון:** עוזר לתכנן את השלבים הבאים בעבודה.
* **דיבוג:** עוזר להבין למה דברים לא עובדים כמצופה.
* **בטיחות:** מאפשר לוודא שהכל בסדר לפני commit.

**דוגמאות לשימוש נפוץ:**
* בדיקת מה השתנה לפני commit.
* וידוא שכל הקבצים הנכונים הוכנו ל-commit.
* בדיקת מצב ביחס לענף מרוחק.
* זיהוי קבצים שלא מנוהלים על ידי Git.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת מצב בסיסי
git status

# הצגת מצב בקיצור
git status --short
git status -s

# הצגת מצב עם פירוט מלא
git status --verbose

# הצגת מצב עם קבצים לא מנוהלים
git status --ignored

# הצגת מצב עם קבצים שנמחקו
git status --porcelain

# הצגת מצב עם פורמט JSON
git status --porcelain=2

# הצגת מצב עם קבצים ספציפיים
git status file1.txt file2.txt

# הצגת מצב עם קבצים בתיקיה
git status src/

# הצגת מצב עם קבצים שתאמו ל-pattern
git status "*.js"

# הצגת מצב עם קבצים שתאמו ל-pattern (recursive)
git status "**/*.js"

# הצגת מצב עם קבצים שתאמו ל-pattern (case insensitive)
git status -i "*.TXT"

# הצגת מצב עם קבצים שתאמו ל-pattern (exclude)
git status --exclude="*.log"

# הצגת מצב עם קבצים שתאמו ל-pattern (include)
git status --include="*.py"

# הצגת מצב עם קבצים שתאמו ל-pattern (exclude from .gitignore)
git status --ignored --exclude="*.tmp"

# הצגת מצב עם קבצים שתאמו ל-pattern (include from .gitignore)
git status --ignored --include="*.pyc"
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# הצגת מצב בסיסי
def show_basic_status(repo):
    """הצגת מצב בסיסי של המאגר"""
    print("מצב המאגר:")
    print(f"ענף נוכחי: {repo.active_branch.name}")
    print(f"HEAD: {repo.head.commit.hexsha[:8]}")
    
    # בדיקת שינויים
    if repo.is_dirty():
        print("יש שינויים במאגר")
    else:
        print("המאגר נקי")

# הצגת מצב מפורט
def show_detailed_status(repo):
    """הצגת מצב מפורט של המאגר"""
    print("מצב מפורט:")
    
    # קבצים שהוכנו ל-commit
    staged_files = repo.index.diff('HEAD')
    if staged_files:
        print("\nקבצים שהוכנו ל-commit:")
        for diff in staged_files:
            print(f"  + {diff.a_path}")
    
    # קבצים שעברו שינויים
    unstaged_files = repo.index.diff(None)
    if unstaged_files:
        print("\nקבצים שעברו שינויים:")
        for diff in unstaged_files:
            print(f"  M {diff.a_path}")
    
    # קבצים שלא מנוהלים
    untracked_files = repo.untracked_files
    if untracked_files:
        print("\nקבצים שלא מנוהלים:")
        for file in untracked_files:
            print(f"  ? {file}")

# בדיקת מצב של קובץ ספציפי
def check_file_status(repo, file_path):
    """בדיקת מצב של קובץ ספציפי"""
    try:
        # בדיקה אם הקובץ קיים
        if not os.path.exists(file_path):
            print(f"קובץ {file_path} לא קיים")
            return
        
        # בדיקת מצב הקובץ
        if file_path in repo.untracked_files:
            print(f"{file_path}: לא מנוהל")
        elif file_path in [diff.a_path for diff in repo.index.diff('HEAD')]:
            print(f"{file_path}: הוכן ל-commit")
        elif file_path in [diff.a_path for diff in repo.index.diff(None)]:
            print(f"{file_path}: עבר שינויים")
        else:
            print(f"{file_path}: לא השתנה")
            
    except Exception as e:
        print(f"שגיאה בבדיקת מצב {file_path}: {e}")

# הצגת סטטיסטיקות מצב
def show_status_stats(repo):
    """הצגת סטטיסטיקות מצב המאגר"""
    print("סטטיסטיקות מצב:")
    
    # ספירת קבצים שהוכנו
    staged_count = len(repo.index.diff('HEAD'))
    print(f"קבצים שהוכנו ל-commit: {staged_count}")
    
    # ספירת קבצים שעברו שינויים
    unstaged_count = len(repo.index.diff(None))
    print(f"קבצים שעברו שינויים: {unstaged_count}")
    
    # ספירת קבצים שלא מנוהלים
    untracked_count = len(repo.untracked_files)
    print(f"קבצים שלא מנוהלים: {untracked_count}")
    
    # בדיקת מצב ביחס לענף מרוחק
    try:
        ahead, behind = repo.count_commits()
        if ahead > 0:
            print(f"מקדים את הענף המרוחק ב-{ahead} התחייבויות")
        if behind > 0:
            print(f"מפגר אחרי הענף המרוחק ב-{behind} התחייבויות")
    except:
        print("לא ניתן לבדוק מצב ביחס לענף מרוחק")

# בדיקת מצב עם פילטרים
def show_filtered_status(repo, file_pattern=None, include_ignored=False):
    """הצגת מצב עם פילטרים"""
    print("מצב עם פילטרים:")
    
    if file_pattern:
        print(f"פילטר: {file_pattern}")
    
    # קבצים שהוכנו
    staged_files = [f for f in repo.index.diff('HEAD') 
                   if not file_pattern or file_pattern in f.a_path]
    if staged_files:
        print("\nקבצים שהוכנו:")
        for diff in staged_files:
            print(f"  + {diff.a_path}")
    
    # קבצים שעברו שינויים
    unstaged_files = [f for f in repo.index.diff(None) 
                     if not file_pattern or file_pattern in f.a_path]
    if unstaged_files:
        print("\nקבצים שעברו שינויים:")
        for diff in unstaged_files:
            print(f"  M {diff.a_path}")
    
    # קבצים שלא מנוהלים
    untracked_files = [f for f in repo.untracked_files 
                      if not file_pattern or file_pattern in f]
    if untracked_files:
        print("\nקבצים שלא מנוהלים:")
        for file in untracked_files:
            print(f"  ? {file}")

# דוגמה לשימוש
if __name__ == "__main__":
    # הצגת מצב בסיסי
    show_basic_status(repo)
    
    # הצגת מצב מפורט
    show_detailed_status(repo)
    
    # הצגת סטטיסטיקות
    show_status_stats(repo)
    
    # בדיקת מצב של קובץ ספציפי
    check_file_status(repo, "README.md")
    
    # הצגת מצב עם פילטר
    show_filtered_status(repo, ".py")
```

## מונחים קשורים

* [Working Directory (אזור העבודה)](./working-directory.md)
* [Staging Area (אזור ההכנה)](./staging.md)
* [Commit (התחייבות)](./commit.md)
* [Add (הוספה)](./add.md)
* [Diff (הבדלים)](./diff.md)

## מקורות מידע נוספים

* [תיעוד Git על git status](https://git-scm.com/docs/git-status)
* [Git Status Tutorial](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.repo.base.Repo.is_dirty)
* [Understanding Git Status](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_checking_status)