# asterisk -> '*'
# It usually looks like this:
# def f(*args, **kwargs):

# What does variable mean here is
# that you do not know before hand that 
# how many arguments can be passed to your function by the user 
# so in this case you use these two keywords.

# 1. *args
# *args is used to send a non-keyworded variable length argument list to the function.
# Positional Argument
def function_1(simple_arg, *more_arg):
    print("This is " + str(simple_arg))
    for arg in more_arg:
        print("And this is : "+str(arg))

if __name__ == "__main__":
    function_1('sinlge_asterisk', 'simple', 3, 10*2, 100.231)

# 2. **kwargs
# **kwargs allows you to pass keyworded variable length of arguments to a function. 
# You should use **kwargs if you want to handle named arguments in a function.
# Keywords Argument
def function_2(simple_arg, **more_kwargs):
    print("This is "+str(simple_arg))
    for kwargs_key, kwargs_value in more_kwargs.items():
        print("And this is : " + str(kwargs_key) + " - " + str(kwargs_value))

if __name__ == "__main__":
    function_2('double_asterick', kwarg_1="No 1", kwarg_2=30, kwarg_3=10*2, kwarg_4=10.31123 )
    function_2('double_asterick',)

# 3. Combine *args and **kwargs
def function_3(simple_arg, *args, **kwargs):
    print("This is "+str(simple_arg))
    i = 0
    for a in args:
        print(str(i)+" : "+str(a))
        i += 1
    i = 0
    for key, val in kwargs.items():
        print(str(i)+" : " + str(key) + " - " + str(val))
        i += 1

if __name__ == "__main__":
    function_3("Hello", "x", 1, 10.2, x=10, y="12", z=12.3)

# 4. More examples
def function_4(x, y, z):
    print(x)
    print(y)
    print(z)

if __name__ == "__main__":
    # This is a tuple
    args = ("Hello", 10, 31.23)
    # This is a dict
    kwargs = {"x" : "Hi", "y" : 31, "z" : 22.31} 

    function_4(*args)
    function_4(**kwargs)

# 5. More examples
def f_5(*a, **aa):
    print("Positional: ",a , type(a))
    print("Keywords: ",aa , type(aa))

if __name__ == "__main__":
    f_5("Hello", 5, x=10, y="Cyka")
    # Positional Argument will be stored as a tuple
    # Keywords Argument will be stored as a dict