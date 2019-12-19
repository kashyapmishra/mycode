k=input('enter the string')
m=[]
l=[k[0]+k[1],k[1]+k[0]]
if len(k)==2:
    l=[k[0]+k[1],k[1]+k[0]]
else:
    for i in range(2,len(k)):
        for e in l:
            for j in range(len(e)):
                m.append(e[:j:]+k[i]+e[j::])
        l=m
# print(k[2::])           

#for i in
print(l)