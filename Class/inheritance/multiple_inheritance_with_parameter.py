class A(object):
    def __init__(self, x):
        self.x = x
        print("This is A" + str(self.x))

class B(object):
    def __init__(self, v):
        self.v = v
        print("This is B" + str(self.v))

class C(object):
    def __init__(self, w):
        self.w = w
        print("This is C" + str(self.w))

# Class Q inherit from A -> B -> C
# A, B, C is the same level
# The tree:
# A  B  C
#  \ | /
#   \|/
#    Q   
class Q(A,B,C):
    def __init__(self,x,v,w,var):
        A.__init__(self,x)
        B.__init__(self,v)
        C.__init__(self,w)
        self.var = var
        print("This is Q" + str(self.var))

print("---")
q = Q(0, 1, 2, 3)
print(Q.__mro__)