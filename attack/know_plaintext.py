from utils.utils import map_int2letter

def Know_plaintext(ciphered,plain):
	key = ''
	for i in range(len(plain)):
		diff = ord(ciphered[i])-ord(plain[i])
		diff = 26 + diff if diff < 0 else diff
		key += map_int2letter[diff%26]
	return key