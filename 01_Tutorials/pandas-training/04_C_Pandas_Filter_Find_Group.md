# Advanced Pandas:  Grouping and Tidying Data

| Part A | Part B | Part C |
|--------|--------|--------|
| [Pandas Basics][part-a] | [Clean and Tidy Data][part-b] | **Finding and Grouping Data** |

In this tutorial we will explore two key concepts for working with complex datasets:

* Groupby functions, which allows you to perform tasks on defined subsets of your data
* Various ways to "tidy" your data so that you can more easily explore it


[Read more](https://pandas.pydata.org/about/).

[Tutorials](https://www.w3schools.com/python/pandas/default.asp).

[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Contents of this Tutorial

## Filter Rows: Logical Tests and Boolean Series
## Searching for Strings and SubStrings
## Bins:  From Continuous to Categorical Data
## Groupby Functions


Pandas **data frames** are the basic unit upon which all operations take place.  Data frames are like spreadsheets, with columns and rows.

Indeed, Pandas can easily import spreadsheets in **CSV** (comma separated values) format.  We will also import data from databases in **JSON** format (Java Script Object Notation), similar to a Python dictionary. There are special scripts for working with JSON, too.

Pandas can export as well as import these formats (among others).

## Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

## Meet the Beatles

The Pandas library has a vast array of tools for sorting, filtering, grouping, analyzing, and even visualizing tabluar data of various kinds:  strings, booleans, integers, floats, dates, and so on.  We begin with data about the albums and songs issued by the Beatles. The data are drawn from two sources:

* A set from **Spotify** that includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1CBiNbxqF4FHWMkFv-C6nl7AyOJUFqycrR-EvWvDZEWY/edit#gid=953807965).

* A set compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs:  author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts.  View these data on [Github]('https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv').

We will work with both of these sets, and in the process learn how to inspect, clean, combine, filter, group, and analyze the information they contain.

We give the URL of the CSV file a name (simply for convenience), then pass that name to the `read_csv('source_file_name')` method, and name the resulting data frame.

```python
beatles_spotify_csv = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCv45ldJmq0isl2bvWok7AbD5C6JWA0Xf1tBqow5ngX7_ox8c2d846PnH9iLp_SikzgYmvdPHe9k7G/pub?output=csv'

beatles_spotify = pd.read_csv(beatles_spotify_csv)

```

and 

```python
beatles_billboard_csv = 'https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv'

beatles_billboard = pd.read_csv(beatles_billboard_csv)
```


## Filter Rows

**Filter rows based on some logical condition or string** in one or more columns.  There are several possibilities.  

### Logical Tests and Boolean Series

Testing a single column for a logical condition returns a Boolean series of True/False values for all 'rows':

```python
beatles_billboard['Year'] > 1969
```

It is then possible to apply this Boolean series as a kind of 'mask' against the entire dataframe.  In effect we are asking for a slice of the dataframe where the given column is  `True`:

```python
beatles_billboard[beatles_billboard['Year'] > 1969]
```

We can even *reverse* the Boolean values, thus returning a dataframe that matches everything *except* the rows matching the given condition (note the extra parenthesis to clarify the syntax):

```python
beatles_billboard[~(beatles_billboard['Year'] > 1964)]
```

## Searching for Strings and SubStrings

Note the differences between:

*  `str.contains()`, which matches **any substring in that cell** and
*  `isin(["sub_string_1", "sub_string_2"])`, which checks whether any of the complete items in the list matches the full cell contents

#### `The str.contains()` Method

For example here we filter to tracks with "unreleased" in the `Album.debut` column. The **items within "[]" become a Boolean series**:

```python
[beatles_billboard['Album.debut'].str.contains("unreleased")]
```

This is then used to **mask** the complete data trame (rows with "True" are retained), which happens when we append this list to the name of the dataframe itself.  In effect we are saying "return df where [these conditions] are True"

```python
beatles_billboard[beatles_billboard['Album.debut'].str.contains("unreleased")]
```

But we can also **invert the Boolean series**, so that the string "unreleased" is **False**.  "~" (the tilde) is used to invert the mask:

```python
beatles_billboard[~beatles_billboard['Album.debut'].str.contains("unreleased")]
```

Or we can **filter with two conditions** (the above, plus "Year < 1965".  Notice that in this case each condition (which will be a set of True/False values) is surrounded in `()`, and then together linked by `&` as part of the complete `[]` test.

```python
beatles_billboard[(beatles_billboard['Album.debut'].str.contains("unreleased")) & (beatles_billboard['Year'] < 1965)]
```
#### The `isin()` Method

The **isin()** method works if you are looking for *one or more substrings in a given cell*.  Note that the strings must be presented as a "list", thus **`isin(["substring_1", "substring_2"])`**.  For example, this, which returns either "Lennon" OR "McCartney" (in any context within that column):

```python
beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```


## Bins:  From Continuous to Categorical Data

Another important tool is being able to categorize data. Oftentimes, this is done through "binning" -- assigning the entry to one of several discrete categories based on some continuous value. 

### Boolean Bins

In the following example, we will use the values in the "danceability" column (expressed as floats ranging from 0 to 1) to classify a track as a Dance Tune (0 => Not a Dance Tune; 1 => Definitely a Dance Tune). 

Here we are using the *Beatles_Spotify* data:

First, you need to think about picking a certain threshold value. Is Get Back by the Beatles (0.628 danceability rating) a Dance Tune? How about Doctor Robert (0.392 danceability score)? Use the code cell below to **pick your danceability threshold value** and save it as a variable. 

```python
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.000, 0.500, "right"), "Dance Tune"] = 0
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.510, 1.000, "right"), "Dance Tune"] = 1
beatles_spotify
```

### Categorical Bins

Sometimes, a simple True/False ranking isn't enough. For example, the "tempo" column provides the Beat Per Minute musical tempo value for a given track; this value typically ranges between 1 and ~500 bpm. While it is possible to classify tracks into Slow and Not Slow, it might be more useful to, for example, categorize them into "Slow", "Medium", and "Fast". 

#### `cut` and `qcut`:  Creating Categorical Bins Automatically

Pandas provides two powerful methods for putting scalar data into bins, and (in turn) labeling the bins as part of the dataframe.

The `cut` method will divide your scalar data into "n" bins, with each bin representing an **equal segment of your original range**.  There are several parameters and options that allow you do deal with special cases. In the code below, we set `include_lowest=True` so that the 'items representing the lowest' of each bin boundary are include in the relevant bin.  Read the  [Pandas Cut Documentation](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)

The bins are of equal size, but contain different numbers of items:
 
```python
binned_data = pd.cut(our_data["danceability"], bins=4)
binned_data.value_counts().sort_index()
```

![Alt text](images/bins.png)


The `qcut` method takes the distribution (and not just the range) of your data into account.  With this method, Pandas will create categories in which there is are an **equal number of items** in each range.  For example if we asked for 5 bins, and if 80% of your values are equally distributed in the lowest 40% of your range, we might expect to see four 'bands' for that range, and only one band for the remaining band (that is: five bands in all, each with the same number of items in it).

Here the bins are of different size, but contain equal numbers of items:

```python
# each bin will have the same proportion of items in it
q_binned = pd.qcut(our_data["danceability"], q=4)
q_binned.value_counts().sort_index()
```

![Alt text](images/bins_q.png)


#### Adding Labels to the Bins

It's also possible to add labels to each of these bins.

With `cut` method:

```python
# specify a list of columns to be binned and labeled
binned_cols = ['danceability',
 'energy',
 'key',
 'loudness',
 'speechiness',
 'liveness',
 'valence',
 'tempo',
 'duration_ms']
# now make a copy 
our_data_binned = our_data.copy()
# label the bins and count the number of labels for use below
labels = ['l', 'm', 'h', 's']
bin_count = len(labels)
# loop over the columns and 'cut' the data, returning new columns with the individual rows labeled
for column in binned_cols:
    our_data_binned[f"{column}_binned"] = pd.cut(our_data_binned[column], bins=bin_count, labels=labels)
```


With `qcut` method:

```python
# specify a list of columns to be binned and labeled
binned_cols = ['danceability',
 'energy',
 'key',
 'loudness',
 'speechiness',
 'liveness',
 'valence',
 'tempo',
 'duration_ms']
# now make a copy of the dataframe
our_data_q_binned = our_data.copy()
# label the bins and count the number of labels for use below
labels = ['l', 'm', 'h', 's']
bin_count = len(labels)
# loop over the columns and 'cut' the data, returning new columns with the individual rows labeled
# note that here we need to `drop` items that might be duplicated across bins
for column in binned_cols:
    our_data_q_binned[f"{column}_q_binned"] = pd.qcut(our_data_q_binned[column], 
                                                 q=bin_count,
                                                labels = labels,
                                                 duplicates='drop')
```

## Groupby Functions

Learn more about Groupby [here](https://medium.com/towards-data-science/pandas-groupby-aggregate-transform-filter-c95ba3444bbb).

**Groupby** functions allow you to organize and analyze data that share certain features.  For instance, we could find the **number of songs per album**:

```python
beatles_billboard.groupby("Album.debut")["Title"].count()
```

![Alt text](<images/pd 6.png>)

Or focus on the relative activity of Lennon and McCartney across the years, first by filtering to only their work:

```python
beatles_jl_pm = beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```

Then find the 'groups':

```python
grouped = beatles_jl_pm.groupby(["Songwriter"])
grouped.groups
```

And inspect a single "group":

```python
grouped.get_group("Lennon")
```

And finally to compare the outputs by grouping via two columns, songwriter and year.

"Size" considers _all_ the rows (even ones with NaNs).

```python
beatles_jl_pm.groupby(['Songwriter','Year']).size()
```

"Count" includes only the rows with valid data.

```python
beatles_jl_pm.groupby(['Songwriter','Year']).count()
```

There are many other functions that can be applied to aggregate, filter and transform data within groups!  See the essay above for a guide.

A count of track titles per album:

```python
beatles_billboard.groupby("Album.debut")["Title"].count()
```

Group by Songwriter and Year, showing counts for each:

```python
beatles_jl_pm.groupby(['Songwriter','Year']).size()
```

![Alt text](<images/Pd 7.png>)


## Charts and Graphs

Through libraries like **Plotly Express**, Pandas can quickly produce histograms, charts, and graphs of various kinds (these can even be saved as PNG files for publications).

For example: a histogram of the count of songs per albumn.

```python
beatles_spotify["album"].hist(figsize=(10, 5), bins=100)
plt.xlabel("Album")
plt.xticks(rotation = 60) # Rotates X-Axis Ticks by 60-degrees
plt.ylabel("Song Count")
plt.show()
```

![Alt text](<images/pd 8.png>)


Various built-in math functions allow us to run basic statistics.  Libraries like `numpy` permit many more!



```python
top_50 = beatles_billboard[beatles_billboard["Top.50.Billboard"] > 0].sort_values('Year')

top_50.set_index('Title', inplace=True)
top_50['top-down'] = 50 - top_50['Top.50.Billboard']
top_50['top-down'].plot(kind="bar", figsize=(15, 10))
# ax = plt.gca()
# ax.invert_yaxis()
plt.title("Beatles Top 50 Hits 1962-1969")
plt.xlabel("Song Title")
plt.ylabel("Position in Top 50")
plt.show()
```

![Alt text](<images/pd 9.png>)

| Part A | Part B | Part C |
|--------|--------|--------|
| [Pandas Basics][part-a] | [Clean and Tidy Data][part-b] | **Finding and Grouping Data** |

[part-a]: 04_A_Pandas_Basics.md
[part-b]: 04_B_Pandas_Clean_Tidy.md