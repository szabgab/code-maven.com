 # Tag (תגית)

**הגדרה קצרה:** תגית היא סימון נקודתי בהיסטוריית המאגר (repository) במערכת ניהול גרסאות כמו **Git**, המשמשת בדרך כלל לסימון גרסאות חשובות (למשל: שחרור גרסה v1.0.0).

## הסבר מורחב

`Tag` (תגית) מאפשרת לסמן commit מסוים כנקודת ציון חשובה, כמו שחרור גרסה, milestone, או כל אירוע משמעותי אחר בפרויקט. התגיות ב-Git הן "קלות משקל" (lightweight) או "מועשרות" (annotated), כאשר Annotated Tag כוללת מידע נוסף כמו שם יוצר התגית, תאריך, וחתימה דיגיטלית. התגיות אינן משתנות – הן תמיד מצביעות לאותו commit, גם אם ההיסטוריה משתנה.

היתרונות העיקריים של **Tag** הם:
* **סימון גרסאות:** מאפשר לחזור בקלות לגרסה מסוימת של הפרויקט.
* **שחרור גרסאות:** נהוג להוציא Release על בסיס תגית.
* **מעקב אחר נקודות ציון:** סימון milestones חשובים בפרויקט.

**דוגמאות לשימוש נפוץ:**
* יצירת תגית לגרסה חדשה: `git tag v1.0.0`
* יצירת תגית Annotated: `git tag -a v1.0.0 -m "גרסה ראשונה"`
* דחיפת תגיות למאגר מרוחק: `git push origin v1.0.0`
* הצגת כל התגיות: `git tag`

## דוגמת קוד

### פקודות Git בטרמינל
```bash
# יצירת תגית קלה (lightweight)
git tag v1.0.0

# יצירת תגית Annotated עם הודעה
git tag -a v1.0.0 -m "גרסה ראשונה"

# דחיפת כל התגיות למאגר מרוחק
git push --tags

# דחיפת תגית בודדת
git push origin v1.0.0

# הצגת כל התגיות
git tag
```

### פייתון (שימוש בספריית GitPython)
```python
from git import Repo
repo = Repo('my_repo')
# יצירת תגית קלה
repo.create_tag('v1.0.0')
# יצירת תגית Annotated
repo.create_tag('v1.0.1', message='גרסה שניה')
# הצגת כל התגיות
for tag in repo.tags:
    print(tag)
```

## מונחים קשורים

* [Commit (התחייבות)](./commit.md)
* [Release (גרסה)](./release.md)
* [Branch (ענף)](./branch.md)

## מקורות מידע נוספים

* [תיעוד Git על Tag](https://git-scm.com/docs/git-tag)
* [הסבר על Tag ב-GitHub Docs](https://docs.github.com/en/get-started/quickstart/github-glossary#tag)
