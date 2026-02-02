class Employee:
    def __init__(self, name, position):
        self.name=name
        self.postions=position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
        
    @staticmethod
    def is_valid_position(position):
        valid_position=["Maneger","cook","driver","CEO"]
        return position in valid_position
        
print(Employee.is_valid_position("Maneger"))
    