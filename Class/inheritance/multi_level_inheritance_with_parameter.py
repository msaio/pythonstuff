class A(object):
    def __init__(self, x):
        self.x = x
        print("This is A" + str(self.x))

class B(A):
    def __init__(self, x ,v):
        A.__init__(self, x)
        self.v = v
        print("This is B" + str(self.v))

class C(B):
    def __init__(self, x, v, w):
        B.__init__(self, x, v)
        self.w = w
        print("This is C" + str(self.w))
# Inherit Tree: 
# A->B->C
c = C(0,1,2)
print(C.__mro__)