 # Diff (הצגת הבדלים)

**הגדרה קצרה:** פקודה ב-Git המציגה את ההבדלים בין גרסאות שונות של קבצים, בין ענפים, או בין התחייבויות שונות, במטרה להבין מה השתנה.

## הסבר מורחב

`Diff` (הצגת הבדלים) הוא כלי חיוני ב-Git שמאפשר לך לראות את ההבדלים בין מצבים שונים במאגר. הפקודה מציגה:

* **שורות שנוספו** (marked with +)
* **שורות שנמחקו** (marked with -)
* **שורות שלא השתנו** (context lines)
* **מידע על הקובץ** (file path, mode changes)

היתרונות העיקריים של **Diff** הם:
* **בדיקת שינויים:** מאפשר לראות בדיוק מה השתנה.
* **דיבוג:** עוזר למצוא באגים ולהבין מה השתבש.
* **בקרת איכות:** מאפשר לבדוק שינויים לפני commit.
* **תיעוד:** מספק תיעוד ויזואלי של השינויים.

**דוגמאות לשימוש נפוץ:**
* בדיקת שינויים לפני commit.
* השוואה בין ענפים שונים.
* בדיקת שינויים של התחייבות ספציפית.
* השוואה בין גרסאות שונות של קובץ.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת הבדלים בין working directory ל-staging area
git diff

# הצגת הבדלים בין staging area ל-HEAD
git diff --staged
git diff --cached

# הצגת הבדלים בין שתי התחייבויות
git diff commit1 commit2
git diff HEAD~1 HEAD

# הצגת הבדלים בין ענפים
git diff main feature-branch

# הצגת הבדלים של קובץ ספציפי
git diff file.txt
git diff -- file.txt

# הצגת הבדלים עם פורמט מותאם אישית
git diff --word-diff
git diff --color-words

# הצגת הבדלים עם מספר שורות context
git diff -U5
git diff --unified=10

# הצגת הבדלים עם פורמט קצר
git diff --stat

# הצגת הבדלים עם פורמט מפורט
git diff --numstat

# הצגת הבדלים עם פורמט JSON
git diff --porcelain

# הצגת הבדלים עם פורמט patch
git diff --patch

# הצגת הבדלים עם פורמט side-by-side
git diff --side-by-side

# הצגת הבדלים עם פורמט word-by-word
git diff --word-diff=color

# הצגת הבדלים עם פורמט line-by-line
git diff --word-diff=plain

# הצגת הבדלים עם פורמט character-by-character
git diff --word-diff=porcelain

# הצגת הבדלים עם פורמט unified
git diff --unified=3

# הצגת הבדלים עם פורמט context
git diff --context=3

# הצגת הבדלים עם פורמט ed
git diff --ed

# הצגת הבדלים עם פורמט rcs
git diff --rcs

# הצגת הבדלים עם פורמט summary
git diff --summary

# הצגת הבדלים עם פורמט name-only
git diff --name-only

# הצגת הבדלים עם פורמט name-status
git diff --name-status

# הצגת הבדלים עם פורמט raw
git diff --raw

# הצגת הבדלים עם פורמט binary
git diff --binary

# הצגת הבדלים עם פורמט text
git diff --text

# הצגת הבדלים עם פורמט ignore-space-change
git diff --ignore-space-change

# הצגת הבדלים עם פורמט ignore-all-space
git diff --ignore-all-space

# הצגת הבדלים עם פורמט ignore-blank-lines
git diff --ignore-blank-lines

# הצגת הבדלים עם פורמט ignore-cr-at-eol
git diff --ignore-cr-at-eol

# הצגת הבדלים עם פורמט ignore-space-at-eol
git diff --ignore-space-at-eol

# הצגת הבדלים עם פורמט ignore-trailing-space
git diff --ignore-trailing-space

# הצגת הבדלים עם פורמט ignore-leading-space
git diff --ignore-leading-space

# הצגת הבדלים עם פורמט ignore-space-at-eol
git diff --ignore-space-at-eol

# הצגת הבדלים עם פורמט ignore-cr-at-eol
git diff --ignore-cr-at-eol

# הצגת הבדלים עם פורמט ignore-blank-lines
git diff --ignore-blank-lines

# הצגת הבדלים עם פורמט ignore-all-space
git diff --ignore-all-space

# הצגת הבדלים עם פורמט ignore-space-change
git diff --ignore-space-change

# הצגת הבדלים עם פורמט text
git diff --text

# הצגת הבדלים עם פורמט binary
git diff --binary

# הצגת הבדלים עם פורמט raw
git diff --raw

# הצגת הבדלים עם פורמט name-status
git diff --name-status

# הצגת הבדלים עם פורמט name-only
git diff --name-only

# הצגת הבדלים עם פורמט summary
git diff --summary

# הצגת הבדלים עם פורמט rcs
git diff --rcs

# הצגת הבדלים עם פורמט ed
git diff --ed

# הצגת הבדלים עם פורמט context
git diff --context=3

# הצגת הבדלים עם פורמט unified
git diff --unified=3

# הצגת הבדלים עם פורמט character-by-character
git diff --word-diff=porcelain

# הצגת הבדלים עם פורמט line-by-line
git diff --word-diff=plain

# הצגת הבדלים עם פורמט word-by-word
git diff --word-diff=color

# הצגת הבדלים עם פורמט side-by-side
git diff --side-by-side

# הצגת הבדלים עם פורמט patch
git diff --patch

