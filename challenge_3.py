from urllib import *
import re

site = urlopen( "http://www.pythonchallenge.com/pc/def/equality.html")
source_code = site.read()
site.close()

body = re.split("<!--",source_code,1)[1][1:]
body = body[:body.index("-->")]

small = ""

for c in range(1,len(body)-6):
	if (body[c-1].islower()) and (body[c].isupper()) and (body[c+1].isupper()) and (body[c+2].isupper()) and (body[c+3].islower()) and (body[c+4].isupper()) and (body[c+5].isupper()) and body[c+6].isupper() and (body[c+7].islower()):
		small += body[c+3] 
		
print small