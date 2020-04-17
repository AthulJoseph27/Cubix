package com.example.cubix2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

public class SPLASH extends AppCompatActivity {
    public static int splash_time_out=2000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);


        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent splash = new Intent(SPLASH.this,MainActivity.class);
                startActivity(splash);
                finish();
            }
        },splash_time_out);
    }
}
