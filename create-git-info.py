import subprocess

# git information
branchName = subprocess.getstatusoutput("git branch --show-current")
commitHash = subprocess.getstatusoutput("git log -1 --format=format:\"%H\"")
commitMessage = subprocess.getstatusoutput("git show -s --format=%s")
commitDay = subprocess.getstatusoutput("git log -1 --date=format:\"%Y-%m-%d\" --format=%ad")
uncommitedChanges = subprocess.getstatusoutput("git diff HEAD")

# print git info
print(branchName)
print(commitHash)
print(commitMessage)
print(commitDay)
print(uncommitedChanges)