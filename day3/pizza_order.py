print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "S" :
  bill = 15
  # print(f"Small pizza (S): ${bill}")
  if add_pepperoni == "Y" :
    bill += 2
  if add_pepperoni == "N" :
    bill += 0
  if extra_cheese == "Y" :
    bill += 1
  if extra_cheese == "N" :
    bill += 0
  print(f"Your final bill is: ${bill}.")
elif size == "M" :
  bill = 20
  # print(f"Medium pizza (M): ${bill}")
  if add_pepperoni == "Y" :
    bill += 3
  if add_pepperoni == "N" :
    bill += 0
  if extra_cheese == "Y" :
    bill += 1
  if extra_cheese == "N" :
    bill += 0
  print(f"Your final bill is: ${bill}.")
elif size == "L" :
  bill = 25
  # print(f"Large pizza (L): ${bill}")
  if add_pepperoni == "Y" :
    bill += 3
  if add_pepperoni == "N" :
    bill += 0
  if extra_cheese == "Y" :
    bill += 1
  if extra_cheese == "N" :
    bill += 0
  print(f"Your final bill is: ${bill}.")






