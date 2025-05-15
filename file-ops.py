import os

def list_directories():
    cwd = os.getcwd()
    dir_or_file = os.listdir(cwd)

    def format(dir_or_file):
        path = os.path.join(cwd, dir_or_file)
        return dir_or_file + '/' if os.path.isdir(path) else dir_or_file

    formatted_entries = map(format, dir_or_file)
    for entry in formatted_entries:
        print(entry)

def create_file(filename, text = None):
    with open(filename, 'w') as f:
        if text != None:
            f.write(text)

def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        print(f"Content of {filename}:")
        print(content)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted")
    else:
        print(f"This file does not exist")

def change_directory(path):
    os.chdir(path)
    print(f"Changed directory to {path}")

while(True):
    cwd = os.getcwd()
    path = cwd.split("\\")[-1]
    user_command = input(f"\\{path}\\ : ")
    if user_command == "exit":
            break
    command_list = user_command.split('"')
    command = command_list[0].strip()
    
    match command:
        case "ls":
            list_directories()
        case "read":
            if len(command_list) >= 2:
                filename = command_list[1]
                read_file(filename)
            else:
                print("read \"filename\"")
        case "touch":
            if len(command_list) >= 3:
                filename = command_list[1]
                text = command_list[3] if len(command_list) > 3 else None
                create_file(filename, text)
            else:
                print("touch \"filename\" \"content (optional)\"")
        case "delete":
            if len(command_list) >= 2:
                filename = command_list[1]
                delete_file(filename)
            else:
                print("delete \"filename\"")
        case "cd":
            if len(command_list) >= 2:
                path = command_list[1]
                change_directory(path)
            else:
                print("cd \"path\"")
        case _:
            print("Unknown command.")

# ignore...

# subdirs = [dir for dir in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, dir))]
# print("Sub-directories in current working directory:")
# for dir in subdirs:
#     print(dir)