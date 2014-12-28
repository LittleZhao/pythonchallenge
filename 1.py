#http://www.pythonchallenge.com/pc/def/map.html
#solutions http://www.pythonchallenge.com/pcc/def/ocr.html
import string
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = []
map = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print s.translate(map)
'''
for i in s:
    if ord(i) in range(97, 123):
        print chr((ord(i) + 2 - 97) % 26 + 97),
    else:
        print i,
'''
