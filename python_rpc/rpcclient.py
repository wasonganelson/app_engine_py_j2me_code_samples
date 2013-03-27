import xmlrpclib
import os

proxy = xmlrpclib.ServerProxy("http://41.89.64.176:10000/")
print '\n RPC client powered up .....'
while True:
   os.system('clear')
   string = raw_input('\n\n\t\t\t.....Stocks Watch.....\n\n\tKey in name of a listed company, key in "exit" to shutdown RPC client\n\t:')
   stockname = string.strip()
   if stockname == 'exit':
      break
   else:
      print proxy.getstockquote(stockname)
      print 'Key in Enter to continue ..'
      raw_input('')
print '\n\nRPC client shutting down .....\n\n'

   
