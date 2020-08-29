encoded_txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alpha = "abcdefghijklmnopqrstuvwxyz"
decode_txt = ""
for char in encoded_txt:
    for i in range(0,24):
        if char == alpha[i]:
            decode_txt += alpha[i+2]
            break  
        elif char == "y":
            decode_txt += "a"
            break
        elif char == "z":
            decode_txt += "b"
            break
        elif char == " ":
            decode_txt += " "
            break
        elif char == ".":
            decode_txt += "."
            break
        elif char == "(":
            decode_txt += "("
            break
        elif char == ")":
            decode_txt += ")"
            break
print(decode_txt) 
            

