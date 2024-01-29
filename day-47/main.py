from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import html


my_email = "jonasadjintettey@yahoo.com"
password = "zkmwoqbkciwaiszs"
amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Forwarded-For": "102.176.75.174",
}

response = requests.get(amazon_url, headers=header)
pot_data = response.text
# print(pot_data)

soup = BeautifulSoup(pot_data, "lxml")
data = soup.find(class_="a-offscreen").getText()
price = float(data.split("$")[1])
# print(price)

product_name = soup.select(selector="#productTitle")[0].getText().strip()
# print(product_name)


if price < 100:
    message = f"{product_name} is now ${price}"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs="jonasadjintettey@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{amazon_url}".encode("utf-8")
        )



