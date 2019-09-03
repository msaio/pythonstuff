class A(object):
    def __init__(self,x , *a, **b):
        super(A, self).__init__(*a, **b)
        self.x = x
        print("This is A" + str(self.x))

class Y(object):
    def __init__(self,y , *a, **b):
        super(Y, self).__init__(*a, **b)
        self.y = y
        print("This is Y" + str(self.y))

class Z(object):
    def __init__(self, *a, **b):
        super(Z, self).__init__(*a, **b)
        print("This is Z")

# Class B inherit from Z
class B(Z):
    def __init__(self, v, *a, **b):
        super(B, self).__init__(*a, **b)
        self.v = v
        print("This is B" + str(self.v))

# Class C inherit from Z
class C(Z):
    def __init__(self, w, *a, **b):
        super(C, self).__init__(*a, **b)
        self.w = w
        print("This is C" + str(self.w))

# The tree:
# A      Z       Y
# \     | \      |
#  \    |  \     |
#   \   B   C   /
#    \  |  /   /
#     \ | /   /
#       Q ----

class Q(A,B,C,Y):
    def __init__(self,x, v, w, var, y):
        super(Q, self).__init__(y=y, x=x, v=v, w=w)
        self.var = var
        print("This is Q" + str(self.var))
a = A(0)
print("---")
b = B(1)
c = C(2)
print("---")
q = Q(0, 1, 2, 3, 4)
print(Q.__mro__)