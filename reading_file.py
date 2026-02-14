file_path ="text.txt"

try:
    with open(file_path, "r") as file:
        content =file.read()
        print(content)
    
except FileNotFoundError:
    print("this file was not found")
    
except PermissionError:
    print("you don't have permission")
    