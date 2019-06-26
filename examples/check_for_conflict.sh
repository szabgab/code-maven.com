git init
echo 1 > README
git add README
git commit -m 1
git checkout -b conflict
echo "2 in conflict" >> README
git add .
git commit -m "2 in conflict"
git checkout master
git checkout -b simple
echo 1 > OTHER
git add .
git commit -m "other"
git checkout master
echo 2 >> README
cat README
git add .
git commit -m "2 in master"
git checkout -b fast
echo f > FAST
git add .
git commit -m "fast"
git checkout master
git status
git merge --no-commit --no-ff fast
echo $?
git status
git merge --abort
git status
git merge --no-commit --no-ff simple
echo $?
git status
git merge --abort
git status
git merge --no-commit --no-ff conflict
echo $?
git status
git merge --abort
