#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator. ")
bill = input("What was the total bill?  $")
tip = input("What percentage tip would you like to give? 10, 12, or 15 ")
split = input("How many people to split the bill? ")

the_bill = float(bill)
total_tip = int(tip)
split_bill = int(split)

bill_and_tip = the_bill + (total_tip / 100 * the_bill)

total_per_each = round(bill_and_tip / split_bill, 2)

# The "{:.2f}" helps to state precisely two decimal, without it, the total could be 33.6 instead of 33.60
total_per_each = "{:.2f}" .format(total_per_each)
# print(f"${total_per_each}")

print(f"Each person should pay: ${total_per_each} ")