# GIT and  GitHub Session

### Git is primarily a version control system and a staple in any software

### development project. It usually serves 2 main purposes: code backup

### and code versioning. You can work on your code step-by-step, saving

### each step’s progress along the way in case you need rollback to a

### backup copy!

### The common trouble is that Git can be tricky to use. There are times

### where versions and branches are out of sync and you spend serious

### time just trying to push your code! even worse, not knowing how

### exactly certain commands work could easily lead to accidentally

### deleting or overwriting bits of code!

### That’s why we’ve prepared this session, to teach you how to properly use

### git so we can all get on to coding!

# Install and setup

## Installing

### First thing’s first, we have to install git to use it! We can do it quick and

### easy using apt:


```
sudo apt install git-all
```
## Basic setup

### If you’d like, you can go ahead and save your git username and email so

### that you won’t have to enter them in again for future git commands.

```
git config --global user.name "User Name"
git config --global user.email "email"
```
## Colours

### A neat trick that some people often miss is that you can enable some

### extra colouring to git, so that you can read the output of the commands

### easier!

```
git config --global color.ui true
```
# Basic version control

## Initialising git

### Now we can start versioning our project. Go ahead and navigate to the

### directory you want to setup version control for in the terminal using the

### standard “cd” command. Now you can initialise a git repository like

### this:

```
git init
```
### This creates a new subdirectory named .git that contains all of your

### necessary repository files — a Git repository skeleton. At this point,

### nothing in your project is tracked yet.

## Adding and committing


### To start version-controlling existing files you should start by tracking

### those files and do an initial commit. To accomplish that, you start by

### adding the files to git that you would like to be attached to your git

### project.

```
git add <file>git commit -m 'first commit'
```
## Remote backup

### Great! You’ve now started versioning your GitHub project locally. If

### you would like to save and backup your project remotely, you’ll need to

### create a remote repository on GitHub (it’s free!). So first head on over

### to github.com and create a repository. Then, use the link of the

### repository to add it as the origin of your local git project i.e where that

### code will be stored.

### General example git remote add origin \ (^)
```
https://github.com/ _user_ / _repo_ .git
```
### An example with a repository of mine git remote add origin \
```
https://github.com/AppcellonApps/Bootcamp.git
```

### Then you can go ahead and push your code to GitHub... viola! You’ve

### backed up your code!

```
git push origin master
```
# Working with your files

## Status checking

### The main tool you use to determine which files are in which state is the

### git status command. It allows you to see which of your files have

### already been committed and which haven’t. If you run this command


### when all files have already been committed and pushed, you should see

### something like this:

$ git status# On branch master (^)
nothing to commit (working directory clean)

### If you add a new file to your project, and the file didn’t exist before,

### when you run a $ git status you should see your untracked file like

### this:

$ git status# On branch master (^)
# Untracked files:# (use "git add <file>..." to include in what will be (^)
committed)#
# READMEnothing added to commit but untracked files present (use (^)
"git add" to track)

### This makes $ git status really useful for a quick check of what you

### have backed up already and what you only have locally.

## Advanced file adding

### There are a few more advanced ways of adding files to Git that will

### make your workflow more efficient. Instead of trying to look for all the

### files that have changes and adding them one-by-one, we can do the

### following:

```
### Adding files one by onegit add filename
```
(^) ### Adding all files in the current directory
git add -A
### Adding all files changes in the current directorygit add.
(^) ### Choosing what changes to add (this will got through all
your ### changes and you can 'Y' or 'N' the changes)git add -p


## Advanced commits

### Previously, we saw that we could commit a file to Git using $ git

### commit -m "commit message" . That’s all fine and dandy for short

### commit messages, but if you want to do something more elaborate

### you’ll need a bit more:

### Commit staged file(s) ### This is typically used for shorter commit messages (^)
git commit -m 'commit message'
### Add file and commit in one shotgit commit filename -m 'commit message' (^)
(^) ### Add file and commit staged file
git commit -am 'insert commit message'
### Changing your most recent commit messagegit commit --amend 'new commit message'
(^) # Combine a sequence of commits together into a single one
### You might use this to organise a messy commit historygit rebase -i
### This will give you an interface on your core editor:# Commands:
# p, pick = use commit# r, reword = use commit, but edit the commit message (^)
# e, edit = use commit, but stop for amending# s, squash = use commit, but meld into previous commit (^)
# f, fixup = like "squash", but discard this commit's logmessage
# x, exec = run command (the rest of the line) using shell

# Branching and merging

### The master branch of your GitHub repository should always contain

### working and stable code. However, you may want to also back up

### some code that you are currently working on, but isn’t entirely stable.

### Maybe you’re adding a new feature, you’re experimenting and breaking

### the code a lot, but you still want to keep a back up to save your

