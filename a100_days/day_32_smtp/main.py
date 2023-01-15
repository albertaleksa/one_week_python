import smtplib
import os
from dotenv import load_dotenv

load_dotenv(override=True)
MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_EMAIL_PASSWORD']

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="dread66620@gmail.com",
        msg="Subject:Test email\n\nThis is a test email from Python app."
    )
