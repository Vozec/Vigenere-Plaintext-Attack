import argparse
from datetime import datetime

## LOGGER CLASS
class bcolors:
    WHITE = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
all_context = {
    'progress':bcolors.HEADER,
    'white':bcolors.WHITE,
    'info':bcolors.WARNING,
    'flag':bcolors.OKGREEN,
    'log':bcolors.OKBLUE,
    'error':bcolors.FAIL,
    'warning':bcolors.OKCYAN,
    None:''}
def logger(message,context=None,newline=0,tab=0,quiet=False):
	if(quiet):
		print(message)
	else:
	    final = ""
	    final += '\n'*newline
	    now = datetime.now()
	    final += now.strftime("%H:%M:%S")
	    final += " | "
	    final += all_context[context]
	    final += '\t'*tab
	    final += ' '
	    final += message
	    final += bcolors.ENDC
	    print(final)


## UTILS
def parse_args():
	parser = argparse.ArgumentParser(add_help=True, description='This tool automates a plaintext attack on a vigenere cryptosystem')
	parser.add_argument("-p",dest="plaintext",type=str,required=True, help="Know Plaintext")
	parser.add_argument("-c",dest="cipher",type=str,required=True, help="Ciphered text")
	parser.add_argument("-q",dest="quiet",action="store_true",required=False,default=False, help="Quiet mode")
	return parser.parse_args()

def header():
	logger(r"""
  _   ___      ___  __     _    ______        __ 
 | | / (_)__ _/ _ \/ /__ _(_)__/_  __/____ __/ /_
 | |/ / / _ `/ ___/ / _ `/ / _ \/ / / -_) \ / __/
 |___/_/\_, /_/  /_/\_,_/_/_//_/_/  \__/_\_\\__/ 
       /___/                                     

""",'log',0,0)

## MAIN
mapping = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def attack(ciphered,plain):
	key = ''
	for i in range(len(plain)):
		diff = ord(ciphered[i])-ord(plain[i])
		diff = 26 + diff if diff < 0 else diff
		key += mapping[diff]
	return key

def main(args):
	if(not args.quiet):
		header()

	quiet	 = args.quiet
	plain    = ''.join([l for l in args.plaintext if l in 'abcdefghijklmnopqrstuvwxyz'])
	ciphered = ''.join([l for l in args.cipher    if l in 'abcdefghijklmnopqrstuvwxyz'])

	if(len(plain)>len(ciphered)):
		logger('The known plain-text is greater than the cipher-text','error',0,0,quiet)
		return -1

	key = attack(ciphered[:len(plain)],plain)
	
	logger('The key start probably by "%s"'%key,'flag',0,0,quiet)

if __name__ == '__main__': 
	main(parse_args())