def fac(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact

n=int(input('Enter the number : '))
f=fac(n)
print('The factorial is : ', f)

def fac(n):
  fact=1
  i=1
  while i<=n:
    fact=fact*i
    i=i+1
  return fact

n=int(input('Enter the number : '))
f=fac(n)
print('The factorial is : ', f)

def ruppe(n):
  inr =n*83
  print(inr)
  return inr

n=int(input("Enter the amount in USD : "))
print('The amount in INR : ', ruppe(n))

def fnum(n):
  if n==0:
   return
  elif n%2==0:
    print('EVEN')
  else:
    print('ODD')

n=int(input('Enter the number : '))
fnum(n)

def count_lower_upper(s):
  d={"UPPER_CASE":0, "LOWER_CASE":0, "DIGIT":0}
  for c in s:
    if c.isupper():
      d["UPPER_CASE"]+=1
    elif c.islower():
      d["LOWER_CASE"]+=1
    else:
      d['DIGIT']+=1

  return(d)

s=input('Enter the string : ')
counts=count_lower_upper(s)
print(counts)



def count_lower_upper(s):
  d={"UPPER_CASE":0, "LOWER_CASE":0, "DIGIT":0}
  for i in range(len(s)):
    if s[i].isupper():
      d["UPPER_CASE"]+=1
    elif s[i].islower():
      d["LOWER_CASE"]+=1
    else:
      d['DIGIT']+=1

  return(d)

s=input('Enter the string : ')
counts=count_lower_upper(s)
print(counts)

def count_lower_upper(s):
  d={"UPPER_CASE":0, "LOWER_CASE":0, "DIGIT":0}
  i=0
  while i < len(s): # i<len(s) because index i=len(s) does not exist as indexing starts from 0 and ends at {len(s)-1}
    if s[i].isupper():
      d["UPPER_CASE"]+=1
    elif s[i].islower():
      d["LOWER_CASE"]+=1
    else:
      d['DIGIT']+=1
    i+=1

  return(d)

s=input('Enter the string : ')
counts=count_lower_upper(s)
print(counts)

def compute(n):
  s=0
  num=0
  for i in range(0,4):
    num=num*10+n
    s+=num
  return s

n=int(input('Enter the number : '))
sum=compute(n)
print(sum)

def compute(n):
  s=(1234)*n
  return s

n=int(input('Enter the number : '))
sum=compute(n)
print(sum)

def create_list(l1,l2):
  l3=l1+l2
  return(l3)

l1=[10,20,30,40,50]
l2=[1,2,3,4,5]
l3=create_list(l1,l2)
l3.sort()
print(l3)

#remove duplicate elements from the list
def sanitize_list(l):
  s=set(l)
  l=[i for i in s] #l=[*s]/l=list(s) aslo works same
  l.sort()
  return(l)

l=[10,10,21,69,46,23,72,46,51,51]
l1=sanitize_list(l)
print(l1)

#recursive function for finding the factorial of a number
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

n=int(input('Enter the number : '))
f=factorial(n)
print('The factorial value is : ', f)

#recursive function for sum of n natural numbers
def sum_numbers(n):
  if n<=0:
    return 0
  else:
    return n + sum_numbers(n-1)

n=int(input('Enter a natural number'))
s=sum_numbers(n)
print(s)

#recursive function to print all elemnts of a list
def print_it(l,i=0):
  if i==len(l):
    return
  else:
    print(l[i])
    print_it(l,i+1)

l=[1,2,3,4,5]
print_it(l)