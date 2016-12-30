import os, random
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 

def jencrypt(key,text):

	IV = os.urandom(16)
	print ('\nIV CREATED: ', IV, '\n')
	encryptor = AES.new(key,AES.MODE_CBC, IV)
	output = IV
	readable = 'blank'

	while len(readable) != 0: 
		readable = text[:16]
		#print ('readable: ',readable)
		text = text[16:]
		#print ('remaining: ', text)

#		if len(text) == 0: 
#			break
		if len(readable) < 16: 
			readable = readable.zfill(16)
			print ('TEXT ZFILLED: ', readable)
			cipher = encryptor.encrypt(readable)
			print ('last cipher:', cipher)
			print('output: ', output + cipher)

			return output + cipher
		cipher = encryptor.encrypt(readable)
		print ('just encrypted: ', readable)
		#print('Encrypted output: ', IV + cipher)
		output += cipher

#	print('output: ', output)
#	return output


def dencrypt(password, text):
	hashedp = getKey(password.encode('utf-8'))
	IV = text[:16]
	print ('\nIV FROM READ: ', IV,'\n' )
	decryptor = AES.new(hashedp, AES.MODE_CBC, IV)

	remaining = text[16:]
	result = ""
	print ('Initial:', remaining, '\n')
	chunk = 'blank'

	while len(chunk) != 0: 
		chunk = remaining[:16]
		print ('CHUNK:', chunk)
		remaining = remaining[16:]
		print ('Re: ', remaining)

		dec = decryptor.decrypt(chunk)
		print ('DEC IS', dec)

		dez = dec.decode('utf-8')
		if len(remaining) == 0 : 
			print ('Striped chunked:', chunk)
			dez = dez.lstrip('0')
			print ('Result:', dez)
			print ('FINAL RESULT: ', result + dez)
			return result + dez			
		result += dez
		print ('\n')

def getKey(password):
	hasher = SHA256.new()
	hasher.update(password)
	return hasher.digest()

key = input('Enter password: ')
text = input('Enter text: ')
getKey(key.encode('utf-8'))
hello = jencrypt(getKey(key.encode('utf-8')),text) 

dencrypt(input('Enter password: '), hello) 