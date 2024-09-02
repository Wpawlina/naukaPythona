base=2
exp=0
maxExp=16
while exp<=16:
    print(2**exp)
    exp+=1

values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i=0
max=len(values)-2
while i<max:
    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print(values[i],values[i+1],values[i+2])
    i+=1

number=1
prevNumber=0

while number <50:
    print(prevNumber,'+',number,'=',prevNumber+number)
    prevNumber=number
    number+=1
'''
import random
myNuber=random.randint(0,20000)
x=-1
while x!=myNuber:
    x=int(input('Podaj liczbe:'))
    if x> myNuber:
        print('Za duza')
    if x<myNuber:
        print('Za małą')
print(x)
'''
import math
i=1
intrest=0.03
cap=20000
while i <=10:
    cap=math.floor((cap*(1+intrest))*100)/100
    print('kapital po  %2d latach wynosi %5.2f' % (i,cap) )
    i+=1

tekst='''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

words=tekst.replace('\n',' ').replace('.','').replace(',','').split(' ')

longWords=0
shortWords=0

for word in words:
    if len(word)>6:
        longWords+=1
        continue
    shortWords+=1

print(shortWords,longWords)




a=1
b=1
for i in range(3,21):
    a,b=b,a+b
    print(i,b)

tekst='''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

words=tekst.replace('\n',' ').split(' ')

for word in words:
    if 'p' in word:
        print(word)

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}  
for key in dictionary:
    print(key,dictionary[key],sep=' - ')

wordsCount={}

for word in words:
    if word in wordsCount:
        wordsCount[word]+=1
        continue
    wordsCount[word]=1
    #wordsCount.setdefault(word,1)

print(wordsCount)


