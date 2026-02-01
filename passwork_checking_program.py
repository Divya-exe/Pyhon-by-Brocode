import string
psw = input("enter a password: ")
if len(psw) >= 8:
    for chars in psw:
        if not chars.isupper():
            has_upper =True
        if chars.islower():
            has_lower =True
        if chars.isdigit():
            has_digit =True
        
    print(psw)    
    
else:
    print("password must must be in 8 charaters ")   
    
