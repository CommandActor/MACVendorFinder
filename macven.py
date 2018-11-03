#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address

# ######### EDITED BY CommandActor ######### #

import urllib.request as urllib2
import json
import codecs
import sys

if len(sys.argv) != 2:
	print("Error: incorrect args, must be 1")
	print("Use: python3 macven.py [mac]")
	exit()


if list(sys.argv[1]).count(":") != 5 or len(sys.argv[1]) != 17:
	print("Error: invalid MAC")
	exit()

#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
#Mac address to lookup vendor from
mac_address = sys.argv[1]
request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))
#Print company name
try:
	str((obj['result']['company']+"<br/>"))
except KeyError:
	print ("\n" + mac_address + " => Unknown\n")
	exit()
print ("\n" + mac_address + " => " + str((obj['result']['company']+"<br/>")).replace("<br/>", "") + "\n")
