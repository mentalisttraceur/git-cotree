A script which prepares a Git repository
for a `git worktree`-centric workflow.

This script assumes you have a normal Git repo,
and converts it into a state which is very clean
if you want to switch to a workflow where every
checkout is in a `git worktree` instead of in
one central working directory.

Your current work will be automatically
moved into a worktree named after your
current branch for you.

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

The script itself should be extremely safe and
robust, never losing repository configuration,
uncommitted changes, or untracked files. Of
course, a bug might have slipped in, so maybe
back up anything important before running it.

The whole approach and repository setup to
achieve the best `git worktree`-centric user
experience is something I only just now came
up with - it seems to work so far and I am
already dogfooding it (including for this repo
as I write this!), but maybe I just haven't
discovered some serious lurking flaw yet.
