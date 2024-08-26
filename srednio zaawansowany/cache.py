import time
import functools

@functools.lru_cache(maxsize=32)
def factorial(n):
    time.sleep(0.1)
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

star=time.time()  
for i in range(1,11):
    print(i,'! =',factorial(i))
end=time.time() 
print('czas wykonania:',end-star)   

print(factorial.cache_info())