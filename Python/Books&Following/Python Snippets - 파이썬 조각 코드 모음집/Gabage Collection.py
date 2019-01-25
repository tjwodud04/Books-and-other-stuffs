#class A:
#    def __del__(self):
#        print("deleted")

#a = A()
#del(a)

#---------------------------

class A:
    def __del__(self):
        print("deleted")

a = A()
b = a

del(a)
#---------------------------

import sys
class A:
    pass
a = A()
b = a

print(sys.getrefcount(a))