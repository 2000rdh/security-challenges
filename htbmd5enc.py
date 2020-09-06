#This Python program was written for "emdee five for life" on hackthebox.eu
#It pulls a string from the challenge's webpage and hashes it, then posts it back

import requests
import hashlib
from bs4 import BeautifulSoup

url = 'http://docker.hackthebox.eu:[port]' #port varies

#create a session
s = requests.session()

#extract the necessary string from the HTML
md5string = s.get(url)
temp = BeautifulSoup(md5string.content, 'html5lib')
temp2 = temp.find('h3').getText()

#hash the string
result = (hashlib.md5(temp2.encode('utf-8'))).hexdigest()

#post the hash
data = {'hash': result}
resp = s.post(url, data = data)

#get the result!
t = BeautifulSoup(resp.content, 'html5lib')
print(t)
