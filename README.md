# Git Co-Tree: `git worktree` for humans

`git-cotree` is a nice way to have more than
one branch checked out at the same time.

`git-cotree` lets you effortlessly switch
between normal Git and an "every branch is
its own directory" setup, even mid-workflow.

`git-cotree` is streamlined so that the
manual overhead of managing more work trees
will never dissuade you from using them.


## Installation

Just copy the `git-cotree` script from this repo.
The only dependency is `git`.

> [!TIP]
> Once `git-cotree` is in your `PATH`,
> it can be invoked as `git cotree`.


## Why is it called "co"-tree?

Both "C.O." for "checkout" and like the
"[co](https://en.wiktionary.org/wiki/co-#English)"
in "coroutine": multiple work trees,
**c**hecked **o**ut **co**ncurrently.


## TODO: more docs

Most of [the `git worktree` documentation](https://git-scm.com/docs/git-worktree)
applies.

Concretely, `git-cotree` is a minimal wrapper
combining the core features of `git worktree`,
`git branch`, and `git checkout`.

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
