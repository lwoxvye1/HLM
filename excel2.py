import xlrd
fname = "红楼梦分词.xlsx"
bk = xlrd.open_workbook(fname)
# x
sheet1 = bk.sheet_by_name("开头")
x_nrows = sheet1.nrows
x_ncols = sheet1.ncols
x_list = []
for i in range(0, x_nrows):
    x_data = sheet1.row_values(i)
    x_list.extend(x_data)
print(x_list)
sheet2 = bk.sheet_by_name("转换")
y_nrows = sheet2.nrows
y_ncols = sheet2.ncols
y_list = []
for i in range(0, y_nrows):
    y_data = sheet2.row_values(i)
    y_list.extend(y_data)
print(y_list)
sheet3 = bk.sheet_by_name("结尾")
z_nrows = sheet3.nrows
z_ncols = sheet3.ncols
z_list = []
for i in range(0, z_nrows):
    z_data = sheet3.row_values(i)
    z_list.extend(z_data)
print(z_list)
