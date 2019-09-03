# Link to for details:  https://www.python-course.eu/classes_and_type.php
## Old Style
class robot_old_a:
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        return "Hi, I am" + self.name

## b inherit from a
class robot_old_b(robot_old_a):
    pass

if __name__ == "__main__":
    a = robot_old_a("Alan")
    b = robot_old_b("Bran")
    
    print(type(robot_old_a), type(robot_old_b))
    print(type(a), type(b))

## Output:
## Python2:
# (<type 'classobj'>, <type 'classobj'>)
# (<type 'instance'>, <type 'instance'>)
## Python3:
# <class 'type'> <class 'type'>
# <class '__main__.robot_old_a'> <class '__main__.robot_old_a'>

## New Style
class robot_new_a(object):
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        return "Hi, I am" + self.name

class robot_new_b(robot_new_a):
    pass

if __name__ == "__main__":
    a = robot_new_a("Alex")
    b = robot_new_b("Beck")

    print(type(robot_new_a), type(robot_new_b))
    print(type(a), type(b))
## Output:
## Python2:
# (<type 'type'>, <type 'type'>)
# (<class '__main__.robot_new_a'>, <class '__main__.robot_new_b'>
## Python3:
# <class 'type'> <class 'type'>
# <class '__main__.robot_new_a'> <class '__main__.robot_new_b'>

# Another style(Similar With New style):

def robot_c_init(self, name):
    self.name = name

robot_c = type("robot_c",
                (),
                {"counter":0,
                "__init__":robot_c_init,
                "sayHello":lambda self: "Hi, I am " + self.name
                }
            )

if __name__ == "__main__":
    c = robot_c("Cody")
    print(c.name)
    print(c.sayHello())

    print(type(robot_c))
    print(type(c))
    print(c.__dict__)
    print(robot_c.__dict__)