# הצגת הבדלים עם פורמט porcelain
git diff --porcelain

# הצגת הבדלים עם פורמט מפורט
git diff --numstat

# הצגת הבדלים עם פורמט קצר
git diff --stat

# הצגת הבדלים עם פורמט word-by-word
git diff --word-diff

# הצגת הבדלים עם פורמט מותאם אישית
git diff --color-words

# הצגת הבדלים של קובץ ספציפי
git diff -- file.txt

# הצגת הבדלים של קובץ ספציפי
git diff file.txt

# הצגת הבדלים בין ענפים
git diff feature-branch

# הצגת הבדלים בין ענפים
git diff main feature-branch

# הצגת הבדלים בין שתי התחייבויות
git diff HEAD~1 HEAD

# הצגת הבדלים בין שתי התחייבויות
git diff commit1 commit2

# הצגת הבדלים בין staging area ל-HEAD
git diff --cached

# הצגת הבדלים בין staging area ל-HEAD
git diff --staged

# הצגת הבדלים בין working directory ל-staging area
git diff
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# הצגת הבדלים בסיסיים
def show_basic_diff(repo):
    """הצגת הבדלים בסיסיים"""
    try:
        diff = repo.git.diff()
        if diff:
            print("הבדלים בין working directory ל-staging area:")
            print(diff)
        else:
            print("אין הבדלים")
    except Exception as e:
        print(f"שגיאה בהצגת הבדלים: {e}")

# הצגת הבדלים של קובץ ספציפי
def show_file_diff(repo, file_path):
    """הצגת הבדלים של קובץ ספציפי"""
    try:
        diff = repo.git.diff('--', file_path)
        if diff:
            print(f"הבדלים בקובץ {file_path}:")
            print(diff)
        else:
            print(f"אין הבדלים בקובץ {file_path}")
    except Exception as e:
        print(f"שגיאה בהצגת הבדלים של {file_path}: {e}")

# הצגת הבדלים בין התחייבויות
def show_commit_diff(repo, commit1, commit2):
    """הצגת הבדלים בין שתי התחייבויות"""
    try:
        diff = repo.git.diff(commit1, commit2)
        if diff:
            print(f"הבדלים בין {commit1[:8]} ל-{commit2[:8]}:")
            print(diff)
        else:
            print("אין הבדלים בין ההתחייבויות")
    except Exception as e:
        print(f"שגיאה בהצגת הבדלים בין התחייבויות: {e}")

# הצגת הבדלים בין ענפים
def show_branch_diff(repo, branch1, branch2):
    """הצגת הבדלים בין שני ענפים"""
    try:
        diff = repo.git.diff(branch1, branch2)
        if diff:
            print(f"הבדלים בין ענף {branch1} לענף {branch2}:")
            print(diff)
        else:
            print("אין הבדלים בין הענפים")
    except Exception as e:
        print(f"שגיאה בהצגת הבדלים בין ענפים: {e}")

# הצגת הבדלים עם סטטיסטיקות
def show_diff_stats(repo):
    """הצגת הבדלים עם סטטיסטיקות"""
    try:
        stats = repo.git.diff('--stat')
        if stats:
            print("סטטיסטיקות הבדלים:")
            print(stats)
        else:
            print("אין הבדלים")
    except Exception as e:
        print(f"שגיאה בהצגת סטטיסטיקות: {e}")

# הצגת הבדלים עם פורמט מותאם אישית
def show_custom_diff(repo, format_type='word-diff'):
    """הצגת הבדלים עם פורמט מותאם אישית"""
    try:
        if format_type == 'word-diff':
            diff = repo.git.diff('--word-diff')
        elif format_type == 'stat':
            diff = repo.git.diff('--stat')
        elif format_type == 'name-only':
            diff = repo.git.diff('--name-only')
        else:
            diff = repo.git.diff()
        
        if diff:
            print(f"הבדלים בפורמט {format_type}:")
            print(diff)
        else:
            print("אין הבדלים")
    except Exception as e:
        print(f"שגיאה בהצגת הבדלים בפורמט {format_type}: {e}")

# דוגמה לשימוש
if __name__ == "__main__":
    # הצגת הבדלים בסיסיים
    show_basic_diff(repo)
    
    # הצגת הבדלים של קובץ ספציפי
    show_file_diff(repo, "README.md")
    
    # הצגת הבדלים בין התחייבויות
    commits = list(repo.iter_commits('HEAD', max_count=2))
    if len(commits) >= 2:
        show_commit_diff(repo, commits[1].hexsha, commits[0].hexsha)
    
    # הצגת הבדלים בין ענפים
    show_branch_diff(repo, "main", "develop")
    
    # הצגת סטטיסטיקות
    show_diff_stats(repo)
    
    # הצגת הבדלים בפורמטים שונים
    show_custom_diff(repo, 'word-diff')
    show_custom_diff(repo, 'stat')
    show_custom_diff(repo, 'name-only')
```

## מונחים קשורים

* [Status (מצב)](./status.md)
* [Commit (התחייבות)](./commit.md)
* [Branch (ענף)](./branch.md)
* [Staging Area (אזור ההכנה)](./staging.md)
* [Working Directory (אזור העבודה)](./working-directory.md)

## מקורות מידע נוספים

* [תיעוד Git על git diff](https://git-scm.com/docs/git-diff)
* [Git Diff Tutorial](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.diff)
* [Understanding Git Diff](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_viewing_changes)