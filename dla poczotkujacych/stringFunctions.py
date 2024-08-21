line='this IS a very STRANGE text'
print(line.capitalize())
print(line.casefold)
print(line.lower())
print(line.upper())
print(line.title())
print(line.swapcase())
print(line.find('e'))
print(line.rfind('e'))
print(line.startswith('this'))
print(line.endswith('TEXT'))

import string

print(string.digits)
list=line.split(' ')
print(list)
listText='\n'.join(list)
print(listText)


poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

list=poem.split('\n')
for i in range(8):
    print(list[i])
    print(list[i+8])
    