##################### Extra Hard Starting Project ######################
import random

import pandas
import datetime as dt
import smtplib
# 1. Update the birthdays.csv

MY_EMAIL = "jndjrdn12345@gmail.com"
MY_PASSWORD = "zufuspgkstkkqgwz"

birthday = {}

def add_a_birthday(name, email, year, month, day):
    birthday["name"] = [name]
    birthday["email"] = [email]
    birthday["year"] = [year]
    birthday["month"] = [month]
    birthday["day"] = [day]
    print(birthday)
    df = pandas.DataFrame.from_dict(birthday)
    df.to_csv("birthdays.csv", mode="a", index=False, header=False)


# add_a_birthday(name="Sorya", email="sorya.s-e@hotmail.fr", year=1995, month=3, day=4)
# add_a_birthday(name="Gaël", email="gael.francoise@gmail.com", year=1997, month=8, day=28)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv", index_col=False)
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        content = letter.read()
        content = content.replace('[NAME]', birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday !\n\n{content}")






