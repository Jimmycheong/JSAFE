import os, random
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 

def jencrypt(key,text):
	IV = os.urandom(16)
	encryptor = AES.new(key,AES.MODE_CBC, IV)
	output = IV
	readable = 'blank'

	while len(readable) != 0: 
		readable = text[:16]
		text = text[16:]
		if len(readable) < 16: 
			readable = readable.zfill(16)
			cipher = encryptor.encrypt(readable)
#			print('output: ', output + cipher)
			return output + cipher
		cipher = encryptor.encrypt(readable)
		output += cipher

def dencrypt(password, text):
	hashedp = getKey(password.encode('utf-8'))
	IV,remaining = text[:16],text[16:]
	print ('remaining: ', remaining)
	print ('remaining: ' , type(remaining))
	decryptor = AES.new(hashedp, AES.MODE_CBC, IV)
	result, chunk = "", "blank"

	while len(chunk) != 0: 
		chunk = remaining[:16]
		remaining = remaining[16:]
		#chunk = chunk.decode('utf-8')
		#print (decryptor.decrypt(chunk)) 
		dez = decryptor.decrypt(chunk).decode('utf-8')
		if len(remaining) == 0 : 
			output = result + dez.lstrip('0') 
			print ('FINAL RESULT: ', output)
			return output		
		result += dez
	print ('Incorrect password: Try again!')

def getKey(password):
	hasher = SHA256.new()
	hasher.update(password)
	return hasher.digest()

#key = input('Enter password: ')
#text = input('Enter text: ')
#getKey(key.encode('utf-8'))
#hello = jencrypt(getKey(key.encode('utf-8')),text) 

#print ('Hello:', hello)
#print (type(hello)#)
#dencrypt(input('Enter password: '), hello) 
