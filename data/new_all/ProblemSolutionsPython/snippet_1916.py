# python program to print 
# hollow half diamond star
  
  
# function to print hollow
# half diamond star
def hollow_half_diamond(N):
      
    # this for loop is for 
    # printing upper half 
    for i in range( 1, N + 1):
        for j in range(1, i + 1):
              
            # this is the condition to 
            # print "#" only on the
            # boundaries
            if i == j or j == 1:
                print("#", end =" ")
                  
            # print " "(space) on the rest
            # of the area
            else:
                print(" ", end =" ")
        print()
      
    # this for loop is to print lower half
    for i in range(N - 1, 0, -1):
          
        for j in range(1, i + 1):
              
            if j == 1 or i == j:
                print("#", end =" ")
              
            else:
                print(" ", end =" ")
          
        print()
  
# Driver Code
if __name__ == "__main__":
    N = 7
    hollow_half_diamond( N )