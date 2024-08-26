workDays=[19,21,22,21,20,22]


enumeratedWorkDays=list(enumerate(workDays))
print(enumeratedWorkDays)

for pos,value in enumerate(workDays):
    print('Position:',pos,'Value:',value)

months=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
monthsWorkDays=list(zip(months,workDays))
print(monthsWorkDays)

for month,workDay in zip(months,workDays):
    print('Month:',month,'Work days:',workDay)

for pos,(month,workDay) in enumerate(zip(months,workDays)):
    print('Position:',pos,'Month:',month,'Work days:',workDay)


print('===============================')

projects=['Brexit','Nord Stream','US Mexico Border']
leaders=['Theresa May','Wladimir Putin','Donald Trump and Bill Clinton']
for project,leader in zip(projects,leaders):
    print('The leader of',project,'is',leader)

dates=['2016-06-23','2016-08-29','1994-01-01']
for project,leader,date in zip(projects,leaders,dates):
    print('The leader of',project,'is',leader,'and start date is',date)


for id,(project,leader,date) in enumerate(zip(projects,leaders,dates)):
    print('ID:',id,'The leader of',project,'is',leader,'and start date is',date)