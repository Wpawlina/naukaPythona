import time,math





source='line +=1'

line=0

sourceCompiled=compile(source,'internal variable source','exec')

exec(sourceCompiled)

print(line)


start=time.time()
for i in range(100000):
    exec(source)
print('exec time:',time.time()-start)

start=time.time()
for i in range(100000):
    exec(sourceCompiled)
print('exec compiled time:',time.time()-start)


formulas=['abs(x**3 - x**0.5)','abs(math.sin(x) * x**2)']

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)
for formula in formulas:
    print('formula:',formula)
    results_list = []
    start=time.time()
    for x in argument_list:
        result=eval(formula)
        results_list.append(result)
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    print('time:',time.time()-start)
print('='*30)

for formula in formulas:
    print('formula:',formula)
    compiled_formula=compile(formula,'internal variable formula','eval')
    results_list = []
    start=time.time()
    for x in argument_list:
        result=eval(compiled_formula)
        results_list.append(result)
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    print('time:',time.time()-start)
