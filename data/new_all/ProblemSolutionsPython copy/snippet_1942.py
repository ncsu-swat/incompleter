# Function to concatenated string with uncommon 
# characters of two strings 
  
def uncommonConcat(str1, str2): 
  
    # convert both strings into set 
    set1 = set(str1) 
    set2 = set(str2) 
  
    # take intersection of two sets to get list of 
    # common characters 
    common = list(set1 & set2) 
  
    # separate out characters in each string 
    # which are not common in both strings 
    result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common] 
  
    # join each character without space to get 
    # final string 
    print( ''.join(result) )
  
# Driver program 
if __name__ == "__main__": 
    str1 = 'aacdb'
    str2 = 'gafd'
    uncommonConcat(str1,str2)