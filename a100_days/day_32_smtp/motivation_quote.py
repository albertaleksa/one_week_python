import datetime as dt
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv(override=True)
MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_EMAIL_PASSWORD']


def get_quote():
    # Read quotes from file into the list
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    # Get random quote
    return random.choice(quotes)


def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="dread66620@gmail.com",
            msg=f"Subject:Quote of the Day\n\n{quote}"
        )


if __name__ == '__main__':
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 3:
        random_quote = get_quote()
        send_email(random_quote)