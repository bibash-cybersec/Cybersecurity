# 🐧 OverTheWire Bandit - Level 3

## 🎯 Objective

The goal of this level is to find the password for the next level.

After entering the `inhere` directory, the challenge file was hidden from the normal directory listing.

---

## 🔎 Enumeration

First, I entered the `inhere` directory:

```
cd inhere
```

I then used:

```
ls
```

The directory appeared to contain no visible files.

However, Linux can hide files whose names begin with a `.`.

---

## 🔍 Finding Hidden Files

I used:

```
ls -a
```

The `-a` option tells `ls` to show **all files**, including hidden files.

The output included:

```
.
..
...Hiding-From-You
```

The entries `.` and `..` are special directory references:

* `.` represents the current directory.
* `..` represents the parent directory.

The actual challenge file was:

```
...Hiding-From-You
```

---

## 💻 Solution

I read the file using:

```
cat ...Hiding-From-You
```

This displayed the password for the next Bandit level.

🔒 **Password:** Not published.

---

## 🧠 What I Learned

Linux normally hides files and directories whose names begin with `.`.

The command:

```
ls -a
```

shows both normal and hidden files.

The `-a` means:

```
all
```

Therefore:

```
ls
```

shows normal entries, while:

```
ls -a
```

also shows hidden entries.

---

## 📚 Commands & Concepts Learned

| Command / Concept | Purpose                                 |
| ----------------- | --------------------------------------- |
| `cd`              | Changes the current directory           |
| `ls`              | Lists visible files and directories     |
| `ls -a`           | Lists all files, including hidden files |
| `cat`             | Displays file contents                  |
| `.`               | Represents the current directory        |
| `..`              | Represents the parent directory         |
| Hidden files      | Files whose names begin with `.`        |

---

## 🛡️ Cybersecurity Relevance

Hidden files are common in Linux environments and can contain configuration files, application data, credentials, scripts, or other information.

During security assessments, simply running:

```
ls
```

may not reveal everything in a directory.

Understanding how to enumerate hidden files is therefore an important Linux reconnaissance skill.

---

## 💡 Key Takeaway

```text
Directory appears empty
        ↓
ls
        ↓
No visible files
        ↓
ls -a
        ↓
Hidden file discovered
        ↓
cat ...Hiding-From-You
        ↓
Password obtained
```

---

