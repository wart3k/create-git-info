# create-git-info
A script that generates a header file with Git information. The script creates an .h-file. The h-file contains 
information such as commit hash, current branch, the date ... <br>
The script can be used e.g. in VSCode as a pre-build script

## What you get
The header file can look like this (Actual content may vary)
```C
#ifndef GIT_INFO_H
#define GIT_INFO_H

#define GIT_BRANCH_NAME		"main"
#define GIT_COMMIT_MESSAGE	"detect uncommitted changes"
#define GIT_HASH		"bc43cb5f14c3ff7be544f4b993a9007df9e82624"
#define GIT_DATE		"2023-03-25"

#ifdef GIT_UNCOMMITTED_CHANGES
#ifdef DEBUG
#warning "There are uncommitted changes"
#endif /* DEBUG */
#ifdef RELEASE
#error "There are uncommitted changes"
#endif /*  RELEASE */
#endif /* GIT_UNCOMMITTED_CHANGES */

#endif /* GIT_INFO_H */
```
If there are uncommitted changes on build, then the following expression is added
```C
#define GIT_UNCOMMITTED_CHANGES
```

## How to use in VS Code
Place the create-git-info.py file in the directory with a .git folder.<br>
Add into your platformio.ini the line
```platformio
extern_script = pre:create-git-info.py
```
When using the header file for the first time, "undefined references" errors can occur because the h file has not 
yet been created. In this case the script should be executed once or a dummy header should be generated.

## Remarks
Currently only tested on a Linux OS