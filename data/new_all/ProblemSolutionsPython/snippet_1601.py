import numpy as geek 
  
gfg = geek.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
  
# without trim parameter
# returns an array without leading and trailing zeros 
  
res = geek.trim_zeros(gfg)
print(res)