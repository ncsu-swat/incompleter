#Source: https://stackoverflow.com/questions/48277354/typeerror-a-bytes-like-object-is-required-not-str-how-can-i-fix-this
import urllib.request
import urllib.parse

def read_text():
    quotes = open("C:\Check Profanity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    address = "http://www.wdylike.appspot.com/?q="+encoded_text
    connection = urllib.request.urlopen(address)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()