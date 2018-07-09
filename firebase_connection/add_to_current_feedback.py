# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:54:17 2018

@author: Sikandar Kumar
"""

import pyrebase
import json
import load_mov
from load_mov import init_Load_mov
from load_mov import convert_to_json
import pandas as pd 


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


#how the json file in the current feedback
data = json.load(open('data2.json')) 
def add_feedback(key):
		db.child("CurrentFeedback")
		db.child(key).set(data)


    
def stream_handler1(post):
    if post['path'] == '/':
        pass
    else:
        k=post['path'].strip("/")
        if k+'/name':
            add_feedback(k)
        print(k)
        print('current_feedback streaming')
        my_stream1.close()



###############################################################################
#get the intrest matrix
def stream_handler2(post):
    if post['path'] == "/":
        pass
    else:
        k=post['path'].strip("/")
        key = k.strip('/Personal_info/Intrest')
        print(key)
        intr = db.child('userdetails').child(key).child('Personal_info').child('Intrest').get().val()
        print(type(intr))
        mov_list,id_list,gen_final=init_Load_mov(intr)      # pass likes string into init_Load_mov
        a=convert_to_json(id_list,gen_final)
        with open('data6.json','w') as outfile:
            json.dump(a,outfile)
            
        









my_stream1 = db.child("Users").stream(stream_handler1,stream_id = "current_feed")
my_stream2 = db.child("userdetails").stream(stream_handler2,stream_id = "intrest_matrix")










