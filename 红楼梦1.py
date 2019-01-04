import urllib
import urllib.request
import re
import codecs
from bs4 import BeautifulSoup as bs
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
    book.append(chapter)
#   print(book[0])
# 一章节,一章节导入

all_count = []
count = 0
for i in range(120):
    for j in ["话说", "却说", "且说", "彼时", "一日", "那日", "当下", "那时", "次日", "原来", "这里", "因类"]:
        if j in book[i]:
            count += 1
    all_count.append(count)
    count = 0
print(all_count)
random_book_count = [all_count[0], all_count[0], all_count[0], all_count[0],all_count[0],all_count[0], all_count[0], all_count[0], all_count[0], all_count[0], ]

