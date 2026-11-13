# Git workflow: step by step
 
The `main` branch is protected. You **cannot** push to it directly. All changes reach `main` through a pull request that a teammate has approved.
 
← Back to [README](../README.md)
 
Then open a pull request on GitHub, get one approval, and **Squash and merge**.
 
## What each step does
 
### 1. Switch to `main`
```bash
git checkout main
```
Moves you onto the `main` branch. Always start a new task from `main`, never from someone else's branch or an old task branch.
 
### 2. Get the latest version
```bash
git pull
```
Downloads everything teammates have merged since you last pulled. Skipping this means your branch starts out of date, which leads to merge conflicts later.
 
### 3. Create your task branch
```bash
git checkout -b feature/S2-4-survey-list
```
Creates a new branch **and** switches to it (`-b` = new branch). Name it `feature/<task ID>-<short-description>`, using the task ID from the Sprint backlog, lowercase words separated by hyphens.
 
### 4. Do the work
Write code, save files, and test that it runs. You can check what you've changed at any time:
```bash
git status        # which files changed
git diff          # the exact lines changed
```
 
### 5. Stage your changes
```bash
git add .
```
Marks all changed files in the current folder to be included in the next commit. To add only specific files, name them instead, e.g. `git add backend/main.py`.
 
### 6. Commit
```bash
git commit -m "S2-4: add survey list with placeholder data"
```
Saves a snapshot on **your** branch. Start the message with the task ID, then say what you did. Commit little and often. Each commit is a save point you can go back to.
 
### 7. Push your branch to GitHub
```bash
git push -u origin feature/S2-4-survey-list
```
Uploads your branch. `-u` links your local branch to GitHub, so next time you can just type `git push`. Pushing to your own branch needs no approval.
 
### 8. Open a pull request (on GitHub)
1. Go to the repo on GitHub and click **Compare & pull request**.
2. Base branch: `main`, compare branch: your branch.
3. Title: `S2-4: Survey list with placeholder data`. Say in the description what you did and how to test it.
4. Ask a teammate to review.
### 9. Review and merge
- The reviewer opens **Files changed** and either comments or clicks **Review changes → Approve**.
- If they ask for changes: fix them on the same branch, commit, `git push`. The PR updates automatically and needs approving again.
- Once approved and all comments are resolved, click **Squash and merge**, then **Delete branch**.
### 10. Clean up locally and start the next task
```bash
git checkout main
git pull                                   # now includes your merged work
git branch -d feature/S2-4-survey-list     # delete the old local branch
```
Then go back to step 3 for your next task.
 
## Keeping your branch up to date
 
If a task takes a few days and others have merged work into `main` meanwhile, bring their changes into your branch before opening your PR:
 
```bash
git checkout main
git pull
git checkout feature/S2-4-survey-list
git merge main
```
 
If Git reports a **conflict**, open the files it lists, choose the correct lines between the `<<<<<<<` and `>>>>>>>` markers, delete the markers, then:
 
```bash
git add .
git commit -m "S2-4: merge latest main"
git push
```