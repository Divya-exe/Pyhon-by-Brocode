#for text file
# file_path ="text.txt"

# try:
#     with open(file_path, "r") as file:
#         content =file.read()
#         print(content)
    
# except FileNotFoundError:
#     print("this file was not found")
    
# except PermissionError:
#     print("you don't have permission")

#<-----------------------   json   --------------------->


# for json file

# import json
# file_path ="text.json"

# try:
#     with open(file_path, "r") as file:
#         content =json.load(file)
#         print(content)
    
# except FileNotFoundError:
#   print("this file was not found")

# except PermissionError:
#     print("you don't have permission")

#<-----------------------   CSV   --------------------->  

import csv
file_path ="text.csv"

try:
    with open(file_path, "r") as file:
        content =csv.reader(file)
        for line in content:
            print(line)
    
except FileNotFoundError:
  print("this file was not found")

except PermissionError:
    print("you don't have permission")
    