# This is a nested list
x = [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
print(x)
# we change the first element of the first-nested-child list
x[0][0] = "gay"
print(x)
print("It's quite obviously, right?")
print("But....")
# This is a simple list
x = ['a', 'b', 'c']
print(x)
# Let's make it a nested list
y = [x] * 4
print(y)
# Here we go
y[0][0] = "gay"
print(y)
# With the first list above x is an only list with 4 nested list inside with similar element
# The second x, which we * 4, makes y turn into 4 references to x, that's why this happens when we change the elements
y[0][1] = "Super Gay"
print(y)
y[0][2] = "Mega Gay"
print(y) 

