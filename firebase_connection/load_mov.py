import pandas as pd
import json
def get_index(a):
    a=list(a)
    index=[]

    for i in range(len(a)):
        if a[i]=='1':
            index.append(i)

    return index


def init_Load_mov(a):
    str_to_genre={0:'none',1:'horror',2:'action',3:'adventure',4:'fantasy',\
                 5:'thriller',6:'comedy',7:'crime',8:'science fiction'}
    index=get_index(a)
    counter=[]
    mov_list=[]
    id_list=[]
    for i in index:
        counter.append(0)


    book=pd.read_csv('data50.csv')
    gen_final=[]
    for i in range(len(book)-1):
        mov_name=book['title'][i]
        gen=json.loads(book['genres'][i])
        mov_id=book['id'][i]
        #title=json.loads(book['title'][i])

        gen_list=[]
        
        for j in gen:
            gen_list.append(j['name'].lower())
            #print(j['name'].lower())
            
        #print(gen_list)
        c=0
        for i in range(len(index)):
            
            if(str_to_genre[index[i]] in gen_list):
                
                if(counter[i]<=4):
                    c=1
                    counter[i]=counter[i]+1
            if c==1:                                             #movie is already added in some other genre
                break
                
                #print "yes "
                #print str_to_genre[index[i]]
        
        if c==1:
            mov_list.append(mov_name)
            id_list.append(mov_id)
            gen_final.append(gen_list)
            #print mov_name,mov_id,gen_list
        if(len(mov_list)>10):
            break
    return mov_list,id_list,gen_final
    #print index



def convert_to_json(id_list,gen_final):
    book=pd.read_csv('data50.csv')
    final_data=[]
    gen_final2=[]
    for i in gen_final:
        c=""
        for count,j in enumerate(i):
#            j=j.encode("ascii")
            c=c+j
            if(count!=len(i)-1):
                c=c+ " | "
        gen_final2.append(c)        
    
    c=0
    for i in range(len(book)-1):
        dic={}
        for j in id_list:
            if j==book['id'][i]:
                dic['card_id']=str(j)
                dic['genre']=gen_final2[c]
                dic['name']=book['title'][i]
                dic['photo_id']=book['photo_id'][i]
                dic['url']=book['homepage'][i]
                c=c+1
        if dic:
            final_data.append(dic)        

        final_dic={}
        final_dic['Data']=final_data
        #final_dic=json.dumps(final_dic)
    return final_dic 

    
    
    
    
    
#mov_list,id_list,gen_final=init_Load_mov()      # pass likes string into init_Load_mov
##print len(mov_list)
##print("final list")
##print(mov_list,id_list,gen_final)
#a=convert_to_json(id_list,gen_final)
#with open('dataaaa.json','w') as outfile:
#    json.dump(a,outfile)
    
