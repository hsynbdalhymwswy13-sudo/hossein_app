package com.hossein.gallery;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.GridLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends Activity {

    LinearLayout mainLayout;
    GridLayout photoGrid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mainLayout = new LinearLayout(this);
        mainLayout.setOrientation(LinearLayout.VERTICAL);
        mainLayout.setBackgroundColor(Color.WHITE);

        TextView title = new TextView(this);
        title.setText("🖼️  گالری حسین");
        title.setTextSize(26);
        title.setTextColor(Color.BLACK);
        title.setGravity(Gravity.CENTER);
        title.setPadding(10, 25, 10, 25);

        mainLayout.addView(title);

        LinearLayout menu = new LinearLayout(this);
        menu.setOrientation(LinearLayout.HORIZONTAL);
        menu.setGravity(Gravity.CENTER);

        Button photos = new Button(this);
        photos.setText("📷 تصاویر");

        Button albums = new Button(this);
        albums.setText("📁 آلبوم‌ها");

        Button favorites = new Button(this);
        favorites.setText("❤️ علاقه‌مندی‌ها");

        menu.addView(photos);
        menu.addView(albums);
        menu.addView(favorites);

        mainLayout.addView(menu);

        photoGrid = new GridLayout(this);
        photoGrid.setColumnCount(3);
        photoGrid.setPadding(8, 8, 8, 8);

        mainLayout.addView(photoGrid);

        photos.setOnClickListener(v -> showMessage("تصاویر گوشی"));

        albums.setOnClickListener(v -> showMessage("آلبوم‌ها"));

        favorites.setOnClickListener(v -> showMessage("علاقه‌مندی‌ها"));

        setContentView(mainLayout);
    }

    private void showMessage(String message) {
        TextView text = new TextView(this);
        text.setText(message);
        text.setTextSize(22);
        text.setTextColor(Color.DKGRAY);
        text.setGravity(Gravity.CENTER);
        text.setPadding(10, 40, 10, 40);

        photoGrid.removeAllViews();
        photoGrid.addView(text);
    }
}
