import datetime
def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

# Usage demo1:
print todayAt (17), todayAt (17, 15)

# Usage demo2:    
timeNow = datetime.datetime.now()
if timeNow < todayAt (17):
   print "Too Early"
