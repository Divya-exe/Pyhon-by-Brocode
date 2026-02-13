import json
import csv
#employees= ["Divya","Divya" ,"divya"]
# employee ={
#     "name" : "Divya",
#     "age" : 20,
#     "status" :  "single"
# }

employees = [["Name", "Age", "Status"],
             ["divya",20,"single"],
             ["jadav",20, "single"],
             ["divya", 20 , "single"]]


file_path = "D:\\python by bro code\\text.csv"

try:
    with open(file_path, 'w') as file:
        writer= csv.writer(file)
        
        print(f"csv file '{file_path} was created")
except FileExistsError:
    print("That file already exists!")