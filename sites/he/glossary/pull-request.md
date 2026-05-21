# Pull Request (בקשת משיכה)

**הגדרה קצרה:** פעולה בפלטפורמות ניהול קוד כמו **GitHub** ו-**GitLab**, המאפשרת למפתח להציע שינויים שביצע במאגר קוד (לרוב ב-Fork או בענף נפרד) כדי שייבחנו ויתמזגו (merge) למאגר המקורי.

## הסבר מורחב

`Pull Request` (בקשת משיכה) הוא תהליך מרכזי בשיתוף פעולה בפרויקטי קוד פתוח ובפיתוח צוותי. כאשר מפתח מסיים לבצע שינויים בקוד (לרוב ב-Fork או בענף branch), הוא יוצר Pull Request כדי להציע את השינויים למאגר המקורי. בעלי המאגר או המתחזקים בודקים את השינויים, מבצעים הערות וביקורות, ובסיום – יכולים לאשר ולמזג (merge) את השינויים לקוד הראשי.

היתרונות העיקריים של **Pull Request** הם:
* **ביקורת קוד:** מאפשר למתחזקים ולחברי צוות לבדוק, להעיר ולהציע שיפורים לפני מיזוג השינויים.
* **תיעוד:** כל Pull Request מתועד, כולל היסטוריית שינויים, דיונים והערות.
* **שיתוף פעולה:** מאפשר עבודה משותפת, גם בין אנשים שאין להם הרשאות ישירות לכתוב למאגר המקורי.

**דוגמאות לשימוש נפוץ:**
* כאשר רוצים להציע תיקון באג או פיצ'ר חדש לפרויקט קוד פתוח.
* כאשר עובדים בצוות ורוצים שמישהו אחר יעבור על הקוד לפני מיזוגו.
* כאשר רוצים לנהל תהליך מסודר של בדיקות וביקורות קוד.

## דוגמת קוד

### יצירת Pull Request ב-GitHub דרך הממשק הגרפי
1. דוחפים (push) את השינויים לענף חדש במאגר המרוחק (למשל: `feature/login`).
2. נכנסים לעמוד המאגר ב-GitHub, ולוחצים על "Compare & pull request".
3. ממלאים כותרת ותיאור, ולוחצים על "Create pull request".

### יצירת Pull Request מהטרמינל (באמצעות GitHub CLI)
```bash
# יצירת Pull Request מהענף הנוכחי לענף הראשי (main)
gh pr create --base main --head feature/login --title "הוספת מסך התחברות" --body "הוספת מסך התחברות עם ולידציה."
```

### פייתון (שימוש בספריית PyGithub)
```python
from github import Github

# התחברות ל-GitHub (יש להכניס טוקן אישי)
g = Github("your_github_token")
repo = g.get_repo("user/repo")

# יצירת Pull Request
pr = repo.create_pull(
    title="הוספת מסך התחברות",
    body="הוספת מסך התחברות עם ולידציה.",
    head="feature/login",
    base="main"
)
print(f"Pull Request created: {pr.html_url}")
```

## מונחים קשורים

* [Repository (מאגר קוד)](./repository.md)
* [Fork (מזלג)](./fork.md)
* [Clone (שכפול)](./clone.md)

## מקורות מידע נוספים

* [תיעוד GitHub על Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
* [תיעוד GitLab על Merge Requests](https://docs.gitlab.com/ee/user/project/merge_requests/)
