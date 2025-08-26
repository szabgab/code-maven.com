# Project (פרויקט)

**הגדרה קצרה:** Project הוא כלי לניהול משימות, תכנון, תעדוף ומעקב אחר התקדמות בפרויקטים של קוד פתוח או קוד סגור, בעיקר בפלטפורמות כמו **GitHub** ו-**GitLab**.

## הסבר מורחב

Project (פרויקט) בפלטפורמות ניהול קוד הוא לוח עבודה (Board) המאפשר לארגן Issues, Pull Requests ומשימות אחרות בעמודות (Columns) לפי סטטוס, עדיפות, או שלב בתהליך העבודה. ניתן ליצור לוחות Kanban, Roadmaps, או כל מבנה אחר שמתאים לצוות. כל Project מאפשר תצוגה ויזואלית של התקדמות, תעדוף משימות, הקצאת אחראים, ותכנון גרסאות עתידיות. הכלי מסייע בשקיפות, תיאום ושיתוף פעולה בין חברי הצוות.

היתרונות העיקריים של **Project** הם:
* **תכנון וארגון:** מאפשר תכנון מסודר של משימות, פיצ'רים ובאגים.
* **מעקב ויזואלי:** תצוגה גרפית של סטטוס המשימות (למשל: To do, In progress, Done).
* **שקיפות ושיתוף פעולה:** כל חברי הצוות רואים את התקדמות הפרויקט בזמן אמת.

**דוגמאות לשימוש נפוץ:**
* יצירת לוח Kanban לניהול משימות בפרויקט.
* תעדוף Issues ו-Pull Requests לפי דחיפות.
* תכנון Roadmap לגרסאות עתידיות.

## דוגמת קוד

### יצירת Project ב-GitHub (דרך הממשק הגרפי)
1. נכנסים לעמוד המאגר או הארגון ב-GitHub.
2. לוחצים על "Projects" > "New project".
3. בוחרים תבנית (Kanban, Table, וכו'), נותנים שם ותיאור.
4. מוסיפים Issues, Pull Requests או כרטיסים ידניים.

### עבודה עם Projects מהטרמינל (באמצעות GitHub CLI)
```bash
# יצירת Project חדש (דורש הרשאות מתאימות)
gh project create --title "Roadmap 2024" --format board

# הצגת כל הפרויקטים במאגר
gh project list
```

## מונחים קשורים

* [Issue (בעיה/בקשה)](./issue.md)
* [Pull Request (בקשת משיכה)](./pull-request.md)
* [GitHub (גיטהאב)](./github.md)

## מקורות מידע נוספים

* [תיעוד GitHub על Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
* [תיעוד GitLab על Issue Boards](https://docs.gitlab.com/ee/user/project/issue_board.html) 