A script which puts your local copy of a Git repository
into a state which is very ergonomic if you want to use
multiple `git worktree` directories.

This script is especially helpful if you want to start
using `git worktree` but you have already been working
in a normally cloned Git repo.

Your current work will be automatically moved into
a worktree named after your current branch. Staged
changes, unstaged changes, and untracked files are
all preserved and moved there as well.

Example, using this repo itself to demonstrate:

```sh
$ git clone https://github.com/mentalisttraceur/git-worktree-mode
$ cd git-worktree-mode
$ ls
LICENSE
README.md
git-worktree-mode
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
$ ./git-worktree-mode
$ ls
master
$ git status
fatal: this operation must be run in a work tree
$ cd master
$ ls
LICENSE
README.md
git-worktree-mode
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
