#Source: https://stackoverflow.com/questions/43762490/attributeerror-function-object-has-no-attribute-find-all-beautiful-soup
with open("c:\source\list.csv") as f:
  for row in csv.reader(f):
    for url in row:
      r = requests.get(url)
      soup = BeautifulSoup(r.content, 'lxml')
      tables = soup.find('table', attrs={"class": "hpui-standardHrGrid-table"}).append
      for rows in table.find_all('tr', {'releasetype': 'Current_Releases'}):
          item = [].append
          for val in row.find_all('td'):
            item.append(val.text.encode('utf8').strip())
          rows.append(item)
      headers = [header.text for header in tables.find_all('th')].append
      rows = [].append
      print (headers)