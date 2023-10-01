# Git Co-Tree

`git-cotree` makes using multiple Git work
trees for one repo really smooth and clean.

* `git-cotree` automates all of the repetition
  and boilerplate that normally has to go with
  `git worktree`.
* `git-cotree` matches the behavior of typical
  `git` commands better than `git worktree` does.
* `git-cotree` helps keep worktrees organized
  in the most natural and obvious way, all while
  not "spilling out" of your cloned repo folder.
* `git-cotree` makes it seamless to switch from
  a normal single-worktree clone to `git-cotree`.

`git-cotree` is the user experience `git
worktree` should've had from the beginning.

Why "co"-tree?

1. Like the "co" in "coroutine", suggesting
   multiple concurrent Git work trees.
2. "C.O." for "check out": `git cotree <branch>`
   checks out `<branch>` into its own work tree.


## Installation

Just copy the `git-cotree` script from this repo.
It only needs `git` and standard system utilities.

Note: once `git-cotree` is in your PATH, it can
also be invoked as `git cotree` (without the `-`).


## Usage

Let's say you've cloned this repo:

```sh
$ git clone https://github.com/mentalisttraceur/git-cotree
...
$ cd git-cotree
$ git branch
* main
$ ls
LICENSE  README.md  git-cotree
```

### First setup (once per cloned repo)

Run `git cotree --init` to convert your repo to the
Git Co-Tree layout (don't worry: this is just a local
change, it won't have any affect on the remote):

```sh
$ git cotree --init
$ ls
main
$ ls main
LICENSE  README.md  git-cotree
```

<details><summary>

`git cotree --init` will even preserve any changes you
haven't yet committed! [click to see detailed example]

</summary>

```sh
$ git clone https://github.com/mentalisttraceur/git-cotree
...
$ cd git-cotree
$ ls
LICENSE  README.md  git-cotree
$ echo "Example change" >>README.md
$ git add README.md
$ echo "Example change 2" >>README.md
$ echo "Mine now" >LICENSE
$ touch xyz
$ printf 'xyz\n' >.gitignore
$ mkdir empty-directory
$ ls
LICENSE  README.md  empty-directory  git-cotree  xyz
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   LICENSE
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

$ git cotree --init
$ ls
main
$ cd main
$ ls
LICENSE  README.md  empty-directory  git-cotree  xyz
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   LICENSE
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

```

Staged changes, unstaged changes, untracked and ignored
files and directories, all there after the conversion!

</details>

**Warning!** `git-cotree` assumes you started with
a "normal" setup - it won't work if you did something
like `git clone` with the `--bare` option or `git init`
with the `--separate-git-dir` option.


# This documentation is unfinished.

I'll write the rest when I can.
