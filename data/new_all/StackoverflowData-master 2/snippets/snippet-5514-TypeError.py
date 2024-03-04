#Source: https://stackoverflow.com/questions/62653214/how-do-i-fix-typeerror-can-only-concatenate-str-not-bytes-to-str
hwa = b'|\x04\x06\r$>'

msg = '\xff' * 6 + hwa * 16
print(msg)