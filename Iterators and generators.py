def mult(x,y):
  rowsx=len(x)
  colsx=len(x[0])
  rowsy=len(y)
  colsy=len(y[0])

  if colsx!=rowsy:
    return None
  else:
    mat=[]
    for i in range(rowsx):
      lst=[]
      for j in range(colsy):
        temp=0
        for k in range(colsx):
          temp+=x[i][k]*y[k][j]
        lst.append(temp)
      mat.append(lst)
    return mat

x=[[1,2,3],[4,5,6]]
y=[[11,12],[13,14],[15,16]]
m=mult(x,y)
print(m)












x=[[1,2,3],[4,5,6]]
y=[[11,12],[13,14],[15,16]]

l1=[xrow for xrow in x]
print(l1)
l2=[(xrow,ycol) for ycol in zip(*y) for xrow in x]
print(l2)
l3=[[sum(a*b for a,b in zip(xrow,ycol))for ycol in zip(*y)] for xrow in x]
print(l3)















l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'h', 'i', 'j']

# Concatenate corresponding elements from l1 and l2
concatenated_list = [''.join(pair) for pair in zip(l1, l2)]
#List Comprehension: The list comprehension [''.join(pair) for pair in zip(l1, l2)]
#creates a list of concatenated strings. Each pair from zip(l1, l2) is a tuple
# containing corresponding elements from l1 and l2.

print(concatenated_list)













import random

lst=[random.randint(1,20) for n in range(20)]
print(lst)
a=int(input('Enter the number: '))
index=[i for i in range(len(lst)) if a==lst[i]]
print('Number',a,'found at following positions: ',index)














qlist=['What is the capital of France?',
'Which planet is known as the Red Planet?']

alist=[['Berlin','Madrid','Paris','Rome'],['Earth','Mars','Jupiter','Saturn']]

qalist=[]
for q,a in zip(qlist,alist):
  lst=[q,*a]
  qalist.append(lst)
print(qalist)  

















import random

x=int(input('Enter the no. of terms in list: '))

#generating x random integers
num=[random.randint(1,100) for n in range(x)]
print(num)

#sorting the list
lst=sorted(num)
print(lst)
t=len(lst)
if t%2==0:#if x is even, there will be two medians
  print('Median no. are: ',lst[int((t-2)/2)],lst[int(t/2)])
else:#if x is odd, there will be one median
  print('Median no. is: ',lst[int((t-1)/2)])  















num = [5, -12, 27, -34, 48, -51, 63, -74, 85, -92, 106, -115, 128, -139, 150, -164, 175, -182, 197, -205]
ncount=0
for n in num:
  if n<0:
    ncount+=1
print(ncount)

#OR
#lst=[n for n in num if n<0]
#print(len(lst))

l1=[(10, 20, 30), (150.55, 145.60, 157.65), ('A1', 'B1', 'C1')]
l2=list(zip(*l1))
print(l2)