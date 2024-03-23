#Source: https://stackoverflow.com/questions/51152635/typeerror-string-indices-must-be-integers-python
with open ('file location','r') as f:
    urls =[line.strip() for line in f]


lookup = [ ]
for url in urls:
        lookup.append (PubMedLookup(url,email))
i = 0
while True:
    publication = Publication(lookup[i])
    print(
        """
JOURNAL:\n{journal}\n
"""
        .format(**{
            'journal':publication.journal,
            }))
    i +=1
    if i >3:
        break