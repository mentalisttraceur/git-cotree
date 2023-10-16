# Git Co-Tree

`git worktree` for humans.

`git-cotree` makes using multiple worktrees
for one Git repo really smooth and clean.

<details><summary>
[click to expand a more precise explanation for
those familiar with <code>git worktree<code>]
</summary>

* `git-cotree` automates all of the repetition
  and boilerplate that normally has to go with
  `git worktree`.
* `git-cotree` matches the behavior of typical
  `git` commands better than `git worktree` does.
* `git-cotree` helps keep worktrees organized
  in the most natural and obvious way, all while
  * not spilling out of your initial repo folder
    (like normal `git worktree` use does), and
  * not exposing Git internals (as "bare" repo
    workflows trying to make multiple worktrees
    nicer typically end up doing).
* `git-cotree` makes it seamless to switch from
  a normal single-worktree layout to a great
  layout for multiple worktrees at any time
  (no need to have set up for it when you first
  cloned or created the repo).

</details>

Why is it called "co"-tree?

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


### Checkout into new worktree

```
git-cotree <co-tree> [<commit-ish>]
```

```sh
$ git-cotree docs
Preparing worktree (new branch 'docs')
HEAD is now at ...
$ git branch
* docs
+ main
$ ls ..
docs main
$ ls ../docs
LICENSE  README.md  git-cotree
$ cd ../docs
$ git status 
On branch docs
nothing to commit, working tree clean
```

```
$ cd ../main
$ git stash
$ cd ../docs
$ git stash pop
```


###
    git-cotree --delete [--force] <co-tree>
    

### Setting the default to branch from
 
<!--
If you're in a worktree, new branches work
as normal - they start from the commit you
are currently on.

But if you're not in a worktree (you are in
the main repo directory which contains all
of the work trees) what branch should you
-->

```
git-cotree --base <co-tree>
```