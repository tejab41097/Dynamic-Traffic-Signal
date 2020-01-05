package com.tejab.sqlserver;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.sql.ResultSet;

public class Register extends AppCompatActivity {

    EditText email,password;
    String eemail,epassword,ip;
    Button b1,b2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ip=getIntent().getStringExtra("key");
        setContentView(R.layout.activity_register);
        email=findViewById(R.id.editText2);
        password=findViewById(R.id.editText3);
        b1=findViewById(R.id.button);
        b2=findViewById(R.id.button2);
    }

    public void register(View view){
        eemail=email.getText().toString();
        epassword=password.getText().toString();
        LoginProcess newuser=new LoginProcess();
        String toastmsg=newuser.check_register(ip,eemail,epassword);
        if(toastmsg.equals("successful")){
            Toast.makeText(getApplicationContext(),"email:-"+eemail+"\tRegistered",Toast.LENGTH_LONG).show();
            Intent i=new Intent(getApplicationContext(),MainActivity.class);
            i.putExtra("key",ip);
            startActivity(i);
        }else{
            Toast.makeText(getApplicationContext(),toastmsg,Toast.LENGTH_LONG).show();
            email.setText("");
            password.setText("");
        }
    }
}
