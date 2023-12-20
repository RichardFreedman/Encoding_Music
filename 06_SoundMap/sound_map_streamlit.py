import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static



# get the data:

dataset = pd.read_csv('https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/main/06_SoundMap/query-result.csv')

# Example assuming the file is in the same directory as the notebook
full_data = pd.read_csv('https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/main/06_SoundMap/bicomap.csv')


# helper function to create popup data
def _makeMessage(df, indx):

    message = "<br><br>Recording information: <br><br> Description: <br>>" + dataset["description"][indx] # Provides description of the sound
    message += "<br> Date Recorded: <br>>" + dataset["date"][indx] # Provides date it was recorded
    message += "<br> Location: " + str(dataset["location"][indx])
    return message

def _makeMessage_2(df, indx):

    
    message = "<br><br>Recording information: <br><br> Description: <br>>" + full_data["Sound"][indx] # Provides description of the sound
    message += "<br> Time Recorded: <br>>" + full_data["Time"][indx] # Provides time of day it was recorded
    message += "<br> Date Recorded: <br>>" + full_data["Date"][indx] # Provides date it was recorded
    message += "<br> Recorded by: <br>>" + full_data["Recorder"][indx] # Provides recorder
    message += "<br> Recorded on: <br>>" + full_data["Device"][indx] # Provides recorded device
    message += "<br><br> Stats: <br><br> Original sound emitted for: "+ full_data["Purpose"][indx] #Purpose
    message += "<br> Volume, from 1-10: " + str(full_data["Volume"][indx])
    message += "<br> Distractability, from 1-10: " + str(full_data["Distractability"][indx])
    message += "<br> Rowdiness, from 1-10: " + str(full_data["Rowdiness"][indx])
    message += "<br> Pitch, from 1-10: " + str(full_data["Pitch"][indx])
    message += "<br> Multiplicity, from 1-10: " + str(full_data["Multiplicity"][indx])
    message += "<br> Repetition, from 1-10: " + str(full_data["Repetition"][indx])
    message += "<br> Persistence, from 1-10: " + str(full_data["Persistence"][indx])
    return message

# this is the map, with pins for each row of the dataset
#Used this post for help with tooltip formatting https://stackoverflow.com/questions/65524514/how-can-we-get-tooltips-and-popups-to-show-in-folium
st.header('This is a header')
st.markdown('This is some introductory text.')



# here is the sidebar button to show the map
show_map = st.sidebar.checkbox('Show Map', value=False)

if show_map:
    m = folium.Map(location=[40.012831, -75.30926273234793], zoom_start=14)
    tooltip = "Click me!"

    for indx in full_data.index:
        lon = full_data["Longitude"][indx]
        lat = full_data["Latitude"][indx]
        marker = folium.Marker(location=[lat, lon], 
                                tooltip=tooltip, 
                                popup=_makeMessage_2(full_data, indx))
        marker.add_to(m)

    folium_static(m)