# This template is provided to give you a starting point for structuring your code,
# but it is intentionally left empty. You are encouraged to write the entire implementation
# from scratch to help you practice the problem-solving process and reinforce the
# programming concepts we've discussed in class.
#
# Writing code from scratch helps you:
# - Develop a deeper understanding of Python syntax and logic.
# - Improve your problem-solving skills by working through challenges.
# - Gain confidence in implementing object-oriented principles and other key topics.
#
# Please sketch your implementations and logic on paper before writing code.
#
# Important: **Do not change the name of this file**.
# If you submit this file to Gradescope using a different file name, you will receive a penalty of **-10 points**.
#
# Please write your code below.

class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def get_description(self):
        answer=str(self.year)
        answer+=' '+self.make+' '+self.model
        return answer
    
class Car(Vehicle):
    def __init__(self, make, model, year,doors):
        super().__init__(make, model, year)
        self.doors=doors

    def get_description(self):
        return super().get_description()+', '+str(self.doors)+'-door'
    
class Truck(Vehicle):
    def __init__(self, make, model, year,payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity=payload_capacity

    def get_description(self):
        return super().get_description()+', PayLoad capacity: '+str(self.payload_capacity)+' tons'
    
car = Car("Toyota", "Corolla", 2021, 4)
print(car.get_description())
# Output: 2021 Toyota Corolla, 4-door
truck = Truck("Ford", "F-150", 2020, 1.5)
print(truck.get_description())
# Output: 2020 Ford F-150, Payload capacity: 1.5 tons