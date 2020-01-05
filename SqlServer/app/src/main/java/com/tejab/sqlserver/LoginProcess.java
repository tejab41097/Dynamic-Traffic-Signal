package com.tejab.sqlserver;
import android.widget.Toast;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class LoginProcess {
    Connection connect;
    String ConnectionResult = "";

    public String login_check(String ip,String eemail,String epassword) {
        String email,password;
        ConnectionResult="Check Email or password!!";
        try
        {
            ConnectClass conStr=new ConnectClass();
            connect =conStr.connections(ip);
            if(connect==null)
            {
                ConnectionResult = "Check Your Internet Access!";
            }
            else
            {
                String query = "select * from auth_table where email='"+eemail+"' and password='"+epassword+"';";
                Statement stmt = connect.createStatement();
                ResultSet rs = stmt.executeQuery(query);
                while (rs.next()){
                    email= rs.getString("email");
                    password=rs.getString("password");
                    if(email.equals(eemail) && epassword.equals(password)){
                        ConnectionResult="successful";
                        break;
                    }
                }
                connect.close();
            }
        }
        catch (Exception ex)
        {
            ConnectionResult = ex.getMessage();
        }
        return ConnectionResult;
    }

    public String check_register(String ip,String eemail,String epassword){
        if (eemail.equals("")||epassword.equals("")) {
            ConnectionResult = "Please enter valid id & password!!";
        }
        else
        {
        try {
            ConnectClass conStr = new ConnectClass();
            connect = conStr.connections(ip);

                if (connect == null) {
                    ConnectionResult = "Check Your Internet Access!";
                } else {
                    if (Not_already_exist(eemail)) {
                        String query = "insert into auth_table(email,password) values ('" + eemail + "','" + epassword + "');";
                        Statement stmt = connect.createStatement();
                        stmt.executeUpdate(query);
                        ConnectionResult = "successful";
                        connect.close();
                    } else {
                        ConnectionResult = "Id already exist!! please use another id!!";
                    }
                }
            }
        catch(Exception ex)
            {
                ConnectionResult = ex.getMessage();
            }
        }
        return ConnectionResult;
    }

    public boolean Not_already_exist(String eemail) throws SQLException {
        String query="select * from auth_table where email='"+eemail+"';";
        Statement stmt=connect.createStatement();
        ResultSet rs=stmt.executeQuery(query);
        if (!rs.next()){
            return true;
        }else
            return false;
    }
    }
