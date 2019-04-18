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

#Create faker
faker = Faker()

#2d array. Stores array of data in each index. Index is managed using the count variable
tempArray = []


filename = raw_input("Please enter the filename you would like, not including the .csv extension")
#appends .csv to filename
csvFileName = filename + '.csv'

#gets tuple quantity, converts to int for the while loop
tupleQuantity = raw_input("Please enter the number of tuples you would like to generate")
tupleQuantity = int(tupleQuantity, 10) #converts the input to an integer base 10


count = -1
while count < tupleQuantity:
    count += 1
    if count%2 == 1:
        firstName = faker.first_name_male()
        gender = 'male'
    elif count%2 == 0:
        firstName = faker.first_name_female()
        gender = 'female'
    else:
        firstName = faker.first_name_male()
        gender = 'male'
    lastName = faker.last_name()
    fullName = firstName + ' ' + lastName
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
    tempArray.insert(count, [fullName, firstName, lastName, gender, email, phoneNum, state, city, occupation, dateOfBirth, creditCardNum, creditCardSecCode])

#You can use this for loop to print the contents of the array to see what was generated
#i = 0
#for i in tempArray:
#   print(i)

#dataframe used to output as a csv file
my_dataframe = pd.DataFrame(tempArray)
my_dataframe.to_csv(csvFileName, index = False, header = False)
