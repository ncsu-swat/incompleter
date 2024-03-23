#Source: https://stackoverflow.com/questions/70434952/attributeerror-str-object-has-no-attribute-descendants-error-with-automati
PATH = (r"C:\Users\gustavo.vieira\Desktop\python\drivers\msedgedriver.exe")
funds_list = ['VINLAND MACRO MASTER FUNDO DE INVESTIMENTO MULTIMERCADO']
url = 'https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CConsolFdo/FormBuscaParticFdo.aspx'


for i in funds_lista:
    driver = webdriver.Edge(PATH)
    driver.get(url)
    search = driver.find_element_by_name("txtCNPJNome")
    search.send_keys(i)
    search.send_keys(Keys.RETURN)
    driver.find_element_by_link_text(i).click()
    font = driver.find_element_by_link_text('Composição da Carteira').click()
    soup = BeautifulSoup(font)
    rows = soup.find_all("tr")
    print(rows)