#Source: https://stackoverflow.com/questions/49465554/try-to-build-webserver-and-read-html-file-with-typeerror-must-be-str-not-byte
#coding=utf-8

import socket
import re

HOST = ''
PORT = 8000

#Read index.html, put into HTTP response data
index_content = '''
    HTTP/1.x 200 ok
    Content-Type: text/html

    '''

file = open('index.html', 'r')
index_content += file.read()
file.close()

#Read picture, put into HTTP response data
file = open('Yoda.png', 'rb')
pic_content = '''
    HTTP/1.1 200 ok
    Content-Type: image/png

    '''
pic_content += file.read()
file.close()



#Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

#infinite loop
while True:
    # maximum number of requests waiting
    conn, addr = sock.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src  = request.split(' ')[1]

    print ("Connect by: ", addr)
    print ("Request is:\n", request)

    #deal wiht GET method
    if method == 'GET':
        if src == '/index.html':
            content = index_content
        elif src == '/Yoda.png':
            content = pic_content
        elif re.match('^/\?.*$', src):
            entry = src.split('?')[1]      # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            content += entry
            content += '<br /><font color="green" size="7">register successs!</p>'
        else:
            continue


    #deal with POST method
    elif method == 'POST':
        form = request.split('\r\n')
        entry = form[-1]      # main content of the request
        content = '''HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'''
        content += entry
        content += '''<br /><font color="green" size="7">register successs!</p>'''

    ######
    # More operations, such as put the form into database
    # ...
    ######

    else:
        continue

    conn.sendall(content)

    #close connection
    conn.close()