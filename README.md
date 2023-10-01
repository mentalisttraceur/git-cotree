# Git Co-Tree

`git-cotree` makes it easy to have each branch
checked out into its own working directory (aka
"tree").

* `git-cotree` automates the repetition and
  boilerplate that you basically always need
  around `git worktree` calls.
* `git-cotree` matches the interface of common
  `git` commands more than `git worktree` does.
* `git-cotree` provides a clean directory layout
  great for multiple worktrees: the repo's root
  contains just each worktree, named (by default)
  after the branch or tag it checked out.
* `git-cotree` is just a nicer way to use Git's
  built-in support for multiple worktrees, so most
  of your things can already understand them, and
  you can still use all the normal Git commands to
  work with your co-trees - they're just worktrees.
* `git-cotree` makes it seamless to switch a repo
  that you're already using normally to co-trees.

In other words: `git-cotree` is `git worktree` for humans.


## Why is it called "co"-tree?

Both "C.O." for "checkout" and like the "co"
in "coroutine": more than one worktree for a
repo, **c**hecked **o**ut **co**ncurrently.


## Installation

Just copy the `git-cotree` script from this repo.
It only needs `git` and standard system utilities.

**Tip:** once `git-cotree` is in your PATH,
it can also be invoked as `git cotree`.


## Usage

### First setup (once for each repo)

Run `git cotree --init` to convert your repo to the
Git Co-Tree layout (don't worry: this is just a local
change, it won't have any affect on the remote).

For example, in a clone of this repo:

```sh
$ git clone https://github.com/mentalisttraceur/git-cotree
...
$ cd git-cotree
$ git branch
* main
$ ls
LICENSE  README.md  git-cotree
$ git cotree --init
$ ls
main
$ ls main
LICENSE  README.md  git-cotree
```

<details><summary>
<code>git cotree --init</code> will even preserve
any changes you haven't yet committed!
[click to see detailed example]
</summary>

```sh
$ git clone https://github.com/mentalisttraceur/git-cotree
...
$ cd git-cotree
$ ls
LICENSE  README.md  git-cotree
$ echo 'Example change' >>README.md
$ git add README.md
$ echo 'Example change 2' >>README.md
$ echo 'Mine now' >LICENSE
$ touch xyz
$ echo 'xyz' >.gitignore
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
