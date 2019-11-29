import calendar

yy = 2019
mm = 11
#print(calendar.month(yy,mm))
print(calendar.calendar(2019,2,1,6))

# iterweekdays
obj = calendar.Calendar(firstweekday=2) # 0,1,2,3,4,5,6
for day in obj.iterweekdays():
    print(day)

# itermonthdates
obj = calendar.Calendar(firstweekday=5)
for day in obj.itermonthdates(2019,9):
    print(day)

# itermonthdays
obj = calendar.Calendar(firstweekday=2)
for day in obj.itermonthdays(2019,4):
    print(day)

# itermonthdays2()
obj = calendar.Calendar(firstweekday=2)
for day in obj.itermonthdays2(2019,9):
    print(day)