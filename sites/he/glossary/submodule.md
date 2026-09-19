 # Submodule (מודול משנה)

**הגדרה קצרה:** מאגר Git נפרד שמשולב בתוך מאגר Git אחר, מאפשר שימוש בקוד חיצוני תוך שמירה על היסטוריה נפרדת ועדכונים נפרדים.

## הסבר מורחב

`Submodule` (מודול משנה) הוא מאגר Git נפרד שמשולב בתוך מאגר Git אחר. זה מאפשר לך להשתמש בקוד חיצוני (כמו ספריות, כלים או פרויקטים אחרים) תוך שמירה על היסטוריה נפרדת ועדכונים נפרדים.

היתרונות העיקריים של **Submodule** הם:
* **שימוש חוזר בקוד:** מאפשר להשתמש באותו קוד בפרויקטים שונים.
* **היסטוריה נפרדת:** כל submodule שומר על ההיסטוריה שלו.
* **עדכונים נפרדים:** ניתן לעדכן כל submodule בנפרד.
* **גמישות:** מאפשר לשלב פרויקטים חיצוניים בקלות.

**דוגמאות לשימוש נפוץ:**
* שילוב ספריות חיצוניות בפרויקט.
* שימוש בכלים או סקריפטים משותפים.
* שילוב פרויקטים קטנים בפרויקט גדול.
* שימוש בקוד משותף בין צוותים.

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הוספת submodule
git submodule add https://github.com/user/library.git libs/library

# הוספת submodule עם ענף ספציפי
git submodule add -b develop https://github.com/user/library.git libs/library

# שכפול מאגר עם submodules
git clone --recursive https://github.com/user/project.git

# שכפול submodules אחרי clone
git submodule update --init --recursive

# עדכון submodule לגרסה אחרונה
git submodule update --remote

# מעבר לתיקיית submodule
cd libs/library
git checkout main
git pull origin main
cd ../..

# עדכון submodule במאגר הראשי
git add libs/library
git commit -m "עדכון submodule"

# הסרת submodule
git submodule deinit libs/library
git rm libs/library
git commit -m "הסרת submodule"

# הצגת רשימת submodules
git submodule status

# הצגת רשימת submodules עם פרטים
git submodule foreach 'git status'

# עדכון כל submodules
git submodule foreach 'git pull origin main'

# שכפול submodule ספציפי
git submodule update --init libs/library
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
import os

repo = Repo('my_repo')

# הוספת submodule
def add_submodule(repo, url, path):
    """הוספת submodule חדש"""
    try:
        repo.git.submodule('add', url, path)
        print(f"נוסף submodule {path} מ-{url}")
        return True
    except Exception as e:
        print(f"שגיאה בהוספת submodule: {e}")
        return False

# עדכון submodules
def update_submodules(repo):
    """עדכון כל submodules"""
    try:
        repo.git.submodule('update', '--init', '--recursive')
        print("כל submodules עודכנו")
        return True
    except Exception as e:
        print(f"שגיאה בעדכון submodules: {e}")
        return False

# הצגת רשימת submodules
def list_submodules(repo):
    """הצגת רשימת submodules"""
    try:
        submodules = repo.submodules
        print("רשימת submodules:")
        for submodule in submodules:
            print(f"  {submodule.name}: {submodule.url}")
        return submodules
    except Exception as e:
        print(f"שגיאה בהצגת submodules: {e}")
        return []

# עדכון submodule ספציפי
def update_specific_submodule(repo, submodule_name):
    """עדכון submodule ספציפי"""
    try:
        repo.git.submodule('update', '--remote', submodule_name)
        print(f"Submodule {submodule_name} עודכן")
        return True
    except Exception as e:
        print(f"שגיאה בעדכון {submodule_name}: {e}")
        return False

# בדיקת מצב submodules
def check_submodule_status(repo):
    """בדיקת מצב submodules"""
    try:
        status = repo.git.submodule('status')
        print("מצב submodules:")
        print(status)
        return status
    except Exception as e:
        print(f"שגיאה בבדיקת מצב: {e}")
        return None

# דוגמה לשימוש
if __name__ == "__main__":
    # הוספת submodule
    add_submodule(repo, "https://github.com/user/library.git", "libs/library")
    
    # הצגת רשימת submodules
    submodules = list_submodules(repo)
    
    # עדכון submodules
    update_submodules(repo)
    
    # בדיקת מצב
    check_submodule_status(repo)
```

## מונחים קשורים

* [Repository (מאגר)](./repository.md)
* [Clone (שכפול)](./clone.md)
* [Remote (מרוחק)](./remote.md)
* [Commit (התחייבות)](./commit.md)

## מקורות מידע נוספים

* [תיעוד Git על git submodule](https://git-scm.com/docs/git-submodule)
* [Git Submodules Tutorial](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
* [GitPython Documentation](https://gitpython.readthedocs.io/en/stable/reference.html#git.repo.base.Repo.submodules)