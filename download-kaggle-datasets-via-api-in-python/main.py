"""
Store kaggle.json file containing the api key in the following directory:
# ~/.kaggle/kaggle.json
# /home/johnadi/.kaggle/kaggle.json
"""

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()

api.authenticate()

# using this script for downloading movie lens dataset for pyspark recommender system project by @data-science-for-everyone
kaggle.api.dataset_download_files('groushubhammehta21/movie-lens-small-latest-dataset', path='~/Desktop/projects/projects-from-yt-channel-data-science-for-everyone/pyspark-projects/recommender-system-using-movie-lens-dataset', unzip=True)

