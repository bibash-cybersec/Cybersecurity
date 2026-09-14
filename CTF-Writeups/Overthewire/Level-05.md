## 🏴‍☠️ Bandit Level 5 → Level 6

**🎯 Objective:**

Find the password for the next level.

Given Clue
The password is stored in a file somewhere under the `inhere` directory. The correct file has these properties:

* **Human-readable**
* **1033 bytes in size**
* **Not executable**

### 📂 Step 1: Enter the directory

```
cd inhere
```

### 🔎 Step 2: Find the correct file

I use `find` with the required properties:

```
find . -type f -size 1033c ! -executable
```

### 📋 Step 3: Read the file

The command should return the path of the matching file. Then:

```
cat ./path/to/file
```

Replace `./path/to/file` with the path returned by `find`.

### 🧠 What I learned:

* `find` searches for files based on specific conditions.
* `-type f` searches only for regular files.
* `-size 1033c` searches for a file exactly **1033 bytes**.
* `! -executable` excludes executable files.
* Combining conditions makes `find` extremely powerful for Linux reconnaissance.

### 🏁 Result:

The contents of the matching file contain the password for **Bandit Level 6**. 🔐
