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
# Displaying the collected information
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
with open("user_info.txt", "w") as file:
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
print("Your information has been saved to 'user_info.txt'.")
# End of the main file for the database app
# Note: This code is a simple console application and does not include error handling or validation.
# For a production application, consider adding error handling, input validation, and security measures.




