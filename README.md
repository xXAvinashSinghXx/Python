# Basic Git Commands

**Initialization**

1. `git init`: Initializes a new Git repository in a directory.

**Branching**

1. `git branch`: Creates, lists, or deletes branches.
2. `git checkout -b <branch-name>`: Creates a new branch and switches to it.

**Staging**

1. `git add <file_path>`: Stages a file for the next commit.
2. `git add .` or `git add --all`: Stages all changes in the current directory or the entire repository.

**Committing**

1. `git commit -m "<message>"`: Commits staged changes with a commit message.

**Remote Repositories**

1. `git clone <repository-url>`: Clones an existing Git repository to your local machine.
2. `git remote add <name> <url>`: Adds a remote repository to your local repository.

**Merging**

1. `git merge <branch-name>`: Merges changes from another branch into the current branch.

**Resetting**

1. `git reset <commit-hash>`: Resets the current branch to a specific commit.
2. `git reset --hard`: Resets the working directory and staging area to the specified commit.

**Status**

1. `git status`: Displays the status of the repository, including unstaged and staged changes.

**Log**

1. `git log`: Displays a log of all commits made to the repository.

**Checkout**

1. `git checkout <branch-name>`: Switches to a different branch.
2. `git checkout <commit-hash>`: Switches to a specific commit.

**Stashing**

1. `git stash`: Temporarily saves changes to be reapplied later.
2. `git stash list`: Lists all stashed changes.
3. `git stash apply`: Reapplies the most recent stash.

**Undoing**

1. `git reset HEAD <file>`: Undoes changes to a file.
2. `git reset --hard`: Resets the working directory and staging area to the last commit.
