# Git Co-Tree: `git worktree` for humans

`git-cotree` implements an ergonomic approach to
using multiple Git work trees which I am calling
"co-trees".


## Installation

Just copy the `git-cotree` script from this repo.
It only needs `git` and standard system utilities.

> [!TIP]
> Once `git-cotree` is in your `PATH`,
> it can be invoked as `git cotree`.


## Why is it called "co"-tree?

Both "C.O." for "checkout" and like the
"[co](https://en.wiktionary.org/wiki/co-#English)"
in "coroutine": multiple work trees,
**c**hecked **o**ut **co**ncurrently.


Concretely, `git-cotree` is a minimalistic,
opinionated, and ergonomic wrapper/"porcelain"
around the core functionality of `git worktree`,
`git branch`, and `git checkout`.

Basically, `git-cotree` provides a great developer
experience if you want to use or try using two or
more work trees at the same time.

Run `git-cotree --initialize` (can be
shortened to `--init` or `-i`) inside
an existing repo to get started.

1. Your repository will be rearranged and
   set up for the co-tree workflow.
2. The changes are entirely local. Your next push
   won't change anything for your teammates,
   unless you somehow defeat Git in weird ways.
3. All your staged changes, unstaged changes,
   and untracked files will be preserved.

If you like to explore on your own, take a look at
the `git-cotree --help` output, and play around.
I think it is pretty easy and intuitive. For the
rest of you, I'll write some examples when I can.
