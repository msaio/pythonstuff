# class Animal(object):
#     pass

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

# class Person(object):
#     def __init__(self, name, pet):
#         self.name = name
#         self.pet = pet

# class Employee(Person):
#     def __init__(self, name, pet, salary):
#         super(Employee, self).__init__(name, pet)
#         self.salary = salary

# class User(Employee):
#     def __init__(self,name, pet, salary, password, email):
#         super(User, self).__init__(name, pet, salary)
#         self.password = password
#         self.email = email
#     def showall(self):
#         print self.name
#         print self.pet
#         print self.salary
#         print self.password
#         print self.email

# class computer(object):
#     def __init__(self,name, price):
#         self.name = name
#         print "name: ", self.name
#         self.price = price
#         print "price: ", self.price
#         self.backdoor = None

# class desktop(computer):
#     def __init__(self, name, price, deploy, parts):
#         super(desktop, self).__init__(name, price)
#         self.deploy = deploy
#         print "deploy: ", self.deploy
#         self.parts = parts
#         print "parts: ", self.parts

# class Fish(object):
#     pass

# class Salmon(Fish):
#     pass

# class Halibut(Fish):
#     pass

#python3 code is here:
#begin
#Single Inheritance
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()
#Multiple Inheritance
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.')

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.')
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat') 
#end


#ROG = desktop("GTX1080ti", 10000, "On Desk", 20)