num=int(input('Enter a number : '))
a=num
d=0
while num>0:
  r=num%10
  d=d*10+r
  num=num//10
print(d)
if a==d:
  print('Palindrome')
else:
  print('Not palindrome')

num=int(input('Enter number : '))
fac=1
i=2
while i<=num:
  fac=fac*i
  i=i+1
print(fac)

for i in range(1,501):
  d=0
  num=i
  while num>0:
   r=num%10
   d=d+r*r*r
   num=num//10
  if i==d:
    print(i)


print(2)
for num in range(3,301):
  i=2
  while i<num:
    if num%i==0:
      break
    i=i+1
  else:
    print(num)

for i in range(1,31):
  for j in range(1,31):
    for k in range(1,31):
      if (i*i)+(j*j)==(k*k):
        print('Triplet : ', i, j, k)

p=100000
for i in range(1,11):
  p=p*pow((10/11),i)
  print('Year', 11-i, ' : ', int(p))

l=[10,20,30,40,50,60,70,80,90,100]
t=len(l)
for i in range(t-1,-1,-2):
  print(l[i])

for i in range(2,1001):
  for j in range(2,1001):
    for k in range(2,1001):
      if (i*i*i)+(j*j*j)==k:
        print(k)
        break

import random
l=[]
for i in range(21):
  l.append(random.randint(1,100))
print(l)
while True:
  Opr=int(input('''
   1 Put value and find its index
   2 Exit
   '''))
  if Opr==1:

    n=int(input('Enter the value : '))
    idx=l.index(n)
    print(idx)
  elif Opr==2:
    break