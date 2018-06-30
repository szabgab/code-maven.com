#!/bin/bash

REPO='git-demo'

if [ "$1" == "" ]
then
    echo $0 DIRNAME
    exit 1
fi

echo "$1"
mkdir $1
cd $1

mkdir $REPO
cd $REPO
git init --bare
cd ..

git clone $REPO a
echo "[user]
	name = A 
	email = a@code-maven.com
" >> a/.git/config

git clone $REPO b
echo "[user]
	name = B 
	email = b@code-maven.com
" >> b/.git/config

cd a
echo "First line" > README
git add .
git commit -m "first line"

echo "Second line" >> README
git add .
git commit -m "second line"

echo "Third line" >> README
git add .
git commit -m "third line"

git push


cd ../b/
git pull

git branch feature
git checkout feature
echo "B 1" >> README
git add .
git commit -m "b 1"

echo "B 2" >> README
git add .
git commit -m "b 2"
git push -u origin feature

# gitk --all

cd ../a/

# work on the same feature
git pull
git branch feature origin/feature
git checkout feature

perl -i -p -e 's/^/A 1\n/ if $. == 1' README
git add .
git commit -m "a 1"
git push

cd ../b

echo "B 3" >> README
git add .
git commit -m "b 3"


git checkout master
echo "M 1" >> MASTER
git add .
git commit -m "m 1"
git push

git checkout feature
git merge master -m "merge master 1"

gitk --all

git pull --rebase

gitk --all


git checkout master
echo "M 2" >> MASTER
git add .
git commit -m "m 2"
git push

git checkout feature
git merge master -m "merge master 2"
gitk --all


