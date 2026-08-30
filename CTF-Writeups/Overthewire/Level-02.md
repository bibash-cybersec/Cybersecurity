# 🐧 OverTheWire Bandit - Level 2

## 🎯 Objective

The goal of this level is to find the password for the next level.

After connecting to the Bandit Level 2 environment, I found a file named:

```
--spaces in this filename--
```

The challenge was to read a file whose name contains spaces and begins with `--`.

---

## 🔎 Enumeration

I started by listing the files in the current directory:

```bash
ls
```

The output was:

```
--spaces in this filename--
```

The filename presented two challenges:

1. It contains spaces.
2. It begins with `--`, which can be interpreted by Linux commands as an option.

---

## 🧪 Initial Attempt

I first tried:

```
cat "--spaces in this filename--"
```

However, `cat` interpreted the filename as an argument beginning with `--` and returned an error.

This showed me that quoting the filename alone was not enough in this situation.

---

## 💡 Solution

I used `--` to tell `cat` to stop processing command-line options.

```
cat -- "--spaces in this filename--"
```

This successfully displayed the password for the next level.

🔒 **Password:** Not published.

---

## 🧠 Why Does `--` Work?

In many Linux command-line programs, `--` is used to indicate:

> Stop processing options. Treat everything that follows as an argument.

Therefore:

```
cat -- "--spaces in this filename--"
```

can be understood as:

```
cat
 ↓
--                         → Stop processing options
 ↓
"--spaces in this filename--" → Treat this as the filename
```

This allows `cat` to correctly access the file.



## 📚 Commands & Concepts Learned

| Command / Concept | Purpose                                             |
| ----------------- | --------------------------------------------------- |
| `ls`              | Lists files and directories                         |
| `cat`             | Displays the contents of a file                     |
| `--`              | Stops option processing                             |
| `./`              | Refers to the current directory                     |
| `\`               | Escapes special characters                          |
| Quoting           | Allows spaces to be treated as part of one argument |

---

## 🛡️ Cybersecurity Relevance

Understanding how command-line arguments are interpreted is important when working with Linux systems, scripts, and security tools.

Files or inputs beginning with characters such as `-` can sometimes be interpreted as command options instead of normal data.

If scripts do not handle user-controlled filenames or arguments carefully, this can potentially lead to unexpected command behavior.

Understanding argument parsing is therefore an important Linux and cybersecurity fundamental.

---

## 💡 What I Learned

This level taught me that simply putting a filename in quotes does not always solve every command-line problem.

When a filename begins with `--`, the command may interpret it as an option.

Using:

```
cat -- "filename"
```

tells the command to stop processing options and treat the following value as a filename.

### Key takeaway

```
Filename
   ↓
Contains spaces + begins with --
   ↓
Command may interpret it as an option
   ↓
Use --
   ↓
cat -- "filename"
```

---

