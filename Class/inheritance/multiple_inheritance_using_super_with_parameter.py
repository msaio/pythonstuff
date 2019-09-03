class A(object):
    def __init__(self, x, *a, **b):
        super(A,self).__init__(*a, **b)
        self.x = x
        print("This is A" + str(self.x))

class B(object):
    def __init__(self, v, *a, **b):
        super(B,self).__init__(*a, **b)
        self.v = v
        print("This is B" + str(self.v))

class C(object):
    def __init__(self, w, *a, **b):
        super(C,self).__init__(*a, **b)
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
        super(Q, self).__init__(x=x, v=v, w=w)
        self.var = var
        print("This is Q" + str(self.var))
print("---")
q = Q(0, 1, 2, 3)
print q.w
print(Q.__mro__)