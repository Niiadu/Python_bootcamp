print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 170 :
  print("You can ride the rollercoster")
  age = int(input("whats your age? "))
  if age < 12 :
    print("Please pay $5")
  elif age <= 18 :
    print("Please pay $7")
  else: 
    print("Please pay $12")
else:
  print("You cant ride the rollercoster")