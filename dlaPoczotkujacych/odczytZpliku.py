file=open("test.txt",'r')

content=file.read()
print(content)

print('========')
file.close()

with open("test.txt",'r') as file:
    content=file.read()
    print(content)

print('========')

with open("test.txt",'r') as file:
    
    for line in file:
        print(line.strip())

print('========')

with open("test.txt",'r') as file:
    lines=file.readlines()
    print(lines)

print('========')
with open("test.txt",'r') as file:
    fragmet=file.read(5)# czyta 5 bajtow z pliku
    while fragmet:
        print(fragmet.strip(),file.tell())
        fragmet=file.read(5)

with open("test.txt",'r') as file:
    with open("test.txt",'w') as file:
        pass