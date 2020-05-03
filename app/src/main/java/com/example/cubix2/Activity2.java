package com.example.cubix2;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Camera;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;
import org.opencv.android.BaseLoaderCallback;
import org.opencv.android.CameraBridgeViewBase;
import org.opencv.android.JavaCameraView;
import org.opencv.android.OpenCVLoader;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

import static com.example.cubix2.MainActivity.Error_Scan;

public class Activity2 extends AppCompatActivity implements CameraBridgeViewBase.CvCameraViewListener2 {
    CameraBridgeViewBase cameraBridgeViewBase;
    BaseLoaderCallback baseLoaderCallback;
    private boolean state=false;
    private StringBuilder cube_face = new StringBuilder();
    public static String Cube_Face = "";
    public String Activate_Submit="ACTIVATE SUBMIT";
    public static final String Current_Face="         ";
    public static  final String Face_Number="Face Number";
    public static int Count_save=0;
    public static int x=0;
    Mat frame;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_2);

        cameraBridgeViewBase = (JavaCameraView) findViewById(R.id.CameraView);
        cameraBridgeViewBase.setVisibility(SurfaceView.VISIBLE);
        cameraBridgeViewBase.setCvCameraViewListener(this);

        baseLoaderCallback = new BaseLoaderCallback(this) {
            @Override
            public void onManagerConnected(int status) {
                super.onManagerConnected(status);
                switch (status) {
                    case BaseLoaderCallback.SUCCESS:
                        cameraBridgeViewBase.enableView();
                        break;
                    default:
                        super.onManagerConnected(status);
                        break;
                }
            }
        };



    }
    public void save(View Button)
    {
        state = true;
        x = getIntent().getIntExtra(Error_Scan,0);
        if(x==0)
            Count_save++;

    }

    @Override
    public void onCameraViewStarted(int width, int height)
    {
        frame = new Mat(height,width, CvType.CV_8UC4);
    }

    @Override
    public void onCameraViewStopped()
    {
        frame.release();
        MainActivity.mCustomview.update_cube(Cube_Face,Count_save);
        Intent intent = new Intent(this, MainActivity.class);
        intent.putExtra(Current_Face,Cube_Face);
        intent.putExtra(Face_Number,Count_save);
        startActivity(intent);
    }

    @Override
    public Mat onCameraFrame(CameraBridgeViewBase.CvCameraViewFrame inputFrame) {
        int i, j, c;
        double[] d;
        double h[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        double s[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        double v[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        double h_avg[] = new double[9];
        double s_avg[] = new double[9];
        double v_avg[] = new double[9];
        cube_face.setLength(0);
        Mat frame1 = new Mat();
//DO NOT FORGET TO CHANGE THE VALUES OF COORDINATES IN THE LOOP***********************************************************************
        frame = inputFrame.rgba();
        Core.rotate(frame,frame,Core.ROTATE_90_CLOCKWISE);
        Imgproc.rectangle(frame,new Point(100,100),new Point(220,220),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(100,250),new Point(220,370),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(100,400),new Point(220,520),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(250,100),new Point(370,220),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(250,250),new Point(370,370),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(250,400),new Point(370,520),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(400,100),new Point(520,220),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(400,250),new Point(520,370),new Scalar(169,169,169),3);
        Imgproc.rectangle(frame,new Point(400,400),new Point(520,520),new Scalar(169,169,169),3);
        if (state)
        {

            c=0;
            state=false;
            Imgproc.cvtColor(frame, frame1, Imgproc.COLOR_RGB2HSV, 3);
            Imgproc.GaussianBlur(frame1, frame1, new Size(3, 3), 0);
          /*

            Scalar lower_blue = new Scalar(91, 130, 133);
            Scalar higher_blue = new Scalar(114, 255, 255);
            Scalar lower_white = new Scalar(0, 0, 153);
            Scalar higher_white = new Scalar(117, 97, 241);
            Scalar lower_red = new Scalar(110, 130, 112);
            Scalar higher_red = new Scalar(179, 255, 255);
            Scalar lower_green = new Scalar(20, 60, 127);
            Scalar higher_green = new Scalar(64, 227, 200);
            Scalar lower_yellow = new Scalar(20, 61, 153);
            Scalar higher_yellow = new Scalar(46, 255, 255);
            Scalar lower_orange = new Scalar(0, 115, 163);
            Scalar higher_orange = new Scalar(18, 255, 255);

          */
            for (i = 103; i < 217; i++)
                for (j = 103; j < 217; j++)
                {
                    d = frame1.get(i, j);
                    h[0] = h[0] + d[0];
                    s[0] = s[0] + d[1];
                    v[0] = v[0] + d[2];
                    c++;
                }

            for (i = 103; i < 217; i++)
                for (j = 253; j < 367; j++)
                {
                    d = frame1.get(i, j);
                    h[1] = h[1] + d[0];
                    s[1] = s[1] + d[1];
                    v[1] = v[1] + d[2];
                }

            for (i = 103; i < 217; i++)
                for (j = 403; j < 517; j++)
                {
                    d = frame1.get(i, j);
                    h[2] = h[2] + d[0];
                    s[2] = s[2] + d[1];
                    v[2] = v[2] + d[2];
                }

            for (i = 253; i < 367; i++)
                for (j = 103; j < 217; j++)
                {
                    d = frame1.get(i, j);
                    h[3] = h[3] + d[0];
                    s[3] = s[3] + d[1];
                    v[3] = v[3] + d[2];
                }

            for (i = 253; i < 367; i++)
                for (j = 253; j < 367; j++)
                {
                    d = frame1.get(i, j);
                    h[4] = h[4] + d[0];
                    s[4] = s[4] + d[1];
                    v[4] = v[4] + d[2];
                }

            for (i = 253; i < 367; i++)
                for (j = 403; j < 517; j++)
                {
                    d = frame1.get(i, j);
                    h[5] = h[5] + d[0];
                    s[5] = s[5] + d[1];
                    v[5] = v[5] + d[2];
                }

            for (i = 403; i < 517; i++)
                for (j = 103; j < 217; j++)
                {
                    d = frame1.get(i, j);
                    h[6] = h[6] + d[0];
                    s[6] = s[6] + d[1];
                    v[6] = v[6] + d[2];
                }

            for (i = 403; i < 517; i++)
                for (j = 253; j < 367; j++)
                {
                    d = frame1.get(i, j);
                    h[7] = h[7] + d[0];
                    s[7] = s[7] + d[1];
                    v[7] = v[7] + d[2];
                }

            for (i = 403; i < 517; i++)
                for (j = 403; j < 517; j++)
                {
                    d = frame1.get(i, j);
                    h[8] = h[8] + d[0];
                    s[8] = s[8] + d[1];
                    v[8] = v[8] + d[2];
                }

            for (i = 0; i < 9; i++)
            {
                h_avg[i] = h[i] / c;
                s_avg[i] = s[i] / c;
                v_avg[i] = v[i] / c;

            }
            for (i = 0; i < 9; i++)
            {
                if (h_avg[i] > 80 && h_avg[i] < 115 && s_avg[i] > 70 && v_avg[i] > 109)
                    cube_face.append('B');
                else if (h_avg[i] > 110 && h_avg[i] < 179 && s_avg[i] > 130 && s_avg[i] < 255 && v_avg[i] > 112 && v_avg[i] < 255)
                    cube_face.append('R');
                else if (h_avg[i] > 20 && h_avg[i] < 64 && s_avg[i] > 60 && s_avg[i] < 227 && v_avg[i] > 127 && v_avg[i] < 200)
                    cube_face.append('G');
                else if (h_avg[i] > 20 && h_avg[i] < 46 && s_avg[i] > 61 && s_avg[i] < 255 && v_avg[i] > 153 && v_avg[i] < 255)
                    cube_face.append('Y');
                else if (h_avg[i] > 0 && h_avg[i] < 117 && s_avg[i] > 0 && s_avg[i] < 90 && v_avg[i] > 115 && v_avg[i] < 247)
                    cube_face.append('W');
                else if (h_avg[i] > 0 && h_avg[i] < 18 && s_avg[i] > 115 && s_avg[i] < 255 && v_avg[i] > 163 && v_avg[i] < 255)
                    cube_face.append('O');
                else
                    cube_face.append('W');
            }
            Cube_Face = cube_face.toString();
            finish();
        }
        return frame;

    }


    @Override
    protected void onResume()
    {
        super.onResume();

        if (!OpenCVLoader.initDebug())

            Toast.makeText(getApplicationContext(), "There's a problem !", Toast.LENGTH_SHORT).show();
        else

            baseLoaderCallback.onManagerConnected(baseLoaderCallback.SUCCESS);



    }

    @Override
    protected void onPause()
    {
        super.onPause();
        if (cameraBridgeViewBase != null) {

            cameraBridgeViewBase.disableView();
        }
    }





}