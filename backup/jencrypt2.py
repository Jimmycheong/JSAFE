import os, random
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 

def jencrypt(key,text):

	IV = os.urandom(16)
	encryptor = AES.new(key,AES.MODE_CBC, IV)
	output = IV

	while text: 
		readable = text[:16]
		print ('readable: ',readable)
		text = text[16:]
		print ('remaining: ', text)

		if len(text) == 0: 
			break

		if len(text) < 16: 
			text = text.zfill(16)
		cipher = encryptor.encrypt(readable)
		print ('just encrypted: ', readable)
		print('Encrypted output: ', IV + cipher)
		output += cipher

	print('output: ', output)
	return output


def dencrypt(password, text):
	hashedp = getKey(password.encode('utf-8'))
	IV = text[:16]
	print ('IV')
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

key = input('Enter password: ')
text = input('Enter text: ')
getKey(key.encode('utf-8'))
hello = jencrypt(getKey(key.encode('utf-8')),text) 

dencrypt(input('Enter password: '), hello) 