# Git "Co-Tree"

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

**Warning!** `git-cotree` currently assumes you
start with the "normal" setup: you have one work
tree which contains your `.git` directory. If
you don't know what this means you're probably
fine, but if you know you did something like
`git clone` with the `--bare` option, `git init`
with the `--separate-git-dir` option, or `git
worktree add`, then before running `git-cotree`,
make sure you understand what `git-cotree` does
before running it.

Run `git-cotree --initialize` (`--initialize` can
be abbreviated to `--init` or `-i`) inside an
existing repo to get started.

1. Your repository will be rearranged and
   set up for the co-tree workflow.
2. The changes are entirely local. Your next push
   won't change anything for your teammates,
   unless you somehow defeat Git in weird ways.
3. All your staged changes, unstaged changes, and
   untracked files will all be preserved.

If you like to explore on your own, take a look at
the `git-coretree --help` output, and play around.
Otherwise, let's look at an example:

## Example

### Install and Example Setup

Before we can get to the good parts, we need
to actually get `git-cotree` and set some
basic stuff up for the example. We'll hit
both birds with one stone by using this repo
for the example.

First, clone this repo:

```sh
$ git clone https://github.com/mentalisttraceur/git-cotree
```

Next, let's go inside the repo and take a look around:

```sh
$ cd git-cotree/
$ ls
LICENSE  README.md  git-cotree
```

For this example, we can run `git-cotree` from inside this repo.
But if you like it you'll probably want to copy it into your
`PATH` or otherwise put it somewhere where it's easy to run.
(Personally, I put mine into the `git-core` directory where all
official `git` subcommands run, but that's a bit extreme.)

Anyway, let's make a couple changes, just so that you
can see how it takes care to not lose your uncommitted
work (which is very important because we often don't
realize we want multiple work trees until we're in the
middle of some work!):

```sh
$ echo x >>LICENSE
$ echo x >>README.md
$ git add README.md
$ echo x >>scrap.txt
$ ls
LICENSE  README.md  git-cotree  scrap.txt
```

Okay, now that we've made some changes, let's
take a quick look at the `git status`:

```sh
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

Wow, we've got a lot of stuff going on.
I sure hope `git-cotree` can handle it!
(It can.)

### Switching to Co-Trees

Ok, now we're ready for the cool `git-cotree` parts!

```sh
$ ./git-cotree --init
```

Silent is good. If something was
wrong it would print an error.

Now let's look at what we've
gotten ourselves into:

```sh
$ git status
fatal: this operation must be run in a work tree
```

Woah, what happened?
Don't worry!
This folder is now your co-tree "root",
where all your co-tree work trees will
live. That is why it is no longer a
work tree itself. See, it created a
new folder for the branch we were on:

```sh
$ ls
master
```

Let's go inside:

```sh
$ cd master
$ ls
LICENSE  README.md  git-cotree  scrap.txt
```

Now here's the really great part - all
those uncommitted changes from earlier?
`git-cotree --init` totally handled them:

```sh
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

Magical! We were in the middle of some work,
we decided we wanted to switch to co-trees,
we ran one command, and boom! It just works,
with the smallest possible interruption.

### Using Co-Trees

Finally, we're ready to actually do something.

(Since that first example was so amazing,
I'm just going to assume you've already
eagerly installed `git-cotree` into your
`PATH`, so all remaining examples will
be calling `git-cotree` instead of a
relative path.)

So where were we? Oh right, we were working
on adding `x` characters to the end of our
files. Let's get back to that.

Oh no! Suddenly, your boss appears demanding
an urgent hotfix! Quick, let's make a hotfix
branch, and check it out into a new work tree!

```sh
$ git-cotree emergency-hotfix
Preparing worktree (new branch 'emergency-hotfix')
HEAD is now at 4274166 Latest commit message in the current branch
```

Cool. So our `master` branch's work tree is still
the same, but now in the co-tree root we have a
new work tree:

```sh
$ ls
LICENSE  README.md  git-cotree  scrap.txt
$ cd ..
$ ls
emergency-hotfix  master
```


