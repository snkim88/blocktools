#!/usr/bin/python
import sys
from blocktools import Block, BlockHeader

def parse(blockchain):
    print('Parsing Block Chain')
    continueParsing = True
    counter = 0
    blockchain.seek(0, 2)
    fSize = blockchain.tell() - 80 #Minus last Block header size for partial file
    blockchain.seek(0, 0)
    
    while continueParsing:
        print(counter)
        try:
            block = Block(blockchain)
            continueParsing = block.continueParsing
            if continueParsing:
                print((str(block)))
        except Exception as ex:
            print(('Error:', ex))
            break
            
        counter+=1

def main():
    if len(sys.argv) < 2:
            print('Usage: sight.py filename')
    else:
        with open(sys.argv[1], 'rb') as blockchain:
            parse(blockchain)



if __name__ == '__main__':
    main()
