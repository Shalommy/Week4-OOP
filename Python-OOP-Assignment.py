class Person:
    def __init__(self, name, age, gender):
     self.name = name
     self.age = age
     self.gender = gender
    
    def introduce(self):
        print(f"Hello, your name is {self.name}. You are {self.age} years old and you are a {self.gender}.")

person1 = Person("Mary", 30, "female" )
person1.introduce()
