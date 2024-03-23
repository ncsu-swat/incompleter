#Source: https://stackoverflow.com/questions/62198079/my-code-is-giving-me-a-type-error-even-though-i-have-taken-care-of-the-type-pl
import os, random, re
os.chdir('.\\american date files')
for i in range(20):
    file = open(f'{random.randint(1, 12)}-{random.randint(1, 31)}-{random.randint(2000, 2099)}', 'w')
    file.close()
ame_dates = os.listdir()
ame_date = re.compile(r'(\d\d?)-(\d\d?)-(\d\d\d\d)')
euro_dates = [ame_date.sub(f'{ame_date.search(date).group(2)}-{ame_date.search(date).group(1)}-{ame_date.search(date).group(3)}', date) for date in ame_dates]
count = 0
for dirname, foldername, filename in os.walk(r'E:\pranil\python\doing stuff with python\american date files'):
    replacer = euro_dates[count]
    os.rename(filename, replacer)
    count += 1