#python file detection
import os
file_path = "D:\\python by bro code\\text.txt"
if os.path.exists(file_path):
    print(f"the loaction '{file_path}' exxist")
    if os.path.isfile(file_path):
        print("that if file")
    
else:
    print("not here")