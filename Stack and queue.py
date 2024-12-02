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