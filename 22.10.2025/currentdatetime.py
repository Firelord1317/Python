from  datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date:", today)
print("\nCurrent time:", now.time())

print("Date components:", today.year, today.month, today.day)