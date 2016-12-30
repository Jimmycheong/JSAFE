import os, random
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 

def jencrypt(key,text):

	chunksize = 16*1024
	IV = os.urandom(16)
	encryptor = AES.new(key,AES.MODE_CBC, IV)
#	print ('text: ', text )

	text =  (text.zfill(16))

#12345678901234678

#	while True:
#		read
	#	if len(chunk) == 0 : 
	#		break 
	#	
	#	elif len(chunk) % 16 != 0:
	#		chunk += ' ' * (16 - (len(chunk) %16))

	cipher = encryptor.encrypt(text)
	print('Encrypted output: ', IV + cipher)
	return  IV + cipher

def dencrypt(password, text):
	hashedp = getKey(password.encode('utf-8'))
	IV = text[:16]
	btext = text[16:]
	decryptor = AES.new(hashedp, AES.MODE_CBC, IV)
	dez = decryptor.decrypt(btext)
	print ('dez: ', dez)
	print ('Dechipered: ', dez.decode('utf-8').lstrip('0'))
	return decryptor.decrypt(btext)

def getKey(password):
	hasher = SHA256.new()
	hasher.update(password)
	return hasher.digest()

key = input('Enter password')
text = input('Enter text')
getKey(key.encode('utf-8'))
hello = jencrypt(getKey(key.encode('utf-8')),text) 

dencrypt(input('Enter password: '), hello) 