import urllib.request
from bs4 import BeautifulSoup as bs

book1 = []
book2 = []
book3 = []
for i in range(30):
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
    for i in range(40):
        book1.append(chapter)
    for i in range(40, 80):
        book2.append(chapter)
    for i in range(80, 120):
        book3.append(chapter)
with open("红楼梦1.txt", "wb")as f:
    for i in book1:
        f.write(i.encode("utf-8"))
with open("红楼梦2.txt", "wb")as f:
    for i in book2:
        f.write(i.encode("utf-8"))
with open("红楼梦3.txt", "wb")as f:
    for i in book3:
        f.write(i.encode("utf-8"))
