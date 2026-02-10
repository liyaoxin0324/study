from calculator import *
a_add = add(4,5)
print(a_add)
a_sub = subtract(7,2)
print(a_sub)
a_mul = multiply(3,4)
print(a_mul)
try:
     a_div = divide(5,0)
     print(a_div)
except ValueError as e:
     print(e)




