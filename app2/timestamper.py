import time #need this for timestamping ...
import math #need this to floor time values ...

def timestamper(timestamp):
   value = ""
   currenttime = int(time.time())
   timespan = currenttime - timestamp
   if int(math.floor(timespan/86400)) >= 1:
      if int(math.floor(timespan/86400)) == 1:
         value = "1 day ago"
      else:
         value = "%d days ago" % ( int(math.floor(timespan/86400)))
   elif int(math.floor(timespan/3600)) >= 1:
      if int(math.floor(timespan/3600)) == 1:
         value = "1 hour ago"
      else:
         value = "%d hours ago" % ( int(math.floor(timespan/3600)))
   elif int(math.floor(timespan/60)) >= 1:
      value = "%d min ago" % (int(math.floor(timespan/60)))
   else:
      value = "%d sec ago" % (int(math.floor(timespan))+1)
   return value
#end def timestamper
