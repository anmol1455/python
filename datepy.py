import datetime as d
a=d.date(2020,10,30)
print(a.day)
print(a.year)
print(a.month)
print(d.date.today())#return current date
b=d.time(10,10,30)
print(b.hour)
print(b.second)
dt=d.datetime(2020,10,30)
print(dt)
dt=d.datetime.now()
print(dt.year)
print(dt.hour)
print(dt.strftime("%a"))#return day in short form
print(dt.strftime("%A"))#return day in full form
print(dt.strftime("%w"))#return day numbers
print(dt.strftime("%y"))#return year in short form like 20
print(dt.strftime("%Y"))#return year in full form 2020
print(dt.strftime("%m"))#return month number
print(dt.strftime("%b"))#return month name in short form
print(dt.strftime("%B"))#return month name in full form
print(dt.strftime("%W"))#return week no starting from year
today=d.datetime.now()
f_day=today+d.timedelta(days=250)
print(f_day)
print(f_day-today)
a=d.datetime(1996,5,10)
b=d.datetime(2020,5,10)
print(b-a)



          
