## Data 100 Spring 2022 website

Public facing repo for Data 100, Spring 2022

Note to staff: **Always** pull changes before making any edits. Merge conflicts (even those resolved automatically) can break things on the Datahub side.

The `main` branch is used for Datahub. To edit ds100.org github pages (Syllabus, etc.), switch to the `gh-pages` branch. Some common commands:

```
git branch -a         # see all local and remote branches

git checkout gh-pages                # if branch exists locally, or
git checkout --track origin/gh-pages # if branch exists remotely
...                   # edit, commit
git push              # pushes local branch to remote branch
```
