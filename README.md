# Movie-Recommendation-App
<p align="center">
  <img width="800" height="300" src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/logo.png?raw=true">
</p>
It is a movie recommender App which recommends you movie according to your interest and ratings,  I used Content and popularity based filtering which generates movie recommendation using Machine Learning python script running in cloud pushing all  the processed results to the user mobile application.

## UI sample

|Login|Registration|Recommendations
|------------|-------------|---------------|
| <img src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/LoginScreen.png?raw=true" width="250"> | <img src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/Registration.png?raw=true" width="250"> | <img src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/Recommendations.png?raw=true" width="250">

#### Rating Bar

<img src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/RatingBar.gif?raw=true" width="500">

#### Firebase Database

<img src="https://github.com/CS-savvy/Movie-Recommendation-App/blob/master/DatabaseForApp.png?raw=true" width="500">

## Recommender Engine
___
### Basic functioning of the engine 
 order to build the recommendation engine, I will basically proceed in two steps:
- 1/ determine $N$ films with a content similar to the entry provided by the user
- 2/ select the 5 most popular films among these $N$ films

#### Similarity
When builing the engine, the first step thus consists in defining a criteria that would tell us how close two films are. To do so, I start from the description of the film that was selected by the user: from it, I get the director name, the names of the actors and a few keywords. I then build a matrix where each row corresponds to a film of the database and where the columns correspond to the previous quantities (director + actors + keywords) plus the *k* genres.

In this matrix, the $a_{ij}$ coefficients take either the value 0 or 1 depending on the correspondance between the significance of column $j$ and the content of film $i$. For exemple, if "keyword 1" is in film $i$, we will have $a_{ij}$ = 1 and 0 otherwise. Once this matrix has been defined, we determine the distance between two films according to:

                                     d(m,n) = sqrt( sum( a(m,i) - a(n,i) ) ) 

At this stage, we just have to select the N films which are the closest from the entry selected by the user.

#### Popularity

According to similarities between entries, we get a list of $N$ films. At this stage, I select 5 films from this list and, to do so, I give a score for every entry. I decide de compute the score according to 3 criteria:
- the IMDB score
- the number of votes the entry received
- the year of release

The two first criteria will be a direct measure of the popularity of the various entries in IMDB. For the third criterium, I introduce the release year since the database spans films from the early $XX^{th}$ century up to now. I assume that people's favorite films will be most of the time from the same epoch.

Then, I calculate the score according to the formula:
 score = IMDB^2 * gaussian kernel(vote_count) * gaussian kernel(year of release)

gaussian function:

exp( - (x - mean)/(2*correlaton cofficient))


USE find_similarities(dataframe , index of movie , del_sequels = True, verbose = True)  FUNCTION TO GET YOUR RECOMMENDATIONS.
