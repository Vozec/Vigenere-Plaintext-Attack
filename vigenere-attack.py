from utils.logger import logger
from utils.utils  import parse_args,header,map_int2letter,map_letter2int,Guess

from attack.know_plaintext import Know_plaintext
from attack.key 	 	   import Guess_Key_Lenght

def vigenere(message,cle,decode=False):
	text , index  = "" , 0
	for i in range(len(message)):
		letter = message[i]
		if(letter in 'abcdefghijklmnopqrstuvwxyz'):
			key   = cle[index % len(cle)]
			text += map_int2letter[(map_letter2int[letter]-map_letter2int[key])%26]
			index += 1
		else:
			text += letter
	return text



def main(args):
	header()

	key  	 = None
	ciphered = ''.join([l for l in args.cipher.lower() if l in 'abcdefghijklmnopqrstuvwxyz'])

	# Detect Key Lenght
	key_lenght = Guess_Key_Lenght(ciphered)
	if(key_lenght != -1):
		logger('The key seems to be %s chars'%key_lenght,'log',0,0)
	else:
		logger('Unable to detect the key lenght ...','log',0,0)

	Guess(args.plaintext.lower(),args.cipher.lower())

	# Plaintext attack
	if(args.plaintext):
		plain	= ''.join([l for l in args.plaintext if l in 'abcdefghijklmnopqrstuvwxyz'])
		logger('Trying Know Plaintext attack... ','info',1,0)
		if(len(plain)>len(ciphered)):
			logger('The known plain-text is greater than the cipher-text','error',0,0)
			return -1
		else:
			key = Know_plaintext(ciphered[:len(plain)],plain)
			logger('The key start probably by "%s"'%key,'flag',1,0)

	if(key):
		decoded = vigenere(args.cipher.lower(),key,True)
		logger('The clear text is then :','info',1,0)
		logger(decoded,'flag',0,1)

		# Guess the end of the key with google
		# + Bruteforce

if __name__ == '__main__': 
	main(parse_args())