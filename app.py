import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dae615d49e44b62535630d936c59ed0e&language=en-US'.format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similar[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id)) #fetch poster from API

    return recommended_movies, posters

movies_dict = pickle.load(open('Movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similar = pickle.load(open('similar.pkl', 'rb'))

st.title('Movie Recommender System')

items = st.selectbox('You can go through the Movies List below: ', movies['title'].values)

if st.button('Related Movies'):
    st.text('Similar movies you may like...')
    names, posters = recommend(items)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])