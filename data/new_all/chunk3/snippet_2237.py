#Source: https://stackoverflow.com/questions/55936150/why-do-i-get-a-typeerror-when-passing-a-bytes-string-to-magic-from-buffer
In [17]: response = requests.get('https://upload.wikimedia.org/wikipedia/commons/3/31/Red-dot-5px.png')                                                                           

In [18]: response.content                                                                                                                                                         
Out[18]: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x05\x00\x00\x00\x05\x08\x06\x00\x00\x00\x8do&\xe5\x00\x00\x00\x1cIDAT\x08\xd7c\xf8\xff\xff?\xc3\x7f\x06 \x05\xc3 \x12\x84\xd01\xf1\x82X\xcd\x04\x00\x0e\xf55\xcb\xd1\x8e\x0e\x1f\x00\x00\x00\x00IEND\xaeB`\x82'

In [19]: magic.from_buffer(response.content, mime=True)                                                                                                                           
Out[19]: 'image/png'