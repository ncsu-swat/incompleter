#Source: https://stackoverflow.com/questions/15879866/typeerror-object-new-takes-no-parameters-when-using-generators
class Prime():
    def _init_(self,i):
        self.i=i

def print_value(self):          
    while(True):
        yield(self.i)
        self.i+=self.i
p = Prime(1)
for numb in p.print_value():
    if(numb>100):
       break
    print(numb)