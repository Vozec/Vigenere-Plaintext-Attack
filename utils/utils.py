import argparse
from utils.logger import logger

def parse_args():
	parser = argparse.ArgumentParser(add_help=True, description='This tool automates a plaintext attack on a vigenere cryptosystem')
	parser.add_argument("-p",dest="plaintext",type=str,required=False, help="Know Plaintext")
	parser.add_argument("-c",dest="cipher",type=str,required=True, help="Ciphered text")
	parser.add_argument("-f",dest="format",type=str,required=False, help="Format Flag")
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

map_letter2int = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,}
map_int2letter = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}


def Guess(plain,cipher):
	know = '\033[92m%s\033[0m'%plain
	for letter in cipher[len(plain):]:
		if(not letter in map_letter2int.keys()):
			know += '\033[92m%s\033[0m'%letter
		else:
			know += '\033[91mx\033[0m'
	logger('Know Plaintext :','info',1,0)
	print('\t\t%s'%know)