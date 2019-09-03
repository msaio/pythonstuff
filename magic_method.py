# Length:
class Length:
    __metric = {"mm":0.001, "cm":0.01, "dm":0.1, "m":1, "dam":10, "hm":100, "km":1000,
                "in":0.0254, "ft":0.3048, "yd":0.9144,
                "mi":1609.344}
    
    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
        self.value = l / Length.__metric[self.unit]
        return self
    
    def __radd__(self, other):
        return Length.__add__(self, other)
    
    def __str__(self):
        return str(self.Converse2Metres()) + " m"
    
    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"

if __name__ == "__main__":
    x = Length(1, "km")
    print(repr(x))
    repr_of_x = repr(x)
    print(eval(repr_of_x))
    print(x)

    x = Length(1, "km") + Length(30, "ft") + Length(100,"mm") + Length(50, "in")
    print(x)

    x += 10
    print(x)

    x = 10 + Length(19, "m")
    print(x)
    print("-----------")

# Polynomial
class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        
    def __call__(self, x=None):
        if x is not None:
            res = 0
            for index, coeff in enumerate(self.coefficients):
                res += coeff * x** index
            return res
        elif x is None:
            print("Nothing to do")
            return self.coefficients

if __name__ == "__main__":
    p1 = Polynomial(1)
    # print(p1.coefficients, type(p1.coefficients))

    p2 = Polynomial(1,2)
    # print(p2.coefficients)

    p3 = Polynomial(1,2,3)
    
    for i in range(1,4):
        print(i, p1(i), p2(i), p3(i))
        # p1 
        # i=1, p1, p1.lenght()=1, res=0
        # |
        # v 
        # x=1, index=0, coeff=1, res=0
        # |
        # v 
        # res= res + coeff*x**index <=> res= 0 + 1 * 1^0 <=> res= 1
        #####
        # p2 
        # i=1, p2, p2.lenght()=2, res=0
        # |
        # v 
        # x=1, index=0, coeff=1, res=0
        # |
        # v 
        # res= res + coeff*x**index <=> res= 0 + 1 * 1^0 <=> res= 1

        # i=1, p2, p2.lenght()=2, res=0
        # |
        # v 
        # x=1, index=1, coeff=2, res=0
        # |
        # v 
        # res= res + coeff*x**index <=> res= 1 + 2 * 1^1 <=> res= 3
        # Keep going and we got p3, just similarly

    print("--")
    print(p1())
    print(p2())
    print(p3())
    print("-----------")

# More in Class/currency.py