package com.tejab.sqlserver;
import android.annotation.SuppressLint;
import android.os.StrictMode;
import android.util.Log;
import java.sql.Connection;
import java.sql.DriverManager;

public class ConnectClass {
    String db,DBUserNameStr,DBPasswordStr;
    public  Connection DbConn;

    @SuppressLint("NewApi")
    public Connection connections(String ip)
    {
        String port = "1433";
        String username = "sa";
        String password = "1234";
        String db = "Store";
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                .permitAll().build();
        StrictMode.setThreadPolicy(policy);
        try  {
            Class.forName("net.sourceforge.jtds.jdbc.Driver").newInstance();
            DbConn = DriverManager.getConnection("jdbc:jtds:sqlserver://"+ip+":"+port+"/"+db+";user=" + username + ";password=" + password);
            Log.w("Connection","open");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return DbConn;
    }
}
