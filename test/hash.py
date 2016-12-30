import os, random
from Crypto.Hash import SHA256 

key = input('Enter a string: ')

def getKey(password):
	hasher = SHA256.new()
	hasher.update(password)
	h = hasher.digest()
	print (h)
	return h 

getKey(key.encode('utf-8'))
