# Method 1: import module

# import myModule
# res = myModule.chkEven(1)

# Method 2: import all functions/variables/class

# from myModule import *
# res = chkPositive(-5) 

# Method 3: import only required functions

# from myModule import chkEven
# res = chkEven(8)

# Method 4: Alias name

from myModule import chkEven as ce
res = ce(8)
print(res)
print(__name__)