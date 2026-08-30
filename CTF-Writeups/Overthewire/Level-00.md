# 🐧 Bandit Level 00

## 🎯 Objective

Connect to the Bandit Level 0 server using SSH and access the environment provided for the challenge.

## 🔎 Approach

The challenge introduces SSH and the basic Linux command line.

I used SSH to connect to the remote system and then inspected the environment.

## 💻 Commands

```
ssh bandit0@<bandit-host>
```

After connecting, I used basic Linux commands to inspect the directory.

```
pwd
ls
```

## 🧠 What I Learned

This level introduced the basic workflow for connecting to a remote Linux system using SSH.

I learned:

* What SSH is used for
* How SSH authentication works at a basic level
* How to connect to a remote Linux machine
* How to inspect the current working directory
* How to list files

## 🛡️ Cybersecurity Relevance

SSH is widely used for remote administration of Linux systems.

Understanding how SSH works is important for both defensive security and authorised penetration testing.

## 📚 Key Commands

| Command | Purpose                       |
| ------- | ----------------------------- |
| `ssh`   | Connect to a remote system    |
| `pwd`   | Display the current directory |
| `ls`    | List files and directories    |

## 💡 Takeaway

The first step in working with a Linux server is becoming comfortable with the command line and understanding how remote access works.
