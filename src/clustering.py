import numpy as np
import pandas as pd
import time

# Dask
import dask.array as da
import dask.dataframe as dd
from dask_ml import preprocessing
from dask_ml.metrics import euclidean_distances
from dask_ml.cluster import KMeans
from dask_ml.cluster import SpectralClustering

# LocalFiles
import features_engineering as fte


def userGenresMatrix(ratings_ddf, genres_dummies):
    # Receives the ratings Dask Dataframe with ratings count per user and genres dummies already added.
    # Returns a matrix with userId and the sum of genres dummies per user.
    g_userid = ratings_ddf.groupby('userId')
    users_genres = g_userid[genres_dummies.columns].sum()
    return users_genres


def dropZeroColumns(ratings_ddf, genres_dummies):
    to_drop = [e for e in ratings.columns if ratings[e].max() == 0]
    genres_dummies = genres_dummies.drop(columns=to_drop)
    return genres_dummies


def main():
    ratings = dd.read_csv(
        '/content/drive/My Drive/movie-recommender-input/ratings.csv')
    ratings = fte.addUserFeatures(ratings_ddf)
    genres_dummies = dd.read_csv(
        '/content/drive/My Drive/movie-recommender-input/genres_dummies.csv')
    fte.addGenresDummies(ratings, genres_dummies)
    users_genres = userGenresMatrix(ratings, genres_dummies)
    # dropZeroColumns(users_genres)


if __name__ == "__main__":
    main()
