##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import random
import pandas
import datetime as dt

placeholder = "[NAME]"
my_email = "jonasadjintettey@yahoo.com"
password = "zkmwoqbkciwaiszs"

details = pandas.read_csv("birthdays.csv")
dict_detail = details.to_dict(orient="records")
# new_details = {row.month: row.day for (index, row) in details.iterrows()}
# print(new_details)

time = dt.datetime.now()
today_month = time.month
today_day = time.day


with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as random_letter:
    new_letter = random_letter.read()

for name in dict_detail:
    if name["day"] == today_day and name['month'] == today_month:
        document = new_letter.replace(placeholder, name["name"])
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=name["email"], msg=f"Subject:Happy Birthday\n\n{document}")



