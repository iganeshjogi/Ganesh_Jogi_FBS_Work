# Method 1: import package

import myPackage
res = myPackage.myFunctions.addition(10,20)
print(res) 

# Method 2: import all functions

from myPackage.myFunctions import *
res = addition(10,20)
print(res)