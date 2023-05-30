import smtplib
import random
import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()



quotes = []
with open("quotes.txt") as data:
    content = data.readlines()

def send():
    for i in content:
        quotes.append(i)
    daily_quote = random.choice(quotes)

    my_gmail = "boydanzee@gmail.com"
    password = "rlebcifzblcrlenf"

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs="alphaanimefori99@gmail.com",
                            msg=f"Subject:Daily Quotes\n\n{daily_quote}")
        connection.sendmail(from_addr=my_gmail,
                            to_addrs="ugochukwuanosike1@gmail.com",
                            msg=f"Subject:Daily Quotes\n\n{daily_quote}")
        connection.sendmail(from_addr=my_gmail, to_addrs="rosemarymshelia85@gmail.com",
                            msg=f"Subject:Daily Quotes\n\n{daily_quote}")
        connection.sendmail(from_addr=my_gmail, to_addrs="danielrobert1702@gmail.com",
                            msg=f"Subject:Daily Quotes\n\n{daily_quote}")


if day_of_week == 0:
    send()
