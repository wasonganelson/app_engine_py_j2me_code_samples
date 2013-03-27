import time #need this for timestamping ...
import math #need this to floor time values ...
from database import * #need this module to populate datastore ...

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
#end def timestamper ...

def timestamper1(departuretime, timestamp):
   value = ""
   currenttime = int(time.time())
   timespan = departuretime - (currenttime - timestamp)
   if int(math.floor(timespan/86400)) >= 1:
      if int(math.floor(timespan/86400)) == 1:
         value = "1 day"
      else:
         value = "%d days" % ( int(math.floor(timespan/86400)))
   elif int(math.floor(timespan/3600)) >= 1:
      if int(math.floor(timespan/3600)) == 1:
         value = "1 hour"
      else:
         value = "%d hours" % ( int(math.floor(timespan/3600)))
   elif int(math.floor(timespan/60)) >= 1:
      value = "%d min" % (int(math.floor(timespan/60)))
   else:
      value = "%d sec" % (int(math.floor(timespan))+1)
   return value
#end def timestamper1 ...

def updatedatastore():
   #update ridesshared table ...
   query = Ridessharedtable.all()
   query.order('timestamp') #order by timestamp desc ... least recent to most recent  ...
   query.filter('status','active')
   queryresults = query
   if not queryresults:
      donothin = ""
   else:
      for rideshared in queryresults:
         departuretime = rideshared.departuretime
         timestamp = rideshared.timestamp
         currenttime = int(time.time())
         timespan = departuretime - (currenttime - timestamp)
         if timespan <= 0: 
            rideshared.status = 'inactive'
            rideshared.put()

   #update liftseekers table ...
   query = Liftseekerstable.all()
   query.order('timestamp') #order by timestamp desc ... least recent to most recent  ...
   query.filter('status','active')
   queryresults = query
   if not queryresults:
      donothin = ""
   else:
      for liftseeker in queryresults:
         departuretime = liftseeker.departuretime
         timestamp = liftseeker.timestamp
         currenttime = int(time.time())
         timespan = departuretime - (currenttime - timestamp)
         if timespan <= 0:
            liftseeker.status = 'inactive'
            liftseeker.put()

#end def timestamper1 ...
