

---

# Spotify Functions for the Encoding Music Course
## Table of Contents:
1. [Analyze a Single Playlist](#analyze-a-single-playlist)
2. [Analyze Multiple Playlists](#analyze-multiple-playlists)
3. [Analyze a User's Tracks](#analyze-user-tracks)
4. [Charting Data](#charting-data)

##  <span style="color:olive"> Analyze a Single Playlist </span> <a name="analyze-a-single-playlist"></a>

#### This function is used to get the audio features of a Spotify playlist such as: 
- Artist
- Album
- Track Name
- Track ID
- Danceablility
- Energy
- Key
- Loudness
- Mode
- Speechiness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Durations (in ms)
- Time Signature
#### To use this function, you need the creator username of the playlist and the playlist ID. 
---
#### For example:
![Alt text](images/Spotify_Playlist_Example.png)
Image Source: [“Warm Fuzzy Feeling” Playlist by Spotify from Medium Article](https://miro.medium.com/v2/resize:fit:1400/1*P9nEAoRKqybJ4qiORrN7xA.png)

#### From the image above, we get the following:
```python
creator_id = "spotify"
```
![Alt text](images/Spotify_Playlist_URL.webp)
Image Source: [“Warm Fuzzy Feeling” Playlist URL from Medium Article](https://miro.medium.com/v2/resize:fit:1106/format:webp/1*RARQekRU6bKakcNTIJo4bQ.png)
#### From the image above, we get the following:
```python
playlist_id = "37i9dQZF1DX5IDTimEWoTd"
```
---
#### Now that we know both the creator username and the playlist ID, we can call the  function <span style="color:olive">analyze_playlist</span> to return a dataframe of the analysis of the playlist:

```python
playlist_data_frame = analyze_playlist(creator_id, playlist_id) #Stores the resulting data frame as the variable: playlist_data_frame
playlist_data_frame.head() #Displays the first n rows of the data frame 
```
<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/Spotify_Single_Playlist_Head.png)


</Details>

<Details>
<Summary>Full Code</Summary>

```python
def analyze_playlist(creator, playlist_id):
# source: Max Hilsdorf (https://towardsdatascience.com/how-to-create-large-music-datasets-using-spotipy-40e7242cc6a6)

    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id", 
                             "danceability", "energy", "key", "loudness", "mode", "speechiness",
                             "instrumentalness", "liveness", "valence", "tempo", "duration_ms", "time_signature"]
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    # Create empty dict
    playlist_features = {}
    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df
```
</Details>

---
## <span style="color:olive"> Analyze Multiple Playlists </span> <a name="analyze-multiple-playlists"></a>
#### This function returns the same data frame as the function from above, but allows you to analyze multiple playlists.
---
#### To use this function, you need to create a dictionary of playlists. To do so, see the example code below.
```python
playlist_dict = {
    "PLAYLIST NAME HERE": ("CREATOR_ID HERE", "PLAYLIST_ID HERE")
}
```
```python
playlist_dict = {
    "warm_fuzzy_feeling" : ("spotify", "37i9dQZF1DX5IDTimEWoTd"), 
    #Follow the same format to add more playlists
}
```
---
#### Now that we have created our playlist dictionary, we can call the function <span style="color:olive">analyze_playlist_dict</span> to analyze the audio features of the songs in multiple playlists.
```python
multiple_playlist_data_frame = analyze_playlist_dict(playlist_dict)
multiple_playlist_data_frame.head()
```
<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/Spotify_Multiple_Playlist_Head.png)


</Details>
<Details>
<Summary>Full Code</Summary>

```python
def analyze_playlist_dict(playlist_dict):
    
    # Loop through every playlist in the dict and analyze it
    for i, (key, val) in enumerate(playlist_dict.items()):
        playlist_df = analyze_playlist(*val)
        # Add a playlist column so that we can see which playlist a track belongs too
        playlist_df["playlist"] = key
        # Create or concat df
        if i == 0:
            playlist_dict_df = playlist_df
        else:
            playlist_dict_df = pd.concat([playlist_dict_df, playlist_df], ignore_index = True)
            
    return playlist_dict_df
```
</Details>

---

##  <span style="color:olive"> Analyze All of a User's Tracks </span> <a name="analyze-user-tracks"></a>
#### This function allows you to obtain and analyze all the tracks from a user's followed public playlists.

---

#### To use this function, you need to have the Spotify username of the user you want to analyze the tracks from.
```python
my_username = "spotify"
```

---

#### Now that we have the user's Spotify username, we can call the function <span style="color:olive">get_all_user_tracks</span> to analyze all tracks.

```python
all_user_tracks = get_all_user_tracks(my_username)
all_user_tracks.head()
```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/Spotify_All_User_Tracks_Head.png)


</Details>
<Details>
<Summary>Full Code</Summary>

```python
def get_all_user_tracks(username):
  all_my_playlists = pd.DataFrame(sp.user_playlists(username))
  list_of_dataframes = []

  for playlist in all_my_playlists.index:
    current_playlist = pd.DataFrame(sp.user_playlist_tracks(username, all_my_playlists["items"][playlist]["id"]))
    current_playlist_audio = get_audio_features_df(current_playlist)
    if all_my_playlists["items"][playlist]["name"]:
      current_playlist_audio["playlist_name"] = all_my_playlists["items"][playlist]["name"]
    else:
       current_playlist_audio["playlist_name"] = None
    list_of_dataframes.append(current_playlist_audio)

  return pd.concat(list_of_dataframes)
```
</Details>

## Charting Data
As we now have a collection of data points that represent different feature values for one complete playlist, we should be able to graph our findings using Altair. While there are many available charts, we will start with graphing **one feature's values for every item (track) in the series**. 

### A Scatterplot of a Playlist (based on one audio feature)

To illustrate this concept, we will use **Altair's scatterplot** to chart **each track's tempo**. This could be done by setting the Chart's data source to **audio_features_df**, it's **x** variable to **track_name** and it's **y** variable to **tempo**.

Here's our chart:


```python
alt.Chart(audio_features_df).mark_point().encode(
    x="track_name",
    y='tempo'
)
```


![Alt text](images/spot_5.png)



Note: by default, Altair will sort the tracks alphabetically. If you prefer to keep the original sorting or sort them some particular way, you should toggle the **sort** attribute on the axis of interest. Specifically, we will set up our **x** variable this way: *x=alt.X("track_name", sort=None)* instead of *x="track_name"*. 

You can read more about **Altair's axis sorting** [here](https://altair-viz.github.io/user_guide/generated/channels/altair.X.html). 

### Adding Multiple Variables: Plotting Correlations


While there are many available charts, one useful way to visually illustrate a correlation between two variables (think DataFrame columns) is **constructing a scatterplot using two data ranges**. 

In general, a Scatterplot requires **two variables (data ranges)** that will be mapped according to their corresponding values. For example, consider **"energy"** and **"loudness"**. Our first track (Shaggy: Boombastic) has an "energy" score of 0.538 and a "loudness" score of -16.183, which together make one of the points on the scatterplot: (0.538, -16.183); the second track (Ini Kamoze: Here Comes The Hotstepper) makes up the (0.454, -8.598) datapoint – hopefully, you can see where this is going.

You can read more about Altair's scatterplots [here](https://altair-viz.github.io/gallery/scatter_tooltips.html).

In the example below, we are using **audio_features_df** as the data source, **"energy"** as the x (horizontal variable) and **"loudness"** as the y (vertical variable). Let's take a look at the result:


```python
alt.Chart(audio_features_df).mark_point().encode(
    x='energy',
    y='loudness'
)
```


![Alt text](images/spot_6.png)


As you can see in the example above, "energy" and "loudness" tend to have somewhat of a **corresponding upward trend**: for items with higher "energy", "valence" tends to be higher, too. This, in turn, corresponds to our natural hypothesis: one could normally expect a higher-energy track to be louder. Mathematically, the relationship between these two variables could be described as one having **positive correlation**. 

Learn [more about correlations](https://www.washington.edu/assessment/scanning-scoring/scoring/reports/correlations/).  Also see Edgar Leon's [regressions tutorial](https://github.com/RichardFreedman/Encoding_Music/blob/dev_Edgar/Regressions.md)

Using Pandas' built-in *pandas.Series.corr()* method, it is extremely easy to obtain the **Correlation Coefficient** for the two variables:


```python
audio_features_df['energy'].corr(audio_features_df['loudness'])
```




    0.5252140232410945

### Radar Plots

Radar (or Polar) plots are a useful way to represent multiple variables at once.

Read more about the various features via [Plotly](https://plotly.com/python/radar-chart/) (under scatter plots):

While there is a multitude of aspects to correlation (including test types, sample sizes, strengths, variance, and many other factors), it sometimes can be a useful statistical measure in your Music Data Analysis exploration.

This function is available via the spotipy_tools.py library, so the following is just for purposes of explanation (or if you want to adapt it in some way):


```python
feature_columns = ["danceability", "energy", "speechiness", "liveness", "instrumentalness", "valence", "danceability"]
def createRadarElement(row, feature_cols):
    return go.Scatterpolar(
        r = row[feature_cols].values.tolist(), 
        theta = feature_cols, 
        mode = 'lines', 
        name = row['track_name'])

def get_radar_plot(playlist_id, features_list):
    current_playlist_audio_df = get_audio_features_df(pd.DataFrame(sp.playlist_items(playlist_id)))
    current_data = list(current_playlist_audio_df.apply(createRadarElement, axis=1, args=(features_list, )))  
    fig = go.Figure(current_data, )
    fig.show(renderer='iframe')
    fig.write_image(playlist_id + '.png', width=1200, height=800)
    
def get_radar_plots(playlist_id_list, features_list):
    for item in playlist_id_list:
        get_radar_plot(item, features_list)
```


```python
playlist_id = "1NppEwvZhkjeG3ZTYoOwVM"
get_radar_plot(playlist_id, feature_columns)
```

![Alt text](images/spot_34.png)

### Categorization:  From Continuous to Discrete Variables

To categorize your tracks, you would sometimes need to map their values from a continuous range onto a discrete range. Typically, we call this process **"binning"**. Binning usually involves creating a new column within the existing (or in a new) DataFrame such that the new column's values correspond to the discretely defined categories of the item (based on some threshold value).

Read more about [continuous and discrete variables](https://en.wikipedia.org/wiki/Continuous_or_discrete_variable).

For example, consider **"danceability"** – a continuous variable with values ranging from 0 to 1. In order to **"bin"** our tracks, we will classify everything with a "danceability" score of 0.75 and higher as a dance tune. For this, we'll create a new column – "dance_tune", and if a track's "danceability" score is equal to or above 0.75, its "dance_tune" value should be True; otherwise, it should be set to False.

This can be easily done using Pandas and NumPy's [np.where method](https://numpy.org/doc/stable/reference/generated/numpy.where.html).

Here's how to do it:


```python
feature_based_tracks = audio_features_df.copy() # make a copy of the DataFrame
feature_based_tracks["dance_tune"] = np.where(feature_based_tracks['danceability'] >= 0.75, True, False)
feature_based_tracks.head()
```

![Alt text](images/spot_7.png)

At this point, you should be able to see which tunes are "Dance Tunes" based on our categorization threshold. Excitingly, Altair provides an easy way to visualize our findings using a **bar chart**.

You can learn more about Altair's bar charts [here](https://altair-viz.github.io/gallery/simple_bar_chart.html).

Here's how to do it:


```python
alt.Chart(feature_based_tracks).mark_bar().encode(
    x='dance_tune',
    y='count()'
)
```

![Alt text](images/spot_8.png)




As you can see, our data indicates that out of 16 songs in the playlist, 13 are Dance Tunes (e.g. have a "danceability" score of at least 0.75) and 3 are not. 

<br> 

If we were looking to make our lives even more complicated, we could **bin "energy"** based on a 0.75 "energy" score threshold:


```python
feature_based_tracks["energy_tune"] = np.where(feature_based_tracks['energy'] >= 0.75, True, False)
feature_based_tracks.head()
```

![Alt text](images/spot_10.png)





Based on this information, we can **analyze the composition** of our modified DataFrame using Altair. For example, one could think: out of the dance tunes, are most high energy or low energy? 

Here's a way to find out using Altair:


```python
bars = alt.Chart().mark_bar().encode(
    x=alt.X('energy_tune', title=""),
    y=alt.Y('count()', title='Count'),
    color=alt.Color('energy_tune', title="High energy")
)

alt.layer(bars, data=feature_based_tracks).facet(
    column=alt.Column('dance_tune', title = "Dance tune")
)
```


![Alt text](images/spot_11.png)



Alternatively, we can use **Altair's built-in bin method** of the Chart object to produce more standard binning. This is typically useful when creating a Histogram.

You can learn more about binning and histograms in Altair [here](https://altair-viz.github.io/gallery/simple_histogram.html).

Here's an example:


```python
alt.Chart(feature_based_tracks).mark_bar().encode(
    alt.X("danceability", bin=True),
    y='count()',
)
```

![Alt text](images/spot_12.png)



Another extremely useful tool is **sorting a DataFrame** based on one or many columns. As an example, we can sort our brand new DataFrame by the Tracks' "energy":


```python
my_sorted_df = feature_based_tracks.sort_values(['energy'], ascending=[True])
my_sorted_df.head()
```

![Alt text](images/spot_13.png)



Things to note here:
* the tracks in this new DataFrame are arranged based on their "energy" scores
* the tracks' indices are now inconsequent (the leftmost column), but could be easily reset (check out Pandas B lab)
* the tracks can also be sorted by multiple columns (specified in the value list)

Let's **chart the Tracks' "energy" based on our new DataFrame**:


```python
alt.Chart(my_sorted_df).mark_point().encode(
    x=alt.X("track_name", sort=None),
    y="energy"
)
```

![Alt text](images/spot_14.png)
