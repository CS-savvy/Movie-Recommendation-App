package com.pro.treecom;

import android.os.Bundle;
import android.support.annotation.IdRes;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import com.roughike.bottombar.BottomBar;
import com.roughike.bottombar.OnMenuTabClickListener;



public class MainActivity extends AppCompatActivity {


    BottomBar mBottomBar;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mBottomBar = BottomBar.attach(this , savedInstanceState);

        mBottomBar.setItemsFromMenu(R.menu.menu_main, new OnMenuTabClickListener() {
            @Override
            public void onMenuTabSelected(@IdRes int menuItemId) {
                if (menuItemId == R.id.Bottombaritemone)
                {

                    Recom f = new Recom();
                    getSupportFragmentManager().beginTransaction().replace(R.id.frame,f).commit();
                }
                else if (menuItemId == R.id.Bottombaritemtwo)
                {
                    Trending f = new Trending();
                    getSupportFragmentManager().beginTransaction().replace(R.id.frame , f).commit();
                }
                else if (menuItemId == R.id.Bottombaritemthree)
                {
                    Watchlist f = new Watchlist();
                    getSupportFragmentManager().beginTransaction().replace(R.id.frame,f).commit();
                }
                else if (menuItemId == R.id.Bottombaritemfour)
                {
                    profile f = new profile();
                    getSupportFragmentManager().beginTransaction().replace(R.id.frame,f).commit();
                }
            }

            @Override
            public void onMenuTabReSelected(@IdRes int menuItemId) {

            }
        });

        mBottomBar.mapColorForTab(0 , "#2196F3");
        mBottomBar.mapColorForTab(1 , "#168c41");
        mBottomBar.mapColorForTab(2 , "#F44336");
        mBottomBar.mapColorForTab(3 , "#AB47BC");

    }
}