
### Bandit Level 4 → Level 5

**🎯 Objective:**

Find the password for the next level. The password is stored in the **only human-readable file** in the `inhere` directory.

**📂 Location:**

```
inhere/
```

**🔎 Step 1: Enter the directory**

```
cd inhere
```

**📋 Step 2: List the files**

```
ls
```

**🔍 Step 3: Identify the file types**

```
file ./*
```

Look for the file identified as **ASCII text** or another human-readable text file.

**🔓 Step 4: Read the correct file**

```
cat ./filename
```

Replace `filename` with the human-readable file I discovered.

**🧠 What I learned:**

* `file` identifies the type/content of a file.
* `./*` allows us to check multiple files at once.
* `cat` displays the contents of a file.
* `./filename` is useful when dealing with filenames that could otherwise be interpreted as command options.

**🏁 Result:**
The contents of the human-readable file give the password for **Bandit Level 5**.
