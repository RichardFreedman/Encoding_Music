## Working with Our Voyager Data and Voyager Spotify Data in Pandas


```
import pandas as pd
```

### Get the CSV Files 

- One is the combined results of all our data cleaning
- The other is spotify data for all items


```
cleaned_voyager = pd.read_csv('https://bit.ly/cleaned_voyager_data')
voyager_spotify = pd.read_csv('https://bit.ly/our_voyager_spotify')
```

### Check the Columns




```
cleaned_voyager.columns.to_list()
```

```
voyager_spotify.columns.to_list()
```

### Combined the Two Sets Using Selected Title Columns as the common elements

`'Title (Pursner)'` in the cleaned data
`'track_name'` in the spotify data


```
voyager_combined = pd.merge(right=cleaned_voyager, 
         left=voyager_spotify, 
         right_on="Title (Pursner)", 
         left_on="track_name", 
         how="left")
voyager_combined
```


