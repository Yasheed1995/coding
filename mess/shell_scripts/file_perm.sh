#!bin/bash
#Program:
#   User input a filename, program will check the following:
#   1.)exist? 2.) file/directory? 3.) file permissions
# History:
# 2016/10/22 Logan  First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
# 1. let user input the filename, and check whether the user really inputed
echo "Please input a filename, I will check the filename's type and permission. \n\n"
read -p "Input a filename : " filename
test -z ${filename} && echo "You MUST input a filename." && exit 0
# 2. check whether the file really exist? if not, show message and exit the program.
test ! -e ${filename} && echo "The filename '${filename}' DO NOT exist" && exit 0
# 3. start to check the type and permission
test -f ${filename} && filetype="regulare file"
test -d ${filename} && filetype="dirctory"
test -r ${filename} && perm="readable"
test -w ${filename} && perm="${perm} writable"
test -x ${filename} && perm="${perm} writable"
# 4. start to output informations!
echo "The filename: ${filename} is a ${filetype}"
echo "And the permissions for you are : ${perm}"
 
