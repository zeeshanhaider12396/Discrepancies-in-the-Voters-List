n1,n2,n3=map(int,input().split())
l1=[]
l2=[]
l3=[]
for i in range(n1):
    a=int(input())
    l1.append(a)
for i in range(n2):
    b=int(input())
    l2.append(b)
for i in range(n3):
    c=int(input())
    l3.append(c)
#print(l1,l2,l3)
l4=[]
set1=set(l1)
set2=set(l2)
set3=set(l3)
set4=set(l4)
set4=set1.intersection(set2).union(set1.intersection(set3))
set4=set2.intersection(set3).union(set4)
set4=list(set4)
print(len(set4))
set4.sort()
for i in set4:
    print(i)
#print(set4,sep="\n")
