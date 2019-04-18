Grayson Berman
CPSC 408
berma117@mail.chapman.edu
April 16, 2019
1760244
Assignment 3

This assignment required me to make a Database with five tables. 
The five tables are: 
1) Persons (Personid, fullName, firstName, and lastName)
2) ContactInfo (Personid, email, phoneNum)
3) BillingInfo (Personid, creditCardNum, creditCardSecCode)
4) Location (Personid, state, city)
5) ProfileInfo (Personid, occupation, dateOfBirth, gender, state, city)

I made fake data using pycharm. The file is called FakerDataGenerator.py
It allows input to make a file with a .csv extension. It allows input to choose how many tuples to make.
It has these attributes: 
fullName, firstName, lastName, gender, email, phoneNum, state, city, occupation, dateOfBirth, creditCardNum, creditCardSecCode
It prints out to a CSV file. I provided a CSV file in the repo called FakerData.csv

This file is used to generate fake data using Faker. You need to install Faker and pandas using pip in the python console in order to generate and export the data as a CSV
Karl Hickel showed me how faker works and gave me a link to the website https://faker.readthedocs.io/en/master/locales/en_US.html#faker-providers-credit-card
so that I could find functions for Faker.

