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

I created a DatabaseConnector class in a java file called DatabaseConnector.java.
It has a default constructor and a function getCon() used to create a connectiton to my specific SQL server using my 
user/pass/ip/port, and includes useSSL=false. useSSL=false was needed because I was receiving an error when
trying to connect without it.
I had to download a mysql-connector-java-5.1.47.zip which had a jar file. I loaded it into my project libraries. 
Some other students didn't have this issue, I think it may have been with the way I set up my project in IntelliJ.

The CSVReader.java file is used to read in data from a CSV file and pass it into the DB on my sql server.
Running the CSVReader.java file allows you to enter a filepath to a CSV file (either one you've generated using my faker file or the one I've provided) and will pass it to my SQL server.
