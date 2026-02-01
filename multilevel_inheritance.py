class Animal:
    def __init__(self,name):
        self.name=name
        
    def sleep(self):
        print(f"{self.name} is slepping")
        
class Prey(Animal):
    def flee(self):
        print("This animal is Fleeing")
        

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
        

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit= Rabbit("little")
hawk = Hawk("hose")
fish = Fish("luna")


fish.hunt()