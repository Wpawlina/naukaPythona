instructions=['say hello','say how are you','abort','ask for money','say thank you','say goodbye']
instructionsApproved=[]
for ins in instructions:
    print('Adding instruction:',ins)
    instructionsApproved.append(ins)
    if ins=='abort':
        print('Aborting the operation')
        instructionsApproved.clear()
        break
else:
    print('All instructions have been added')

print('Approved instructions:',instructionsApproved)    
print('===============================')

i=0
while i<len(instructions):
    print('Adding instruction:',instructions[i])
    instructionsApproved.append(instructions[i])
    if instructions[i]=='abort':
        print('Aborting the operation')
        instructionsApproved.clear()
        break
    i+=1
else:
    print('All instructions have been added')
print('Approved instructions:',instructionsApproved)


import os
import urllib.request

data_dir=r'srednio zawansowany\contentOfWebsites'

pages=[{'name':'mobilo','url':'http://www.mobilo24.eu/'},{'name':'nonexistent','url':'http://abc.cde.fgh.ijk.pl/'},{'name':'kursy','url':'http://www.kursyonline24.eu/'}]

for page in pages:
    path=os.path.join(data_dir,page['name']+'.html')
    try:
        print('Processing:',page['url'])
        urllib.request.urlretrieve(page['url'],path)
    except:
        print('Failed to download:',page['url'])
        break
else:
    print('All pages downloaded successfully')
    


