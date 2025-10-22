import random
import time

def getRandomDate(startDate, endDate):
   print("Generating a random date between", startDate, "and", endDate)
   randomGenerator = random.random()
   dateformat = "%d-%m-%Y"
   starttime = time.mktime(time.strptime(startDate, dateformat))
   endtime = time.mktime(time.strptime(endDate, dateformat))
   randomtime = starttime + randomGenerator * (endtime - starttime)
   randomDate = time.strftime(dateformat, time.localtime(randomtime))
   return randomDate
print("Random date:", getRandomDate("01-01-2020", "31-12-2025"))