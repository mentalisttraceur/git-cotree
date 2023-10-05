#!/bin/sh -
mkdir -p "$1"/d &&
cd "$1" &&
git init &&
echo z >d/.a &&
git add d/.a &&
echo y >>d/.a &&
echo x >d/.b &&
echo d/.b >.gitignore &&
git add .gitignore &&
echo w >d/.c &&
mkdir e &&
echo v >e/.f &&
echo u >g &&
git add g &&
rm g &&
mkdir g &&
mkdir h &&
echo t >h/i &&
git add h/i &&
rm -r h &&
echo s >h &&
git commit -m 'test commit 1' &&
git checkout -b "$2"
