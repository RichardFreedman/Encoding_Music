# Advanced Pandas:  Filtering, Finding, and Grouping

| Part A | Part B | Part C | Part D |
|--------|--------|--------|--------|
| [Pandas Basics][part-a] | [Clean Data][part-b] | [Tidy Data][part-c] | **Filtering, Finding, and Grouping** |

In this tutorial we will explore two key concepts for working with complex datasets:

* Groupby functions, which allows you to perform tasks on defined subsets of your data
**TODO: modify this header**
* Various ways to "tidy" your data so that you can more easily explore it


Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

Contents of this Tutorial

<!---
7/16/24 TODO

Do we need new heading for Explore/melt/pivot, as prelude to Groupby?  Or perhaps just include in Groupby?

--->

|    | Contents of this Tutorial               | 
|----|-----------------------------------------|
| X. | [**Filter Rows: Logical Tests and Boolean Series**]() |
| X. | [**Searching for Strings and SubStrings**]() |
| X. | [**Bins:  From Continuous to Categorical Data**]() |
| X. | [**Explode, Melt, and Pivot Your Data**]() |
| X. | [**Groupby Functions**]() |

## Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

## Meet the Beatles (Again)

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

## A Basic Filter

An important feature in Pandas is the ability to look at only rows that meet a desired condition. This is called **filtering**. 

To filter, you need to write a **boolean condition** that will be evaluated for each row. Only rows for which this condition is `True` will be returned.

There are several types of conditions you can create.

### What is a condition?

One example of a condition in plain English:

> "does this row have the value `'Abbey Road'` in the `'Album.debut'` column?"

For every row, this will either be `True` or `False`. Let's take a look at how you would write this condition in Python and Pandas:

