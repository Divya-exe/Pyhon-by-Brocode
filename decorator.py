def add_sprinkles(funs):
    def wrapper(*args,**kwargs):
        print("*You add sprinkles*")
        funs(*args,**kwargs)
    return wrapper
    
def add_fudge(funs):    
    def wrapper(*args,**kwargs):
        print("*You add fudge*")
        funs(*args,**kwargs)
    return wrapper
    
@add_sprinkles
@add_fudge

def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")
    
get_ice_cream("buttersctoch") 
    