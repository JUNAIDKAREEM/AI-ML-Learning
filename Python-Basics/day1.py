#even or odd
num=int(input("enter a number"))
if num%2==0:
  print("even number")
else:
  print("odd number")
  #factorial
  n=int(input("enter a number for a factorial:"))
  fact=1
  for i in range(1,n-1):
    print("factorial:",fact)
    #mutliplication table
  t=int(input('enter a number for table:'))
  for i in range (1,11):
    print(t,'x',i,'=',t*i)
