import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text

def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return soup

def job_data(soup):
    data_str = ''
    for item in soup.find_all('a', class_='jobtitle turnstileLink'):
        data_str = data_str + item.get_text()
    result_1 = data_str.split('\n')
    return result_1

def company_data(soup):
    data_str = ''
    for item in soup.find_all('div', class_='sjcl'):
        data_str = data_str + item.get_text()
    result_1 = data_str.split('\n')
    res = []
    for i in range(1, len(result_1)):
        if len(result_1[i]) > 1:
            res.append(result_1[i])
    return res
if __name__ == '__main__':
    job = 'data+science+internship'
    Location = 'Noida%2C+Uttar+Pradesh'
    url = 'https://in.indeed.com/jobs?q=' + job + '&l=' + Location
    soup = html_code(url)
    job_res = job_data(soup)
    com_res = company_data(soup)
    temp = 0
    for i in range(1, len(job_res)):
        j = temp
        for j in range(temp, 2 + temp):
            print('Company Name and Address : ' + com_res[j])
        temp = j
        print('Job : ' + job_res[i])
        print('-----------------------------')