import SimpleXMLRPCServer
import urllib

def getstockquote(stockname):
    proxies = {'http':'http://phy:phy@10.2.21.7:80/'}
    try:
       connection = urllib.urlopen("http://www.nellydata.com/suntra/livedata.asp", proxies = proxies)
       stream = connection.read()
       connection.close()
       f = open('1.txt','w')
       f.write(stream)
       f.close()
    except: print '\n\nData fetched from local source file .... could not make network connection \n\n'
    reply = '\n\tSorry ! Company not listed in the on the Nairobi Stock Exchange\n\n'
    connection = urllib.urlopen("http://localhost/python/stocks.php")
    stream = connection.read()
    connection.close()
    stockstring = '$'
    for x in stream:
       if x == '\t' or '':
          continue
       else:
           stockstring = stockstring + x
    stocklist = []
    stocklist = stockstring.splitlines()
    for x in stocklist:
       if x == stockname:
	 yesterday = stocklist[stocklist.index(stockname)+1]
         today = stocklist[stocklist.index(stockname)+2]
	 pricechange = stocklist[stocklist.index(stockname)+3]
         pcntchange = stocklist[stocklist.index(stockname)+5]
	 high = stocklist[stocklist.index(stockname)+6]
	 low = stocklist[stocklist.index(stockname)+7]
	 nooftrades = stocklist[stocklist.index(stockname)+8]
	 sharestraded = stocklist[stocklist.index(stockname)+9]
         if pricechange == '':
	    pricechange = '0.00'
	 reply = '\n '+stockname+':'+'\n\tYesterday :'+yesterday+'\n\tToday :'+today+'\n\tPrice Change :'+pricechange+'\n\tPercentage Change :'+pcntchange+'\n\tHigh :'+high+'\n\tLow :'+low+'\n\tNo of Trades :'+nooftrades+'\n\tShares traded :'+sharestraded+'\n\n'
       else:
          continue
    return reply

        

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("41.89.64.32", 10000))
#server = SimpleXMLRPCServer.SimpleXMLRPCServer(("192.168.2.3", 10000))
server.register_function(getstockquote)
try:
   print "\n\nServer powered up, listening on port 10000 ...."
   server.serve_forever()
except KeyboardInterrupt:
   print "\n\nServer shutting down ...."
