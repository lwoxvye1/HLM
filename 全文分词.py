import urllib.request
import re
from bs4 import BeautifulSoup as bs
import codecs
book = []
for i in range(120):
    print("处理第{}回...".format(i+1))
    if i+1 < 10:
        url = "http://www.purepen.com/hlm/00{}.htm".format(i+1)
    elif i+1 < 100:
        url = "http://www.purepen.com/hlm/0{}.htm".format(i+1)
    else:
        url = "http://www.purepen.com/hlm/{}.htm".format(i+1)
    response = urllib.request.urlopen(url)
    bsObj = bs(response.read().decode('gb18030'))
    chapter = bsObj.table.font.contents[0]
    book.append(chapter[:-1])

with open('红楼梦.txt', 'wb') as f:
    for i in book:
        f.write(i.encode("utf-8"))
