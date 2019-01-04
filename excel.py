import xlrd
fname = "红楼梦分词.xlsx"
bk = xlrd.open_workbook(fname)
sheet1 = bk.sheet_by_name("开头")
nrows = sheet1.nrows
ncols = sheet1.ncols
# print("nrows{0},ncols{1}".format(nrows, ncols))
# cell_value = sheet1.cell_value(0, 0)
row_list = []
for i in range(0, nrows):
    row_data = sheet1.row_values(i)
    row_list.append(row_data)
print(row_list)
