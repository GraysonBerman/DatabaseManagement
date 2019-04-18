//Grayson Berman
//CPSC 408
//berma117@mail.chapman.edu
//April 17, 2019
//1760244
//Assignment 3

//This file is used to create a function tto connect to my specific database. 
//You call the getCon() in the main.java file to make the connection.

//Based on the code you did in class

import java.sql.*; //for sql statements

public class DatabaseConnector {


    DatabaseConnector(){
    }

    public java.sql.Connection getCon(){
        Connection con = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            String connectionUrl = "jdbc:mysql://35.185.232.90:3306/dating_db?useSSL=false";
            con = DriverManager.getConnection(connectionUrl, "grayson", "steakandlobster");
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Connection failed");
        }
        System.out.println("Connected");
        return con;
    }

}
