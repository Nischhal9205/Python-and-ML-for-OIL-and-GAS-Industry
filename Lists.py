fahr=[25,36,100,49]
for i, f in enumerate(fahr):
  c=int(5/9*(f-32))
  fahr[i]=c
  print(f,c)
print(fahr)

lst=[10,31,100,46,79,92,57]
lst.sort()
print(lst)
n=len(lst)
if n%2==0:
  i=int(n/2-1)
  j=int(n/2)
  median=(lst[i]+lst[j])/2
else:
  i=int((n-1)/2)
  median=lst[i]
print('Median value : ', median)

num=[-1,-19,20,57,-69,72,-92]
pos=[]
neg=[]
for n in num:
  if n<0:
    neg.append(n)
  else:
    pos.append(n)
print('Negative integers : ', neg)
print('Positive integers : ', pos)


# Sample list containing both positive and negative integers
numbers = [10, -5, 23, -11, 0, 8, -42, 19, -7]

# List to store negative numbers
negative_numbers = []

# Loop through each number in the list
for num in numbers:
    # Check if the number is negative
    if num < 0:
        # Add the negative number to the negative_numbers list
        negative_numbers.append(num)

# Print the list of negative numbers
print("Negative numbers in the list are:", negative_numbers)


lst1=['abc','def','ghi','jkl']
lst2=[]
for word in lst1:
  lst2.append(word[0])
print(lst2)

lst1=['abcr','defscs','ghikc','jklskjcghjc']
lst2=[]
for word in lst1:
  n=len(word)
  lst2.append(word[n-1])
print(lst2)

l=[10,20,30,40,50,60,70,80,90,100]
t=len(l)
for i in range(t-1,-1,-2):
  print(l[i])

l=[]
while True:
  c=int(input('''
   1 Enqueue element
   2 Dequeue element
   3 Front element
   4 Rear element
   5 Display Queue
   6 Exit
   '''))
  if c==1: #add an element to the list
    e=int(input('Enter element : '))
    l.append(e)
    print(l)
  elif c==2: #delete the first element
    if len(l)==0:
      print('Empty Queue')
    else:
      del l[0]
      print(l)
  elif c==3: #shows the first element
    if len(l)==0:
      print('Empty Queue')
    else:
      print('Front element : ', l[0])
  elif c==4: #shows the last element
    if len(l)==0:
      print('Empty Queue')
    else:
      t=len(l)
      print('Rear element : ', l[t-1])
  elif c==5: #displays the list
    print('Dispaly Queue : ', l)
  else: #exits the programme
    break


x=[1,3,5,7,9]
y=[2,4,6,8]
x[2]=y
print(x)
x=x[:2]+[*y]+x[3:]
print(x)
x.sort()
print(x)

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

l=['abc','def','ghi','jkl','mno']
for i, item in enumerate(l):
  l[i]=item.upper()
print(l)

fahr=[25,36,100,49]
cel=[]
for f in fahr:
  c=int(5/9*(f-32))
  cel.append(c)
print(cel)

fahr=[25,36,100,49]
cel=[]
for i, f in enumerate(fahr):
  c=int(5/9*(f-32))
  cel.append(c)
print(cel)

l1=[1,2,3,4,5,6,7,8,8,9,10,11,11,15,16,16,18,20,20]
l2=[]
for i, num in enumerate(l1):
  if l1[i]==num:
    l1.remove(num)
    l2.append(num)
print(l1)
print(l2)