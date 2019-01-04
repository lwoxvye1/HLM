import jieba
import xlsxwriter
wb = xlsxwriter.Workbook("总分词结果2.xls")
ws1 = wb.add_worksheet("总分词结果")
# 前四十回
all_chaps1 = []
with open('红楼梦前四十回.txt', "r", encoding="utf-8") as f:
    for chap in f.readlines():
        all_chaps1.append(chap)

dictionary1 = []
for i in all_chaps1:
    words = list(jieba.cut(i))
    dictionary1.extend(words)
# print(len(dictionary1))


num1 = 0
for i in range(193777):
    ws1.write(i, 0, dictionary1[num1])
    num1 += 1

# 中四十回
all_chaps2 = []
with open('红楼梦中四十回.txt', "r", encoding="utf-8") as f:
    for chap in f.readlines():
        all_chaps2.append(chap)

dictionary2 = []
for i in all_chaps2:
    words = list(jieba.cut(i))
    dictionary2.extend(words)
# print(len(dictionary2))

num2 = 0
for i in range(226798):
        ws1.write(i, 1, dictionary2[num2])
        num2 += 1


# 后四十回
all_chaps3 = []
with open('红楼梦后四十回.txt', "r", encoding="utf-8") as f:
    for chap in f.readlines():
        all_chaps3.append(chap)

dictionary3 = []
for i in all_chaps3:
    words = list(jieba.cut(i))
    dictionary3.extend(words)
# print(len(dictionary3))

num3 = 0
for i in range(203797):
    ws1.write(i, 2, dictionary3[num3])
    num3 += 1

wb.close()
