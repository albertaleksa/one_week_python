import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "albert.aleksa.by@gmail.com"
MY_PASSWORD = "cxmvdmkzhurxlakm"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


def send_email(to_email, text):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Birthday\n\n{text}"
        )


if __name__ == '__main__':
    # Read csv
    data = pandas.read_csv("birthdays.csv")
    # Get today date
    now = dt.datetime.now()
    month = now.month
    date = now.day
    # Find in csv records with today date
    birth_data = data[(data.month == month) & (data.day == date)]
    name_list = birth_data["name"].to_list()
    email_list = birth_data["email"].to_list()
    # For each matches record
    for i in range(len(name_list)):
        name = name_list[i]
        email = email_list[i]
        # Pick a random letter from letter templates
        random_number = random.randint(1, 3)
        print(random_number)
        letter_file_name = f"letter_templates/letter_{random_number}.txt"
        with open(letter_file_name) as file:
            letter = file.read()
        # Replace the [NAME] with person's actual name from csv
        new_letter = letter.replace(PLACEHOLDER, name)
        # Send the letter
        send_email(email, new_letter)
