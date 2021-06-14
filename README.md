A script which puts your local copy of a Git repository
into a state which is very ergonomic if you want to use
multiple `git worktree` directories.

This script is especially helpful if you want to start
using `git worktree`, but you want the experience to
be mor ergonomic, and you have already been working in
a normally cloned Git repository.

Your current work will be automatically moved into
a worktree named after your current branch. Staged
changes, unstaged changes, and untracked files are
all preserved and moved there as well.

Example, using this repo itself to demonstrate:

```sh
$ git clone https://github.com/mentalisttraceur/git-worktree-mode
Cloning into 'git-worktree-mode'...
remote: Enumerating objects: 19, done.
remote: Counting objects: 100% (19/19), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 19 (delta 7), reused 17 (delta 5), pack-reused 0
Receiving objects: 100% (19/19), done.
Resolving deltas: 100% (7/7), done.
$ cd git-worktree-mode/
$ ls
LICENSE  README.md  git-worktree-mode
$ echo x >>LICENSE
$ echo x >>README.md
$ git add README.md
$ echo x >>scrap.txt
$ ls
LICENSE  README.md  git-worktree-mode  scrap.txt
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   LICENSE

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        scrap.txt

$ ./git-worktree-mode
$ git status
fatal: this operation must be run in a work tree
$ ls
master
$ cd master
$ ls
LICENSE  README.md  git-worktree-mode  scrap.txt
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   LICENSE

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        scrap.txt

```
