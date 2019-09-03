# Multi copies of the method ans() in each class P:
class P1:
    def ans(self, *args):
        return 42

class P2:
    def ans(self, *args):
        return 42

class P3:
    def ans(self, *args):
        return 42

if __name__ == "__main__":
    x = P1()
    y = P2()
    z = P3()
    print(x.ans())
    print(y.ans())
    print(z.ans())

    print("-----------")


# Create an ans class and each P class inherit:
class the_ans:
    def ans(self, *args):
        return 42

class P_1(the_ans):
    pass

class P_2(the_ans):
    pass

class P_3(the_ans):
    pass

if __name__ == "__main__":
    a = P_1()
    b = P_2()
    c = P_3()
    print(a.ans())
    print(b.ans())
    print(c.ans())
    print("-----------")

# Each P class will always have ans() method as we design as above
# Now, we dont know if we need ans() or not:
if __name__ == "__main__":
    inp = raw_input("Want an answer? (y/n)")
    if inp == "y":
        required = True
    else:
        required = False

    def ans(self, *args):
        return 42

    class P__1: 
        pass
    if required:
        P__1.ans = ans

    class P__2: 
        pass
    if required:
        P__2.ans = ans

    class P__3: 
        pass
    if required:
        P__3.ans = ans

    k = P__1()
    l = P__2()
    h = P__3()

    if required:
        print(k.ans())
        print(l.ans())
        print(h.ans())
    else:
        print("Nope")
    
    print("-----------")


# Now we will use a manager function to augment the classes (add ans() to P class)
if __name__ == "__main__":
    inp = raw_input("Want an answer? (y/n)")
    if inp == "y":
        required = True
    else:
        required = False

    def ans(self, *args):
        return 42
    def augment_ans(cls):
        if required:
            cls.ans = ans

    class P___1: 
        pass
    augment_ans(P___1)
    class P___2: 
        pass
    augment_ans(P___2)
    class P___3: 
        pass
    augment_ans(P___3)
        
    w = P___1()
    e = P___2()
    r = P___3()

    if required:
        print(w.ans())
        print(e.ans())
        print(r.ans())
    else:
        print("Nope")
    
    print("-----------")

# We must not forget to call manager function augment_ans()
# So, the code should be excuted automatically.

if __name__ == "__main__":
    inp = raw_input("Want an answer? (y/n)")
    if inp == "y":
        required = True
    else:
        required = False

    def ans(self, *args):
        return 42
    def augment_ans(cls):
        if required:
            cls.ans = ans
        # Must return the class
        return cls

    @augment_ans
    class P____1: 
        pass
    
    @augment_ans
    class P____2: 
        pass
    
    @augment_ans
    class P____3: 
        pass
        
    f = P____1()
    g = P____2()
    v = P____3()

    if required:
        print(f.ans())
        print(g.ans())
        print(v.ans())
    else:
        print("Nope")
    
    print("-----------")

