#Source: https://stackoverflow.com/questions/59697444/typeerror-unsupported-operand-types-for-str-and-int-python
import datetime


q= datetime.date(2004,12,25)

e= datetime.date(2019,11,23) 

f= datetime.date(2019,11,26)

p= datetime.date(2004,12,13)

nam=[["attack on titan",10,"completed",p,q],["one punch man",10,"WATCHING",e,f]]

print("|         NAME           | SCORE |   STATUS   |  DATE STARTED  |    DATE ENDED   |") 

for KI in nam:
  print("|",KI[0]," "*22-len(KI[0]),"|"," ",KI[1]," ","|",KI[2]," "*(10-len(KI[2])),"|",""*2,KI[3], 
         " "*2,"|"," "*3,KI[4]," "*2,"|")