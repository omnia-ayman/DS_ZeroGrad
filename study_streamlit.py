#import important libraries needed
import streamlit as st
import pandas as pd
import numpy as np

#study widgets before sidebar
#sidebar: option in side .. all inputs in widgits below any thing but in side bar
st.sidebar.checkbox('click checkbox')
st.sidebar.button('click button')
st.sidebar.radio('pick an audio' , ['male' , 'female'])
st.sidebar.title("main title")
st.sidebar.header("header")
st.sidebar.subheader('subheader')
st.sidebar.markdown("markdown")


#streamlit widgets text , media(photos , videos)
st.title("main title")
st.header("header")
st.subheader('subheader')
st.markdown("markdown")
st.caption('caption')
st.code('code')
st.latex('latex')
st.image("data:image/png;base64,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")
st.video('https://youtu.be/MgLlEMteQqg?si=awRe7fObrS-Pn_qa')
#markdown have styling such as: * ** ## ### ~~ 
#study styling of media

#assign next input widgites in variables to be used then 
#streamlit input buttons, selectors..
st.checkbox('click checkbox')
st.button('click button')
st.radio('pick an audio' , ['male' , 'female'])
st.slider('pick a number' , 0  , 100 )
st.select_slider('pick a word' , ['good' , 'verygood' , 'excellent' ])
st.selectbox ('interested in computer science' , ['yes' , 'no'])
st.multiselect('choose three fields u r interested in' , ['AI' , 'DATA SCIENCE' , 'DATA ANALYSIS' , 'CYBER SECURITY' , 'CLOUD' , 'IT' , 'WEB' , 'APP'])


#streamlit input number, files
st.number_input('pick a number' , 0 , 50)
st.text_input('input the text')
st.text_area('write a brief about you in this text area')
st.date_input('input you birthday date')
st.time_input('input time')
st.file_uploader('upload a file')
st.color_picker('choose your favourite color')

#display progress
import time
#it shows the percent of completion
st.progress(10)
#text shown with the spinner
with st.spinner('wait for the spinner'):
    time.sleep(3)
    st.balloons()

#status with coloring : make state or color the header
st.success("success")
st.warning("warning")
st.error("error")
st.info("some info")
st.exception(RuntimeError("this is run time error"))

#matplotlib and plotly for visualization
#make the same lines for plotly just add the next line
#st.plotly_chart(chart) 

#multible pages
#make a folder, in this folder create the all pages you need and it will connect with each other cause it"s the same directory
#run the main page and you will find the other pages in the sidebar

# make a head title of the file
st.title('Uber pickups in NYC')

#reading the data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# write @st.cache to make the file does not load the data again every time it's opened
@st.cache

#print the data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#preparing the text
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(1000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

#the head title of the dataframe
#st.subheader('Raw data')
#show the data
#st.write(data)

# checkbox if the user wants to show the data or not
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#the head title of the visualization
st.subheader('Number of pickups by hour')
#making a histogram of a specific column
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#draw the histogram
st.bar_chart(hist_values)

#the head title of the map
st.subheader('Map of all pickups')
#draing the map
st.map(data)


hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

#making a slider
hour_to_filter = st.slider('hour', 0, 23, 17) 
st.map(hour_to_filter)

