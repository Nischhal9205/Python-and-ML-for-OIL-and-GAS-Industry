l=[num for num in range(2,50) if num%2==0 and num%4==0]
print(l)

import random
s1={random.randint(15,45) for n in range(20)}
print(s1)
count=len({n for n in s1 if n<30})
print(count)
s2={n for n in s1 if n<30}
print(s2)

s1='dreams may change, but friends are forever'
l=[''.join(w.capitalize() for w in s1.split())]
print(l)

mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[9,8,7],[6,5,4],[3,2,1]]
mat3=[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0])) for i in range(len(mat1))]
print(mat3)

l=[(i,j) for i in range(1,6) for j in range(1,6)]
print(l)

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[num*10 for num in l1]
print(l2)

lst = [0, 1]
[lst.append(lst[k - 1] + lst[k - 2]) for k in range(2, 20)]
print('First 20 Fibonacci numbers:', lst)

l=[[n for n in range(41) if n%2==0], [n for n in range(41) if n%2!=0]]
print(l)

l=[-23,-4,-5,67,98,-32,45,-12,-45,43,77]
l1=[n for n in l if n<0]
l1.sort()
l2=[n for n in l if n>0]
l2.sort()
print(l1,l2)

l=['abc','def','ghi','jkl','mno']
l1=[''.join(w.capitalize()) for w in l]
print(l1)