import os, random
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 

text = 'My name is Jimmy'

key = 'firstkey'
fkey = '00112233445566778899aabbccddeeff'

def jencrypt(key,text):

	IV = os.urandom(16)
	print ('IV looks like this: ', IV ,'\n')

	encryptor = AES.new(key,AES.MODE_CBC, IV)
	cipher = encryptor.encrypt(text)
	print("Cipher: ", cipher , '\n')

	output = IV + cipher
	print ('OUTPUT: ', output , '\n')
	return  output

def dencrypt(pasy, text):

	print ('pasy: ', pasy)
	hashedp = getKey(pasy.encode('utf-8'))
	print ('hashedp: ', hashedp)

	print('FIRST 11 removed',text[16:], '\n')
	IV = text[:16]
	btext = text[16:]

	decryptor = AES.new(hashedp, AES.MODE_CBC, IV)
	decipher = decryptor.decrypt(btext)
	print ('decipher: ', decipher)
	return decipher


def getKey(password):
	hasher = SHA256.new()
	#print (hasher.digest())
	return hasher.digest()


#getKey(key.encode('utf-8'))

hello = jencrypt(getKey(key.encode('utf-8')),text) 

dencrypt(input('Enter password: '), hello) 