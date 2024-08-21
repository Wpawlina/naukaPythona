import os
import time


print("Current directory is: ",os.getcwd())


currentDir=os.getcwd()
filaName='result.txt'
fullPath=os.path.join(currentDir,filaName)
print('\n the constructed path is: ',fullPath)
relativePath='output.txt'
print('\n The absolute path is: ',os.path.abspath(relativePath))

filepath=r'C:\Users\wojpa\OneDrive\zd\python\udemy\dla poczotkujacych\print.py'
print('\n The file name part is ',os.path.basename(filepath))
print('\n The directory part is: ',os.path.dirname(filepath))

print('\n Is file existing: ',os.path.exists(filepath))


if os.path.exists(filepath):
    print('\n last modift date is: ',os.path.getmtime(filepath))
    print('\n last modify date is: ',time.localtime(os.path.getmtime(filepath)))

    print('\n File size is: ',os.path.getsize(filepath))

    print('\n is it a file:',os.path.isfile(filepath))
    print('\n is it a dir:',os.path.isdir(filepath))

    print('\n Path splitted:',os.path.split(filepath))
    print('\n Only file name part:',os.path.split(filepath)[1])

    print('\n Path splitted into drive:',os.path.splitdrive(filepath))
    print('\n Only drive:',os.path.splitdrive(filepath)[0])


