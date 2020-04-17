package com.example.cubix2.views;
import android.content.Context;
import android.content.Intent;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.view.View;

import androidx.annotation.Nullable;

import com.example.cubix2.MainActivity;

import java.util.jar.Attributes;

public class CustomView extends View
{
    private static final int Square_Size=50;
    private Rect mRectSquare;
    private Paint mPaintSquare;

    private static char cube[][]={{' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
            {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},};


    public CustomView(Context context)
    {
        super(context);

        init(null);
    }

    public CustomView(Context context, AttributeSet attrs)
    {
        super(context, attrs);

        init(attrs);
    }

    public CustomView(Context context, AttributeSet attrs, int defStyleAttr)
    {
        super(context, attrs, defStyleAttr);

        init(attrs);
    }

    public CustomView(Context context, AttributeSet attrs, int defStyleAttr, int defStyleRes)
    {
        super(context, attrs, defStyleAttr, defStyleRes);

        init(attrs);
    }

    private void init(@Nullable AttributeSet set)
    {
        mRectSquare = new Rect();
        mPaintSquare = new Paint(Paint.ANTI_ALIAS_FLAG);
        /*This is done as ,if these are declare in onDraw when we call the function again will cause
        unexpected errors.
        ANTI_ALIAS_FLAG makes the drawn image more pixelated
         */
    }
    public void update_cube(String s , int f )
    {

        if(f==1)
        {
            cube[3][0]=s.charAt(0);
            cube[3][1]=s.charAt(1);
            cube[3][2]=s.charAt(2);

            cube[4][0]=s.charAt(3);
            cube[4][1]=s.charAt(4);
            cube[4][2]=s.charAt(5);

            cube[5][0]=s.charAt(6);
            cube[5][1]=s.charAt(7);
            cube[5][2]=s.charAt(8);
        }
        else if(f==2)
        {
            cube[3][3]=s.charAt(0);
            cube[3][4]=s.charAt(1);
            cube[3][5]=s.charAt(2);

            cube[4][3]=s.charAt(3);
            cube[4][4]=s.charAt(4);
            cube[4][5]=s.charAt(5);

            cube[5][3]=s.charAt(6);
            cube[5][4]=s.charAt(7);
            cube[5][5]=s.charAt(8);
        }
        else if(f==3)
        {
            cube[3][6]=s.charAt(0);
            cube[3][7]=s.charAt(1);
            cube[3][8]=s.charAt(2);

            cube[4][6]=s.charAt(3);
            cube[4][7]=s.charAt(4);
            cube[4][8]=s.charAt(5);

            cube[5][6]=s.charAt(6);
            cube[5][7]=s.charAt(7);
            cube[5][8]=s.charAt(8);
        }
        else if(f==4)
        {
            cube[3][9]=s.charAt(0);
            cube[3][10]=s.charAt(1);
            cube[3][11]=s.charAt(2);

            cube[4][9]=s.charAt(3);
            cube[4][10]=s.charAt(4);
            cube[4][11]=s.charAt(5);

            cube[5][9]=s.charAt(6);
            cube[5][10]=s.charAt(7);
            cube[5][11]=s.charAt(8);
        }
        else if(f==5)
        {
            cube[0][3]=s.charAt(0);
            cube[0][4]=s.charAt(1);
            cube[0][5]=s.charAt(2);

            cube[1][3]=s.charAt(3);
            cube[1][4]=s.charAt(4);
            cube[1][5]=s.charAt(5);

            cube[2][3]=s.charAt(6);
            cube[2][4]=s.charAt(7);
            cube[2][5]=s.charAt(8);
        }
        else if(f==6)
        {
            cube[6][3]=s.charAt(0);
            cube[6][4]=s.charAt(1);
            cube[6][5]=s.charAt(2);

            cube[7][3]=s.charAt(3);
            cube[7][4]=s.charAt(4);
            cube[7][5]=s.charAt(5);

            cube[8][3]=s.charAt(6);
            cube[8][4]=s.charAt(7);
            cube[8][5]=s.charAt(8);
        }



        postInvalidate();
    }
    @Override
    protected void onDraw(Canvas canvas) {
        int i, j;
        mRectSquare.left = 0;
        mRectSquare.top = 0;
        mRectSquare.right = 50;
        mRectSquare.bottom = 50;

        System.out.println(cube[2][3]);


        for (i = 0; i <=8; i++) {
            for (j = 0; j <=11; j++) {
                if (cube[i][j] == ' ') {

                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'R') {
                    mPaintSquare.setColor(Color.RED);
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'B') {
                    mPaintSquare.setColor(Color.rgb(65, 185, 225));
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'W') {
                    mPaintSquare.setColor(Color.WHITE);
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'Y') {
                    mPaintSquare.setColor(Color.YELLOW);
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'O') {
                    mPaintSquare.setColor(Color.rgb(255, 165, 0));
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
                if (cube[i][j] == 'G') {
                    mPaintSquare.setColor(Color.GREEN);
                    canvas.drawRect(mRectSquare, mPaintSquare);
                    mRectSquare.left = mRectSquare.left + Square_Size + 5;
                    mRectSquare.right = mRectSquare.right + Square_Size + 5;

                }
            }
            mRectSquare.top = mRectSquare.top + Square_Size + 5;
            mRectSquare.bottom = Square_Size + mRectSquare.bottom + 5;
            mRectSquare.left = 0;
            mRectSquare.right = 50;
        }
    }

}
