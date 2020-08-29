import pickle

file = open("banner.p")
image1 = pickle.load(file)
for i in image1:
    for k in i:
        print k[0] * k[1],
    print "" 