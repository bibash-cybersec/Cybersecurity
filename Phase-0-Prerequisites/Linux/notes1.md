## Linux File Permission
- Owner rwx = read, write, execute
- Group rw- = read, write only no execute
- Other r-- = read only

 ## Permission values 
 - read = 4
 - write = 2
 - execute = 1
 - none = 0

 ## Combinations
- rwx = 4+2+1 = 7
- rw- = 4+2+0 = 6
- r-x = 4+0+1 = 5
- r-- = 4+0+0 = 4
- -wx = 0+2+1 = 3
- -w- = 0+2+0 = 2
- --x = 0+0+1 = 1

 ## Common Permissions sets:
 - 777 = rwxrwxrwx (everyone full access)
 - 755 = rwxr-xr-x ( owner full, other read and executes)
 - 644 = rw-r--r-- (owner read and write other read only)
 - 600 = rw------- (owner read and write other none)
 - 400 = r-------- (owner read only other none)
 - 000 = --------- (no permission at all)

## Two ways to use chmod:
1. Numeric (Octal) - most common
   * chmod 755 script.sh  { rwxr-xr-x }
   * chmod 644 file.txt  { rw-r--r-- }
   * chmod 600 file.txt { rw------- }
   * chmod 777 file.txt { rwxrwxrwx }

2. Symbolic
   * chmod u+x script.sh  {add execute to owner}
   * chmod g-w file.txt {remove write from group}
   * chmod o+r file.txt { add write to other}
   * chmod a+x script.sh { add execute to all}

Note:
1. u = user/owner
2. g = group
3. o = other
4. a = all
