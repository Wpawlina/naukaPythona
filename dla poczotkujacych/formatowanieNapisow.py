message='Processing file %s'# % o
print(message  % ('file_1_txt'))
message2='File %s has size %d KB'
print(message2  % ('file_1_txt',100))
message3='File %20s has size %10d KB'
print(message3  % ('file_1_txt',100))
message4='Processing file {:s}'
print(message4.format('file1.txt'))
message5='File {1:s} has size {0:d}'
print(message5.format(100,'file_1.txt'))
message6='File {1:20s} has size {0:10d}'
print(message6.format(100,'file_1.txt'))
helloMessage="Heloo %s!"
print(helloMessage % ('Kate'))
helloMessage="Heloo {:s}!"
print(helloMessage.format('Chris'))
helloMessage="%s has %d %s"
print(helloMessage % ('Kate',1,'animal'))
helloMessage="{:s} has {:d} {:s}"
print(helloMessage.format('Chris',10000,'$'))
line='{:20s} costs {:6d} €'
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))