import urllib
import re
from BeautifulSoup import *
from BeautifulSoup import *
#html=urllib.urlopen(" http://python-data.dr-chuck.net/comments_42.html").read()
html=urllib.urlopen(" http://python-data.dr-chuck.net/comments_217908.html").read()
soup=BeautifulSoup(html)
sum=0
"""
for tr in soup.findAll('tr'):
    for span in tr.findAll('span'):
        sum=sum+int(''.join(re.findall(">([0-9]+)<",str(span.extract()))))
"""
print sum
