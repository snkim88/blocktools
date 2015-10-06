from blocktools.types import *
from hashlib import sha256

class BlockHeader:
    def __init__(self, blockchain):
        self.version = uint4(blockchain)
        self.previousHash = hash32(blockchain)
        self.merkleHash = hash32(blockchain)
        self.time = uint4(blockchain)
        self.bits = uint4(blockchain)
        self.nonce = uint4(blockchain)
        
    def __unicode__(self):
        return """Version:\t %d
Previous Hash\t %s
Merkle Root\t %s
Time\t\t %s
Difficulty\t %8x
Nonce\t\t %s""" % (
                    self.version, hashStr(self.previousHash), hashStr(self.merkleHash),
                    str(self.time), self.bits, self.nonce
                )
                
    def __str__(self):
        return self.__unicode__().encode('utf-8')
        
    def hash(self):
        header_bin = pack_uint4(self.version) + \
            pack_hash32(self.previousHash) + \
            pack_hash32(self.merkleHash) + \
            pack_uint4(self.time) + \
            pack_uint4(self.bits) + \
            pack_uint4(self.nonce)
        
        return sha256(sha256(header_bin).digest()).digest()[::-1].encode('hex')

class Block:
    def __init__(self, blockchain):
        self.magicNum = uint4(blockchain)
        self.blocksize = uint4(blockchain)
        self.setHeader(blockchain)
        self.txCount = varint(blockchain)
        self.Txs = []

        for i in range(0, self.txCount):
            tx = Tx(blockchain)
            self.Txs.append(tx)

    def setHeader(self, blockchain):
        self.blockHeader = BlockHeader(blockchain)
        
    def __unicode__(self):
            return """Magic No: \t%8x
Blocksize: \t%d
########## Block Header ##########
%s
##### Tx Count: %d
%s
"""         % (
                self.magicNum, self.blocksize, str(self.blockHeader), self.txCount,
                '\n'.join([str(tx) for tx in self.Txs])
            )
            
    def __str__(self):
        return self.__unicode__().encode('utf-8')

class Tx:
    def __init__(self, blockchain):
        self.version = uint4(blockchain)
        self.inCount = varint(blockchain)
        self.inputs = []
        for i in range(0, self.inCount):
            input = txInput(blockchain)
            self.inputs.append(input)
        self.outCount = varint(blockchain)
        self.outputs = []
        if self.outCount > 0:
            for i in range(0, self.outCount):
                output = txOutput(blockchain)
                self.outputs.append(output)    
        self.lockTime = uint4(blockchain)
        
    def __unicode__(self):
        return """========== New Transaction ==========
Tx Version: \t%d
Inputs: \t%d
%s
Outputs: \t%d
%s
Lock Time: \t%d
"""     % (
            self.version,
            self.inCount, '\n'.join([str(i) for i in self.inputs]),
            self.outCount, '\n'.join([str(o) for o in self.outputs]),
            self.lockTime
        )
            
    def __str__(self):
        return self.__unicode__().encode('utf-8')
                

class txInput:
    def __init__(self, blockchain):
        self.prevhash = hash32(blockchain)
        self.txOutId = uint4(blockchain)
        self.scriptLen = varint(blockchain)
        self.scriptSig = blockchain.read(self.scriptLen)
        self.seqNo = uint4(blockchain)
        
    def __unicode__(self):
        return """< Previous Hash: \t%s
< Tx Out Index: \t%8x
< Script Length: \t%d
< Script Sig: \t\t%s
< Sequence: \t\t%8x
"""     % (
            hashStr(self.prevhash),
            self.txOutId,
            self.scriptLen,
            hashStr(self.scriptSig),
            self.seqNo
        )
            
    def __str__(self):
        return self.__unicode__().encode('utf-8')
        
class txOutput:
    def __init__(self, blockchain):    
        self.value = uint8(blockchain)
        self.scriptLen = varint(blockchain)
        self.pubkey = blockchain.read(self.scriptLen)
        
    def __unicode__(self):
        return """> Value: \t%d
> Script Len: \t%d
> Pubkey: \t%s
"""     % (
            self.value,
            self.scriptLen,
            hashStr(self.pubkey)
        )
            
    def __str__(self):
        return self.__unicode__().encode('utf-8')
