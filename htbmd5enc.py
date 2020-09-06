import requests
import hashlib
from bs4 import BeautifulSoup

url = 'http://docker.hackthebox.eu:31516'

s = requests.session()
md5string = s.get(url)
temp = BeautifulSoup(md5string.content, 'html5lib')
temp2 = temp.find('h3').getText()
result = (hashlib.md5(temp2.encode('utf-8'))).hexdigest()
data = {'hash': result}
resp = s.post(url, data = data)
t = BeautifulSoup(resp.content, 'html5lib')
print(t)