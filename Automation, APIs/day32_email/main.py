import datetime as dt
import random
import smtplib
import pandas
##################### Extra Hard Starting Project ######################
#for smtp email authentication
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv", header = None)
data = data.rename({0:"nm", 1:"email", 2:"year", 3:"month", 4:"day"}, axis = "columns")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
bday_plushes = {}
today_birthday = False

for (index,row) in data.iterrows():
    if int(row.month) == now.month and int(row.day) == now.day:
        today_birthday = True
        bday_plushes[row.nm] =  row

bday_wishes = []
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_birthday:
    for name in bday_plushes:
        pick_me = random.choice(range(1,4))
        file_name = "letter_templates/letter_" + str(pick_me) + ".txt"
        with open(file_name, "r") as f:
            letter = f.read()
            new_letter = letter.replace("[NAME]", name )
            bday_wishes.append( {"name": name, "email":bday_plushes[name]["email"], "msg": new_letter})


# 4. Send the letter generated in step 3 to that person's email address.
if len(bday_wishes) > 0 :
    for dic_msg in bday_wishes:
        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=dic_msg["email"],
                msg=f"Subject:Happy Birthday!\n\n{dic_msg['msg']}"
            )



