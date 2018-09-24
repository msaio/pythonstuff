class parent(object):
    def implicit(self):
        print "parent implicit()"
    def override(self):
        print "parent override()"
    def altered(self):
        print "parent altered()"

class child(parent):
    def override(self):
        print "child override()"
    def altered(self):
        print "child before altered()"
        super(child,self).altered()
        print "child after altered()"

pa = parent()
so = child()

pa.implicit()
so.implicit()
print "------------------"
pa.override()
so.override()
print "------------------"
pa.altered()
so.altered()