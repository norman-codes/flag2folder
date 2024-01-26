# Flag2Folder: File Organization Tool

```py
________/\\\\\____/\\\\\\\\\____________/\\\\\_        
 ______/\\\///___/\\\///////\\\________/\\\///__       
  _____/\\\______\///______\//\\\______/\\\______      
   __/\\\\\\\\\_____________/\\\/____/\\\\\\\\\___     
    _\////\\\//___________/\\\//_____\////\\\//____    
     ____\/\\\__________/\\\//___________\/\\\______   
      ____\/\\\________/\\\/______________\/\\\______  
       ____\/\\\_______/\\\\\\\\\\\\\\\____\/\\\______ 
        ____\///_______\///////////////_____\///_______
```

## Overview
Welcome to Flag2Folder! This tool allows you to organize files into specified folders based on flags in their filenames. It's a simple yet powerful way to manage your files, whether they are images, documents, or any other type.

## Use Case

Ideal for organizing datasets, managing document libraries, or simply keeping your download folder uncluttered. Whether you're a data scientist, a software developer, or just someone who loves organization, flag2folder is here to help streamline your file management.

## Key Features

- **Custom Flag/Folder Mapping**: Users can define unique flags and corresponding folder names. Files containing these flags in their names are automatically moved to the specified folders.
- **Directory Flexibility**: Set source and destination directories with ease. The tool defaults to the current directory but allows for quick changes as needed.
- **Interactive Console Interface**: Straightforward and user-friendly, the console interface guides users through setting flags, adding/removing folder pairs, and executing the sorting process.
- **Preview & Confirmation**: Before executing, the tool provides a preview of the expected file organization, requiring user confirmation to proceed. This ensures accuracy and user control.

## Getting Started

- Clone the repository and run the script in a Python environment.
  - Or test it out online on [Replit](https://replit.com/@Normanb17/Flag2Folder-Example#main.py)!
- Follow the interactive prompts to set your flag/folder pairs and directories.
- Execute and watch your files get organized effortlessly!

## How to Use
1. **Choose Your Files**: Start by uploading the files you want to organize into this Replit workspace, or using the ones provided by default for testing.

2. **Run the Script**: Click the 'Run' button to start the script. It will initiate in the Replit console.

3. **Set Directories** (Optional):
   - The script uses the current working directory in Replit by default.
   - To change source and destination directories, use the [S]et directories option.

4. **Manage Flag/Folder Pairs**:
   - **Add**: Use the [A]dd action to create flag/folder pairs. Flags are keywords the script looks for in filenames, and each flag is linked to a folder.
     - The relationship between flags and folders is "many-to-one". In other words, you can have one or more flags but they must lead to one folder.
   - **Remove**: Select [R]emove to delete a specific flag/folder pair.
   - **Clear All**: Choose [C]lear all to remove all flag/folder pairs.

5. **Execute File Organization**:
   - With your flag/folder pairs set, use the [E]xecute action to start organizing your files. Files with specified flags in their names will be moved to the designated folders.

6. **Review and Exit**:
   - After execution, check the folders to see your organized files.
   - To exit the script, choose the [Q]uit action.

## Example Usage
Some example files exist by default for testing. Let's take a look at them and walk through flag2folder's functionality with them.

### The Files
Flag2Folder works with any file type, but for simplicity we're using these 6 text files:
  - f1_abc.txt
  - f1_def.txt
  - f1_ghi.txt
  - f2_abc.txt
  - f2_def.txt
  - f3_ghi.txt

Any part of the file's name can be considered a flag. Here, the files are distinctly labeled with "f1" and "f2" as clear examples of flags, but you could also use any part of the file name, such as "abc" or even "_".

### Adding a Flag/Folder Pair

Suppose you want to sort the files with "f1" in their name into a folder called Flag1 and "f2" into a folder called Flag2.

We can do this by running the [A]dd option and entering the following:
```
Enter the flag(s) to look for in filenames: f1
Enter the folder name to pair with the flag(s): Flag 1
```
Again, but this time for the second flag:
```
Enter the flag(s) to look for in filenames: f2
Enter the folder name to pair with the flag(s): Flag 2
```

_Why do we need to run it twice?_
Flag2Folder maintains a many-to-one relationship between its flags and folders. This means that one or more flags can only lead to one folder.

You should now see the following:
```
Current flag/folder pairs:
  Flag: 'f1' -> Folder: 'Flag 1'
  Flag: 'f2' -> Folder: 'Flag 2'
```

### Execution
Now that you have your desired flag and folder pairs, you can simply choose the [E]xecute action and Flag2Folder will organize your files for you!

**Note that this action is irreversible!**
A preview of the file structure is provided for you to double-check before executing.

Once you do, notice that now the file structure has changed. Instead of 6 text files, you now have 2 folders, Flag 1 and Flag 2, inside of which you have their corresponding files.

```
Flag1
  - f1_abc.txt
  - f1_def.txt
  - f1_ghi.txt
Flag2
  - f2_abc.txt
  - f2_def.txt
  - f2_ghi.txt
```
