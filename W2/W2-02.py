git -p

python all_checks.py >output.txt
 
git add*

git reset HEAD output.txt

git commit -m "it should be os.path.exitst"



touch auto-update.py

touch gather-information.sh

ls -l

git add auto-update.py

git commit -m 'Add two new scripts'

git add gather-information.sh

git commit --amend
#:wq and q!

#test the revert command
git commit -a -m 'Add call to disk_full function'
#can see the all_checks.py has revert it.
git revert HEAD
#check what kind of content has been revert
git log -p -2
#revert the specific commit
git show 7e7743f993e8efdfab0553f1da348ec0bcce2c27

git show 7e7743
#test to revert the commit
git revert 7e7743