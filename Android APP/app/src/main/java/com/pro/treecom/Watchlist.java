package com.pro.treecom;

import android.content.Context;
import android.net.Uri;
import android.support.annotation.Nullable;
import android.support.customtabs.CustomTabsIntent;
import android.support.v4.app.DialogFragment;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.hsalf.smilerating.BaseRating;
import com.hsalf.smilerating.SmileRating;
import com.squareup.picasso.Picasso;

public class Watchlist extends  android.support.v4.app.Fragment {


    private RecyclerView watch_list;
    private FirebaseAuth mAuth;
    private DatabaseReference mbDatabase , uDatabase, bookmark;
    private String user_id;
    private boolean bookmarking = false;
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.frag_watchlist , container ,false);
        watch_list = (RecyclerView)v.findViewById(R.id.watch_list);
        return v;

    }

    public void onViewCreated(View view ,@Nullable Bundle savedInstanceState){
        super.onViewCreated(view ,savedInstanceState);

        mAuth = FirebaseAuth.getInstance();
        user_id = mAuth.getCurrentUser().getUid();
        mbDatabase = FirebaseDatabase.getInstance().getReference().child("data").child("Data");
        uDatabase = FirebaseDatabase.getInstance().getReference().child("Feedbacks").child(user_id).child("Ratings");
        bookmark = FirebaseDatabase.getInstance().getReference().child("Feedbacks").child(user_id).child("Bookmarks");
        LinearLayoutManager l2 = new LinearLayoutManager(getActivity());
        watch_list.setLayoutManager(l2);


    }

    public void onStart()
    {

        super.onStart();

        FirebaseRecyclerAdapter<Ybox,WatchViewHolder> firebaseRecyclerAdapter = new FirebaseRecyclerAdapter<Ybox, WatchViewHolder>(
                Ybox.class,
                R.layout.card,
                WatchViewHolder.class,
                bookmark
        ) {
            @Override
            protected void populateViewHolder(WatchViewHolder viewHolder, Ybox model, int position) {

                final String card_key = getRef(position).getKey();
                final String card_id = model.getCard_id();
                final String url = model.getUrl();
                final String caption = model.getName();
                final String genre = model.getGenre();
                final String pic = model.getPhoto_id();

                viewHolder.setName(caption);
                viewHolder.setGenre(genre);
                viewHolder.setPic(getContext(),pic);
                viewHolder.seturl(url);
                viewHolder.setCard_id(card_id);
                viewHolder.setSmileyBar(card_id);
                viewHolder.setWatch_Btn(card_key);
                viewHolder.watch_Btn.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        bookmarking = true;
                        bookmark.addValueEventListener(new ValueEventListener() {
                            @Override
                            public void onDataChange(DataSnapshot dataSnapshot) {
                                if(bookmarking)
                                {
                                    if(dataSnapshot.hasChild(card_key))
                                    {
                                        bookmark.child(card_key).removeValue();
                                        bookmarking = false;
                                    }
                                    else
                                    {
                                        bookmark.child(card_key).child("card_id").setValue(card_id);
                                        bookmark.child(card_key).child("genre").setValue(genre);
                                        bookmark.child(card_key).child("name").setValue(caption);
                                        bookmark.child(card_key).child("photo_id").setValue(pic);
                                        bookmark.child(card_key).child("url").setValue(url);
                                        bookmarking = false;
                                    }
                                }

                            }

                            @Override
                            public void onCancelled(DatabaseError databaseError) {

                            }
                        });

                    }
                });

                viewHolder.setOnSmilySelectionListener(new WatchViewHolder.RateListener(){
                    @Override
                    public void onSmileySelected(final int smiley , boolean reselected , final String card_id ){
                        final String str = String.valueOf(smiley);
                        uploadRating(reselected , str ,card_id);
                    }
                });

            }

            public WatchViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
                WatchViewHolder viewHolder = super.onCreateViewHolder(parent, viewType);

                viewHolder.setOnClickListener(new WatchViewHolder.ClickListener() {
                    @Override
                    public void onItemClick(View view, int position , String url) {
                        Toast.makeText(getActivity(), url + position, Toast.LENGTH_SHORT).show();
                        redirectUsingCustomTab(url);
                    }


                });
                return viewHolder;
            }
        };

        watch_list.setAdapter(firebaseRecyclerAdapter);



    }


    private void redirectUsingCustomTab(String url)
    {
        Uri uri = Uri.parse(url);

        CustomTabsIntent.Builder intentBuilder = new CustomTabsIntent.Builder();

        // set desired toolbar colors
        intentBuilder.setToolbarColor(ContextCompat.getColor(getContext(), R.color.colorPrimary));
        intentBuilder.setSecondaryToolbarColor(ContextCompat.getColor(getContext(), R.color.colorPrimaryDark));

        // add start and exit animations if you want(optional)
        intentBuilder.setStartAnimations(getContext(), android.R.anim.slide_in_left, android.R.anim.slide_out_right);
        intentBuilder.setExitAnimations(getContext(), android.R.anim.slide_in_left,
                android.R.anim.slide_out_right);

        CustomTabsIntent customTabsIntent = intentBuilder.build();

        customTabsIntent.launchUrl(getContext(), uri);
    }

    private void uploadRating(boolean reselected  , final String rating ,final String card_id)
    {
        if(!reselected) {
            uDatabase.child(card_id).setValue(rating);

        }


    }



    public static class WatchViewHolder extends RecyclerView.ViewHolder
    {
        View mView;
        FirebaseAuth mAuth;
        public Button watch_Btn;
        DatabaseReference mbDatabase;
        DatabaseReference uDatabase ,bookmark;
        String user_id  ,url,card_id;
        public SmileRating rating;
        public WatchViewHolder(View itemView) {
            super(itemView);
            mView = itemView;
            mAuth = FirebaseAuth.getInstance();
            user_id = mAuth.getCurrentUser().getUid();
            mbDatabase = FirebaseDatabase.getInstance().getReference().child("data").child("Data");
            uDatabase = FirebaseDatabase.getInstance().getReference().child("Feedbacks").child(user_id).child("Ratings");
            bookmark = FirebaseDatabase.getInstance().getReference().child("Feedbacks").child(user_id).child("Bookmarks");

            mbDatabase.keepSynced(true);
            uDatabase.keepSynced(true);
            bookmark.keepSynced(true);

            rating = (SmileRating)mView.findViewById(R.id.smile_rating);
            watch_Btn = (Button)mView.findViewById(R.id.button_watchlist);

            rating.setOnSmileySelectionListener(new SmileRating.OnSmileySelectionListener() {
                @Override
                public void onSmileySelected(int smiley, boolean reselected) {
                    mRateListener.onSmileySelected(smiley,reselected,card_id);
                }
            });







            mView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    mClickListener.onItemClick(v , getAdapterPosition(),url);
                }
            });

        }

        private WatchViewHolder.RateListener mRateListener;

        public interface RateListener{
            public void onSmileySelected(int smiley , boolean reselected, String card_id);
        }

        public void setOnSmilySelectionListener(WatchViewHolder.RateListener rateListener)
        {
            mRateListener = rateListener;
        }




        private WatchViewHolder.ClickListener mClickListener;

        public interface ClickListener{
            public void onItemClick(View view, int position ,String url);
        }

        public void setOnClickListener(WatchViewHolder.ClickListener clickListener){
            mClickListener = clickListener;
        }


        public void setSmileyBar(final String card_id)
        {
            uDatabase.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(DataSnapshot dataSnapshot) {
                    String k;
                    int y;
                    if(dataSnapshot.hasChild(card_id))
                    {
                        k = (String)dataSnapshot.child(card_id).getValue();
                        y = Integer.parseInt(k);
                        switch(y)
                        {
                            case 4:
                                rating.setSelectedSmile(BaseRating.GREAT);
                                break;
                            case 3:
                                rating.setSelectedSmile(BaseRating.GOOD);
                                break;
                            case 2:
                                rating.setSelectedSmile(BaseRating.OKAY);
                                break;
                            case 1:
                                rating.setSelectedSmile(BaseRating.BAD);
                                break;
                            case 0:
                                rating.setSelectedSmile(BaseRating.TERRIBLE);
                                break;
                        }


                    }
                }

                @Override
                public void onCancelled(DatabaseError databaseError) {

                }
            });
        }


        public void setWatch_Btn(final String card_key)
        {
            bookmark.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(DataSnapshot dataSnapshot) {

                    if(dataSnapshot.hasChild(card_key))
                        watch_Btn.setText("Bookmarked");
                    else
                        watch_Btn.setText("Bookmark");
                }

                @Override
                public void onCancelled(DatabaseError databaseError) {

                }
            });
        }
        public void setName(String name)
        {
            TextView c_name = (TextView)mView.findViewById(R.id.card_caption);
            c_name.setText(name);
        }

        public void setGenre(String genre)
        {
            TextView Genre = (TextView)mView.findViewById(R.id.card_genre);
            Genre.setText(genre);
        }


        public void seturl(String url)
        {
            this.url = url;
        }

        public void setCard_id(String id){this.card_id = id;}

        public void setPic(Context ctx , String pic )
        {
            ImageView mpic =(ImageView) mView.findViewById(R.id.card_image);
            Picasso.with(ctx).load(pic).into(mpic);
        }
    }

}
