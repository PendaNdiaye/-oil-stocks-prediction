from matplotlib import colors
import streamlit as st
import bot.bot as bot 
import pandas as pd
from model.format_df import format_data
from PIL import Image
image = Image.open('image.jpeg')

st.title('Bitcoin Trading App Based on NLP')
st.image(image, caption='Sunrise by the mountains', width=600)
def get_data(pages):
    headers_data = bot.HeadersData()
    daily_news = headers_data.current_scraper()
    yesterday_news = headers_data.back_scraper(1, pages)
    return yesterday_news + daily_news


################################################################################
st.header('Summary')
st.markdown(
    '''The **data used for the analysis** is retrieved via the **investing.com** website.
It is a site that provides news on the **world financial news** through the publication of articles
from financial media such as Bloomberg, Financial time etc.
The objective of the analysis is to develop an **algorithm capable of measuring 
the influence of news on the price of bitcoin**. The data sources are heterogeneous.
First, we retrieve the historical data (price of the cryptocurrency at the opening, closing etc.)
and then the headlines of the news. We compare the value of the price from the opening to the closing
and we deduce a score (the simplest, here the relative variation of the price over the day). 
**This score is then used as a label for a classification model** (ascending or descending value) based on the NLP
'''
)
################################################################################
st.header('News')

pages = st.sidebar.slider(
    'Select the number of pages you want to scrape', 1, 10)

col1, col2 = st.columns(2)
with col1:
    st.markdown('**Publication Date**')
with col2:
    st.markdown('**News header**')


data = get_data(pages=pages)

max_screen = 5
current_screen = 0
for info in data:
    current_screen += 1
    date = info.get('public_date')
    news = info.get('new_header')
    with col1:
        date = date #+ '#' * (len(news) - len(date)) 
        st.text(date)
    with col2:
        st.text(news)
    if current_screen == max_screen:
        break
st.text('...')

st.markdown('**Aggregate news to a daily base**')

df = pd.DataFrame(data)
format_df = format_data(df)
st.dataframe(format_df, 1000, 1000)

dates = list(format_df.index)
# models
from model.model import predict
preds = predict(data)
#preds = list(preds)

################################################################################
st.header('Past Market Trends')
st.markdown('The market trends based on the last past 90 days for the training data')
import numpy as np
from model.settings import *
history = pd.read_csv(HISTORY_PATH)
cols = ["Dernier", "Ouv."]
for col in cols:
    history[col] = history[col].apply(lambda s: s.split(',')[0])
history[cols] = history[cols].astype("float")
cols = cols + ["Date"]
history = history[cols]
history = history.set_index('Date')
index_h = history.index
import matplotlib.pyplot as plt
plt.style.use('dark_background')
fig, ax = plt.subplots()

color_dict = {'Dernier': 'red', 'Ouv.': 'blue'}
history.plot(ax=ax, figsize=(10, 4), color=[color_dict.get(x, 'yellow') for x in history.columns])

st.pyplot(fig)

history["label"] = history["Dernier"] - history["Ouv."]
vals = history.label.values
percentage = (vals[1:] - vals[:-1])/ vals[:-1]
percentage = [int(per) for per in percentage]
chart_data = pd.DataFrame(percentage, columns=['variation'])
chart_data.index = index_h[1:]
#st.bar_chart(chart_data)
fig, ax = plt.subplots()

chart_data.plot(ax=ax, kind='bar', figsize=(12, 6), stacked=True, color=['red','blue'])
st.pyplot(fig)

################################################################################
st.header('Predictions')

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('**Date**')
with col2:
    st.markdown('**Model Predictions**')


i = 0
for date, pred in zip(dates, preds):
    with col1:
        st.text(date)
    with col2:
        st.text(pred)
