package com.example.calc;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import org.mozilla.javascript.Context;
import org.mozilla.javascript.Scriptable;

public class MainActivity extends AppCompatActivity {
Button btn,equal,ac,c;
TextView in,out;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            equal=findViewById(R.id.btn_equal);
            in = findViewById(R.id.in);
            out = findViewById(R.id.out);
            ac = findViewById(R.id.btn_allClear);
            c=findViewById(R.id.btn_clear);
            btn=findViewById(R.id.btn_2);
            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    getValue(v);
                }
            });

            equal.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    String data =in.getText().toString();
                    Context context= Context.enter();
                    context.setOptimizationLevel(-1);
                    Scriptable scriptable=context.initSafeStandardObjects();

                    String result=context.evaluateString(scriptable,data,"JavaScript",1,null).toString();

                    out.setText(result);
                }
            });
            ac.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    in.setText(" ");
                    out.setText(" ");
                }
            });
            c.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    String data=in.getText().toString();
                    in.setText(data.substring(0,data.length()-1));
                }
            });
            return insets;
        });
    }
    public void getValue(View v)
    {
        Button btn = (Button)v;
        in.setText(in.getText().toString()+btn.getText().toString());
    }
}