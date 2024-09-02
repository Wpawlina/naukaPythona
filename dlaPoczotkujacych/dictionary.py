CountryLeaders={'PL':'Duda','US':'Trump'}
print(CountryLeaders['US'])
CountryLeaders['DE']='Merkel'
print(CountryLeaders.keys())
print(CountryLeaders.items())
print(CountryLeaders.values())

print(CountryLeaders.popitem())#popitem zwraca klucz i wartosc i usuwa ostatni item z dictionary
print(CountryLeaders.pop('PL'))
CountryLeaders['DE']='Merkel'
print(CountryLeaders.setdefault('FR','Macron'))#setdefault odzczytuje wartosc komorki o podanym kluczu jesli dany klucz nie istniej to wyswietla wartosc domyslana (2 parametr) i dodaje taka komorke z domyslna wartoscia do dictionary
print(CountryLeaders.get('US'))
print(CountryLeaders.get('RU'))
print(CountryLeaders)
NewLiders={'RU':'Putin','DE':'Shulz'}
print(NewLiders)
CountryLeaders.update(NewLiders)# update dodaje lub zmienia slownik na wartosci z innego slownika
print(CountryLeaders)

chanels={'Google':1480,'Email':300,'Natural Traffic':440,'Tv Spot':700}
print(chanels['Email'])
chanelsUpdate={'Natural Traffic':520,'News':600}
chanels.update(chanelsUpdate)
print(chanels.keys())
chanels.pop('Email')
print(chanels)

