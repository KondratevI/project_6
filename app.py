import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header('Number of cylinders and relation between condition of a car and its price')
st.write('Number of cylinders')
histogram_cylinders = px.histogram(df, x="cylinders")
st.plotly_chart(histogram_cylinders, use_container_width=False)

st.write('Relation between condition of a car and its price')
cheap_cars = st.checkbox('Only cars cheaper than 100,000')
if cheap_cars:
    scatterplot = px.scatter(df, x="price", y="condition", color="cylinders", size="price")
    scatterplot.update_xaxes(range=[0, 100000])
    st.plotly_chart(scatterplot, use_container_width=False)
else:
    scatterplot = px.scatter(df, x="price", y="condition", color="cylinders", size="price")
    st.plotly_chart(scatterplot, use_container_width=False)
