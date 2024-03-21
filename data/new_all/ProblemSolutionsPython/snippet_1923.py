# Python3 code to demonstrate working of 
# Nested Dictionary with List
# Using loop + zip()
  
# initializing dictionary and list
test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
test_list = [8, 3, 2]
  
# printing original dictionary and list
print("The original dictionary is : " + str(test_dict))
print("The original list is : " + str(test_list))
  
# using zip() and loop to perform 
# combining and assignment respectively.
res = {}
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])
          
# printing result 
print("The mapped dictionary : " + str(res))