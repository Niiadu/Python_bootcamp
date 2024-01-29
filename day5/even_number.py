target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_number = 0

for x in range(0, target + 1) :
  if (x % 2) == 0 :
    even_number += x 
print(even_number)
