from urllib.request import urlopen
from bs4 import BeautifulSoup
bs = BeautifulSoup(html, 'html.parser')
titles = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print('List all the header tags :', *titles, sep='\n\n')