
try:
    number = int(input("Enter a number: "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Please enter numbers only!")

finally:
    print("Program execution completed.")

    
# Exception: an event that interrupts the flow of a program (ZeroDivisionError, ValueError, TypeError) 
#            1. try, 2. except , 3. finally