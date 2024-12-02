D={
'a' : 1,
'b' : 2,
'c' : 3,
'd' : 4,
'e' : 5,
'f' : 6,
'g' : 7,
'h' : 8,
'i' : 9,
'j' : 10,
'k' : 11,
'l' : 12,
'm' : 13,
'n' : 14,
'o' : 15,
'p' : 16,
'q' : 17,
'r' : 18,
's' : 19,
't' : 20,
'u' : 21,
'v' : 22,
'w' : 23,
'x' : 24,
'y' : 25,
'z' : 26
 }
while True:
   X=int(input('''
   1 Enter a word
   2 Exit
   '''))
   if X==1:
     Word=input('Enter a word : ')
     T=len(Word)
     Sum=0
     for i in range(T):
       Sum+=D.get(Word[i])
     print('Your word',Word,'equals to the value : ', Sum)
   elif X==2:
     break














students = {
    'Dipti': {'Maths': 48, 'eng': 60, 'hindi': 95},
    'Smriti': {'Maths': 75, 'eng': 68, 'hindi': 89},
    'Subodh': {'Maths': 45, 'eng': 66, 'hindi': 87}
}

topper_name = ''
topper_marks = 0

for nam, info in students.items():
    total = 0
    for sub, marks in info.items():
        total += marks
    avg = total // 3
    students[nam] = {'Total': total, 'Average': avg}
    if avg > topper_marks:
        topper_name = nam
        topper_marks = avg

print(students)
print('Topper of the class:', topper_name)
print('Topper marks:', topper_marks)













portfolio = { 'accounts' : [ 'SBI', 'IOB'],
              'shares' : ['HDFC', 'ICICI', 'TM', 'TCS'],
              'ornaments' : ['10 gm gold', '1 kg silver']
              }
portfolio['MF']=['Reliance','ABSL']
print(portfolio)
portfolio['accounts']=['Axis','BOB']
print(portfolio)
lst=portfolio['shares']
portfolio['shares']=sorted(lst)
print(portfolio)
del portfolio['ornaments']
print(portfolio)












d1={
    'wheat':20,
    'rice':30,
    'sugar':40
}

d2={
    'wheat':10,
    'rice':20,
    'sugar':30
}
total=0
value=0
for k in d1:
  value+=d1[k]*d2[k]
  total+=value
print('Total bill amount : ', total)













# Dictionary containing grocery items and their prices
grocery_prices = {
    'Apples': 2.50,
    'Bananas': 0.50,
    'Carrots': 1.20,
    'Dates': 3.00,
    'Eggs': 0.20
}

# Dictionary containing grocery items and quantity purchased
grocery_quantities = {
    'Apples': 4,
    'Bananas': 6,
    'Carrots': 5,
    'Dates': 2,
    'Eggs': 12
}

# Dictionary to store the final price of each grocery item
grocery_final_prices = {}

# Calculate the final price for each item
for item in grocery_prices:
    if item in grocery_quantities:
        final_price = grocery_prices[item] * grocery_quantities[item]
        grocery_final_prices[item] = final_price

# Print the final prices dictionary
print(grocery_final_prices)













user_credentials = {
    "user1": "P@ssw0rd123",
    "user2": "SecureP@ss456",
    "user3": "Qwerty!789",
    "user4": "Abcdef#1011",
    "user5": "MyP@ssw0rd",
    "user6": "Passw0rd$2020",
    "user7": "LetM3In!",
    "user8": "P@ssphr@se",
    "user9": "Welcome#123",
    "user10": "1234Secure!"
}
print(user_credentials)
username = input("Enter your username: ")
password = input("Enter your password: ")

for usernam in user_credentials:
    if username == usernam:
        print('Match found for username : ', user_credentials.get(usernam))
        break
    else:
        print('No match found')

keys=[k for k,v in user_credentials.items() if v==password]
if keys:
  print('Match foud for password : ', *keys)
else:
  print('No match found')










user_credentials = {
    "user1": "P@ssw0rd123",
    "user2": "SecureP@ss456",
    "user3": "Qwerty!789",
    "user4": "Abcdef#1011",
    "user5": "MyP@ssw0rd",
    "user6": "Passw0rd$2020",
    "user7": "LetM3In!",
    "user8": "P@ssphr@se",
    "user9": "Welcome#123",
    "user10": "1234Secure!"
}

print(user_credentials)

username = input("Enter your username: ")

if username in user_credentials:
    password = input("Enter your password: ")
    if password == user_credentials[username]:
        print("Username and password matched.")
    else:
        print("Password incorrect.")
else:
    print("Username not found.")
