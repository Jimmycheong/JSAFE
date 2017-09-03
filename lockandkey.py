'''
The following script contains functions to encrypt, decrypt and generate byte hashs

By running this script, you can check if the passwords are correctly generated.

Open the terminal and type python lockandkey.py to run this script.

Ensure all dependancies at installed beforehand.

'''

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def jencrypt(key, text):
	'''
	This function encrypts a byte hash
	'''
	random_number = os.urandom(16)
	encryptor = AES.new(key, AES.MODE_CBC, random_number)
	output = random_number
	readable = 'blank'

	while len(readable) != 0:
		readable = text[:16].encode('utf-8')
		text = text[16:]
		if len(readable) < 16:
			readable = readable.zfill(16)
			cipher = encryptor.encrypt(readable)
			return output + cipher
		cipher = encryptor.encrypt(readable)
		output += cipher

def dencrypt(password, text):
	'''
	TODO: Complete this.
	'''
	hashedp = get_hashed_key(password.encode('utf-8'))
	random_number, remaining = text[:16], text[16:]
	decryptor = AES.new(hashedp, AES.MODE_CBC, random_number)
	result, chunk = "", "blank"

	try:
		while len(chunk) != 0:
			chunk = remaining[:16]
			remaining = remaining[16:]
			dez = decryptor.decrypt(chunk).decode('utf-8')
			if len(remaining) == 0:
				output = result + dez.lstrip('0')
				return output
			result += dez
	except ValueError:
		print('Incorrect password: Try again!')
		return "Password does not match. Confirmation unsuccessful."

def get_hashed_key(password):
	'''
	Generate Hash string

	Return:
		hash string
	'''
	hasher = SHA256.new()
	hasher.update(password)
	return hasher.digest()

#====#====##====#====##====#====##====#====#
#TEST CODE#
#====#====##====#====##====#====##====#====#

if __name__ == '__main__':

	USER_INPUT = input('Enter password: ')
	USER_TEXT = input('Enter text: ')
	get_hashed_key(USER_INPUT.encode('utf-8'))

	BYTE_ENCRYPTED_HASH = jencrypt(get_hashed_key(USER_INPUT.encode('utf-8')), USER_TEXT)
	print('BYTE_ENCRYPTED_HASH:', BYTE_ENCRYPTED_HASH)
	print("Of type: ", type(BYTE_ENCRYPTED_HASH))

	OUTPUT = dencrypt(input('Check password by retyping: '), BYTE_ENCRYPTED_HASH)
	print("Original filler: ", OUTPUT)
