import json
import pandas as pd
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
        rec_list=ok.machine(i)
        number=num[rating[counter]]
        for j in range(number):
            final_list.append(rec_list[j])

    print(final_list)
    return final_list

def convert_to_json2(name_list):
    book=pd.read_csv('tmdb_5000_movies.csv')
    final_data=[]
    #print '2'
##    for i in gen_final:
##        c=""
##        for count,j in enumerate(i):
##            j=j.encode("ascii")
##            c=c+j
##            if(count!=len(i)-1):
##                c=c+ " | "
##        gen_final2.append(c)        
##    
    
    for i in range(len(book)):
        dic={}
        gen=[]
        for j in name_list:
            if j==book['title'][i]:
                dic['card_id']=str(book['id'][i])
                dic['name']=book['title'][i]
                dic['photo_id']=book['photo_id'][i]
                
                dic['url']="http://www.google.com/"
                
                    
                #dic['url']=book['homepage'][i]
                dic['genre']='NAN'
##                k=json.loads(book['genres'][i])
##                print "k= {0}".format(k)
                
##                for i in k:
##                    i['name']=i['name'].encode('ascii')
##                    print i['name']
##                    gen.append(i['name'])
##                print '3'
##
##                print gen
##            c=""
##            print '4'
##            #print 'c={0}'.format(c)
##            for counter,j in enumerate(gen):
##                j=j.encode("ascii")
##                c=c+j
##                print '4.1'
##                if(counter!=len(gen)-1):
##                    c=c+' | '
##                print '4.2'
##                print 'c= {0}'.format(c)
##                print counter,j
##        print c
##        print '5'
##        if(c!=''):
##            dic['genre']=c
##        #dic['genre']=c
##        print dic
                
        if dic:
            final_data.append(dic)        

        final_dic={}
        final_dic['Data']=final_data
        #final_dic=json.dumps(final_dic)
    return final_dic 
            
                

            



    
    
##name=[]
##rating=[]
##f(name,rating)
        
#    
#
#a=['Spider-Man 3','The Chronicles of Narnia: Prince Caspian','Robin Hood','The Golden Compass','Alice in Wonderland'] #recommendations
#k=convert_to_json2(a)
#print (k)
#with open('reclist.json','w') as outfile:
#    json.dump(k,outfile)    
