import streamlit as st
import pandas as pd
import plotly_express as px



# get the data:

# full_data = pd.read_csv('https://github.com/lzsheppard/Bico_Sound_Map/blob/main/query-result.csv', delimiter='\t')

# Example assuming the file is in the same directory as the notebook
full_data = pd.read_csv('https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/main/06_SoundMap/bicomap.csv')
# full_data = pd.read_csv('Bi-Co Sound Map Locations.csv')
full_data.drop('time', axis=1, inplace=True)

# this is the map, with pins for each row of the dataset
#Used this post for help with tooltip formatting https://stackoverflow.com/questions/65524514/how-can-we-get-tooltips-and-popups-to-show-in-folium
st.header('Bi-Co Sound Survey Computational Essay')
st.markdown('By Logan Griffin, Luke Sheppard, Reed Solomon, and Jade Yu')
st.markdown('Sounds of Silence: A Sound Survey of the Bi-Co During Finals Week')



st.sidebar.write("Filter Data")

    # Get the min and max values for the volume column
min_val = full_data['volume'].min()
max_val = full_data['volume'].max()

# Create a slider for the volume column
volume_range = st.sidebar.slider('Volume Range', min_val, max_val, (min_val, max_val))

# Filter the dataframe based on the selected volume range
if 'filtered_df' not in st.session_state:
    st.session_state.filtered_df = full_data[(full_data['volume'] >= volume_range[0]) & (full_data['volume'] <= volume_range[1])]
else: 
    st.session_state.filtered_df = full_data[(full_data['volume'] >= volume_range[0]) & (full_data['volume'] <= volume_range[1])]

show_data = st.sidebar.checkbox('Show Filtered Data', value=False)
if show_data:
    st.dataframe(st.session_state.filtered_df)

# here is the sidebar button to show the map
show_map = st.sidebar.checkbox('Show Map', value=False)
px.set_mapbox_access_token("pk.eyJ1IjoiZnJlZWRtYW4iLCJhIjoiY2xxZnJndjRmMTBwOTJtcXc1YjFlNjcxdCJ9.ih5e7JGYt6Izae0V5gzyEw")

if show_map:
    fig = px.scatter_mapbox(st.session_state.filtered_df, 
                        lat='longitude', 
                        lon='latitude', 
                        hover_name='location', 
                        hover_data={'distractability':True, 
                                    'rowdiness':True, 
                                    'longitude': False,
                                    'latitude': False,
                                    'link': True},
                        color='location',
                        zoom=13.25,
                        mapbox_style="carto-positron",
                    center = {'lat': 40.015, 'lon' : -75.31})

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)

