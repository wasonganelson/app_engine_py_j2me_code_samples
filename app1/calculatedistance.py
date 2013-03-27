import math #need this to floor time values ...

def calculatedistance(x1,y1,x2,y2):
   lat1, lon1 = float(x1), float(y1)
   lat2, lon2 = float(x2), float(y2)
   radius = 6371 # km
   dlat = math.radians(lat2-lat1)
   dlon = math.radians(lon2-lon1)
   a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   d = radius * c * 1000
   return int(d)
#end def calculatedistance...
