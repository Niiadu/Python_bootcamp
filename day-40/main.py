import requests

SHEETY_ENDPOINT = "https://api.sheety.co/9cfa1a5b1e6fe00315efbf11e463676c/flightDeals/users"

print("Welcome tp Jonas's Flight Club")
print("We find the best flight deals and email.")
first_name = input("What is your first name? \n")
last_name = input("What is your last name? \n")
email = input("What is your email? ")
second_email = input("Tye your email again? ")

if email == second_email:
    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=user_data)
    print(response.json())
    print("You're in the club")
else:
    print("Your email doesnt match")

