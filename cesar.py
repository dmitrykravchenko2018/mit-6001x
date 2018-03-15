#!/usr/bin/env python

"""
This function is intended for Cesar encoding/decoding
"""
import string

def cesar(text, shift):
	alphabet = string.ascii_lowercase
	shifted_alphabet = alphabet[shift:] + alphabet[:shift]
	table = str.maketrans(alphabet, shifted_alphabet)
	#print(type(table), table)
	return text.translate(table)

plaintext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq \
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr \
gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

plaintext = 'Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k \
wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. Ro rkc loox boqscdobon\
 pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. \
 Sd rkc loox dro dbknsdsyx yp dro bocsnoxdc yp Okcd Mkwzec dy lomywo \
 Tkmu Pvyboi pyb k pog xsqrdc okmr iokb dy onemkdo sxmywsxq cdenoxdc \
 sx dro gkic, wokxc, kxn odrsmc yp rkmusxq.'

print(cesar(plaintext, 16))
print(cesar("map", 2))
