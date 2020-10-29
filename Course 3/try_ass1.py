from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter count: '))
pos=int(input('Enter position: '))
print('Retrieving: ', url)

while count > 0 :
    count = count - 1
    html=urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
    url=tags[pos - 1].get('href',None)
    print('Retrieving: ', url)
