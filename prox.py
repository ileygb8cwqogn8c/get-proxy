import requests
from bs4 import BeautifulSoup
banner = '''
 |  __ \                           / ____|         | |    
 | |__) | __ _____  ___   _ ______| |  __ _ __ __ _| |__  
 |  ___/ '__/ _ \ \/ / | | |______| | |_ | '__/ _` | '_ \ 
 | |   | | | (_) >  <| |_| |      | |__| | | | (_| | |_) |
 |_|   |_|  \___/_/\_\\__, |       \_____|_|  \__,_|_.__/ 
                       __/ |                 coded by: @foxeditor          
                      |___/                  channel: @montelisa
'''
print(banner)
f = open('prox.txt','w')
def get_site(site):
    r = requests.get(site)
    return r.text
def datas(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')

    for tr in line:
        td = tr.find_all('td')
        ip = td[1].text
        port = td[2].text
        data = ip+':'+port
        print(data)
        f.write(data + '\n')
    f.close()
def main():
    url = 'http://foxtools.ru/Proxy'
    datas(get_site(url))
main()
