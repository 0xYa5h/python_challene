from urllib import *
import re

site = urlopen( "http://www.pythonchallenge.com/pc/def/ocr.html" )
source_code = site.read()
site.close()


mess = re.split("-->", source_code, 1)[1]
mess = mess[7:mess.index("-->")]

charcters = {}
a = ""

for char in mess:
	if char in charcters:
		charcters[char] = charcters[char] + 1

	else:
		charcters[char] = 1
		a += char

print a
