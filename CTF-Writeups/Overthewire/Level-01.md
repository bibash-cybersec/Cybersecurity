# 🐧 Bandit Level 01

## 🎯 Objective
The goal is to find the password for next level there is only one file named - 
## 🔎 Approach

The challenge is that how to work with filename that starts with - (hyphen)

## 💻 Commands

```
ssh bandit1@<bandit-host>
```

After connecting, I used basic Linux commands to inspect the directory.

```
ls
```
Then I noticed there is a filename - , in linux - means a lot so treating it as normal file might gives error so I tried to define the path for the filename
```
cat ./-
this tells cat: to read the file in filename - which revels the password for next level
```

## 🧠 What I Learned
This level demonstrates an important Linux command-line concept


I learned:

The main lesson from this level was that Linux commands do not always interpret filenames exactly as they appear.

When a filename starts with -, explicitly providing its path can prevent the command from interpreting it as an option.

## 🛡️ Cybersecurity Relevance
Filenames can have special characters that affect how commands interpret arguments.

## 📚 Key Commands

| Command | Purpose                       |
| ------- | ----------------------------- |
| `pwd` | Display the current directory   |
|  `ls` | List files and directories |
|  `cat ./-`| read the content inside the file  |

## 💡 Takeaway

Filename: - 

↓ Potentially interpreted specially 

↓ Use an explicit path 

↓ cat ./-
