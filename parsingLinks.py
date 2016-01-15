import urllib
from BeautifulSoup import *
import re
class URL(object):

    @staticmethod
    def _parsing(inputURL,position):
        #url = raw_input('Enter - ')
        url=inputURL
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        # Retrieve all of the anchor tags
        tags = soup('a')

        return tags[position]

    @staticmethod
    def parseURL(inputURL,position,count):

        position -= 1
        finalURL=inputURL
        name=""

        for run in range(0,count):
            tag=URL()._parsing(finalURL,position)
            finalURL=tag.get('href', None)
            name=re.search("<a\s+href=.+>([a-zA-Z]+)</a>",str(tag)).group(1)
        return name




#print URL().parseURL("https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html",3,4)
print URL().parseURL("https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jean.html",18,7)
