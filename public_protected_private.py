class a:
    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z
    
    def method1(self):
        print("This is public")
    
    def _method2(self):
        print("This is protected")
    
    def __method3(self):
        print("This is private")


instance_of_a = a("public", "protected", "private")
print("Property----------------------")
print("----------public------------")
print(instance_of_a.x)
print("----------protected------------")
# people say this is protected, but why i can still access ????
print(instance_of_a._y)
print("----------------------")
# i can even modify it, WTF ??
instance_of_a._y = "can i change the protected property ?"
print(instance_of_a._y)
print("----------------------")
# u can still access the private property 
print(instance_of_a._a__z)
print("----------private------------")
# u ll create a new variable 
instance_of_a.__z = "can i change the private property ?"
print(instance_of_a.__z)
print(instance_of_a._a__z)
print("----------------------")
# ezly modify the value
instance_of_a._a__z = "Can i?"
print(instance_of_a._a__z)
print("Method----------------------")
print("----------public------------")
instance_of_a.method1()
print("----------protected------------")
instance_of_a._method2()
print("----------private------------")
print("I can use this way: instance_of_a.__method3()")
instance_of_a._a__method3()
### There is no protected in python, who says 'there is' is liar or dumbass 