def main():
    print("Welcome to the File Handling Challenge Quiz")
    filename = input("Enter the filename you want to open: ").strip()

    try:
        # trying to open the file in read mode
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()

        if not data:
            # custom case: file exists but is empty
            print("Warning: The file is empty, nothing to modify.")
            return

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
        return
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
        return
    except Exception as e:
        print(f"Unexpected error while reading: {e}")
        return

    # Modify the content somehow (I’ll add line numbers instead of just uppercase)
    lines = data.splitlines()
    modified_lines = []
    for i, line in enumerate(lines, start=1):
        modified_lines.append(f"{i}: {line}")
    modified_text = "\n".join(modified_lines)

    # Write the new content to another file
    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w", encoding="utf-8") as f:
            f.write(modified_text)
    except Exception as e:
        print(f"Could not write the file: {e}")
        return
    finally:
        # finally runs no matter what, good place for clean-up messages
        print("File operation complete (whether successful or not).")

    print(f"✅ Success! Your modified file is saved as '{new_filename}'.")


if __name__ == "__main__":
    main()
