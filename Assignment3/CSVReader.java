/*
Grayson Berman
CPSC 408
berma117@mail.chapman.edu
April 16, 2019
1760244
Assignment 3
This file prompts the user to enter a file path
Then it reads in a CSV file from that file path and send the data to my SQL server
Reference website for creating CSV reader: https://www.callicoder.com/java-read-write-csv-file-apache-commons-csv/
*/


import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;

import java.util.Scanner;




//This class is used for reading in CSV files
public class CSVReader {


    private static String fullName;
    private static String firstName;
    private static String lastName;
    private static String gender;
    private static String email;
    private static String phoneNum;
    private static String state;
    private static String city;
    private static String occupation;
    private static String dateOfBirth;
    private static String creditCardNum;
    private static String creditCardSecCode;

    private static Scanner reader = new Scanner(System.in);
    public static String CSV_FILE_PATH;




    public static void main(String[] args) throws IOException {
        System.out.println("Enter file path of CSV file");
        CSV_FILE_PATH = reader.nextLine();
        try (
                Reader reader = Files.newBufferedReader(Paths.get(CSV_FILE_PATH));
                CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT);
        ) {
            for (CSVRecord csvRecord : csvParser) {
                // Accessing Values by Column Index, gets all 11 rows of info.
                fullName = csvRecord.get(0);
                firstName = csvRecord.get(1);
                lastName = csvRecord.get(2);
                gender = csvRecord.get(3);
                email = csvRecord.get(4);
                phoneNum = csvRecord.get(5);
                state = csvRecord.get(6);
                city = csvRecord.get(7);
                occupation = csvRecord.get(8);
                dateOfBirth = csvRecord.get(9);
                creditCardNum = csvRecord.get(10);
                creditCardSecCode = csvRecord.get(11);
            }
        }

    }
}
