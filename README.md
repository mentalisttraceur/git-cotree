# Git Co-Tree: `git worktree` for humans

`git-cotree` implements an ergonomic approach to
using multiple Git work trees which I am calling
"co-trees".

Concretely, `git-cotree` is a minimalistic,
opinionated, and ergonomic wrapper/"porcelain"
around the core functionality of `git worktree`,
`git branch`, and `git checkout`.

The "co" in "cotree" has a double meaning:

1. It is like the "co" in "coroutine", suggesting
   multiple concurrent and equal Git work trees.
2. It also stands for "check out", because the
   `git-cotree` command largely takes the place
   of `git checkout` in this workflow.

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
