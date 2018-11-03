#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address

# ######### EDITED BY CommandActor ######### #

import urllib.request as urllib2
import json
import codecs
import sys
from pathlib import Path

if len(sys.argv) != 2:
	print("Error: incorrect args, must be 1")
	print("Use: python3 macven.py [maclist.txt]")
	exit()

file = Path(sys.argv[1])
if file.is_file() == False:
	print("Error: Cannot open", sys.argv[1])

file = open(sys.argv[1], "r")
macs = file.readlines()
print("File is valid")
print()

url = "http://macvendors.co/api/"

for mac in macs:

	if mac.rstrip().count(":") != 5 or len(mac.rstrip()) != 17:
		print(mac, "=> INVALID MAC")
		continue

	#Mac address to lookup vendor from
	mac_address = mac.rstrip()
	request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
	response = urllib2.urlopen( request )
	#Fix: json object must be str, not 'bytes'
	reader = codecs.getreader("utf-8")
	obj = json.load(reader(response))
	#Print company name
	try:
		str((obj['result']['company']+"<br/>"))
	except KeyError:
		print (mac_address + " => Unknown\n")
		continue
	print (mac_address + " => " + str((obj['result']['company']+"<br/>")).replace("<br/>", "") + "\n")
