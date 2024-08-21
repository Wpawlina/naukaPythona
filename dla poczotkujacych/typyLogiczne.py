isWeekend=True
print("Is weekend",isWeekend)
temperature=22
print("Temputer =",temperature)
toDoList=''
print("ToDoList =",toDoList)
isHappy=isWeekend and temperature > 20 and toDoList=='' or not isWeekend and temperature < 20 and toDoList!=''
print('Is Happy =',isHappy)


isAutomaticMode=False
is80PercentLight=False
isDirectLight=False
isRainy=True
turnLightsOn=isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

obecnosc=40
srednia=2.5
praca=True
zaliczyl=obecnosc >= 80 and srednia >=3.0 and praca
print(zaliczyl)




