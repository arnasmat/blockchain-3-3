from bitcoin.rpc import RawProxy
from binascii import unhexlify, hexlify
from bitcoin.core import lx
from hashlib import sha256
#from binascii import unhexlify, hexlify

p = RawProxy()
SAT = 100000000

# NOTE: palieku sita cia, nes naudosiu 4 uzd, bet cia susimaisiau ir galvojau, kad reikia bloko hasha imest ir todel norejau castint ji i kita endian blahblah kazkas ten tokio. blogai supratau, bet db supratntu, kad pravers 4 uzd, tai palieku su komentarais lol
# cia error cehckinimas pointless nes nenaudoju tos funkcijos castint lol

#read https://github.com/petertodd/python-bitcoinlib?tab=readme-ov-file#endianness-gotchas
# removed - input -> casts to little endian
# note: input turi but hashas (ne nes isemiau ta x bet palieku 4 uzd), kitaip throwina err
while True:
    try:
        hashInput = input("Input block hash: ")
        break
    except Exception as e:
        print(f"Input must be a hash: {e}")

block = p.getblock(hashInput)

version = int(block['version']).
hashPrevBlock = block['previousblockhash']
hashMerkleRoot = block['merkleroot']
time = int(block['time'])
bits = int(block['bits'])
nonce = int(block['nonce'])

header = version + hashPrevBlock + hashMerkleRoot + time + bits + nonce
# header_hex = ("01000000" + "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" + "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" + "c7f5d74d" + "f2b9441a" + "42a14695")
header_bin = lx(header)
hash1 = sha256(header_bin).digest()
hash2 = sha256(hash1).digest()
print(hexlify(hash2[::-1]).decode("utf-8"))
# print(x(hash2))

print(version)
print(hashPrevBlock)
print(hashMerkleRoot)
print(time)
print(bits)
print(nonce)
