
#Clustering Music Genres

import pandas as pd
import numpy as np
from sklearn import cluster

data = pd.read_csv("Spotify-2000.csv")
print(data.head())


#drop the index column

data = data.drop("Index", axis=1)

print(data.corr())