### progress!

### Branching allows you to work on a separate copy of your code without

### affecting the master branch. When you first create a branch, a complete

### clone of your master branch is created under a new name. You can then

### modify the code in this new branch independently, including

### committing files and such. Once you’re new feature has been fully

### integrated and the code is stable, you merge it into the master branch!


## Branching

### Here’s all of the things you need to create and work on a branch:

```
### Create a local branch to work ongit checkout -b branchname
```
(^) ### Switching between 2 branches
git checkout branch_1git checkout branch_
### Pushing your new local branch to remote as backupgit push -u origin branch_
(^) ### Deleting a local branch - this won't let you delete a
branch ### that hasn't been merged yetgit branch -d branch_
(^) ### Deleting a local branch - this WILL delete a branch even
if it ### hasn't been merged yet!git branch -D branch_
(^) ### Viewing all current branches for the repository,
including both ### local and remote branches. Great to seeif you already have a ### branch for a particular feature
addition, especially on bigger ### projectsgit branch -a
(^) ### Viewing all branches that have been merged into your
current ### branch, including local and remote. Great forseeing where all ### your code has come from!
git branch -a --merged
### Viewing all branches that haven't been merged into yourcurrent ### branch, including local and remote
git branch -a --no-merged
### Viewing all local branchesgit branch
(^) ### Viewing all remote branches
git branch -r
# Rebase master branch into local branch$ git rebase origin/master
(^) # Pushing local branch after rebasing master into local
branch$ git push origin +branchname

## Merging

### Great! Now you’ve learned how to create a branch and work with that

### code! Once you’re done adding the new feature to your branch, you’ll

### want to merge it back into the master branch, so that your master has

### all of the latest code features.


### Here’s how to do it:

```
### First make sure you're looking at master branchgit checkout master
```
(^) ### Now merge your branch to master
git merge branch_

### That’s it! you may have to fix any code conflicts between your branch

### and master, but Git will show you how to do all of that after you type in

### that merge command.

# Fixing mistakes and backtracking

### Mistakes happen .... and they happen frequently with coding! The

### important thing is that we’re able to fix them.

### Have no fear here! Git has everything you need in case you make a

### mistake with the code you push, overwrote something, or just want to

### make a correction to something you pushed.

```
### Switch to the version of the code of the most recentcommit
git reset HEAD git reset HEAD -- filename # for a specific file
### Switch to the version of the code before the most recentcommit
git reset HEAD^ -- filenamegit reset HEAD^ -- filename # for a specific file
### Switch back 3 or 5 commitsgit reset HEAD~3 -- filename
git reset HEAD~3 -- filename # for a specific filegit reset HEAD~5 -- filename
git reset HEAD~5 -- filename # for a specific file
```
### Switch back to a specific commit### Where the '0766c053' is the commit ID (^)
git reset git reset 0766c0530766c053 -- filename -- filename # for a specific file
### The previous commands were what's known as "soft"resets. Your ### code is reset, but git will still keep a (^)
copy of the other code ### handy in case you need it. On theother hand, the --hard flag ### tells Git to overwrite all
changes in the working directory.git reset --hard 0766c


# Useful tips and tricks for Git

### We’re all done with the nitty gritty stuff! Here’s a few more Git tips and

### tricks you may find useful to improve your workflow!

## Searching

```
### Searches for parts of strings in a directorygit grep 'something'
```
(^) ### Searches for parts of strings in a directory and the -n
prints ### out the line numbers where git has found matchesgit grep -n 'something'
(^) ### Searches for parts of string with some context (some
lines ### before and some after the 'something' we are looking (^)
for)git grep -C<number of lines> 'something' (^)
(^) ### Searches for parts of string and also shows lines BEFORE
itgit grep -B<number of lines> 'something' (^)
(^) ### Searches for parts of string and also shows lines AFTER
itgit grep -A<number of lines> 'something'

## Seeing who wrote what

```
### Show alteration history of a file with the name of theauthor
git blame 'filename'
### Show alteration history of a file with the name of theauthor ### and the git commit ID
git blame 'filename' -l
```
## Logging

```
### Show a list of all commits in a repository. This commandshows ### everything about a commit, such as commit ID,
author, date and ### commit message.git log
```

```
### List of commits showing only commit messages and changesgit log -p
```
(^) ### List of commits with the particular string you are
looking forgit log -S 'something' (^)
(^) ### List of commits by author
git log --author 'Author Name'
### Show a summary of the list of commits in a repository.This ### shows a shorter version of the commit ID and the (^)
commit message.git log --oneline (^)
(^) ### Show a list of commits in a repository since yesterday
git log --since=yesterday
### Shows log by author and searching for specific terminside the ### commit message
git log --grep "term" --author "name"

## ...
