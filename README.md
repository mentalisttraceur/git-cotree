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

**Note:** all examples are in a clone
of this repo and build on each other.

### First setup (once for each repo)

TL;DR: `git cotree --init`

Run `git cotree --init` to convert your repo to the
co-tree layout (don't worry: this is just a local
change, it won't have any affect on the remote).

After `git cotree --init`, the repo root is no longer
a working directory: your working directory has moved
into a subdirectory named after your current branch,
and the repo root now just holds your worktrees:

```sh
$ pwd
~/code/git-cotree
$ git branch
* main
$ ls
LICENSE  README.md  git-cotree
$ git cotree --init
$ ls
main
$ cd main
$ ls
LICENSE  README.md  git-cotree
```

<details><summary>
<code>git cotree --init</code> preserves uncommitted changes!
[click to see detailed alternative example with changes]
</summary>

```sh
$ pwd
~/code/git-cotree
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
a "normal" setup - for example, it might not work
if you used the `--bare` option with `git clone`
or the `--separate-git-dir` option with `git init`.


### Checkout into new worktree

TL;DR: `git-cotree <co-tree> [<commit-ish>]`

Without additional options, `git-cotree` is like a
slightly smarter combination of `git checkout` and
`git worktree add`.

If `<co-tree>` is an existing branch, tag, or commit,
`git cotree` will create the worktree with the samme
name in the repo's root directory
from the commit you're currently on (or from the
commit specified by `<commit-ish>`), just like
`git branch` does.

Checking out a branch that already exists upstream:

```sh
$ pwd
~/code/git-cotree/main
$ git branch
* main
$ ls ..
main
$ git cotree example
branch 'example' set up to track 'origin/example'.
HEAD is now at 4bd501d Explain `example` branch
$ git branch
+ example
* main
$ ls ..
example  main
$ cd ../example
$ git branch
* example
+ main
```

# This documentation is unfinished.

I'll write the rest when I can.
