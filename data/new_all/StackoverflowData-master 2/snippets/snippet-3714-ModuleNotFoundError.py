#Source: https://stackoverflow.com/questions/69370337/filenotfounderror-errno-2-no-such-file-or-directory-even-though-it-gives-the
import PyPDF2
import os
import time

#Scan Directory

directory = 'C:\\Users\\Username\\OneDrive\\Desktop\\python'
for file in os.listdir(directory):
    if not file.endswith(".pdf"): #Skip non-PDF files
        continue
    with open(os.path.join(directory,file), 'rb') as pdfFileObj:  # Changes here
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text=pageObj.extractText()
        print("Writing File "+ file +" to TXT.")
        file2=open(r"C:\Users\Username\OneDrive\Desktop\python\\"+file.replace('pdf','txt'),"a") #Write as TXT files
        file2.writelines(text)
        print("Done saving.")
        file2.close()