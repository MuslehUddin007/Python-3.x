import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet Name')

# specifying style
style = xlwt.easyxf('font: bold 1')
# Appling multiple styles
style1 = xlwt.easyxf('font: bold 1, color red;')

# specifying column
sheet1.write(0,0,'SAMPLE',style)

sheet1.write(1,0,'ISBT DEHRADUN')
sheet1.write(2,0,'SHASTRADHARA')
sheet1.write(3,0,'CLEMEN TOWN')
sheet1.write(4,0,'RAJPUR ROAD')
sheet1.write(5,0,'CLOCK TOWER')
sheet1.write(0,1,'ISBT DEHRADUN')
sheet1.write(0,2,'SHASTRADHARA')
sheet1.write(0,3,'CLEMEN TOWN')
sheet1.write(0,4,'RAJPUR ROAD')
sheet1.write(0,5,'CLOCK TOWER')
wb.save("xlwt_example.xls")
