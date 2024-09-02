Tax=(4,7,8,23)
print(Tax[2])
print(Tax[-1])
print(Tax.index(7))
print(Tax.count(8))
print(max(Tax))
#tuple nie mozna edytowac 
TaxList=list(Tax)
print(Tax)
print(TaxList)
TaxList.append(30)
NewTax=tuple(TaxList)
tax1,tax2,tax3,tax4,tax5=TaxList
print(tax1,tax2,tax3,tax4,tax5)
a=10
b=1
a,b=b,a
print(a,b)

marketing=['loyalty program','client promotion','market reaserch']
marketing.append('public relations')
print(marketing[3])
marketing.insert(2,'investor relation')
emailMarketing=marketing.copy()
emailMarketing.sort()
internalEmails=['internal communication']
emailMarketing.extend(internalEmails)
emailMarketingTuple=tuple(emailMarketing)
print(emailMarketingTuple)


