#Source: https://stackoverflow.com/questions/76898146/why-json-loads-fails-with-readlinestypeerror-the-json-object-must-be-str-by
d =json.loads(x.strip("\n") for x in data)