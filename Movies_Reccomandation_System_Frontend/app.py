import pandas as pd
import streamlit as st
import pickle

# Load preprocessed data
movies = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommend function (names only)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title("🎬 Simple Movie Recommender")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("You might also like:")
    for name in recommendations:
        st.write(f"👉 {name}")
