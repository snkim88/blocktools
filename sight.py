#!/usr/bin/python
import sys
from blocktools import *
from block import Block, BlockHeader

def parse(blockchain):
    print 'Parsing Block Chain'
    counter = 0
    while True:
        print counter
        try:
            block = Block(blockchain)
            print str(block)
        except Exception as ex:
            print 'Error:', ex
            break
            
        counter+=1

def main():
    if len(sys.argv) < 2:
            print 'Usage: sight.py filename'
    else:
        with open(sys.argv[1], 'rb') as blockchain:
            parse(blockchain)



if __name__ == '__main__':
    main()
