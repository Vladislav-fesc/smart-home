package com.example.smarthome;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity1 extends AppCompatActivity {
    Button zal , spal1,spal2,spal3,kit,kor,bath;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main1);
        zal = findViewById(R.id.button);
        zal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent = new Intent(MainActivity1.this, MainActivity2.class);
                startActivity(mainIntent);
                finish();
            }
        });
        kit = findViewById(R.id.button3);
        kit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent1 = new Intent(MainActivity1.this, MainActivity3.class);
                startActivity(mainIntent1);
                finish();
            }
        });
        kor = findViewById(R.id.button2);
        kor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent2 = new Intent(MainActivity1.this, MainActivity4.class);
                startActivity(mainIntent2);
                finish();
            }
        });
        bath = findViewById(R.id.button4);
        bath.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent3 = new Intent(MainActivity1.this, MainActivity5.class);
                startActivity(mainIntent3);
                finish();
            }
        });
        spal1 = findViewById(R.id.button5);
        spal1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent4 = new Intent(MainActivity1.this, MainActivity6.class);
                startActivity(mainIntent4);
                finish();
            }
        });
        spal2 = findViewById(R.id.button7);
        spal2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent5 = new Intent(MainActivity1.this, MainActivity7.class);
                startActivity(mainIntent5);
                finish();
            }
        });
        spal3 = findViewById(R.id.button8);
        spal3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mainIntent6 = new Intent(MainActivity1.this, MainActivity8.class);
                startActivity(mainIntent6);
                finish();
            }
        });
    }
}