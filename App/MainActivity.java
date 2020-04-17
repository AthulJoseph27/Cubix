package com.example.cubix2;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import com.example.cubix2.views.CustomView;

import android.annotation.SuppressLint;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.util.List;
import java.util.Set;
import java.util.UUID;

import static java.lang.System.out;

public class MainActivity extends AppCompatActivity {
    public static final String Scanned_Cube_Face = "         ";
    public static final String Error_Scan = "Faulty Scan";
    public static final int err = 1;
    public static int face_no = 0;
    public static String cb_fc = "", t1;
    String address = null, name = null;
    public static String send_cube[] = new String[7];
    public static int send_cube_counter = 0;
    public static CustomView mCustomview;
    BluetoothAdapter myBluetooth = null;
    BluetoothSocket btSocket = null;
    Set<BluetoothDevice> pairedDevices;
    static final UUID myUUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mCustomview = (CustomView) findViewById(R.id.customView);
        findViewById(R.id.btn_scan).setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {


                        openActivity2();

                    }


                }
        );

        findViewById(R.id.Scan_again).setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        openActivity_2();

                    }
                }
        );
            try {setw();} catch (Exception e) {}
    }
    @SuppressLint("ClickableViewAccessibility")
    private void setw() throws IOException {
        bluetooth_connect_device();

        findViewById(R.id.Submit).setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        for (int i = 0; i < 7; i++)
                            cb_fc = cb_fc + send_cube[i];
                        t1 = "Q"+cb_fc+"Z";
                        senddata(t1);

                    }
                }
        );

    }



    private void bluetooth_connect_device() throws IOException
    {
        try
        {
            myBluetooth = BluetoothAdapter.getDefaultAdapter();
            address = myBluetooth.getAddress();
            pairedDevices = myBluetooth.getBondedDevices();
            if (pairedDevices.size()>0)
            {
                for(BluetoothDevice bt : pairedDevices)
                {
                    address=bt.getAddress().toString();name = bt.getName().toString();
                    Toast.makeText(getApplicationContext(),"Connected", Toast.LENGTH_SHORT).show();

                }
            }

        }
        catch(Exception we){}
        myBluetooth = BluetoothAdapter.getDefaultAdapter();//get the mobile bluetooth device
        BluetoothDevice dispositivo = myBluetooth.getRemoteDevice(address);//connects to the device's address and checks if it's available
        btSocket = dispositivo.createInsecureRfcommSocketToServiceRecord(myUUID);//create a RFCOMM (SPP) connection
        btSocket.connect();

    }
    public void openActivity2()
    {
        Intent intent = new Intent(this,Activity2.class);
        startActivityForResult(intent,1);
        face_no=getIntent().getIntExtra(Activity2.Face_Number,0);
        if(face_no>6)
        {
            face_no=0;
            Button btn_x = (Button) findViewById(R.id.btn_scan);
            btn_x.setEnabled(false);
        }
        else
            send_cube[face_no]=getIntent().getStringExtra(Activity2.Current_Face);



    }

    private void senddata(String i)
    {
        try
        {
            if (btSocket!=null )
            {

                btSocket.getOutputStream().write(i.getBytes());
            }

        }
        catch (Exception e)
        {
            Toast.makeText(getApplicationContext(),e.getMessage(), Toast.LENGTH_SHORT).show();

        }

    }
    public void openActivity_2()
    {
        Intent intent = new Intent(this,Activity2.class);
        intent.putExtra(Error_Scan,err);
        startActivity(intent);

    }

}
