from bitcoin.rpc import RawProxy
# from bitcoin.core import x

p = RawProxy()
SAT = 100000000

# NOTE: palieku sita cia, nes naudosiu 4 uzd, bet cia susimaisiau ir galvojau, kad reikia bloko hasha imest ir todel norejau castint ji i kita endian blahblah kazkas ten tokio. blogai supratau, bet db supratntu, kad pravers 4 uzd, tai palieku su komentarais lol
# cia error cehckinimas pointless nes nenaudoju tos funkcijos castint lol

#read https://github.com/petertodd/python-bitcoinlib?tab=readme-ov-file#endianness-gotchas
# removed - input -> casts to little endian
# note: input turi but hashas (ne nes isemiau ta x bet palieku 4 uzd), kitaip throwina err
while True:
    try:
        hashInput = input("Input the transaction hash: ")
        break
    except Exception as e:
        print(f"Input must be a hash: {e}")

raw_tx = p.getrawtransaction(hashInput)
decoded_tx = p.decoderawtransaction(raw_tx)

in_sum = 0
out_sum = 0

for input in decoded_tx['vin']:
#    in_sum+=input['value']
    invout = input['vout']
    #print(invout)
    in_raw_tx = p.getrawtransaction(input['txid'])
    in_decoded_tx = p.decoderawtransaction(in_raw_tx)
    #print(in_decoded_tx['vout'][invout])
    in_sum+= in_decoded_tx['vout'][invout]['value'] * SAT
    #print("\n\n\n\n\n\n\n\n")
    #for invout in in_decoded_tx['vout']:
    #    in_sum+=invout['value']

for output in decoded_tx['vout']:
    out_sum+=output['value'] * SAT

#print(in_sum)
#print(out_sum)

print(f"fee: {int(in_sum - out_sum)}")
