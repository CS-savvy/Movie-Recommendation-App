#main machine learning code 



import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')
import base64
import io
from scipy.misc import imread
import codecs
from IPython.display import HTML
import ml_load

movies=pd.read_csv('G:\\works\\project\\movie_recommendation\\Dataset\\tmdb_5000_movies.csv')
mov=pd.read_csv('G:\\works\\project\\movie_recommendation\\Dataset\\tmdb_5000_credits.csv')

# changing the genres column from json to string
movies['genres']=movies['genres'].apply(json.loads)
for index,i in zip(movies.index,movies['genres']):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]['name']))# the key 'name' contains the name of the genre
    movies.loc[index,'genres']=str(list1)
    
# changing the keywords column from json to string
movies['keywords']=movies['keywords'].apply(json.loads)
for index,i in zip(movies.index,movies['keywords']):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]['name']))
    movies.loc[index,'keywords']=str(list1)
    
## changing the production_companies column from json to string
movies['production_companies']=movies['production_companies'].apply(json.loads)
for index,i in zip(movies.index,movies['production_companies']):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]['name']))
    movies.loc[index,'production_companies']=str(list1)
    
# changing the production_countries column from json to string    
movies['production_countries']=movies['production_countries'].apply(json.loads)
for index,i in zip(movies.index,movies['production_countries']):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]['name']))
    movies.loc[index,'production_countries']=str(list1)
    
# changing the cast column from json to string
mov['cast']=mov['cast'].apply(json.loads)
for index,i in zip(mov.index,mov['cast']):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]['name']))
    mov.loc[index,'cast']=str(list1)

# changing the crew column from json to string    
mov['crew']=mov['crew'].apply(json.loads)
def director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
mov['crew']=mov['crew'].apply(director)
mov.rename(columns={'crew':'director'},inplace=True)

# merging the two csv files
movies=movies.merge(mov,left_on='id',right_on='movie_id',how='left')

movies=movies[['id','original_title','genres','cast','vote_average','director','keywords']]

