# Remote (מאגר מרוחק)

**הגדרה קצרה:** מאגר מרוחק הוא עותק של מאגר קוד (**repository**) שנמצא בשרת חיצוני (למשל GitHub, GitLab או שרת פרטי), ומאפשר שיתוף פעולה בין מפתחים על אותו פרויקט באמצעות רשת האינטרנט.

## הסבר מורחב

`Remote` (מאגר מרוחק) הוא רכיב מרכזי בעבודה עם Git בצוותים ובפרויקטים משותפים. כל מאגר מקומי (local repository) יכול להיות מקושר לאחד או יותר מאגרים מרוחקים. ברירת המחדל לרוב נקראת `origin`. באמצעות פקודות כמו `git push`, `git pull` ו-`git fetch` ניתן לשלוח ולקבל שינויים בין המאגר המקומי למרוחק. כך ניתן לעבוד בצוות, לשמור גיבוי בענן, ולשלב פיתוחים ממפתחים שונים.

היתרונות העיקריים של **Remote** הם:
* **שיתוף פעולה:** מאפשר למספר מפתחים לעבוד יחד על אותו פרויקט מכל מקום בעולם.
* **גיבוי:** שומר עותק עדכני של הקוד וההיסטוריה שלו בשרת חיצוני.
* **ניהול גרסאות מרכזי:** מאפשר שליטה על גרסאות ועדכונים בפרויקט.

**דוגמאות לשימוש נפוץ:**
* קישור מאגר מקומי למרוחק: `git remote add origin https://github.com/user/repo.git`
* בדיקת רשימת המאגרים המרוחקים: `git remote -v`
* עבודה עם מספר מאגרים מרוחקים (למשל origin ו-upstream).

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# הוספת מאגר מרוחק חדש בשם origin
git remote add origin https://github.com/user/repo.git

# הצגת כל המאגרים המרוחקים
git remote -v

# הסרת מאגר מרוחק
git remote remove origin
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
repo = Repo('my_repo')

# הצגת כל המאגרים המרוחקים
for remote in repo.remotes:
    print(remote.name, remote.url)

# הוספת מאגר מרוחק חדש
repo.create_remote('origin', 'https://github.com/user/repo.git')
```

## מונחים קשורים

* [Push (דחיפה)](./push.md)
* [Pull (משיכה)](./pull.md)
* [Fetch (משיכה ללא מיזוג)](./fetch.md)
* [Repository (מאגר קוד)](./repository.md)

## מקורות מידע נוספים

* [תיעוד Git על Remote](https://git-scm.com/docs/git-remote)
* [הסבר על Remote ב-GitHub Docs](https://docs.github.com/en/get-started/quickstart/github-glossary#remote) 