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

echo "B 1" >> README
git add .
git commit -m "b 1"

echo "B 2" >> README
git add .
git commit -m "b 2"

# gitk --all

cd ../a/

perl -i -p -e 's/^/A 1\n/ if $. == 1' README
git add .
git commit -m "a 1"
git push

cd ../b
git pull --rebase

gitk --all



