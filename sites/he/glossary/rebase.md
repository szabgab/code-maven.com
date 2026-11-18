 # Rebase (שינוי בסיס הענף)

**הגדרה קצרה:** פעולה ב-Git המאפשרת לשנות את נקודת הבסיס (base) של ענף, על ידי העתקת התחייבויות מענף אחד לענף אחר, בדרך כלל כדי ליצור היסטוריה ליניארית ונקייה יותר.

## הסבר מורחב

`Rebase` (שינוי בסיס הענף) הוא כלי מתקדם ב-Git שמאפשר "להעביר" התחייבויות מענף אחד לענף אחר. במקום ליצור merge commit שמשלב שני ענפים, rebase יוצר היסטוריה ליניארית על ידי העתקת התחייבויות מהענף הנוכחי אל קצה הענף היעד.

היתרונות העיקריים של **Rebase** הם:
* **היסטוריה נקייה:** יוצר היסטוריה ליניארית ללא merge commits מיותרים.
* **קריאות טובה יותר:** היסטוריה ברורה וקלה להבנה.
* **שליטה טובה יותר:** מאפשר לעצב את ההיסטוריה לפי הצורך.
* **מניעת קונפליקטים:** יכול להפחית קונפליקטים בהשוואה ל-merge.

**דוגמאות לשימוש נפוץ:**
* עדכון ענף feature עם השינויים האחרונים מ-main.
* ניקוי היסטוריה לפני merge ל-main.
* שינוי סדר התחייבויות או שילוב התחייבויות קטנות.
* יצירת היסטוריה נקייה לפרויקט.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# rebase בסיסי - העתקת התחייבויות מ-main לענף הנוכחי
git rebase main

# rebase אינטראקטיבי - מאפשר לערוך, לשלב או למחוק התחייבויות
git rebase -i HEAD~3

# rebase עם המשך אוטומטי במקרה של קונפליקטים
git rebase --continue

# ביטול rebase
git rebase --abort

# rebase עם skip של התחייבות ספציפית
git rebase --skip

# rebase עם עריכת הודעת התחייבות
git rebase -i --reword HEAD~2

# rebase עם שילוב התחייבויות
git rebase -i --squash HEAD~3

# rebase עם ענף מרוחק
git rebase origin/main

# rebase עם שמירת merge commits
git rebase --preserve-merges main
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# rebase בסיסי
try:
    # העתקת התחייבויות מ-main לענף הנוכחי
    repo.git.rebase('main')
    print("Rebase הושלם בהצלחה")
except Exception as e:
    print(f"שגיאה ב-rebase: {e}")
    # ביטול rebase במקרה של שגיאה
    repo.git.rebase('--abort')

# rebase אינטראקטיבי (דורש אינטראקציה ידנית)
def interactive_rebase(repo, commits_count):
    """ביצוע rebase אינטראקטיבי על מספר התחייבויות"""
    try:
        # יצירת קובץ זמני עם הוראות rebase
        rebase_file = f"rebase-{commits_count}.txt"
        with open(rebase_file, 'w') as f:
            f.write(f"pick HEAD~{commits_count} התחייבות ראשונה\n")
            f.write(f"pick HEAD~{commits_count-1} התחייבות שנייה\n")
            f.write(f"pick HEAD~{commits_count-2} התחייבות שלישית\n")
        
        # ביצוע rebase עם הקובץ
        repo.git.rebase('-i', f'HEAD~{commits_count}', 
                       _env={'GIT_EDITOR': f'cat {rebase_file}'})
        
        # ניקוי קובץ זמני
        os.remove(rebase_file)
        print("Interactive rebase הושלם")
        
    except Exception as e:
        print(f"שגיאה ב-interactive rebase: {e}")
        repo.git.rebase('--abort')

# בדיקת מצב לפני ואחרי rebase
def check_rebase_status(repo):
    """בדיקת מצב המאגר לפני ואחרי rebase"""
    print("מצב לפני rebase:")
    print(repo.git.log('--oneline', '-5'))
    
    try:
        # ביצוע rebase
        repo.git.rebase('main')
        print("\nמצב אחרי rebase:")
        print(repo.git.log('--oneline', '-5'))
    except Exception as e:
        print(f"שגיאה: {e}")
        repo.git.rebase('--abort')

# דוגמה לשימוש
if __name__ == "__main__":
    # בדיקת ענף נוכחי
    current_branch = repo.active_branch.name
    print(f"ענף נוכחי: {current_branch}")
    
    # ביצוע rebase רק אם לא על main
    if current_branch != 'main':
        check_rebase_status(repo)
    else:
        print("לא ניתן לבצע rebase על ענף main")
```

## מונחים קשורים

* [Branch (ענף)](./branch.md)
* [Merge (מיזוג)](./merge.md)
* [Commit (התחייבות)](./commit.md)
* [Conflict (קונפליקט)](./conflict.md)
* [Checkout (מעבר)](./checkout.md)

## מקורות מידע נוספים

* [תיעוד Git על git rebase](https://git-scm.com/docs/git-rebase)
* [Git Rebase Tutorial](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.rebase)
* [Interactive Rebase Guide](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)