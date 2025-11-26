from bitcoin.rpc import RawProxy
from binascii import unhexlify, hexlify
from bitcoin.core import lx
from hashlib import sha256
#from binascii import unhexlify, hexlify

# man rodos sito nenaudoju, nes neveike lmao
# to little endian bytes
def tleb(input):
    # https://stackoverflow.com/a/53576675
    return bytearray.fromhex(hex(input)[2:])[::-1]
p = RawProxy()
SAT = 100000000

def little_endian_header_info_to_block_hash(version, hashPrevBlock, hashMerkleRoot, time, bits, nonce):
    header = version + hashPrevBlock + hashMerkleRoot + time + bits + nonce
    hash1 = sha256(header).digest()
    hash2 = sha256(hash1).digest()
    return hexlify(hash2[::-1]).decode("utf-8")

# planvau naudot bet once again realiai nereikejo lol. palieku vstk, nes aj tingiu
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

# cia zr sketchy sprendimas. neradau normalaus clean budo castint skaiciu i little endian bytes. python-bitcoinlib docsuose radau lx(), bet jis tik string -> little endian bytes
# o pvz su skaiciais neradau normaliai kaip, tai busiu honest int'u castinimo buda pasiule AI, nes stackoverflow results buvo keisti ir realiai tik sitas veike
version = block['version'].to_bytes(4, byteorder='little')
hashPrevBlock = lx(block['previousblockhash'])
hashMerkleRoot = lx(block['merkleroot'])
time = block['time'].to_bytes(4, byteorder='little')
bits = int(block['bits'], 16).to_bytes(4, byteorder='little')
nonce = block['nonce'].to_bytes(4, byteorder='little')

cHash = little_endian_header_info_to_block_hash(version, hashPrevBlock, hashMerkleRoot, time, bits, nonce)
print(cHash)

if cHash == hashInput:
    print("wahoo hash is correct all is well")
else:
    print("how did this happen lol, was the blockchain wrong?")

# print(x(hash2))

#print(version)
#print(hashPrevBlock)
#print(hashMerkleRoot)
#print(time)
#print(bits)
#print(nonce)

