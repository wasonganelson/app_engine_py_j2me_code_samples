import time #need this for timestamping ...
import math #need this to floor time values ...

def timestamper(articletimestamp):
   value = ""
   currenttime = int(time.time())
   timespan = currenttime - articletimestamp
   if int(math.floor(timespan/86400)) >= 1:
      if int(math.floor(timespan/86400)) == 1:
         value = "<b>1</b> day ago"
      else:
         value = "<b>%d</b> days ago" % ( int(math.floor(timespan/86400)))
   elif int(math.floor(timespan/3600)) >= 1:
      if int(math.floor(timespan/3600)) == 1:
         value = "<b>1</b> hour ago"
      else:
         value = "<b>%d</b> hours ago" % ( int(math.floor(timespan/3600)))
   elif int(math.floor(timespan/60)) >= 1:
      value = "<b>%d</b> min ago" % (int(math.floor(timespan/60)))
   else:
      value = "<b>%d</b> sec ago" % (int(math.floor(timespan))+1)
   return value
#end def timestamper
