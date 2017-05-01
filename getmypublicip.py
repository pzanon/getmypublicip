#!/usr/bin/python
import time
import datetime
import os
from json import load
from urllib2 import urlopen

html_filename = "/tmp/mypublicip.html"

# get date and time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# get public ip address
my_ip = urlopen('http://ip.42.pl/raw').read()

def writeNewFile():
        with open(html_filename, 'w') as filehtml:
                # create local html to by uploaded to server
                html_code = "<h1>" + my_ip + "</h1>"
                html_code += "<p>" + st + "</p>"
                filehtml.write(html_code)
                filehtml.write("\n")

	# copy html file to server
        os.system("scp " + html_filename + " pzanon@oalbergue.com:~/zanon.ml/")

try:
        fileData = ""
        with open(html_filename, 'r') as filehtml:
		print 'File exists, read it...'
		fileData = filehtml.read()

	# check if ip address remains the same
	if len(fileData) > 0 and fileData.find(my_ip) == -1:
                print 'New IP address found, update file...'
                writeNewFile()
        else:
                print 'Invalid or same IP address found, do not update file...'
except:
        print 'File not found, create a new one and upload it...'
        writeNewFile()
