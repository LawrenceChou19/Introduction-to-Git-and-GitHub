git checktout -b refactor

git add -p
git commit -m 'Rename min_absolute to min_gb, use parameter names'
git log -p origin/main

git log --graph --oneline

git commit -a -m 'Create wrapper fuction for check_disk_full'

git commit -a -m 'Iterate over a list of checks and messages to avoid code duplication'

git commit -a -m 'Allow printing more than one error message'
# * [new branch]      refactor -> refactor
git push -u origin refactor



git checkout main

git log --graph --oneline --all

git checkout refactor 

git rebase main

git log --graph --oneline

git checkout main

git merge refactor

git push --delete origin refactor

git branch -d refactor

git push

#after add the socket module
git commit -a -m 'Add a simple networdk connectivity check'

git fetch

git rebase origin/main

git add health_checks.py

git rebase --continue
git log --graph --oneline

git push