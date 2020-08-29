from urllib import urlopen

site = urlopen(" http://www.pythonchallenge.com/pc/def/linkedlist.php ")
source_code = site.read()
site.close()

new = source_code.split("linkedlist.php?nothing=")[1].split('"><img')[0]

new = str(16044/2)   #this step is after "Yes. Divide by two and keep going."

while new[0].isdigit():
    s = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + new
    site = urlopen( s )
    source_code = site.read()
    site.close()

    new = source_code.split("and the next nothing is ")[1]

    print new