```python
beatles_billboard['Album.debut'] == 'Abbey Road'  # <-- this is our condition
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
0      False
1      False
2      False
3      False
4      False
       ...  
305    False
306    False
307    False
308    False
309    False
Name: Album.debut, Length: 310, dtype: bool</pre>
        </td>
    </tr>
</table>

The result is a Boolean series, where the index for each row in the dataframe is paired with either `True` or `False`. It is then possible to apply this Boolean series as a kind of 'mask' against the entire dataframe. Only the rows that have been assigned `True` in our Boolean series will be returned.

### Apply a Filter

To filter the dataframe, you pass this condition to the dataframe within square brackets, like this:

```python
beatles_billboard[beatles_billboard['Album.debut'] == 'Abbey Road']
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <details>
                <summary>Click to show output</summary>
                <table border="1">
                <thead>
                    <tr>
                    <th></th>
                    <th>Title</th>
                    <th>Year</th>
                    <th>Album.debut</th>
                    <th>Duration</th>
                    <th>Other.releases</th>
                    <th>Genre</th>
                    <th>Songwriter</th>
                    <th>Lead.vocal</th>
                    <th>Top.50.Billboard</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th>27</th>
                    <td>Because</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>165</td>
                    <td>11</td>
                    <td>Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon, McCartney, Harrison</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>36</th>
                    <td>Carry That Weight</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>96</td>
                    <td>5</td>
                    <td>Symphonic Rock, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney, with Lennon, Harrison and Starkey</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>45</th>
                    <td>Come Together</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>258</td>
                    <td>17</td>
                    <td>Blues Rock, Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon</td>
                    <td>6</td>
                    </tr>
                    <tr>
                    <th>81</th>
                    <td>Golden Slumbers</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>91</td>
                    <td>5</td>
                    <td>Rock, Baroque Pop, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>94</th>
                    <td>Her Majesty</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>23</td>
                    <td>8</td>
                    <td>Music Hall, Folk, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>95</th>
                    <td>Here Comes the Sun</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>186</td>
                    <td>6</td>
                    <td>Folk Pop, Pop/Rock</td>
                    <td>Harrison</td>
                    <td>Harrison</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>120</th>
                    <td>I Want You (She's So Heavy)</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>467</td>
                    <td>5</td>
                    <td>Blues Rock, Hard Rock, Progressive Rock, Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>178</th>
                    <td>Maxwell's Silver Hammer</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>207</td>
                    <td>8</td>
                    <td>Rock, Music Hall, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>179</th>
                    <td>Mean Mr. Mustard</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>66</td>
                    <td>6</td>
                    <td>Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>195</th>
                    <td>Octopus's Garden</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>168</td>
                    <td>10</td>
                    <td>Rock, Pop/Rock</td>
                    <td>Starkey, with uncredited assistance from Harrison</td>
                    <td>Starkey</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>196</th>
                    <td>Oh! Darling</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>206</td>
                    <td>9</td>
                    <td>Swamp Pop, Hard Rock, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>208</th>
                    <td>Polythene Pam</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>72</td>
                    <td>8</td>
                    <td>Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>226</th>
                    <td>She Came in Through the Bathroom Window</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>117</td>
                    <td>6</td>
                    <td>Rock, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>237</th>
                    <td>Something</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>179</td>
                    <td>16</td>
                    <td>Rock, Pop/Rock</td>
                    <td>Harrison</td>
                    <td>Harrison</td>
                    <td>30</td>
                    </tr>
                    <tr>
                    <th>241</th>
                    <td>Sun King</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>146</td>
                    <td>6</td>
                    <td>Art Pop, Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>256</th>
                    <td>The End</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>140</td>
                    <td>6</td>
                    <td>Hard Rock, Art Rock, Heavy Metal, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>302</th>
                    <td>You Never Give Me Your Money</td>
                    <td>1969</td>
                    <td>Abbey Road</td>
                    <td>242</td>
                    <td>7</td>
                    <td>Rock, Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    </tr>
                </tbody>
                </table>
            </details>
        </td>
    </tr>
</table>

### Ensuring Success with Filters

Filters can easily cause errors if you try to perform operations that Python and Pandas can't interpret. There are two key things to be aware of when filtering:

* **Fix missing data.** Operations on missing data often don't work, so if your condition will reference any missing data, problems may occur.
* **Fix data types**. If you try to perform a numerical comparison on data stored as a string, for example, you will also get errors.

In other words, remember to clean your data! [Part B][part-b] and [Part C][part-c] will help you. 

### Saving a Filtered DataFrame

If you want to save a filtered dataframe, just assign it to a variable! If you want it to replace your original dataframe, you can use the same name:

```python
beatles_billboard = beatles_billboard[beatles_billboard['Album.debut'] == 'Abbey Road']
```

## Types of Filters

Filtering can be much more powerful than searching for an exact match. Here are some other types of filters.

### Filters on Numerical Data

You can compare value in a certain column to a given value, or even a value in another column. For example, to check whether an album was released after 1969, use the condition `beatles_billboard['Year'] > 1969`. In a filter, that would be:

```python
beatles_billboard[beatles_billboard['Year'] > 1969]
```

You can use any numerical operator in Python (`==`, `!=`, `<`, `<=`, `>`, `>=`).

We can even *invert* the Boolean values, thus returning a dataframe that contains all rows *except* those matching the given condition. We do this use the negation operator `~`, and surrounding the original condition with parentheses `()`:

```python
beatles_billboard[~(beatles_billboard['Year'] > 1964)]
```

### Searching for Strings and SubStrings

To search for strings within a column, there are two methods:

*  `str.contains()`, which checks whether a cell contains the given substring
*  `isin(["string_1", "string_2"])`, which checks whether the cell contents are equal to any string in the given list

#### The `str.contains()` Method

For example here we filter to tracks with `'Anthology'` in the `'Album.debut'` column. The condition we use is:

```python
beatles_billboard['Album.debut'].str.contains('Anthology')
```

As long as the album name contains `'Anthology'`, it will pass the condition. This means the albums `'Anthology 1'`, `'Anthology 2'`, and `'Anthology 3'` will all pass.

Now apply the filter:

```python
beatles_billboard[beatles_billboard['Album.debut'].str.contains('Anthology')]
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <details>
                <summary>Click to show output (first 3 rows only)</summary>
                <table border="1">
                <thead>
                    <tr>
                    <th></th>
                    <th>Title</th>
                    <th>Year</th>
                    <th>Album.debut</th>
                    <th>Duration</th>
                    <th>Other.releases</th>
                    <th>Genre</th>
                    <th>Songwriter</th>
                    <th>Lead.vocal</th>
                    <th>Top.50.Billboard</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th>0</th>
                    <td>12-Bar Original</td>
                    <td>1965</td>
                    <td>Anthology 2</td>
                    <td>174</td>
                    <td>0</td>
                    <td>Blues</td>
                    <td>Lennon, McCartney, Harrison and Starkey</td>
                    <td>NaN</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                    <th>7</th>
                    <td>Ain't She Sweet</td>
                    <td>1961</td>
                    <td>Anthology 1</td>
                    <td>150</td>
                    <td>9</td>
                    <td>Pop/Rock</td>
                    <td>Yellen, Ager</td>
                    <td>Lennon</td>
                    <td>41</td>
                    </tr>
                    <tr>
                    <th>10</th>
                    <td>All Things Must Pass</td>
                    <td>1969</td>
                    <td>Anthology 3</td>
                    <td>227</td>
                    <td>0</td>
                    <td>Folk Rock, Pop/Rock</td>
                    <td>Harrison</td>
                    <td>Harrison</td>
                    <td>-1</td>
                    </tr>
                    <tr>
                        <th>...</th>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                        <td>...</td>
                    </tr>
                </tbody>
                </table>
            </details>
        </td>
    </tr>
</table>

<br>

> This is an example of a filter that **will not work** if your data has not first been cleaned! There are some entries missing in the `'Album.debut'` column. Some suggestions to fix this:
>
> ```python
> # replace missing values with the text "unreleased"
> beatles_billboard['Album.debut'] = beatles_billboard['Album.debut'].fillna('unreleased')
> ```
>
> or:
> ```python
> # drop rows with missing values
> beatles_billboard['Album.debut'] = beatles_billboard['Album.debut'].dropna()
> ```
> &nbsp;

#### The `.isin()` Method

The `.isin()` method works if you are looking for cells that match *at least one of several* possible strings. Note that the strings must be presented as a "list", thus `isin(["string_1", "string_2"])`.  For example, to return rows that have just "Lennon" OR just "McCartney":

```python
beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```

### Filtering with Multiple Conditions

You can filter with several conditions at once using **logical operators**. Surround your conditions with parentheses and place a logical operator between them, e.g. `(condition1) & (condition2)`. You can use any of the following operators:

| Operator | Name | Usage |
|----------|------|-------|
| `&` | and | Both conditions must be true |
| `\|` | or | Either (or both) conditions must be true |

As an example, you can filter for tracks both from one of the "Anthology" albums **and** released before 1965:

```python
beatles_billboard[(beatles_billboard['Album.debut'].str.contains('Anthology')) & (beatles_billboard['Year'] < 1965)]
```

## Bins:  From Continuous to Categorical Data

Another important tool is being able to categorize data. Oftentimes, this is done through "binning" -- assigning the entry to one of several discrete categories based on some continuous value. 

### Boolean Bins

In the following example, we will use the values in the `"danceability"` column (expressed as floats ranging from `0` to `1`) to classify a track as a Dance Tune (`0` => Not a Dance Tune; `1` => Definitely a Dance Tune). 

Here we are using the *beatles_spotify* data:

First, you need to think about picking a certain threshold value. Is Get Back by the Beatles (0.628 danceability rating) a Dance Tune? How about Doctor Robert (0.392 danceability score)? Use the code cell below to **pick your danceability threshold value** and save it as a variable. 

```python
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.000, 0.500, "right"), "Dance Tune"] = 0
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.501, 1.000, "right"), "Dance Tune"] = 1
```

Now we have a new column `'Dance Tune'` with a value of `1.0` if the track *is* a dance tune, and a value of `0.0` if the value is *not* a dance tune.

### Categorical Bins

Sometimes, a simple True/False ranking isn't enough. For example, the "tempo" column provides the Beat Per Minute musical tempo value for a given track; this value typically ranges between 1 and ~500 bpm. While it is possible to classify tracks into Slow and Not Slow, it might be more useful to, for example, categorize them into "Slow", "Medium", and "Fast". 

#### `cut` and `qcut`:  Creating Categorical Bins Automatically

Pandas provides two powerful methods for putting scalar data into bins, and (in turn) labeling the bins as part of the dataframe.

The `cut` method will divide your scalar data into "n" bins, with each bin representing an **equal segment of your original range**.  There are several parameters and options that allow you do deal with special cases. In the code below, we set `include_lowest=True` so that the 'items representing the lowest' of each bin boundary are include in the relevant bin.  Read the [Pandas Cut Documentation][pandas-cut].

The bins are of equal size, but contain different numbers of items:
 
```python
# here the spans of the buckets are the same, but they have different numbers of items in them
binned_data = pd.cut(beatles_spotify["danceability"], bins=4)
```

Let's use `.value_counts()` and `.sort_index()` to see the number of entries in each bin, sorted by the range of the bin:

```python
binned_data.value_counts().sort_index()
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
danceability
(0.145, 0.33]     19
(0.33, 0.513]     62
(0.513, 0.696]    93
(0.696, 0.88]     19
Name: count, dtype: int64</pre>
        </td>
    </tr>
