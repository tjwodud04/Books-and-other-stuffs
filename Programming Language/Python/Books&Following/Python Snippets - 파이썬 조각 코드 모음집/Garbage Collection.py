class A:
   def __del__(self):
       print("deleted")

a = A()

del(a)
#print ("\n")

#---------------------------
class C:
   def __del__(self):
       print("deleted")

d = C()
e = d

del(d)
print ("\n")
#---------------------------

import sys
class A:
    pass
a = A()
b = a

print(sys.getrefcount(a))
#---------------------------

import gc

def test():
    class A:
        pass

    class B:
        def __init__(self, obj):
            self.obj = obj

    a = A()
    b = B(a)

    gc.collect()
    print(gc.get_referents(b))

test()