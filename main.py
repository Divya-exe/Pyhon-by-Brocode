#python file detection
import os
file_path = "D:\python by bro code\text.txt"
if os.path.exists(file_path):
    print(f"the loaction '{file_path}' exxist")
else:
    print("not here")