import numpy as np
arr=[30,40,50,60]
print(arr)
arr1=max(arr)
print(arr1) 
arr2=min(arr)
print(arr2)
arr3=np.mean(arr)
print(arr3)
arr4=np.median(arr)
print(arr4)
diff=np.diff(arr)
print("day to day changes", diff)
fehrenheit=np.array(arr)*9/5+32
print("fehrenheit", fehrenheit)
age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")   
else:    print("you are not eligible to vote")

