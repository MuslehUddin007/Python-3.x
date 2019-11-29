import xlrd

# location 
loc = ("File1.xls")
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# for row 0 column 0
sheet.cell_value(0,0)
print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i),end=" ")

print("\n")
for i in range(sheet.nrows):
    print(sheet.cell_value(i,0),end=" ")

print(sheet.row_values(1))