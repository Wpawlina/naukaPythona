persons=['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']

domain='mycompany.com'

for person in persons:
    email=person + '@'+domain
    print('Email for \t',person,'\tis\t',email)


n=10
wynik=1
for i in range(1,n+1):
    wynik=wynik*i
    print(i,wynik)
