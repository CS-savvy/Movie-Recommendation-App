# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:43:45 2018

@author: Sikandar Kumar
"""

import pyrebase
import json
from pprint import pprint
import movies_recommend
from movies_recommend import funfun
import ml_load2
from ml_load2 import convert_to_json2

config = {
  "apiKey": "AIzaSyCuh5yMtnaUq7nyqLibd9y1eGw0G1fzhUk",
  "authDomain": "treecom-a433e.firebaseapp.com",
  "databaseURL": "https://treecom-a433e.firebaseio.com/",
  "storageBucket": "treecom-a433e.appspot.com",
   "serviceAccount": "treecom-a433e-firebase-adminsdk-2tk10-47eecfbae9.json"
}


#initializing the firebase
firebase = pyrebase.initialize_app(config)

#get the refrence to the database service
db = firebase.database()

#get a refrence to the auth service
auth = firebase.auth()


def delete_ratings_data(key):
    db.child('Feedbacks').child(key).child('Ratings').remove()
    db.child('CurrentFeedback').child(key).child('name').remove()
    
    
def delete_from_json(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        
    for element in list(data):
        data.pop(element)
    
    with open(filename, 'w') as data_file:
        data = json.dump(data, data_file)            

def stream_handler(post):
    if post['path'] == '/':
        pass
    else:
        k=post['path'].strip("/")
        key_list = []
        for i in k:
            if i == '/' :
                break
            else:
                key_list.append(i)
        re = ''.join(key_list)
        data = db.child('Feedbacks').child(re).child('Ratings').get().val()
        print(data)
        
        with open('ratings.json', 'w') as fp:
            json.dump(data, fp)
            
        with open('ratings.json') as data_file:    
            jsondata = json.load(data_file)
            print(type(jsondata))
            pprint(jsondata)
            
            card_id = []
            ratings = []
            for key,value in jsondata.items():
                card_id.append(int(key))
                ratings.append(int(value))
                
        l = len(data)

        if l > 4:
            print("Done")
            li = funfun(card_id,ratings)
            dic1=convert_to_json2(li)
            
            with open('reclist.json','w') as outfile:
                json.dump(dic1,outfile)
                
            delete_ratings_data(re)
            delete_from_json('ratings.json')
            data = json.load(open('reclist.json'))
            db.child("CurrentFeedback")
            db.child(re).child('name').set(data)
        else:
            print("Need more data")
            
            

        
        
        
        
        
        
        
            
my_stream = db.child("Feedbacks").stream(stream_handler)


#my_stream.close()


#==============================================================================
# def delete_ratings_data11(key):
#     data = db.child('Feedbacks').child(key).child('Ratings').get().val()
#     
#     with open('ratings.json') as data_file:
#         ratings_json_data = json.load(data_file)
#         
#     for keyd,valued in data.items():
#         for keyr,valur in ratings_json_data:
#             if keyd == keyr:
#                 db.child('Feedbacks').child(key).child('Ratings').child(keyd).remove()
#==============================================================================
