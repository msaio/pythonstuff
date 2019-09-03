class A(object):
    def __init__(self, x):
        self.x = x
        print("This is A" + str(self.x))

class Z(object):
    def __init__(self):
        print("This is Z")

class B(Z):
    def __init__(self,v):
        Z.__init__(self)
        self.v = v
        print("This is B" + str(self.v))

class C(Z):
    def __init__(self, w):
        Z.__init__(self)
        self.w = w
        print("This is C" + str(self.w))

class Q(A, B, C):
    def __init__(self, x, v, w, var):
        A.__init__(self, x)
        B.__init__(self, v)
        C.__init__(self, w)
        self.var = var
        print("This is Q" + str(self.var))

q = Q(0,1,2,3)
print(Q.__mro__)