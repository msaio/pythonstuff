import module_for_test
from sys import exit
from random import randint
from module_for_test import other 
from module_for_test import another_child 

# module -> dict style
print(module_for_test.mystuff)
print(module_for_test.mystuff['apple'])
print("*********************")
# module style
module_for_test.apple()
print("*********************")

# module -> class style
var = module_for_test.MyStuff()
var.apple()
print("*********************")

# Another class Example
happy_bday = module_for_test.Song(["Happy birthday to you", "Happy birthday to your motherfucker", "Happy birthday to scream 'Fuck U!!'"])

N_word = module_for_test.Song(["Move N word", "Get out the way, N word", "If u see me on the highway, get the F word off my way, N word"])

happy_bday.sing_me_a_song()
N_word.sing_me_a_song()
print("*********************")

# Animal class Example
Dog1 = module_for_test.Dog('Lucky')
print(Dog1.name)
Cat1 = module_for_test.Cat('Bad')
print(Cat1.name)
print("*********************")

# Person class Example
Person1 = module_for_test.Person('Sasha Grey')
Person1.pet = Cat1.name
print("Porn Star: " + Person1.name)
# Employee class Example
Employee1 = module_for_test.Employee('Sasha Grey', 1000000)
Employee1.pet = Person1.pet
print(Employee1.name + " Earns " + str(Employee1.salary) + "USD")
print("And has a pussy named "+"'"+ Employee1.pet +"'")
# HQ Employee class Example
HQ_employee1 = module_for_test.HQ_Employee('Sasha Grey', 1000000, 'Divine')
HQ_employee1.pet = Employee1.pet 
print("Porn Star: " + HQ_employee1.name + " Earns " + str(HQ_employee1.salary) + " USD in " + HQ_employee1.rank + " Rank")
print("And She has a pussy named: " + HQ_employee1.pet)
print("*********************")

# # The Game: Gotthons From Planet Percal #25
# a_map = module_for_test.Map('central_corridor')
# a_game = module_for_test.Engine(a_map)
# a_game.play()

# Inheritance in Python 2
## 1. Implicit Inheritance
dad = module_for_test.parent()
son = module_for_test.child()

dad.implicit()
son.implicit()
print("*********************")

## 2. Override explicitly
dad.override()
son.override()
print("*********************")

## 3. Alter before or after (Using super)
dad.altered()
son.altered()
print("*********************")

## 4. Multiple Inheritance
whoreson = module_for_test.child("AB", "Greys", 18)
whoreson.show_up()
print("*********************")

# Compostion
kid = another_child()
kid.override()
kid.implicit()
kid.altered()
