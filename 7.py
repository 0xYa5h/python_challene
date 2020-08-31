from PIL import Image

oxy = Image.open( "oxygen.png" )

length = 95
breadth = 629

y = 47
ans = ""
for x in range(0, 607, 7):
	a = oxy.getpixel((x,y))

	ans += str(chr(a[1]))

next_lvl = ans.split("is [")[1][:-1]
print(next_lvl)
for i in range(0,len(next_lvl),5):
	print(chr(int(next_lvl[i:i+3])),end="")
print("")