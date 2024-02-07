from datetime import datetime
# from datetime import date
# from datetime import time

# import datetime

# result= dir(datetime.datetime)

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y') # year
result = datetime.strftime(simdi,'%X') # clock
result = datetime.strftime(simdi,'%d') # ayın kaçıncı gunu
result = datetime.strftime(simdi,'%A') # day
result = datetime.strftime(simdi,'%B') # month
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2019 hour 10:12:36'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

print(result)

birthday = datetime(1983,5,9,12,30,10)

print(birthday)