#Create a Vehicle class with max_speed and mileage instance attributes and print them.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        print(f"maximum speed is {self.max_speed} and mileage is{self.mileage}")
    
Vehicle(280,8)




