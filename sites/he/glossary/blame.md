# Blame (הצגת מי שינה כל שורה)

**הגדרה קצרה:** פקודה ב-Git המציגה מי שינה כל שורה בקובץ, כולל זיהוי ההתחייבות, המחבר והתאריך.

## הסבר מורחב

`Blame` (הצגת מי שינה כל שורה) מאפשר לך לראות מי אחראי לכל שורה בקובץ. זה שימושי למציאת מקור באגים, הבנת היסטוריית הקוד, וזיהוי מי צריך לבדוק שינוי ספציפי.

**דוגמאות לשימוש נפוץ:**
* מציאת מי הכניס באג לקוד
* הבנת מי עבד על פיצ'ר מסוים
* זיהוי מי צריך לבדוק שינוי

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הצגת blame של קובץ
git blame file.txt

# הצגת blame עם מספר שורות
git blame -L 10,20 file.txt

# הצגת blame עם תאריכים
git blame --date=short file.txt

# הצגת blame עם זיהוי התחייבות
git blame -w file.txt
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo

repo = Repo('my_repo')

# הצגת blame של קובץ
def show_blame(repo, file_path):
    try:
        blame = repo.blame('HEAD', file_path)
        for commit, lines in blame:
            for line in lines:
                print(f"{commit.hexsha[:8]} {commit.author.name}: {line}")
    except Exception as e:
        print(f"שגיאה: {e}")

# דוגמה
show_blame(repo, "main.py")
```

## מונחים קשורים

* [Log (היסטוריה)](./log.md)
* [Commit (התחייבות)](./commit.md)
* [Diff (הבדלים)](./diff.md)

## מקורות מידע נוספים

* [תיעוד Git על git blame](https://git-scm.com/docs/git-blame) 