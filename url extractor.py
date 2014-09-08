import re
import urllib
from pprint import pprint
import json

firstpic ='https://www.flickr.com/photos/126226072@N03/14811500040/in/set-72157646731999905'
#---------- Open file ----------
opened = urllib.urlopen(firstpic)
code = opened.read()
f = open('urls.txt','w')
# f.write(code)

#---------- Open file ----------

picurl = r'(Y\.photo\.init\()(.+)\);'
matched = re.search(picurl,code)
if matched:
  converted = matched.group(2)
  data=json.loads(converted)
  data=data[u'sizes'][u'o'][u'url']
  # location = print data
  f.write(data)
else:
	print 'not found'
f.close()
