package com.pro.treecom;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class BasicQuestions extends AppCompatActivity {
    private Integer count;
    private Button b1;
    private EditText name,age,location;
    private RadioGroup r1;
    private String n , a,l,sex ,strn , counterStr;
    private FirebaseAuth mAuth;
    private DatabaseReference uDatabase , gDatabase , cfDatabase , testDatabase;
    private String user_id;
    private ProgressDialog mProgress;
    private CheckBox c1,c2,c3,c4,c5,c6,c7,c8;
    private StringBuilder Intrest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        mProgress = new ProgressDialog(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_basic_questions);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        b1 =(Button)findViewById(R.id.Register_Btn);
        name = (EditText)findViewById(R.id.input_name);
        age = (EditText)findViewById(R.id.input_age);
        location = (EditText)findViewById(R.id.input_location);
        r1 = (RadioGroup)findViewById(R.id.radio_gender);
        c1 = (CheckBox)findViewById(R.id.Horror);
        c2 = (CheckBox)findViewById(R.id.Action);
        c3 = (CheckBox)findViewById(R.id.Adventure);
        c4 = (CheckBox)findViewById(R.id.Animation);
        c5 = (CheckBox)findViewById(R.id.Thriller);
        c6 = (CheckBox)findViewById(R.id.Comedy);
        c7 = (CheckBox)findViewById(R.id.Crime);
        c8 = (CheckBox)findViewById(R.id.SciFi);

        mAuth = FirebaseAuth.getInstance();
        user_id = mAuth.getCurrentUser().getUid();
        testDatabase = FirebaseDatabase.getInstance().getReference();
        uDatabase = FirebaseDatabase.getInstance().getReference().child("Users");
        gDatabase =  FirebaseDatabase.getInstance().getReference().child("userdetails");
        cfDatabase =  FirebaseDatabase.getInstance().getReference().child("CurrentFeedback");


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
             n = name.getText().toString();
                a = age.getText().toString();
                l = location.getText().toString();
                 int  k = r1.getCheckedRadioButtonId();
                if(k ==  R.id.radio_male)
                {
                    sex = "male";
                }
                else if (k == R.id.radio_female)
                {
                    sex = "Female";
                }
                else{sex = "NA" ;}
                StringBuilder Intrest = new StringBuilder();
                Intrest.append(0);
                if(c1.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c2.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c3.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c4.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c5.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c6.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c7.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                if(c8.isChecked())
                    Intrest.append(1);
                else
                    Intrest.append(0);
                strn = Intrest.toString();
                if(n.isEmpty() || a.isEmpty() || l.isEmpty())
                {
                    Snackbar.make(v, "Please complete details" , Snackbar.LENGTH_LONG)
                            .setAction("Action", null).show();
                }
                else{
                        uploadData();
                }


            }
        });
        FloatingActionButton fab = (FloatingActionButton)findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
    }

    private void uploadData() {
        mProgress.setMessage("Uploading Data");
        mProgress.show();
       // cfDatabase.child(user_id).child("name").child("Data").child("0").child("card_id").setValue("5251242");
       // cfDatabase.child(user_id).child("name").child("Data").child("0").child("genre").setValue("Loading.....");
       // cfDatabase.child(user_id).child("name").child("Data").child("0").child("name").setValue("Loading.....");

        uDatabase.child(user_id).child("Registration").setValue("0");
        gDatabase.child(user_id).child("Personal_info").child("Name").setValue(n);
        gDatabase.child(user_id).child("Personal_info").child("Age").setValue(a);
        gDatabase.child(user_id).child("Personal_info").child("Location").setValue(l);
        gDatabase.child(user_id).child("Personal_info").child("Gender").setValue(sex);
        gDatabase.child(user_id).child("Personal_info").child("Intrest").setValue(strn);

        changeActivity();
    }

    private void changeActivity() {
        mProgress.dismiss();
        startActivity(new Intent(BasicQuestions.this , MainActivity.class));
    }
}
