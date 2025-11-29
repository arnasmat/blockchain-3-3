# blockchain 3 pratybu uzduoties 3 uzduotis (ir 1 uzduoties bandymo rasyt aprasymas)

## 1 uzd
(rasau antra karta, nes bandant atkurt ir runnint install scriptus ir nuo ju crashino kompas :^).. )
Kaip su viskuo, visu pirma bandziau patikrint ar libbitcoin yra AUR - buvo!.. bet neatnaujintas nuo 2019 metu.

Vis tiek bandziau instaliuot: `yay -S libbitcoin` - ismete, kad daugumos dependencies (skirtingu libbitcoino libu) isvis nerado.

Todel bandziau instaliuot tik system `yay -S libbitcoin-system` - ilgai bande cleanbuildint, bet galiausiai ismete errora
<img width="1917" height="1141" alt="image" src="https://github.com/user-attachments/assets/d499e12e-cbcf-4b35-9a01-5b76809d512f" />

Tada bandziau installint su ju paciu [install scriptu](https://github.com/libbitcoin/libbitcoin-system?tab=readme-ov-file#debianubuntu) - jis ilgai runnino, bet galiausiai ismete 
<img width="592" height="337" alt="image" src="https://github.com/user-attachments/assets/ecf2213f-c4fb-4df8-840f-e08f30e25ab0" /> - o pateiktoje dir tarp include/ buvo tik boost, nebuvo bitcoin

Bandziau pagal ju paciu instrukcijas [projekta buildint su autotools](https://github.com/libbitcoin/libbitcoin-system?tab=readme-ov-file#autotools-advanced-users), dabar nerasiu fotkiu, bet klaidos, kurias pamenu su jais (ne chronologine tvarka):
- Boosto bloga versija -> bandziau downgradint ji ir boost-libs i daug skirtingu versiju (tarp ju ir ju siuloma, kuria buildina su install scriptu) `sudo downgrade boost boost-libs` - vis tiek neveike, nes buvo klaida su naujesne boost-locale versija, kurios negalejau keist, nes ant jos relyino kitos programos. Tarp kitko, del sito po to neveike tam tikros kitos programos, pvz libreoffice lol.
- Kazkas su libsecp256k1 -> buildinau [ju paciu fork'a](https://github.com/libbitcoin/secp256k1) -> vis tiek mete daug klaidu lol
- Daugelis kitu mazu bedu, kuriu dabar nebepamenu, bet pamenu su sitom dviem labiausiai knisaus.

Va daugelis direktorju, i kurias visas bandziau ten siust dalykus, kai kurios jau pratrintos lol. (p.s. necenzurine kalba, nes tuo metu taip jauciausi del kylanciu problemu)
<img width="900" height="295" alt="image" src="https://github.com/user-attachments/assets/56c821e3-d96c-4353-b898-3a703e5b5148" />

Nezinau, kuris is siu etapu cia padejo ar sita padare, bet galiausiai pastebejau, kad visgi kazkas instaliavosi - egzistuoja /usr/local/include/bitcoin
<img width="456" height="90" alt="image" src="https://github.com/user-attachments/assets/86d084f0-38af-41a0-84d0-6dc6457d6320" />

Taciau vis tiek bandant kompiliuoti pateikta koda buvo klaidu:
- `clang++ -std=c++11 -o merkle merkle.cpp $(pkg-config --cflags --libs libbitcoin)` isvis nedetectino, reikejo i terminala ivest/prie .basrhc pridet `export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH`
- tada mete klaida, kad libbitcoin nerasta -> reikejo pakeist i `--libs libbitcoin-system`
- `include <bitcoin/bitcoin.hpp>` not found -> reikejo pakeist i `bitcoin/system.hpp`
- (Dar kazkur cia mete klaidas su libsecp tai bandziau viena is versiju exportint is 
- Kompiliuojant su clang++ mete klaidas, kad kazkas wrong su boost'u
- Kompiliuojant su g++ mete:
```
arnas  ~/libbletcoin  g++ -std=c++11 -o merkle merkle.cpp $(pkg-config --cflags --libs libbitcoin-system)
/usr/bin/ld: /usr/local/lib/libsecp256k1.a(libsecp256k1_la-secp256k1.o): in function `secp256k1_num_mod_inverse':
/home/arnas/libbit/secp256k1/src/num_gmp_impl.h:128:(.text+0x50de): undefined reference to `__gmpn_gcdext'
/usr/bin/ld: /usr/local/lib/libsecp256k1.a(libsecp256k1_la-secp256k1.o): in function `__gmpn_sub':
/usr/include/gmp.h:2204:(.text+0x515d): undefined reference to `__gmpn_sub_n'
/usr/bin/ld: /usr/local/lib/libsecp256k1.a(libsecp256k1_la-secp256k1.o): in function `secp256k1_num_get_bin':
/home/arnas/libbit/secp256k1/src/num_gmp_impl.h:34:(.text+0x537b): undefined reference to `__gmpn_get_str'
/usr/bin/ld: /usr/local/lib/libsecp256k1.a(libsecp256k1_la-secp256k1.o): in function `secp256k1_num_set_bin':
/home/arnas/libbit/secp256k1/src/num_gmp_impl.h:49:(.text+0xc24b): undefined reference to `__gmpn_set_str'
/usr/bin/ld: /home/arnas/libbit/secp256k1/src/num_gmp_impl.h:49:(.text+0xc371): undefined reference to `__gmpn_set_str'
/usr/bin/ld: /home/arnas/libbit/secp256k1/src/num_gmp_impl.h:49:(.text+0xcf45): undefined reference to `__gmpn_set_str'
/usr/bin/ld: /home/arnas/libbit/secp256k1/src/num_gmp_impl.h:49:(.text+0xcf89): undefined reference to `__gmpn_set_str'
collect2: error: ld returned 1 exit status
```
PASTEBIME, kad cia kai kur libsecp256k1 versija yra is /usr/local/lib/..., o kitur is /home/arnas/libbit - viena is vietu, kur bandziau pats builint ju fork'a libseco. Bet bandant deletint libsecp256k1 is `sudo pacman -R libsecp256k1` ir bandant kompiliuot ismete, kad libsec nerasta. dar ten kazkaip bandziau knistis su libsecu, bet uzkniso.

note: gali but, kad parasyta ne taip kaip chronologiskai dariau, nes bandziau pries 2 sav ir mano skundai del sito yra isskirstyti tarp daug zinuciu su daug skirtingu draugu lol.

## 3 uzd
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
