# blockchain 3 pratybu uzduoties 3 uzduotis
(uzduotys darytos ssh'inus i universiteto blockchain node aplinka su vim editorium)

(refleksijos nes nzn ka rasyt cia)
## Apskaičiuokite transakcijos mokestį: Parašykite programą, kuri apskaičiuoja Bitcoin transakcijos mokestį pagal jos hash'ą. 
Sita uzduotis nebuvo tokia sunki, pagrinde pradzioje blogai supratau, kad reikia ivest bloka ir todel tam dariau ivesti, kurioje butu convertinama tarp LE ir BE (vis dar nnz kodel tai dariau, kazkodel galvojau, kad tai padetu)).
nepadejo.

pagrindinis is tikruju issukiu buvo supratimas kaip reikia suskaiciuot kiek kainavo, tai siuo atveju tsg ivesties suma - isvesties suma = fee suma.

also buvo sunku suprast kaip normaliai gaut ivesties suma is UTXO. tai bsk keista, bet proceso tldr: kiekvienam elementui esanciam bloko vin yra nurodytas praeito utxo vout, tada surandi to vin utxo txid, ji decodini ir is jo voutu pasiemi
tik ta, kuri gavai pries tai ir tada paemi jo value ir padaugini is BTC -> SAT ratio, nes ju kaina zymima SAT `in_sum+= in_decoded_tx['vout'][invout]['value'] * SAT`. bsk keista bet aj

o outputus suskaiciuot daug lengviau buvo ir labai panasiai buvo daryta pavyzdyje

fotkyte
https://www.blockchain.com/explorer/transactions/btc/4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d
<img width="962" height="75" alt="image" src="https://github.com/user-attachments/assets/2133ccf9-f3a4-496c-aade-c2acd77e4601" />


## Patikrinkite bloko hash'ą: Parašykite programą, kuri patikrina, ar bloko hash'as yra teisingai apskaičiuotas pagal bloko header'io informaciją.

sitos uzduoties sunkumas buvo little endianness ir big endianness. duotame pavyzdyje visi inputai buvo LE, taciau `p.getblock()` grazina BE values. o pvz yra inputtinti LE kaip hex stringai. beieskant sprendimu python-bitcoinlib radau x() ir lx()
funkcijas skirtas butent tokiam castinimui, bet jie veikia tik stringam. todel su skaiciais buvo sunkiau. ilgai ieskojau normaliu sprendimu internete (palikau tleb() funkcija is stackoverflow), bet neradau normalaus sprendimo.
speju problema buvo tame, kad mano inputas yra neapibrezto ilgio int'as ir outputas buna neapibrezto ilgio, e.g. hexlify tikisi 0x01, bet siti castina i tsg 0x1 ir todel susimaiso viskas blahblah.
zdz galiausiai chatgpt pasiule paprasta sprendima kaip castint

be to,nzn ar teisingai supratau uzduoti - ar reikejo tsg patikrint ar blockchaine suskaicioutas, ar zmogus turetu ivest sita info pats? anyways, gan lengvai galima keisti, kad butu ir kitaip, nes under the hood pagrindine logika yra lengvai reusable funkcijoje.

fotkyte
<img width="858" height="102" alt="image" src="https://github.com/user-attachments/assets/214bae25-7355-4eee-9079-fd9822a3f99d" />

https://www.blockchain.com/explorer/blocks/btc/593468
