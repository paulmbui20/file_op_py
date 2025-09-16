

# File Handling & Error Handling Challenge Quiz
## Objectives

* **Master Files**: Practice opening, reading, writing, and closing files in Python.
* **Handle Errors Like a Pro**: Learn how to deal with problems (like missing files) without crashing the program.

This small project shows how Python can read data from a file, modify it, and then save the new version in another file. Along the way, it demonstrates **exception handling** so the program is safe even if something goes wrong.

---

## What the Program Does

1. Asks the user to type the name of a file.
2. Tries to open the file in **read mode**.

   * If the file doesn’t exist, it shows a clear error message.
   * If the file is empty, it warns the user.
3. Reads the content and **adds line numbers** to each line.
4. Saves the modified content into a new file named:

   ```
   modified_<original_filename>
   ```
5. Prints success messages (or error messages if something failed).

---

## Example Run

```
Welcome to the File Handling Challenge Quiz
Enter the filename you want to open: notes.txt
✅ Success! Your modified file is saved as 'modified_notes.txt'.
```

Contents of `notes.txt`:

```
Hello world
This is Python
File handling is fun
```

Contents of `modified_notes.txt`:

```
1: Hello world
2: This is Python
3: File handling is fun
```

---

## Error Handling 

This program is protected against common issues:

* **FileNotFoundError** → user typed a wrong filename.
* **PermissionError** → user doesn’t have access.
* **Empty files** → warns if the file has no data.
* **Other unexpected errors** → caught by a generic `except`.

It also has a **finally block** to show that file operations are finished, no matter what.

---

## Best Practices Followed 

* Used `with open(...)` so files are closed automatically.
* Checked for empty file content.
* Caught **specific exceptions** before general ones.
* Printed clear error messages for the user.

---

## How to Run 

1. Save the program into a file, e.g., `main.py`.
2. Make sure you have a text file to test with (e.g., `notes.txt`).
3. Run it with:

   ```
   python main.py
   ```
4. Follow the prompts.

---
