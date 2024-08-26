var_x=10

source='var_x = 4'

result=exec(source)
print(result)
print(var_x)

print('='*30)   

source='''
new_var=1
for i in range(5):
    print('-'*i)
    new_var+=i
'''

exec(source)
print(new_var)


source=input('Enter your expression: ')
print(eval(source))

print('='*30)

files_to_process=['srednio zaawansowany\\exampleScripts\\math_sin_square.py','srednio zaawansowany\\exampleScripts\\math_square_root.py']

import os

for file in files_to_process:  
    file=os.path.join(os.getcwd(),file)
    with open(file,'r') as f:
        print(os.path.basename(file))   
        source=f.read()
        #print(source)
        exec(source)
        



