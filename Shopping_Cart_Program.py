foods= []
prices= []
total = 0

while True:
    food=input("enter the food you want to buy: ")
    if food.lower() =="q":
        print("Thnak you Visit Next time..!!")
        break
    else:
        price=float(input(f"Enter the price for the {food}: "))
        foods.append(food)
        prices.append(price)
        
print("-----YOUR CART -----")
        
for food in foods:
    print(food, end="")
    
for price in prices:
    total += price
print() 
print (f"the total {total}")  
        