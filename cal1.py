import numpy as np
a = np.array([30, 40, 50, 60])
b= np.array([10, 20, 30, 40])
c=a+b
print(c)
print(a-b)
print(a*b)  
print(a/b)
print(a%b)  
print(np.dot(a,b))
if np.array_equal(a,b):
    print("a and b are equal")      
else:    print("a and b are not equal") 

