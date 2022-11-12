s='AnamikaSinha1234'
L=list(s)
len(L)
l1=[]
l2=[]
l3=[]


l4=l2+l1+l3
s2="".join(l4)
s2

l1=[data for data in L if data.isupper()]
l2=[data for data in L if data.islower()]
l3=[data for data in L if data not in l1 and data not in l2]

l1.sort()
l2.sort()
l3.sort()
print(l1)
print(l2)
leven=[num for num in l3 if int(num)%2==0 ]
lodd=[num for num in l3 if int(num)%2!=0 ]
newl=l2+l1+lodd+leven
news="".join(newl)
news