#converting to list
movies['genres']=movies['genres'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['genres']=movies['genres'].str.split(',')



for i,j in zip(movies['genres'],movies.index):
    list2=[]
    list2=i
    list2.sort()
    movies.loc[j,'genres']=str(list2)
movies['genres']=movies['genres'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['genres']=movies['genres'].str.split(',')

#generate a genre list
genreList = []
for index, row in movies.iterrows():
    genres = row["genres"]
    
    for genre in genres:
        if genre not in genreList:
            genreList.append(genre)
            


#making the binary lists
def binary(genre_list):
    binaryList = []
    
    for genre in genreList:
        if genre in genre_list:
            binaryList.append(1)
        else:
            binaryList.append(0)
    
    return binaryList

movies['genres_bin'] = movies['genres'].apply(lambda x: binary(x))

movies['genres_bin'].head(4)

movies['cast']=movies['cast'].str.strip('[]').str.replace(' ','').str.replace("'",'').str.replace('"','')
movies['cast']=movies['cast'].str.split(',')



for i,j in zip(movies['cast'],movies.index):
    list2=[]
    list2=i[:4]
    movies.loc[j,'cast']=str(list2)
movies['cast']=movies['cast'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['cast']=movies['cast'].str.split(',')
for i,j in zip(movies['cast'],movies.index):
    list2=[]
    list2=i
    list2.sort()
    movies.loc[j,'cast']=str(list2)
movies['cast']=movies['cast'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['cast']=movies['cast'].str.split(',')


castList = []
for index, row in movies.iterrows():
    cast = row["cast"]
    
    for i in cast:
        if i not in castList:
            castList.append(i)
            
def binary(cast_list):
    binaryList = []
    
    for genre in castList:
        if genre in cast_list:
            binaryList.append(1)
        else:
            binaryList.append(0)
    
    return binaryList

movies['cast_bin'] = movies['cast'].apply(lambda x: binary(x))

movies['cast_bin'].head(2) #binary list for actors in the movie

def xstr(s):
    if s is None:
        return ''
    return str(s)
movies['director']=movies['director'].apply(xstr)

directorList=[]
for i in movies['director']:
    if i not in directorList:
        directorList.append(i)
        
        
def binary(director_list):
    binaryList = []
    
    for direct in directorList:
        if direct in director_list:
            binaryList.append(1)
        else:
            binaryList.append(0)
    
    return binaryList

movies['director_bin'] = movies['director'].apply(lambda x: binary(x))

mask=b'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'


from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords

###extra line 




movies['keywords']=movies['keywords'].str.strip('[]').str.replace(' ','').str.replace("'",'').str.replace('"','')
movies['keywords']=movies['keywords'].str.split(',')
for i,j in zip(movies['keywords'],movies.index):
    list2=[]
    list2=i
    movies.loc[j,'keywords']=str(list2)
movies['keywords']=movies['keywords'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['keywords']=movies['keywords'].str.split(',')
for i,j in zip(movies['keywords'],movies.index):
    list2=[]
    list2=i
    list2.sort()
    movies.loc[j,'keywords']=str(list2)
movies['keywords']=movies['keywords'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['keywords']=movies['keywords'].str.split(',')

words_list = []
for index, row in movies.iterrows():
    genres = row["keywords"]
    
    for genre in genres:
        if genre not in words_list:
            words_list.append(genre)
            
def binary(words):
    binaryList = []
    
    for genre in words_list:
        if genre in words:
            binaryList.append(1)
        else:
            binaryList.append(0)
    
    return binaryList

movies['words_bin'] = movies['keywords'].apply(lambda x: binary(x))

movies=movies[(movies['vote_average']!=0)] #removing the movies with 0 score and without drector names 
movies=movies[movies['director']!='']



#check the similarity between movies
#defined a function Similarity, which will check the similarity between the movies
from scipy import spatial

def Similarity(movieId1, movieId2):
    a = movies.iloc[movieId1]
    b = movies.iloc[movieId2]
    
    genresA = a['genres_bin']
    genresB = b['genres_bin']
    
    genreDistance = spatial.distance.cosine(genresA, genresB)
    
    scoreA = a['cast_bin']
    scoreB = b['cast_bin']
    scoreDistance = spatial.distance.cosine(scoreA, scoreB)
    
    directA = a['director_bin']
    directB = b['director_bin']
    directDistance = spatial.distance.cosine(directA, directB)
    
    wordsA = a['words_bin']
    wordsB = b['words_bin']
    wordsDistance = spatial.distance.cosine(directA, directB)
    return genreDistance + directDistance + scoreDistance + wordsDistance


Similarity(3,160) #lets check similarity between any 2 random movies

new_id=list(range(0,movies.shape[0]))
movies['new_id']=new_id
movies=movies[['original_title','genres','vote_average','genres_bin','cast_bin','new_id','director','director_bin','words_bin']]
movies.head(2)















#predictor


import operator

def whats_my_score(name):
    #name='Batman'
    print('Enter a movie title')
    new_movie=movies[movies['original_title'].str.contains(name)].iloc[0].to_frame().T
    print('Selected Movie: ',new_movie.original_title.values[0])
    def getNeighbors(baseMovie, K):
        distances = []
    
        for index, movie in movies.iterrows():
            if movie['new_id'] != baseMovie['new_id'].values[0]:
                dist = Similarity(baseMovie['new_id'].values[0], movie['new_id'])
                distances.append((movie['new_id'], dist))
    
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
    
        for x in range(K):
            neighbors.append(distances[x])
        return neighbors

    K = 10
    avgRating = 0
    neighbors = getNeighbors(new_movie, K)

    print('\nRecommended Movies: \n')
    rec_mov=[]
    #rec_rating=[]
    for neighbor in neighbors:
        avgRating = avgRating+movies.iloc[neighbor[0]][2]  
        print( movies.iloc[neighbor[0]][0]+" | Genres: "+str(movies.iloc[neighbor[0]][1]).strip('[]').replace(' ','')+" | Rating: "+str(movies.iloc[neighbor[0]][2]))
        #print(movies.iloc[neighbor[0]][0])
        rec_mov.append(movies.iloc[neighbor[0]][0])
        #rec_rating.append(str(movies.iloc[neighbor[0]][2]))
    print('\n')
    avgRating = avgRating/K
    print('The predicted rating for %s is: %f' %(new_movie['original_title'].values[0],avgRating))
    print('The actual rating for %s is %f' %(new_movie['original_title'].values[0],new_movie['vote_average']))
    
    
    print('type of function')
    print(type(new_movie['original_title']))
    print(new_movie.keys())
    print(new_movie['original_title'])
    print(rec_mov)
    return rec_mov




#==============================================================================
# whats_my_score('Batman')
# def ab():
#     print ("hello")
#==============================================================================
def funfun(card_id,rating):
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



def convert_to_json(id_list,gen_final,name_list):
    book=pd.read_csv('data50.csv')
    final_data=[]
    gen_final2=[]
#==============================================================================
#     for i in gen_final:
#         c=""
#         for count,j in enumerate(i):
# #            j=j.encode("ascii")
#             c=c+j
#             if(count!=len(i)-1):
#                 c=c+ " | "
#         gen_final2.append(c)        
#==============================================================================
#    
    c=0
    for i in range(len(book)-1):
        dic={}
        for j in name_list:
            if j==book['name'][i]:
                dic['card_id']=book['card_id'][i]
                
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

    
#name=[]
#rating=[]
#f(name,rating)

    
    





