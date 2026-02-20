psw=input("enter a new password ")
has_upper =False
has_lower = False
has_digit =False

if len(psw) >= 8:
    for char in psw:
        if char.isupper():
            has_upper= True
            print("strong")
        if char.islower():
            has_lower=True
        if char.isdigit():
            has_digit = True
    if has_upper and has_lower and has_digit:
        print("your password is very strong")
    elif has_upper or has_lower or has_digit:
        print("your password is midium")
    else:
        print("week")
else:
    print("Password must be at least 8 characters long ❌")
    
