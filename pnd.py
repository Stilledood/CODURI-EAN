import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('Clean_Dataset.csv')
print(dataset.head())
plt.figure(figsize=(20,7))
plt.ylabel("Number of hits")
plt.xlabel("Artist")
dataset['artist_name'].value_counts().plot(kind='bar')
plt.show()
