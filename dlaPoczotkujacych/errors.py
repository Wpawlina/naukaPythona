import sys
 
file_path ='orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
        except ValueError as e:
            print("Problem with line %s" % line)
            print('Value Error',e)
        except IndexError as e:
            print("Problem with line %s" % line)
            print('Index Error',e)
        
        except:
            print("error")
        else:
             print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
        finally:
            print('\n')

        

print("Processing finished")


  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')