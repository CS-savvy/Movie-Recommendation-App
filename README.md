# Movie-Recommendation-System
It is a movie recommender App which recommends you movie according to your interest and ratings,  I used Content and popularity based filtering which generates movie recommendation using Machine Learning python script running in cloud pushing all  the processed results to the user mobile application.

## Recommender Engine
___
### Basic functioning of the engine 
 order to build the recommendation engine, I will basically proceed in two steps:
- 1/ determine $N$ films with a content similar to the entry provided by the user
- 2/ select the 5 most popular films among these $N$ films

#### Similarity
When builing the engine, the first step thus consists in defining a criteria that would tell us how close two films are. To do so, I start from the description of the film that was selected by the user: from it, I get the director name, the names of the actors and a few keywords. I then build a matrix where each row corresponds to a film of the database and where the columns correspond to the previous quantities (director + actors + keywords) plus the *k* genres.


|  movie title |director   |actor 1   |actor 2   |actor 3   | keyword 1  | keyword 2   | genre 1 | genre 2 | ... | genre k |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|Film 1   | $a_{11}$  |  $a_{12}$ |   |   |  ... |   |   |   |   | $a_{1q}$  |
|...   |   |   |   |   | ...  |   |   |   |   |   |
|Film i   |  $a_{i1}$ | $a_{i2}$ |   |   | $a_{ij}$  |   |   |   |   |  $a_{iq}$ |
|...   |   |   |   |   | ...  |   |   |   |   |   |
| Film p   |$a_{p1}$   | $a_{p2}$  |   |   | ...  |   |   |   |   | $a_{pq}$  |


In this matrix, the $a_{ij}$ coefficients take either the value 0 or 1 depending on the correspondance between the significance of column $j$ and the content of film $i$. For exemple, if "keyword 1" is in film $i$, we will have $a_{ij}$ = 1 and 0 otherwise. Once this matrix has been defined, we determine the distance between two films according to:

\begin{eqnarray}
d_{m, n} = \sqrt{  \sum_{i = 1}^{N} \left( a_{m,i}  - a_{n,i} \right)^2  } 
\end{eqnarray}

At this stage, we just have to select the N films which are the closest from the entry selected by the user.

#### Popularity

According to similarities between entries, we get a list of $N$ films. At this stage, I select 5 films from this list and, to do so, I give a score for every entry. I decide de compute the score according to 3 criteria:
- the IMDB score
- the number of votes the entry received
- the year of release

The two first criteria will be a direct measure of the popularity of the various entries in IMDB. For the third criterium, I introduce the release year since the database spans films from the early $XX^{th}$ century up to now. I assume that people's favorite films will be most of the time from the same epoch.

Then, I calculate the score according to the formula:

\begin{eqnarray}
\mathrm{score} = IMDB^2 \times \phi_{\sigma_1, c_1} \times  \phi_{\sigma_2, c_2}
\end{eqnarray}

where $\phi$ is a gaussian function:

\begin{eqnarray}
\phi_{\sigma, c}(x) \propto \mathrm{exp}\left(-\frac{(x-c)^2}{2 \, \sigma^2}\right)
\end{eqnarray}

For votes, I get the maximum number of votes among the $N$ films and I set $\sigma_1 = c_1 = m$. For years, I put $\sigma_1 = 20$ and I center the gaussian on the title year of the film selected by the user. With the gaussians, I put more weight to the entries with a large number of votes and to the films whose release year is close to the title selected by the user.
