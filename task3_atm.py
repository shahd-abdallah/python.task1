#task 3 ATM
print("hi ATM")
cPIN = 333
balance = 10000
pin = int(input("enter your pin"))
if pin == cPIN :
 print("choose from your options")
 print("1- withdraw")
 print("2- check blance")
 choice = input("enter your choice 1 or 2: ")
if choice == "1" :
  amount = int(input("enter yuor amount"))
  if amount > balance :
   print (" rasied not enough")
  else :
   balance = balance -  amount 
   print("rasied enough")
  print("your balance is : " , balance)
elif choice == "2" :
  print("your balance = " , balance) 