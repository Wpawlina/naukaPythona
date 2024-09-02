text='This is a text.'
print(text.endswith('ext'))
print(text.islower())
print(text.upper().isupper())
print(text.find('is',3))# zwraca wystopienie substringa w stringu
print(text.replace('a','4'))
print(text.replace('a','4').replace('s','5'))
print(text.split(' '))# rozdziela stringa przez separator
sthLikeNumber='1000'
# bład sthLikeNumber+1
print(sthLikeNumber.isdigit())# sprawdzamy czy jest liczba calkowita
print(sthLikeNumber.isdecimal())# sprawdzamy czy jest liczba dziesietna
print(sthLikeNumber.isalpha())# sprawdza czy string zawiera tylko litery alfabetu
print(sthLikeNumber.isalnum())#sprawdza czy jest alfanumeryczny
drive='c:\\'
folder='scripts\\python\\'
file='myscript.py'
path=drive+folder+file
print(path)
justText='text with \nnewline'
print(justText)
justText=r'text \with \nnewline'# literka r oznacza raw text nie interpretuje znaków specjalnych
print(justText)
print('(\\(\\')
print('( -.-)')
print('O_(")(")')
sthLikeNumber=sthLikeNumber+str(1)
print(sthLikeNumber)
print(type(sthLikeNumber))
sthLikeNumber=int(sthLikeNumber)+1
print(sthLikeNumber)
print(type(sthLikeNumber))
article='''Monty Python (also collectively known as the Pythons)[2][3] were a British comedy troupe formed in 1969 consisting of Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. The group came to prominence for the sketch comedy series Monty Python's Flying Circus, which aired on the BBC from 1969 to 1974. Their work then developed into a larger collection that included live shows, films, albums, books, and musicals; their influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Their sketch show has been called "an important moment in the evolution of television comedy".[7]

Monty Python's Flying Circus was loosely structured as a sketch show, but its innovative stream-of-consciousness approach and Gilliam's animation skills pushed the boundaries of what was acceptable in style and content.[8][9] The Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. They followed their television work by making the films Monty Python and the Holy Grail (1975), Life of Brian (1979), and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while it has coloured the work of the early editions of Saturday Night Live through to absurdist trends in television comedy.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution to Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Holy Grail and Life of Brian are frequently ranked on lists of the greatest comedy films. A 2005 poll asked more than 300 comedians, comedy writers, producers, and directors to name the greatest comedians of all time, and half of Monty Python's members made the top 50.[10][11]'''
print(article.upper())
print(article.lower().replace('monty','flying'))
print(article.split(' '))
print('word python appears',article.lower().count('python'),'times')
print('to print the \ you need to put \ twice in your text like this: \\')
print('The best hits of \'80s!!!')
PLN=234
USD=3.65
EUR=4.23
print('cur','exchange','amount',)
print('USD',USD,PLN/USD,sep='\t')
print('EUR',EUR,PLN/EUR,sep='\t')
valueAsTxt='123.45'
factor=1.23
print('value is',valueAsTxt,'factor is',factor,'value*factor=',float(valueAsTxt)*factor)

string='A Python script'
print(string[0])
print(string[2:8])
print(string[2:7])#[start:end:step]
print(string[2:8])
print(string[:8])
print(string[8:])


q='THE EYES'
q=q[0:3]+q[5]+q[3]+q[7]+q[4]+q[6]
print(q)
q='a gentleman'
q=q[3]+q[6:8]+q[2]+q[0]+q[4:6]+q[1]+q[8:]
print(q)
q='THE MORSE CODE'
q=q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[-1]+q[9]+q[-2]+q[5]+q[0]+q[7]
print(q)
#line='Program "Kropka nad i" nadamy o: 22:00'
line='Program "Pytanie na śniadanie" nadamy o: 6:00'
time=line[line.find(':')+2:]
print(time)
pos=line.find('"')+1
pos2=line.find('"',pos)
title=line[pos:pos2]
print(title,time)





