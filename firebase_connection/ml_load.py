import pandas as pd
import movies_recommend as mr
def f(card_id,rating):
    book=pd.read_csv('tmdb_5000_movies.csv')
    name=[]
    for i in range(len(book)-1): 
        for j in card_id:
            if j==book['id'][i]:
                name.append(book['title'][i])
    #name=['a','b','c','d','e','f','g','h','i','j']
    #rating=[4,4,4, 4,4,4,4 ,4,4,4]

    num=[0,0,1,2,3]
    tot_mov=0

    for i in rating:
        tot_mov=tot_mov+num[i]
    print(tot_mov)
    while(tot_mov>10):
        for counter,i in enumerate(num):
            #print(i,counter)
            if(i>0):
                num[counter]=num[counter]-1
        tot_mov=0
        for i in rating:
            tot_mov=tot_mov+num[i]
        print(num,tot_mov)
    rec_list=[]
    final_list=[]
    for counter,i in enumerate(name):
        rec_list=whats_my_score(i)
        
        number=num[rating[counter]]
        for j in range(number):
            final_list.append(rec_list[j])

    print(final_list)
    return final_list

#name=[]
#rating=[]
#f(name,rating)