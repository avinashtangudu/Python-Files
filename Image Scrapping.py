
import urllib
import urllib.request
from bs4 import BeautifulSoup

def get_images(url):
    webpage = urllib.request.urlopen(url)
    soupweb = BeautifulSoup(webpage, "html.parser")
    return soupweb

soup = get_images("http://www.kalanjali.com/")
for image in soup.findAll('image'):
    normal=image.get('src')
    if normal[:1]=="/":
        pic = "http://kalanjali.com/" + normal
    else:
        pic = normal

    imagetemp = image.get('alt')
    if len (imagetemp) == 0:
        filename = str(i)
        i = i+1
    else:
        filename = imagetemp

    imagefile = open(filename + ".jpeg",'wb')
    imagefile.write(urllib.request.urlopen(pic).read())
    imagefile.close()
