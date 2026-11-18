 # Log (הצגת היסטוריית התחייבויות)

**הגדרה קצרה:** פקודה ב-Git המציגה את היסטוריית ההתחייבויות (commits) במאגר, כולל פרטים כמו זיהוי ההתחייבות, המחבר, התאריך וההודעה.

## הסבר מורחב

`Log` (הצגת היסטוריית התחייבויות) הוא כלי חיוני ב-Git שמאפשר לך לחקור את ההיסטוריה של המאגר. הפקודה מציגה מידע מפורט על כל ההתחייבויות, כולל:

* **זיהוי ההתחייבות** (commit hash)
* **מחבר ההתחייבות** (author)
* **תאריך ההתחייבות**
* **הודעת ההתחייבות** (commit message)
* **היסטוריית השינויים** (מה השתנה)

היתרונות העיקריים של **Log** הם:
* **חקירה:** מאפשר להבין איך המאגר התפתח לאורך זמן.
* **דיבוג:** עוזר למצוא מתי ואיפה הוכנס באג.
* **תיעוד:** מספק תיעוד של השינויים שנעשו.
* **שיתוף פעולה:** מאפשר להבין מה אחרים עשו במאגר.

**דוגמאות לשימוש נפוץ:**
* בדיקת היסטוריית שינויים בקובץ ספציפי.
* מציאת התחייבות שבה הוכנס באג.
* הבנת התפתחות פיצ'ר מסוים.
* בדיקת פעילות של מפתח ספציפי.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת היסטוריה בסיסית
git log

# הצגת היסטוריה בקיצור (על שורה אחת)
git log --oneline

# הצגת היסטוריה עם גרף
git log --graph --oneline --all

# הצגת היסטוריה עם פרטים מפורטים
git log --stat

# הצגת היסטוריה עם diff
git log -p

# הצגת היסטוריה של קובץ ספציפי
git log -- file.txt
git log --follow -- file.txt

# הצגת היסטוריה של מפתח ספציפי
git log --author="שם המפתח"

# הצגת היסטוריה לפי תאריך
git log --since="2023-01-01" --until="2023-12-31"

# הצגת היסטוריה עם מספר התחייבויות מוגבל
git log -n 10

# הצגת היסטוריה עם פורמט מותאם אישית
git log --pretty=format:"%h - %an, %ar : %s"

# הצגת היסטוריה עם תגיות
git log --decorate

# הצגת היסטוריה עם שינויים
git log --name-status

# הצגת היסטוריה עם מספר השורות שהשתנו
git log --numstat

# הצגת היסטוריה עם חיפוש בהודעות
git log --grep="באג"

# הצגת היסטוריה עם חיפוש בתוכן
git log -S "פונקציה"

# הצגת היסטוריה עם פילטור לפי סוג שינוי
git log --merges
git log --no-merges
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
from datetime import datetime, timedelta

repo = Repo('my_repo')

# הצגת היסטוריה בסיסית
def show_basic_log(repo, max_count=10):
    """הצגת היסטוריה בסיסית"""
    print("היסטוריית התחייבויות:")
    for commit in repo.iter_commits('HEAD', max_count=max_count):
        print(f"  {commit.hexsha[:8]} - {commit.author.name}: {commit.message.strip()}")

# הצגת היסטוריה מפורטת
def show_detailed_log(repo, max_count=5):
    """הצגת היסטוריה מפורטת"""
    print("היסטוריה מפורטת:")
    for commit in repo.iter_commits('HEAD', max_count=max_count):
        print(f"\nהתחייבות: {commit.hexsha}")
        print(f"מחבר: {commit.author.name} <{commit.author.email}>")
        print(f"תאריך: {commit.authored_datetime}")
        print(f"הודעה: {commit.message.strip()}")
        print(f"הורים: {[p.hexsha[:8] for p in commit.parents]}")

