countries=['FR','US','DE','RU']

print(countries[0])
countries.append('PL')#append dodaje komórke na koncu lisy
countries.insert(2,'ES')#insert wstawian komorek na okreslona pozycje listy
countries.remove('RU')#remove usunie pierwsza komorek o podanej wartosci
countries.sort()# sortuj liste rosnaco
countries.reverse()#oboroc kolejnosc listy
print(countries.pop(2))#pop zwroci element listy i usunie go z niej
print(countries.index("PL"))#index zwróci pozycje komórki o zadanje wartosci 
print(countries.count('DE'))#zwraca ilosc wystopien poszukiwanego  elemntu
newList=['FI','SE']
countries.extend(newList)#extand dodaje na koniec listy zawartosc innej listy

#countriesCopy=countries takie kopiowanie tworzy dowiazanie do listy (wskazuje na to samo miejsce w pamiecie wiec jest referncja a nie kopia)
#countriesCopy.clear() clear czysci dana list

countriesCopy=countries.copy()#copy tworzy nowa tablice z tymi samymi wartosciami co podana lista ( kopia a nie referncja)
countriesCopy.clear()

print(countriesCopy)
print(countries)

hitTitles=['BROTHERS IN ARMS','BOHEMIAN RAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STROM','WISH YOU WERE HERE']
hitTitles.append('CHILD IN TIME')
hitTitles.append('AGAIN')
hitTitles.insert(2,'HOTEL CALIFORNIA')
hitTitles.insert(0,'THE SOUND OF SILENCE')
print(hitTitles.index('HOTEL CALIFORNIA'))
hitTitles.remove('HOTEL CALIFORNIA')
hitTitles[0]='ENJOY THE SILENCE'
print(len(hitTitles))
hitsToRead=hitTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
additionalSongs=['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead.count('WISH YOU WERE HERE'),hitsToRead.count('RIDERS ON THE STROM'))
hitsToRead.clear()



