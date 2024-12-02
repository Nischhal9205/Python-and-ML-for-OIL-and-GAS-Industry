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