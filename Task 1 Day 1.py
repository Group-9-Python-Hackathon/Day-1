from calendar import calendar
from datetime import date
from datetime import datetime
from struct import calcsize

date = str(date.today())
day = datetime.today().strftime('%a')
print("Date: "+date)
print("Day: "+day)
if day == "Sat":
    print("Fare : 60")
elif day == "Sun":
    print("Fare : 80")
else:
    print("Fare : 100")
    
