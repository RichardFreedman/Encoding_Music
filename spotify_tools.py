# These functions are used with the Spotify API and Spotipy by Max Hilsdorf to work with audio feature data

# import the following libraries

import pandas as pd
import plotly.graph_objects as go

# Replace with your own Spotify API credentials
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'

# Initialize Spotipy client
# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

def get_audio_features_df(playlist, spotipy_client):
    
    # Create an empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    for track in playlist["items"]:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        # Get audio features
        audio_features = spotipy_client.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the DataFrames
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df

def analyze_playlist(creator, playlist_id, spotipy_client):
    playlist_features_list = ["artist", "album", "track_name", "track_id", 
                             "danceability", "energy", "key", "loudness", "mode", "speechiness",
                             "instrumentalness", "liveness", "valence", "tempo", "duration_ms", "time_signature"]
    playlist_df = pd.DataFrame(columns=playlist_features_list)
    
    playlist_features = {}
    
    playlist = spotipy_client.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        audio_features = spotipy_client.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        track_df = pd.DataFrame(playlist_features, index=[0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)
        
    return playlist_df

def analyze_playlist_dict(playlist_dict, spotipy_client):
    for i, (key, val) in enumerate(playlist_dict.items()):
        playlist_df = analyze_playlist(*val, spotipy_client=spotipy_client)
        playlist_df["playlist"] = key
        
        if i == 0:
            playlist_dict_df = playlist_df
        else:
            playlist_dict_df = pd.concat([playlist_dict_df, playlist_df], ignore_index=True)
            
    return playlist_dict_df

def get_all_user_tracks(username, spotipy_client):
    all_my_playlists = pd.DataFrame(spotipy_client.user_playlists(username))
    list_of_dataframes = []

    for playlist in all_my_playlists.index:
        current_playlist = pd.DataFrame(spotipy_client.user_playlist_tracks(username, all_my_playlists["items"][playlist]["id"]))
        current_playlist_audio = get_audio_features_df(current_playlist)
        if all_my_playlists["items"][playlist]["name"]:
            current_playlist_audio["playlist_name"] = all_my_playlists["items"][playlist]["name"]
        else:
            current_playlist_audio["playlist_name"] = None
        list_of_dataframes.append(current_playlist_audio)

    return pd.concat(list_of_dataframes)

def createRadarElement(row, feature_cols):
    return go.Scatterpolar(
        r = row[feature_cols].values.tolist(), 
        theta = feature_cols, 
        mode = 'lines', 
        name = row['track_name'])

def get_radar_plot(playlist_id, features_list, spotipy_client):
    current_playlist_audio_df = get_audio_features_df(pd.DataFrame(spotipy_client.playlist_items(playlist_id)))
    current_data = list(current_playlist_audio_df.apply(createRadarElement, axis=1, args=(features_list, )))  
    fig = go.Figure(current_data, )
    fig.show(renderer='iframe')
    fig.write_image(playlist_id + '.png', width=1200, height=800)
    
def get_radar_plots(playlist_id_list, features_list):
    for item in playlist_id_list:
        get_radar_plot(item, features_list)