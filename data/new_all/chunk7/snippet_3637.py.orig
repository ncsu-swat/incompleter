#Source: https://stackoverflow.com/questions/70298185/str-object-has-no-attribute-append-attribute-error-when-i-try-append-to-dict
import glob
import os

def main():

 direct = r"C:\Users\Inzaghi\Desktop\Ondra_origin"

 main_dict={}

 for filename in glob.glob(os.path.join(direct, '*.spe')): 
  
    with open(filename,'r') as file:    
        print ('file read: ' + filename)
        lst=[]
        for line in file:
            line = line.replace('# ','')
            if len(line) == 14:
                line = line.rstrip().split()
                lst.append(line[1])
      
        for count, n in enumerate(lst[:-4]):
            if count in main_dict:
                main_dict[count].append(n)
            else:
                 main_dict[count]=n
                 
with open (direct+'\celkovy_file.txt','a') as f:
     for i in range(0,len(main_dict)):
         f.write(main_dict[i] + '\n')
print('Done')

if __name__=='__main__':
    main() 