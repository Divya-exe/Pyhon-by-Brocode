class Animals:
    alive = True
    
class Dog(Animals):
    def speak(self):
        print("Woof!")

class Cat(Animals):
    def speak(self):
        print("MEOW!")

class Car(Animals):
    def speak(self):
        print("HONK!")
    
Animals=[Dog(),Cat(),Car()]
for animal in Animals:
    animal.speak()
    print(animal.alive)