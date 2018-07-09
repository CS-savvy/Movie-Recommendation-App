package com.pro.treecom;

/**
 * Created by Mukul on 2/19/2018.
 */

public class Ybox {

    String card_id;
    String name;
    String photo_id;
    String url;
    String genre ;

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }



    public Ybox() {

    }

    public Ybox(String card_id,String name,String photo_id,String url ,String genre)
    {
        this.card_id = card_id;
        this.name = name;
        this.photo_id = photo_id;
        this.url = url;
        this.genre = genre;
    }

    public Ybox(String name,String photo_id,String url,String genre)
    {
        this.name = name;
        this.photo_id = photo_id;
        this.url = url;
        this.genre = genre;
    }

    public String getCard_id() {
        return card_id;
    }

    public void setCard_id(String card_id) {
        this.card_id = card_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoto_id() {
        return photo_id;
    }

    public void setPhoto_id(String photo_id) {
        this.photo_id = photo_id;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}
