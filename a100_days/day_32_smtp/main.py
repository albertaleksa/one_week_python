import smtplib

my_email = "albert.aleksa.by@gmail.com"
password = "cxmvdmkzhurxlakm"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dread66620@gmail.com",
        msg="Subject:Test email\n\nThis is a test email from Python app."
    )