</table>

The `qcut` method takes the distribution (and not just the range) of your data into account.  With this method, Pandas will create categories in which there is are an **equal number of items** in each range.  For example if we asked for 5 bins, and if 80% of your values are equally distributed in the lowest 40% of your range, we might expect to see four 'bands' for that range, and only one band for the remaining band (that is: five bands in all, each with the same number of items in it).

Here the bins are of different size, but contain equal numbers of items:

```python
# each bin will have the same proportion of items in it
q_binned = pd.qcut(our_data["danceability"], q=4)
```

Let's check the output:

```python
q_binned.value_counts().sort_index()
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
danceability
(0.145, 0.419]    49
(0.419, 0.533]    48
(0.533, 0.612]    48
(0.612, 0.88]     48
Name: count, dtype: int64</pre>
        </td>
    </tr>
</table>

#### Adding Labels to the Bins

It's also possible to add labels to each of these bins as you create them.

With `cut` method:

```python
binned_data = pd.cut(beatles_spotify["danceability"], bins=4, labels=['l', 'm', 'h', 's'])
``` 

With `qcut` method:

```python
binned_data = pd.qcut(beatles_spotify["danceability"], q=4, labels=['l', 'm', 'h', 's'])
```

## Groupby Functions

`groupby` is a powerful method that saves time when working with subsets (groups) of your data that share a certain characteristic.

Imagine you want to find the average duration of tracks in the album "Help!". Without `groupby`, you'd write something like:

```python
beatles_billboard[beatles_billboard['Album.debut'] == 'Help!']['Duration'].mean()
```

> `.mean()` returns the average of all the values in a numerical column

This is perfectly good, concise code. But what if you want to find the average duration of every album? You would have to find all the album names, filter for each of them one at a time, then compute the average for each - not a trivial task!

Instead, you can use `groupby` to separate your data into groups. In one line, this would be:

```python
beatles_billboard.groupby('Album.debut')['Duration'].mean()
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre style="white-space: pre;">
Album.debut
Abbey Road                                                         166.411765
Anthology 1                                                        147.619048
Anthology 2                                                        181.250000
Anthology 3                                                        181.222222
Help!                                                              146.285714<details><summary>Click to show more</summary>Let It Be                                                          175.750000
Let It Be... Naked - Fly on the Wall bonus disc                    176.000000
Live at the BBC                                                    137.548387
Live! at the Star-Club in Hamburg, Germany; 1962                   150.000000
Magical Mystery Tour                                               200.000000
On Air - Live at the BBC Volume 2                                  109.000000
Revolver                                                           150.181818
Rock 'n' Roll Music                                                153.000000
Rubber Soul                                                        150.800000
Sgt. Pepper's Lonely Hearts Club Band                              182.769231
The Beatles                                                        185.266667
The Beatles Bootleg Recordings 1963                                117.000000
The Beatles' Christmas Album                                       183.000000
UK: 1967-1970 US: Hey Jude                                         226.333333
UK: A Collection of Beatles Oldies US: 1962-1966                   116.000000
UK: A Collection of Beatles Oldies US: Beatles '65                 145.000000
UK: A Collection of Beatles Oldies US: Beatles VI                  150.000000
UK: A Collection of Beatles Oldies US: Hey Jude                    138.000000
UK: A Collection of Beatles Oldies US: Meet The Beatles!           144.000000
UK: A Collection of Beatles Oldies US: The Beatles Second Album    138.000000
UK: A Collection of Beatles Oldies US: Yesterday and Today         152.500000
UK: A Hard Day's Night US: 1962-1966                               152.000000
UK: A Hard Day's Night US: Beatles '65                             140.000000
UK: A Hard Day's Night US: Hey Jude                                147.500000
UK: A Hard Day's Night US: Something New                           137.500000
UK: A Hard Day's Night US: The Beatles Second Album                157.000000
UK: Beatles for Sale US: Beatles '65                               141.875000
UK: Beatles for Sale US: Beatles VI                                145.500000
UK: Help! US: Beatles VI                                           152.000000
UK: Help! US: Rubber Soul                                          121.000000
UK: Help! US: Yesterday and Today                                  131.000000
UK: Past Masters Volume 1 US: The Beatles Second Album             126.500000
UK: Please Please Me US: Meet The Beatles!                         175.000000
UK: Please Please Me US: Rarities                                  108.000000
UK: Please Please Me US: The Early Beatles                         141.181818
UK: Rarities US: Beatles '65                                       183.000000
UK: Rarities US: Beatles VI                                        161.000000
UK: Rarities US: Hey Jude                                          179.000000
UK: Rarities US: Meet The Beatles!                                 133.000000
UK: Rarities US: Rarities                                          185.333333
UK: Rarities US: Something New                                     146.000000
UK: Rarities US: The Beatles Second Album                          121.000000
UK: Revolver US: Yesterday and Today                               146.000000
UK: Rock 'n' Roll Music US: Something New                          146.000000
UK: Rock 'n' Roll Music US: The Beatles Second Album               130.000000
UK: Rubber Soul US: Yesterday and Today                            156.250000
UK: With the Beatles US: Meet The Beatles!                         128.555556
UK: With the Beatles US: The Beatles Second Album                  164.000000
Yellow Submarine                                                   229.750000
Name: Duration, dtype: float64</details></pre>
        </td>
    </tr>
</table>

Imagine you want to find the number of tracks in the album "Help!" using the `beatles_billboard` dataset. Without `groupby`, you would have to:

1. Filter the dataframe to contain only tracks where `beatles_billboard'Album.debut' == 'Help!'`
2. Use the `.nunique()` method on the `'Title'` column

This may seem relatively straightforward! But what if you wanted to do 


Let's imagine you want to find information about a subset of the data that all share a certain characteristic. For example, the number of albums that all share the same name. You could filter a dataframe, selecting only the rows with the desired album. Then you could count the number of unique tracks using the `.nunique()` method

<!--TODO: update this link-->
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

| Part A | Part B | Part C | Part D |
|--------|--------|--------|--------|
| [Pandas Basics][part-a] | [Clean Data][part-b] | [Tidy Data][part-c] | **Filtering, Finding, and Grouping** |

[part-a]: 04_A_Pandas_Basics.md
[part-b]: 04_B_Pandas_Clean.md
[part-c]: 04_C_Pandas_Tidy.md
[pandas-cut]: https://pandas.pydata.org/docs/reference/api/pandas.cut.html