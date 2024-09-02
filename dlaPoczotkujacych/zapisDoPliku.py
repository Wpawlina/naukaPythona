fileName='output.txt'
line="Europe"
cities=['London','Berlin','Paris','Warsaw','Madrid','Rome']
file=open(fileName,'w')
file.write(line)
file.write('\n')
file.writelines(cities)
file.close()