import urllib.request
import numpy
import numpy as np
import KNN
from bs4 import BeautifulSoup as bs
import xlrd
import xlwt
import random

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

# 导入excel
fname = "红楼梦分词4.xlsx"
bk = xlrd.open_workbook(fname)
# x
sheet1 = bk.sheet_by_name("开头")
x_nrows = sheet1.nrows
x_ncols = sheet1.ncols
x_list = []
for i in range(0, x_nrows):
    x_data = sheet1.row_values(i)
    x_list.extend(x_data)
# print(x_list)
sheet2 = bk.sheet_by_name("转换")
y_nrows = sheet2.nrows
y_ncols = sheet2.ncols
y_list = []
for i in range(0, y_nrows):
    y_data = sheet2.row_values(i)
    y_list.extend(y_data)
# print(y_list)
sheet3 = bk.sheet_by_name("结尾")
z_nrows = sheet3.nrows
z_ncols = sheet3.ncols
z_list = []
for i in range(0, z_nrows):
    z_data = sheet3.row_values(i)
    z_list.extend(z_data)
# print(z_list)
# 数据处理
all_count = []
count1 = 0
count2 = 0
count3 = 0
for i in range(120):
    for j in x_list:
        if j in book[i]:
            count1 += 1
    for k in y_list:
        if k in book[i]:
            count2 += 1
    for l in z_list:
        if l in book[i]:
            count3 += 1
    all_count.append([count1, count2, count3])
    count1 = 0
    count2 = 0
    count3 = 0

# 动态excel
wb = xlwt.Workbook(encoding="utf-8")
for z in range(10):
    # 随机取训练数组
    random_book = []
    list80 = []
    list40 = []
    for i in range(79):
        list80.append(i)
    random_book.extend(random.sample(list80, 6))
    for i in range(79, 120):
        list40.append(i)
    random_book.extend(random.sample(list40, 3))
    # print(random_book)
    random_book_count = []
    for i in range(9):
        # print(all_count[random_book[i]])
        random_book_count.append(all_count[random_book[i]])
    # print(random_book_count)

    # KNN
    dataSet, labels = KNN.createDataSet(random_book_count)
    outputLabel = []
    for i in range(120):
        test = np.array(all_count[i])
        k = 2
        outputLabel.append(KNN.clissfy0(test, dataSet, labels, k))
        # print("第%d章是%s类" % (i+1, outputLabel[i]))
        # print(all_count[i])
    # 导出excel
    ws = wb.add_sheet("红楼梦结果%d" % (z+1))
    ws.write(0, 0, label="章节")
    ws.write(0, 1, label="x")
    ws.write(0, 2, label="y")
    ws.write(0, 3, label="z")
    ws.write(0, 4, label="类别")
    for i in range(1, 121):
        ws.write(i, 0, "第%d章" % i)
        ws.write(i, 1, all_count[i-1][0])
        ws.write(i, 2, all_count[i-1][1])
        ws.write(i, 3, all_count[i-1][2])
        ws.write(i, 4, "%s类" % outputLabel[i-1])
wb.save("红楼梦结果.xls")
