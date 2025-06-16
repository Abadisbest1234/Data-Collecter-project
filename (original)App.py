# this is the main file for the database app
print("Welcome to my database app!")
print("We will be asking you some questions to get started.")
## Collecting user information
FirstName = input("What is your first name? ")
LastName = input("What is your last name? ")
Age_years = int(input("What year were you born? "))
Age = 2025- Age_years
Email = input("What is your email address? ")
PhoneNumber = input("What is your phone number? ")
if Age < 18:
    student = input("Whats the name of your educatiniol insitution? ")
else:
    schoolorwork = input("What is the name of your school or workplace? ")
roi = input("Are you a citizen of Republic of Ireland? (yes/no)? ")
if roi.lower() == "yes":
    address = input("What is your address? ")
    contanint = "Europe"                          
    country = "Ireland"
    county = input("What is your county? ")
else:
    Eu = input("Are you a citizen of any European Union country? (yes/no)? ")
    if Eu.lower() == "yes":
        address = input("What is your address? ")
        contanint = "Europe"
        country = input("What is your country? ")
        county = input("What is your county? ")
    else:
        address = input("What is your address? ")
        contanint = input("What continent do you live in? ")
        country = input("What is your country? ")
        county = input("What is your county? ")
import uuid
from datetime import datetime
#review the information provided by the user

print("\nThank you for providing your information!")
print(f"First Name: {FirstName}")
print(f"Last Name: {LastName}")
print(f"Age: {Age} years")
print(f"Email: {Email}")
print(f"Phone Number: {PhoneNumber}")
if Age < 18:
    print(f"Educational Institution: {student}")
else:
    print(f"School/Workplace: {schoolorwork}")
print(f"Citizen of Republic of Ireland: {roi}")
print(f"Address: {address}")
print(f"Continent: {contanint}")
print(f"Country: {country}")
print(f"County: {county}")
# Saving the information to a file
with open("user_info.txt", "a") as file:
    file.write(f"User ID: {uuid.uuid4()}\n")
    file.write(f"Date of Entry: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"First Name: {FirstName}\n")
    file.write(f"Last Name: {LastName}\n")
    file.write(f"Age: {Age} years\n")
    file.write(f"Email: {Email}\n")
    file.write(f"Phone Number: {PhoneNumber}\n")
    if Age < 18:
        file.write(f"Educational Institution: {student}\n")
    else:
        file.write(f"School/Workplace: {schoolorwork}\n")
    file.write(f"Citizen of Republic of Ireland: {roi}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Continent: {contanint}\n")
    file.write(f"Country: {country}\n")
    file.write(f"County: {county}\n")
    file.write("------------------\n")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "abadisbest1234@gmail.com"
receiver_email = Email  # The email inputted by the user
password = "jwcy vaek pfom rqlu"  # Use an app password if using Gmail

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Thank you for your submission " + FirstName + " " + LastName + "!"

body = f"Hello {FirstName},\n\nThank you for submitting your information. \n Abad's database app has successfully saved your details.\n\nHere is a summary of the information you provided:\n your user id is {uuid.uuid4()}\nDate of Entry: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nFirst Name: {FirstName}\nLast Name: {LastName}\nAge: {Age} years\nEmail: {Email}\nPhone Number: {PhoneNumber}\n"
message.attach(MIMEText(body, "plain"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
# ...existing code...

print("Your information has been saved to 'user_info.txt' and a confirmation email has been sent to you.")





