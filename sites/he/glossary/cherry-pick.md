 # Cherry-pick (בחירת התחייבות ספציפית)

**הגדרה קצרה:** פעולה ב-Git המאפשרת לבחור התחייבות ספציפית מענף אחד ולהעתיק אותה לענף אחר, ללא העתקת כל ההיסטוריה של הענף המקורי.

## הסבר מורחב

`Cherry-pick` (בחירת התחייבות ספציפית) הוא כלי שימושי ב-Git כאשר אתה רוצה להעתיק התחייבות ספציפית או מספר התחייבויות מענף אחד לענף אחר, מבלי להעתיק את כל הענף או לבצע merge מלא. זה שימושי במיוחד כאשר יש התחייבות עם תיקון או פיצ'ר שאתה רוצה להחיל על ענף אחר.

היתרונות העיקריים של **Cherry-pick** הם:
* **בחירה מדויקת:** מאפשר לבחור התחייבויות ספציפיות בלבד.
* **גמישות:** לא צריך להעתיק את כל ההיסטוריה של הענף.
* **תיקונים מהירים:** מאפשר להחיל תיקון על מספר ענפים.
* **שליטה טובה:** מאפשר לשלוט בדיוק איזה שינויים להחיל.

**דוגמאות לשימוש נפוץ:**
* העתקת תיקון bug מענף develop לענף main.
* העתקת פיצ'ר ספציפי לענף release.
* העתקת התחייבות עם תיקון דחוף לענפים שונים.
* בחירת התחייבויות ספציפיות מתוך branch גדול.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# cherry-pick של התחייבות אחת
git cherry-pick abc1234

# cherry-pick של מספר התחייבויות
git cherry-pick abc1234 def5678 ghi9012

# cherry-pick של טווח התחייבויות (לא כולל הראשונה)
git cherry-pick abc1234..def5678

# cherry-pick עם המשך אוטומטי במקרה של קונפליקטים
git cherry-pick --continue

# ביטול cherry-pick
git cherry-pick --abort

# cherry-pick עם skip של התחייבות בעייתיות
git cherry-pick --skip

# cherry-pick ללא יצירת התחייבות (רק שינויים)
git cherry-pick --no-commit abc1234

# cherry-pick עם עריכת הודעת התחייבות
git cherry-pick -e abc1234

# cherry-pick עם שמירת מחבר המקור
git cherry-pick -x abc1234

# cherry-pick עם אימות חתימה
git cherry-pick --verify-signatures abc1234

# cherry-pick של התחייבות עם תיקון אוטומטי
git cherry-pick --strategy=recursive -X theirs abc1234
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# cherry-pick בסיסי
def cherry_pick_commit(repo, commit_hash):
    """ביצוע cherry-pick של התחייבות ספציפית"""
    try:
        repo.git.cherry_pick(commit_hash)
        print(f"Cherry-pick של {commit_hash} הושלם בהצלחה")
        return True
    except Exception as e:
        print(f"שגיאה ב-cherry-pick: {e}")
        return False

# cherry-pick של מספר התחייבויות
def cherry_pick_multiple(repo, commit_hashes):
    """ביצוע cherry-pick של מספר התחייבויות"""
    successful_picks = []
    failed_picks = []
    
    for commit_hash in commit_hashes:
        try:
            repo.git.cherry_pick(commit_hash)
            successful_picks.append(commit_hash)
            print(f"✓ Cherry-pick של {commit_hash} הושלם")
        except Exception as e:
            failed_picks.append(commit_hash)
            print(f"✗ שגיאה ב-cherry-pick של {commit_hash}: {e}")
            # ביטול cherry-pick כושל
            try:
                repo.git.cherry_pick('--abort')
            except:
                pass
    
    return successful_picks, failed_picks

# cherry-pick עם טיפול בקונפליקטים
def cherry_pick_with_conflict_resolution(repo, commit_hash, strategy='theirs'):
    """ביצוע cherry-pick עם אסטרטגיה לפתרון קונפליקטים"""
    try:
        # ניסיון cherry-pick רגיל
        repo.git.cherry_pick(commit_hash)
        print(f"Cherry-pick של {commit_hash} הושלם ללא קונפליקטים")
        return True
    except Exception as e:
        if "conflict" in str(e).lower():
            print(f"קונפליקט ב-cherry-pick של {commit_hash}, מנסה לפתור...")
            try:
                # פתרון קונפליקטים עם אסטרטגיה
                repo.git.cherry_pick('--strategy=recursive', f'-X{strategy}')
                print(f"קונפליקט נפתר בהצלחה")
                return True
            except Exception as e2:
                print(f"לא ניתן לפתור קונפליקט: {e2}")
                repo.git.cherry_pick('--abort')
                return False
        else:
            print(f"שגיאה אחרת: {e}")
            return False

# בדיקת התחייבויות זמינות ל-cherry-pick
def find_commits_for_cherry_pick(repo, source_branch, target_branch):
    """מציאת התחייבויות שניתן לבצע עליהן cherry-pick"""
    try:
        # מעבר לענף המקור
        repo.git.checkout(source_branch)
        
        # קבלת התחייבויות שלא קיימות בענף היעד
        commits = repo.git.log(
            f'{target_branch}..HEAD',
            '--oneline',
            '--no-merges'
        ).split('\n')
        
        # ניקוי רשימה
        commits = [commit.strip() for commit in commits if commit.strip()]
        
        print(f"התחייבויות זמינות ל-cherry-pick מ-{source_branch} ל-{target_branch}:")
        for i, commit in enumerate(commits, 1):
            print(f"{i}. {commit}")
        
        return commits
        
    except Exception as e:
        print(f"שגיאה במציאת התחייבויות: {e}")
        return []

# דוגמה לשימוש
if __name__ == "__main__":
    # דוגמה: cherry-pick של תיקון bug
    bug_fix_commit = "abc1234"
    if cherry_pick_commit(repo, bug_fix_commit):
        print("תיקון ה-bug הוחל בהצלחה")
    
    # דוגמה: cherry-pick של מספר התחייבויות
    feature_commits = ["def5678", "ghi9012", "jkl3456"]
    successful, failed = cherry_pick_multiple(repo, feature_commits)
    
    print(f"\nסיכום:")
    print(f"התחייבויות שהוחלו בהצלחה: {len(successful)}")
    print(f"התחייבויות שנכשלו: {len(failed)}")
```

## מונחים קשורים

* [Commit (התחייבות)](./commit.md)
* [Branch (ענף)](./branch.md)
* [Merge (מיזוג)](./merge.md)
* [Rebase (שינוי בסיס)](./rebase.md)
* [Conflict (קונפליקט)](./conflict.md)

## מקורות מידע נוספים

* [תיעוד Git על git cherry-pick](https://git-scm.com/docs/git-cherry-pick)
* [Git Cherry-pick Tutorial](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.cmd.Git.cherry_pick)
* [Advanced Cherry-pick Strategies](https://git-scm.com/docs/git-cherry-pick#_examples)