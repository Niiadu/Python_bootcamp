import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 3:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    my_email = "jonasadjintettey@yahoo.com"
    password = "zkmwoqbkciwaiszs"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="jonasadjintettey@gmail.com",
                            msg=f"Subject:Good Morning\n\n{quote}")
