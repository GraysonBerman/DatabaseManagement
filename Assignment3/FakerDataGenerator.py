#Grayson Berman
#CPSC 408
#berma117@mail.chapman.edu
#April 16, 2019
#1760244
#Assignment 3
#This file is used to generate fake data using Faker. You need to install Faker and pandas
#using pip in the python console in order to generate and export the data as a CSV
#Karl Hickel showed me how faker works and gave me a link to the website https://faker.readthedocs.io/en/master/locales/en_US.html#faker-providers-credit-card
#so that I could find functions for Faker. He also showed me the link below so that I can learn how to output and read the CSV file.
#https://www.callicoder.com/java-read-write-csv-file-apache-commons-csv/
#I intend to use this as a data generator for my final project, so I used variables that would be 'necessary' for a dating website.




from faker import Faker
import pandas as pd


faker = Faker()

#make an array called tablename[] , fill the array values using faker things like name = (fake.name())
#use a loop (while or for) to populate the array with data
#move that array into the correct table
#tablename.insert(count, [arr 0, arr 1])

#2d array. Stores array of data in each index. Index is managed using the count variable
tempArray = []

count = -1
while count < 50:
    count += 1

    firstName = faker.first_name()
    lastName = faker.last_name()
    #emailDomain is used in combination with first/last to generate an email using the same names
    emailDomain = faker.free_email_domain()
    #email concatenates vars to create firstnamelastname@emaildomain
    email = firstName + lastName + '@' + emailDomain
    phoneNum = faker.msisdn()
    state = faker.state()
    city = faker.city()
    occupation = faker.job()
    dateOfBirth = faker.date_of_birth(tzinfo=None, minimum_age = 18, maximum_age = 80)
    creditCardNum = faker.credit_card_number(card_type = None)
    creditCardSecCode = faker.credit_card_security_code(card_type=None)
    tempArray.insert(count, [firstName, lastName, email, phoneNum, state, city, occupation, dateOfBirth, creditCardNum, creditCardSecCode])

#You can use this for loop to print the contents of the array to see what was generated
#i = 0
#for i in tempArray:
#    print(i)

#dataframe used to output as a csv file called FakerData.csv
my_dataframe = pd.DataFrame(tempArray)
my_dataframe.to_csv('FakerData.csv', index = False, header = False)

