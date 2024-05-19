import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('/content/one-star-michelin-restaurants.csv')
print(df.head())

region_count = df['region'].value_counts().reset_index()
region_count.columns = ['region', 'count']

plt.figure(figsize=(10, 6))
plt.bar(region_count['region'], region_count['count'], color='skyblue')
plt.xlabel('Região')
plt.ylabel('Número de Restaurantes Premiados')
plt.title('Número de Restaurantes com Uma Estrela Michelin por Região')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
