import streamlit as st
import pickle
import time


col1, col2 = st.columns([1, 10])  
with col1:
    st.image("imdb.png", width=100)
    
    


col1, col2 = st.columns(2)

with col1:
    st.image("camera.jpg", width=350)

with col2:
    st.image("reco.jpg", width=400)


st.write("A movie recommendation system is an application of data science and machine learning that suggests films to users based on their preferences, viewing history, or user behavior. These systems use algorithms " \
"such as content-based filtering, which recommends movies similar to those a user has liked before" \
"By analyzing data such as genre, cast, ratings, and user interactions, movie recommendation systems aim to enhance user experience by providing personalized suggestions, reducing the effort required to find appealing content. " \
"These systems are widely used on streaming platforms like Netflix, Amazon Prime Video, and Hulu.")

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')
movies = pickle.load(open('rec_movie.pkl','rb'))
similarity = pickle.load(open('model.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    with st.spinner("Fetching movies..."):
         time.sleep(2)
    for i in recommended_movie_names:
            st.write(i)
st.write('You can recommend movies to us by adding them to the list')
if st.button('Add Movies'):
    st.text_area('write something')
    st.button('Submit')


