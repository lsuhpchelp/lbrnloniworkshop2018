# Version Control using Git Exercise

## Setup your git environment

TODO:

- First time set up to configure your identity. Look at the slide "First time Git setup".
- Define a git command alias </br>
`git config --global alias.graph 'log --all --oneline --decorate --graph'`</br> Look at the slide "Add a useful command before Travel"

## Build a local repository from scratch

TODO:
 
- Initialize an empty git repository in your /home directory, e.g., `/home/hpctrn01/myrepo`.
- Create a new text file named "myfirstfile.txt" in the repository
- Add the following three lines step by step to the myfirstfile.txt, each time you add a line, use git to add your changes and commit to the repository:</br>
`I learned Git Version Control today.`</br>
`Git is flexible.`</br>
`Git is easy to use.`</br>
- If you are new to using text editors on Linux you probably want to use nano instead of vi/emacs as your default text editor.
- Use the git command `git log` or the command alias `git graph` we defined earlier to see the 3 commits.
- Try to travel through different version history using `git reset --hard <commit-hash>` and `git reflog`

## Create a branch, make changes, merge, logs

TODO: 

- Create a dev branch, add the following line to "myfirstfile.txt" and commit your changes to the dev branch:</br>
`I now create a dev branch`</br>
- Switch to the master branch, merge master branch with the dev branch.
- Switch to the dev branch, add the following line to the file and commit your changes:</br>
`Git branch is fast AND easy.`
- Switch to the master branch, add the following line to the file and commit your changes:</br>
`Git branch is fast & easy.`
- Try to merge the master branch with the dev branch, there will be a conflict during the merge, resolve the conflict and merge the dev branch, delete the dev branch when merge is complete
- Use the command alias `git graph` to visualize the commit and branch history.

## Push your repository to GitHub

TODO: 

- If you do not have a GitHub account, register one at https://github.com/
- Create a new remote repository using your GitHub account and then push your local repository to the remote repository.

