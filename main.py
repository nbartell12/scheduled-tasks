import os
import smtplib
import random

my_email = os.environ.get("MY_EMAIL")
app_pass = os.environ.get("MY_PASSWORD")
me = "nicky.bartell@gmail.com"
kayla = "kaylawalsh180@gmail.com"

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=me,
                        msg=f"Subject: Motivational Quote\n\n{quote}")

