# These functions are used with the Spotify API and Spotipy by Max Hilsdorf to work with audio feature data

# import the following libraries

import pandas as pd
import plotly.graph_objects as go
import time

# 1. Establish Credentials.
# Replace with your own Spotify API credentials

# client_id = 'your_client_id'
# client_secret = 'your_client_secret'

# 2 Initialize Spotipy client

# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

# 3. Obtain User Playlist Track Information. This is the basic metadata for each track in a list, and to
# obtain it, you must pass in the user_id and the playlist_id.  The function returns json.

# user_id = "rich6833spot"
# playlist_id = "75OAYmyh848DuB16eLqBtk"

# playlist_tracks(user_id: String, playlist_id: String): json_dict
# playlist_tracks = pd.DataFrame(sp.user_playlist_tracks(user_id, playlist_id))

# 4. Get Audio Features. Pass this to the function below, being sure to include a value for the `time_delay` before retry (`2` is suggested), 
# and also the spotipy client (which in our case is `sp`)

# The function returns a dataframe with all the audio features for your playlist

def get_audio_features_slowly(playlist_tracks, time_delay, sp):
    track_info = playlist_tracks.apply(lambda row: row["items"]["track"], axis=1).to_list()
    track_dict_list = []
    for track in track_info:
        try:
            time.sleep(time_delay)
            this_track_dict = {
                'track_id' : track['id'],
                'track_title' : track['name'],
                'artist_name' : track['artists'][0]['name']}
            audio_features_temp = sp.audio_features(track['id'])[0]
            # test for missing values
            this_track_dict.update(audio_features_temp)
            track_dict_list.append(this_track_dict)
        except Exception as e:
            print(e, track['id'])
    audio_features = pd.DataFrame(track_dict_list)
    return audio_features

# 5. Get Audio Features for Multiple Playlists. Begin by making a dictionary as follows:
# 
# playlist_dict = {
#     "PLAYLIST NAME HERE": ("CREATOR_ID HERE", "PLAYLIST_ID HERE")
# }
# For example:

# playlist_dict = {
#     "voyager" : ("rich6833spot", "75OAYmyh848DuB16eLqBtk"), 
#     "phrygian" : ("rich6833spot", "3LssUmwJxSBf3WoEz4aJuC")
#     #Follow the same format to add more playlists
# }

# Note that the "NAME" field above will appear as a separate column in the resulting combined dataframe, 
# thus identifying the data from each original playlist.

# Now pass that dictionary, the time delay (`2` is good) and the spotify client established above to the function.

# Typical use below.  Note that the 

# get_multiple_audio_features_slowly(playlist_dict, 2, sp)

def get_multiple_audio_features_slowly(playlist_dict, time_delay, sp):
    list_of_audio_dfs = []
    for playlist_name, value in playlist_dict.items():
        time.sleep(30)
        print(f"Getting tracks for playlist {playlist_name}")
        playlist_tracks = pd.DataFrame(sp.user_playlist_tracks(value[0], value[1]))
        if playlist_tracks is None:
            continue
        try:
            audio_features_this_playlist = get_audio_features_slowly(playlist_tracks, time_delay, sp)
            audio_features_this_playlist["playlist_title"] = playlist_name
            audio_features_this_playlist.to_csv(f"{playlist_name}.csv")
            list_of_audio_dfs.append(audio_features_this_playlist)
        except Exception as e:
            print(e)
    combined_audio_features = pd.concat(list_of_audio_dfs)
    return combined_audio_features

# 6. Get Dictionary of All Playlists for a Given User.  The result can then be used with the `get_multiple_audio_features_slowly` function above

def get_user_playlists(user_id, spotify_client):
    playlists = spotify_client.user_playlists(user_id)
    playlist_dictionary = {}
    for playlist in playlists['items']:
        playlist_dictionary[playlist['name']] = (user_id, playlist['id'])
    return playlist_dictionary



# 7. Radar Plot Functions
# Be sure to pecify the audio features.  Note that with Radar plots the first and last item in the following list must be the same (in order to complete the plot!)

# feature_list = ["danceability", "energy", "speechiness", "liveness", "instrumentalness", "valence", "danceability"]

# This plots the Radar Elements

def createRadarElement(row, feature_list, chosen_column_to_plot):
    return go.Scatterpolar(
        r = row[feature_list].values.tolist(), 
        theta = feature_list, 
        mode = 'lines', 
        name = row[chosen_column_to_plot])

# This builds the plot for ONE playlist audio feature dataframe.
# Note that you can pass in a custom name for your file


def get_radar_plot(feature_list, local_df, chosen_column_to_plot, file_name='Radar Plot of Audio Features'):
    current_data = list(local_df.apply(createRadarElement, axis=1, args=(feature_list, chosen_column_to_plot)))  
    fig = go.Figure(current_data, )
    fig.layout.title=file_name
    fig.show(renderer='iframe')
    fig.write_image(file_name + ".png", width=1200, height=800)

# Typical useage

# get_radar_plot(feature_columns, our_data, chosen_column_to_plot="track_title", file_name='Radar Plot of Audio Features')

