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

# generate header
file = open("git-info.h", "w")
file.write("#ifndef GIT_INFO_H\n")
file.write("#define GIT_INFO_H\n")
file.write("\n")

file.write("#define GIT_BRANCH_NAME\t\tasd\n")
file.write("#define GIT_HASH\t\t\tasd\n")
file.write("#define GIT_COMMIT_MESSAGE\tasd\n")
file.write("#define GIT_DATE\t\t\tasd\n")

file.write("\n")
file.write("#endif /* GIT_INFO_H */\n")
file.close()