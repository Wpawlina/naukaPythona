import numpy as np

a=np.array([1,2,3])
print('a',a)

b=np.array(([[9.0,8.0,7.0],[6.0,5.0,4.0]]))
print('b',b)
print('dim of b: ',b.ndim)
print('shape of b: ',b.shape)
a=np.array([1,2,3],dtype='int8')
print('a itmesize (bytes) : ',a.itemsize)
print('total size of b: ',b.size)
print('total number of bytes used by a :',a.nbytes)
print('b[0][2]',b[0,2])
print('first row of b:',b[0,:])
print('first column of b:',b[:,0])
c=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('c[0,1:6:2]',c[0,1:6:2])
c[1,5]=20
print('c',c)
c[:,2]=[1,2]
print('c',c)
#all 0 matrix
d=np.zeros((2,3),dtype='int16')
#all 1 matrix   
e=np.ones((2,3))
#any other number
f=np.full((2,2),99.0,dtype='float16')
# array like another array filled with given number
f=np.full_like(b,4)
#random decimal number
g=np.random.rand(4,2)
g=np.random.random_sample(a.shape)
print('random from sample: ',g)
#random int numbers
g=np.random.randint(7,10,size=(3,2))
print('random ints',g)
#identity matrixs
h=np.identity(5)
print('identity 5\n',h)

#repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=1)
print('repeat ',r1)
output=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
output[1:4,1:4]=z
print('output\n',output)

#copying array

a=np.array([[1,2,3],[4,5,6]])
b=a.copy()
b[0,0]=100
print('a',a)
print('b',b)


#mathematics
a=np.array([1,2,3,4],dtype='float16')


print('a+=2',a+2)

print('a-=2',a-2)

print('a*=2',a*2)

print('a/=2',a/2)

print('a**2',a**2)

print('sin(a)',np.sin(a))

print('cos(a)',np.cos(a))

#linear algebra

a=np.full((2,3),2)
b=np.full((3,2),3)
print('a*b',np.matmul(a,b))

#determinant
c=np.identity(4)
print('determinant',np.linalg.det(c))

#inverted matrix
c=np.array([[1,2],[3,4]])
print('iverted matrix',np.linalg.inv(c))    

#eig values and eig vectors
c=np.array([[4,0],[0,3]])
print('eig values',np.linalg.eig(c))

#statistics
stats=np.array([[1,2,3],[4,5,6]])
print('min',np.min(stats))
print('max',np.max(stats))
print('min axis 0',np.min(stats,axis=0))
print('min axis 1',np.min(stats,axis=1))
print('sum ',np.sum(stats))


#reorganizing arrays
before=np.array([[1,2,3,4],[5,6,7,8]])
after=before.reshape((4,2))
print('after',after)
#vertically stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print('verticall stack',np.vstack([v1,v2]))
#horizontal stacking vectors
h1=np.ones((2,4))
h2=np.zeros((2,2))
print('horizontal stack',np.hstack([h1,h2])) 

#miscellaneous
data=np.genfromtxt('NumPy/data.txt',delimiter=',')
print('data',data.astype('int32'))

#Advanced indexing and boolean masking

print('data>50',data>50)
print('data[data>50]',data[data>50].astype('int32'))
#indexing with a list in NumPy
a=np.array([1,2,3,4,5,6,7,8,9])
print('a[[1,2,8]]',a[[1,2,8]])

#any and all
print('any',np.any(data>50))
print('all',np.all(data>50))
print('all',np.all(data>0,axis=0))


print('data>50 and data<100',(data>50) & (data<100))

