import os
import shutil

def create_directory(path):
    # Create a directory if it doesn't exist.
    if not os.path.exists(path):
        os.makedirs(path)

def validate_directory(path):
    # Check if the provided path is a valid directory.
    if not os.path.isdir(path):
        print(f"ERROR: '{path}' is not a valid directory.")
        return False
    return True

def move_files_to_folders(src_dir, dest_dir, flag_folder_map):
    # Move files to respective folders based on the flag in their filenames.
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):
            for flag, folder in flag_folder_map.items():
                if flag in file:
                    folder_path = os.path.join(dest_dir, folder)
                    create_directory(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    break  # Stop checking other flags once a match is found

def confirm_execution(dest_dir, flag_folder_map):
    # Display a preview of the file structure and confirm execution.
    folder_flag_map = {}
    for flag, folder in flag_folder_map.items():
        folder_flag_map.setdefault(folder, []).append(flag)

    print("\nPreview of the file structure:")
    for folder, flags in folder_flag_map.items():
        print(f"{dest_dir}/{folder} | containing {', '.join(flags)}")

    confirmation = input("Is this correct? (y/n): ").strip().lower()
    return confirmation == 'y'

# source: https://patorjk.com/software/taag/
def print_ascii_art():
    # Print ASCII art of 'f2f'.
    print("=" * 60)
    print(r"""
________/\\\\\____/\\\\\\\\\____________/\\\\\_        
 ______/\\\///___/\\\///////\\\________/\\\///__       
  _____/\\\______\///______\//\\\______/\\\______      
   __/\\\\\\\\\_____________/\\\/____/\\\\\\\\\___     
    _\////\\\//___________/\\\//_____\////\\\//____    
     ____\/\\\__________/\\\//___________\/\\\______   
      ____\/\\\________/\\\/______________\/\\\______  
       ____\/\\\_______/\\\\\\\\\\\\\\\____\/\\\______ 
        ____\///_______\///////////////_____\///_______
  """)
    print("=" * 60)

# source: https://emojicombos.com/star
def print_goodbye_ascii_art():
    print(r"""
⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣏⠻⣶⣤⡶⢾⡿⠁⠀⢠⣄⡀⢀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣼⠷⠀⠀⠁⢀⣿⠃⠀⠀⢀⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠴⣾⣯⣅⣀⠀⠀⠀⠈⢻⣦⡀⠒⠻⠿⣿⡿⠿⠓⠂⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⢻⡇⣤⣾⣿⣷⣿⣿⣤⠀⠀⣿⠁⠀⠀⠀⢀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⡿⠏⠀⢀⠀⠀⠿⣶⣤⣤⣤⣄⣀⣴⣿⡿⢻⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠟⠁⠀⢀⣼⠀⠀⠀⠹⣿⣟⠿⠿⠿⡿⠋⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢳⣶⣶⣿⣿⣇⣀⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠛⠿⣿⣦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⠿⠋⠁⠀⣹⣿⠳⠀⠀⠀⠀⠀⠀⢀⣠⣽⣿⡿⠟⠃
⠀⠀⠀⠀⠀⢰⠿⠛⠻⢿⡇⠀⠀⠀⣰⣿⠏⠀⠀⢀⠀⠀⠀⣾⣿⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣰⣿⣿⣾⣿⠿⢿⣷⣀⢀⣿⡇⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠁⠀⠀⠀⠀⠙⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀
    """)

def main():
    print_ascii_art()
    print("Welcome to flag2folder!")
    print("A tool to easily sort files into designated folders\nusing custom flag/folder pairs.\n")
    src_dir = os.getcwd()
    dest_dir = os.getcwd()

    flag_folder_map = {}
    while True:
        print("-" * 60)
        print("Source Directory:", src_dir)
        print("Destination Directory:", dest_dir)
        print("\nCurrent flag/folder pairs:")
        for flag, folder in flag_folder_map.items():
            print(f"  Flag: '{flag}' -> Folder: '{folder}'")
        print("-" * 60)

        action = input("\nChoose an action: [A]dd, [R]emove, [C]lear all, [S]et directories, [E]xecute, [Q]uit: ").strip().upper()
        
        if action == "A":
            print("\nAdd a flag/folder pair. Inputs are case-sensitive.\nExample 1: Flag: 'POS', Folder: 'positive'\nExample 2: Flag: 'HAP', Folder: 'positive/happy'\n")
            flag = input("Enter the flag to look for in filenames: ")
            folder = input("Enter the folder name for this flag: ")
            flag_folder_map[flag] = folder
        elif action == "R":
            print("\nRemove a flag/folder pair. Enter the exact flag to remove it.\n")
            if len(flag_folder_map) == 0:
                print("\nERROR: There are no flag/folder pairs.")
                continue
            flag = input("Enter the flag to remove: ")
            if flag in flag_folder_map:
                del flag_folder_map[flag]
            else:
                print("ERROR: Flag not found.")
        elif action == "C":
            print("\nClear all flag/folder pairs. This action cannot be undone.")
            confirmation = input("Are you sure you want to clear all pairs? (y/n): ").strip().lower()
            if confirmation == 'y':
                flag_folder_map.clear()
                print("SUCCESS: All flag/folder pairs have been cleared.")
            else:
                print("Clear action cancelled.")
        elif action == "S":
            print("\nSet new source and destination directories. Leave blank and press enter if no change. \nMake sure you input absolute paths to valid directories.\nExample: C:/users/datasets/test_1\n")
            new_src_dir = input("Set a new source directory: ").strip()
            if new_src_dir and validate_directory(new_src_dir):
                src_dir = new_src_dir

            new_dest_dir = input("Set a new destination directory: ").strip()
            if new_dest_dir and validate_directory(new_dest_dir):
                dest_dir = new_dest_dir
        elif action == "E":
            print("\nExecute the file organization based on the current flag/folder pairs.")
            if confirm_execution(dest_dir, flag_folder_map):
                move_files_to_folders(src_dir, dest_dir, flag_folder_map)
                print("\nSUCCESS: Files have been organized.")
            else:
                print("Execution cancelled.")
        elif action == "Q":
            break
        else:
            print("\nERROR: Invalid action. Please choose again.")

    print("=" * 60)
    print_goodbye_ascii_art()
    print("Thank you for using flag2folder!")
    print("=" * 60)

# Note: this code requires a local Python environment to run properly.

if __name__ == "__main__":
    main()
