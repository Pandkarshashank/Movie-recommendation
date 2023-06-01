import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(r"D:\assign\dsbda\movie_dataset.csv")
title = df['title']
df = df.select_dtypes(exclude=['object'])
df = df.dropna(axis=1)
df = pd.concat([df, title], axis=1)

X = df[['budget', 'popularity', 'revenue', 'vote_average', 'vote_count']].values
similarity_matrix = cosine_similarity(X, X)

def recommend_movies(movie_index, similarity_matrix, n=5):
    movie_scores = list(enumerate(similarity_matrix[movie_index]))
    movie_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)
    top_movies = movie_scores[1:n+1]  # Exclude the movie itself from recommendations
    return [df.iloc[movie[0]]['title'] for movie in top_movies]