# הצגת היסטוריה של קובץ ספציפי
def show_file_log(repo, file_path, max_count=10):
    """הצגת היסטוריה של קובץ ספציפי"""
    try:
        print(f"היסטוריה של {file_path}:")
        for commit in repo.iter_commits('HEAD', paths=file_path, max_count=max_count):
            print(f"  {commit.hexsha[:8]} - {commit.message.strip()}")
    except Exception as e:
        print(f"שגיאה בהצגת היסטוריה של {file_path}: {e}")

# הצגת היסטוריה של מפתח ספציפי
def show_author_log(repo, author_name, max_count=10):
    """הצגת היסטוריה של מפתח ספציפי"""
    print(f"התחייבויות של {author_name}:")
    for commit in repo.iter_commits('HEAD', author=author_name, max_count=max_count):
        print(f"  {commit.hexsha[:8]} - {commit.message.strip()}")

# הצגת היסטוריה לפי תאריך
def show_date_range_log(repo, since_date, until_date=None):
    """הצגת היסטוריה בטווח תאריכים"""
    if until_date is None:
        until_date = datetime.now()
    
    print(f"התחייבויות מ-{since_date} עד {until_date}:")
    for commit in repo.iter_commits('HEAD', since=since_date, until=until_date):
        print(f"  {commit.hexsha[:8]} - {commit.authored_datetime.date()} - {commit.message.strip()}")

# חיפוש התחייבויות לפי תוכן
def search_commits_by_content(repo, search_term, max_count=10):
    """חיפוש התחייבויות לפי תוכן"""
    print(f"התחייבויות המכילות '{search_term}':")
    for commit in repo.iter_commits('HEAD', max_count=max_count):
        if search_term.lower() in commit.message.lower():
            print(f"  {commit.hexsha[:8]} - {commit.message.strip()}")

# הצגת סטטיסטיקות
def show_commit_stats(repo, max_count=50):
    """הצגת סטטיסטיקות התחייבויות"""
    commits = list(repo.iter_commits('HEAD', max_count=max_count))
    
    # ספירת התחייבויות לפי מחבר
    authors = {}
    for commit in commits:
        author = commit.author.name
        authors[author] = authors.get(author, 0) + 1
    
    print("סטטיסטיקות התחייבויות:")
    print(f"סה"כ התחייבויות: {len(commits)}")
    print("\nהתחייבויות לפי מחבר:")
    for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
        print(f"  {author}: {count}")

# הצגת היסטוריה עם גרף
def show_graph_log(repo, max_count=20):
    """הצגת היסטוריה עם גרף"""
    print("היסטוריה עם גרף:")
    for commit in repo.iter_commits('HEAD', max_count=max_count):
        # יצירת גרף פשוט
        level = len(list(commit.parents))
        indent = "  " * level
        print(f"{indent}* {commit.hexsha[:8]} - {commit.message.strip()}")

# דוגמה לשימוש
if __name__ == "__main__":
    # הצגת היסטוריה בסיסית
    show_basic_log(repo, 5)
    
    # הצגת היסטוריה מפורטת
    show_detailed_log(repo, 3)
    
    # הצגת היסטוריה של קובץ ספציפי
    show_file_log(repo, "README.md", 5)
    
    # הצגת היסטוריה לפי תאריך
    week_ago = datetime.now() - timedelta(days=7)
    show_date_range_log(repo, week_ago)
    
    # חיפוש התחייבויות
    search_commits_by_content(repo, "באג", 10)
    
    # הצגת סטטיסטיקות
    show_commit_stats(repo, 20)
```

## מונחים קשורים

* [Commit (התחייבות)](./commit.md)
* [Branch (ענף)](./branch.md)
* [Diff (הבדלים)](./diff.md)
* [Blame (האשמה)](./blame.md)
* [History (היסטוריה)](./history.md)

## מקורות מידע נוספים

* [תיעוד Git על git log](https://git-scm.com/docs/git-log)
* [Git Log Tutorial](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.repo.base.Repo.iter_commits)
* [Advanced Git Log Formatting](https://git-scm.com/docs/git-log#_pretty_formats)