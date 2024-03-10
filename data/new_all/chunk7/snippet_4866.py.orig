#Source: https://stackoverflow.com/questions/44511613/python-file-read-questions-filenotfounderror
file_path ='D:\summer2017\4\pi2.txt'
with open('pi2.txt')as file_object:
    content1=file_object.read()
    print(content1.rstrip())
#it works and print 3.14****
#D:\summer2017 is this project folder


file_path =r'F:\test\123.txt'
with open('123.txt')as file_object:
    content1=file_object.read()
    print(content1.rstrip())
#FileNotFoundError: [Errno 2] No such file or directory: '123.txt'
# i create a 123.txt in F:\test
# but it can not read

file_path =r'F:\test\pi2.txt'
with open('pi2.txt')as file_object:
    content1=file_object.read()
    print(content1.rstrip())
# i create another pi2.txt in F:\test
# now it can be found
# in this txt there are some random alphabet and nums but not 3.14****
# but it also print the pi num