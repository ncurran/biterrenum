#!/usr/bin/env python
import binascii
import sys

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
#
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)
#https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

before = sys.argv[1]
binary = text_to_bits(before)

i = 0
for char in text_to_bits(before):
    error = text_to_bits(before)
    error = [char for char in error]
    if error[i] == '0':
        error[i] = '1'
    if error[i] == '1':
        error[i] = '0'
    error = ''.join([char for char in error])
    #print( '%s'%(error) )
    error = text_from_bits(error)
    print('%s'%error)
    i+=1
