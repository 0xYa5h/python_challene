import zipfile

zzip = zipfile.ZipFile("channel.zip", 'r')
fil = zzip.open("90052.txt","r")
next_nothing = fil.read()
n1 = next_nothing.split("is ")[1]
p =""
while n1[0].isdigit():

	n2 = n1 + ".txt"
	file1 = zzip.open(n2,"r")
	n1 = file1.read()
	
	n1 = n1.split("is ")[1]
	p += zzip.getinfo(n1 +".txt").comment
	print(p)
	

    
