import subprocess

# git information
branchNameIdx, branchNameStr = subprocess.getstatusoutput("git branch --show-current")
commitHashIdx, commitHashStr = subprocess.getstatusoutput("git log -1 --format=format:\"%H\"")
commitMessageIdx, commitMessageStr = subprocess.getstatusoutput("git show -s --format=%s")
commitDayIdx, commitDayStr = subprocess.getstatusoutput("git log -1 --date=format:\"%Y-%m-%d\" --format=%ad")
#uncommitedChangesIdx, uncommitedChangesStr = subprocess.getstatusoutput("git diff HEAD")

# print git info
#print(branchNameStr)
#print(commitHashStr)
#print(commitMessageStr)
#print(commitDayStr)
#print(uncommitedChangesStr)

# generate strings
branchNameDefine = ("#define GIT_BRANCH_NAME\t\t\"" + branchNameStr +"\"\n")
commitMessageDefine = ("#define GIT_COMMIT_MESSAGE\t\"" + commitMessageStr +"\"\n")
commitHashDefine = ("#define GIT_HASH\t\t\t\"" + commitHashStr +"\"\n")
gitDateDefine = ("#define GIT_DATE\t\t\t\"" + commitDayStr +"\"\n")

# generate header
file = open("git-info.h", "w")
file.write("#ifndef GIT_INFO_H\n")
file.write("#define GIT_INFO_H\n")
file.write("\n")

file.write(branchNameDefine)
file.write(commitMessageDefine)
file.write(commitHashDefine)
file.write(gitDateDefine)

file.write("\n")
file.write("#endif /* GIT_INFO_H */\n")
file.close()