git checktout -b refactor

git add -p
git commit -m 'Rename min_absolute to min_gb, use parameter names'
git log -p origin/main

git log --graph --oneline