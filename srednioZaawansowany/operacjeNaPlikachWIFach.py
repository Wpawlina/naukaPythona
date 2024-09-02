import os

path=r'srednio zaawansowany\test.txt'



'''
if os.path.isfile(path):
    print('Plik istnieje')
else:
    print('Plik nie istnieje')
    print('Tworze plik')
    open(path.replace('\\','/'),'x').close()
    print('Plik zostal utworzony')
'''

result=os.path.isfile(path) or open(path,'x').close()
print(result)


def countWords(path):
    if os.path.isfile(path):
        with open(path,'r') as file:
            content=file.read()
            words=content.split()
            return len(words)
    else:
        return None
    
path=r'srednio zaawansowany\test2.txt'


if os.path.isfile(path):
    print(countWords(path))
result=os.path.isfile(path) and print(countWords(path))
print(result)