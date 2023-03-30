git commit -a -m "Call check_reboot from main, exit with 1 on error"
git log -p
git show "Specific ID 439edd244560b18b89ae8ba90361b8984b893c4d"
git log --stat

git rm all_checks.py
git mv all.py check_free_space.py

.gitignore
echo .DS_STORE > .gitignore
ls -la
git add .gitignore
git commit -m 'Add a gitignore file, ignoring .DS_STORE files'


