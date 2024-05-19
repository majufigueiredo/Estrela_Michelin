import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


csv_url = 'https://raw.githubusercontent.com/majufigueiredo/Estrela_Michelin/main/one-star-michelin-restaurants.csv'


df = pd.read_csv(csv_url)


st.write(df.head())

region_count = df['region'].value_counts().reset_index()
region_count.columns = ['region', 'count']


plt.figure(figsize=(10, 6))
plt.bar(region_count['region'], region_count['count'], color='skyblue')
plt.xlabel('Região')
plt.ylabel('Número de Restaurantes Premiados')
plt.title('Número de Restaurantes com Uma Estrela Michelin por Região')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


st.pyplot(plt)


