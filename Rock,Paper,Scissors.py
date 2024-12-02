import random

while True:

  ccount=0
  ucount=0

  x=int(input('''
   1.YES|Play
   2.NO|Exit
   '''))

  if x==1:
    i=0
    while i<=2:

      y=int(input('''
       0.ROCK
       1.PAPER
       2.SCISSORS
       '''))

      l=['ROCK','PAPER','SCISSORS']
      n=random.randint(0,2)
      print('You chose : ', l[y])
      print('Computer chose : ',l[n])

      if y==0 and n==1:
        print('You lose round no. : ',i)
        ccount+=1
      elif y==0 and n==2:
        print('You win round no. : ',i)
        ucount+=1
      elif y==1 and n==0:
        print('You win round no. : ',i)
        ucount+=1
      elif y==1 and n==2:
        print('You lose round no. : ',i)
        ccount+=1
      elif y==2 and n==0:
        print('You lose round no. : ',i)
        ccount+=1
      elif y==2 and n==1:
        print('You win round no. : ',i)
        ucount+=1
      else:
        print('Round no.',i,'draw')

      i+=1

  else:
    break

  print('Computer won',ccount,'rounds')
  print('You won',ucount,'rounds')

  if ucount>ccount:
    print('You win the game')
  elif ucount<ccount:
    print('You lost the game')
  else:
    print('Game draw')