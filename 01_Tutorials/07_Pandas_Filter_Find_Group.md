| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | **Filtering, Finding, and Grouping** | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

# Advanced Pandas: Filtering, Finding, and Grouping

In this tutorial we will explore several key concepts for working with complex datasets:

* **Filters**, which allow you to select a subset of the dataset based on specified conditions
* **Bins**, which allow you to categorize and organize your data
* **Groups**, which allow you to perform the same operation on several distinct subsets of your data simultaneously (among other things)
* The ways in which **tidy data** is essential for all of these tools

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

Contents of this Tutorial

|    | Contents of this Tutorial               | 
|----|-----------------------------------------|
| 1. | [**A Basic Filter**](#a-basic-filter) |
| 2. | [**Using Filters**](#using-filters) |
| 3. | [**Bins: From Continuous to Categorical Data**](#bins-from-continuous-to-categorical-data) |
| 4. | [**Groupby Functions**](#groupby-functions) |

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

In other words, remember to clean your data! [Pandas: Clean Data][pandas-clean] and [Pandas: Tidy Data][pandas-tidy] will help you. 

### Saving a Filtered DataFrame

If you want to save a filtered dataframe, just assign it to a variable! If you want it to replace your original dataframe, you can use the same name:

```python
beatles_billboard = beatles_billboard[beatles_billboard['Album.debut'] == 'Abbey Road']
```

## Using Filters

Filtering can be much more powerful than searching for an exact match. Here are some other **types of filters**.

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

`groupby` is a powerful method that saves time when working with subsets (groups) of your data that share a certain characteristic. Some of its most important use cases are **compiling statistics for several subsets of your data, simultaneously** and **creating graphs based on those subsets**.

However, `groupby` also requires special attention to the tidiness of your data in order for it to function correctly.

In this section:

|    | Topic |
|----|-------|
| 1. | [Introduction to `groupby`](#introduction-to-groupby) |
| 2. | [Cleaning data for `groupby`](#cleaning-data-for-groupby) |
| 3. | [Examples using `groupby`](#examples-using-groupby) |
| 3. | [A brief `groupby` reference](#a-brief-groupby-reference) |

### Introduction to `groupby`

Imagine you want to find the average duration of tracks in the album "Help!". Without `groupby`, you'd write something like:

```python
beatles_billboard[beatles_billboard['Album.debut'] == 'Help!']['Duration'].mean()
```

> `.mean()` returns the average of all the values in a numerical column

This is perfectly good, concise code. But what if you want to find the average duration of *every* album? You would have to find all the album names, filter for each of them one at a time, then compute the average for each - not a trivial task!

Instead, you can use `groupby` to separate your data into groups. Pandas can then apply the same operation to each group individually. In one line, this would be:

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

Pandas Tutor provides an excellent visualization of this with a subset of the data (just a few columns and albums) [here][pandas-tutor-groupby-1]. Copy and paste the code snippet below if it does not automatically load in.

<details><summary>Code snippet for Pandas Tutor</summary>

```python
import pandas as pd
import io

csv = '''
Title,Album.debut,Duration
Another Girl,Help!,124
Eleanor Rigby,Revolver,128
For No One,Revolver,121
Girl,Rubber Soul,153
Good Day Sunshine,Revolver,129
Got to Get You into My Life,Revolver,147
Help!,Help!,138
"Here, There and Everywhere",Revolver,145
I Need You,Help!,148
I Want to Tell You,Revolver,149
I'm Looking Through You,Rubber Soul,147
In My Life,Rubber Soul,148
Love You To,Revolver,181
Michelle,Rubber Soul,160
Norwegian Wood (This Bird Has Flown),Rubber Soul,125
Run for Your Life,Rubber Soul,138
She Said She Said,Revolver,157
Taxman,Revolver,159
The Night Before,Help!,153
The Word,Rubber Soul,161
Think for Yourself,Rubber Soul,138
Ticket to Ride,Help!,190
Tomorrow Never Knows,Revolver,178
Wait,Rubber Soul,136
Yellow Submarine,Revolver,158
You Won't See Me,Rubber Soul,202
You're Going to Lose That Girl,Help!,140
You've Got to Hide Your Love Away,Help!,131
'''

songs = pd.read_csv(io.StringIO(csv))
songs = songs[['Title', 'Album.debut', 'Duration']].sort_values('Album.debut')

songs.groupby('Album.debut')['Duration'].mean()
```
</details>

### Cleaning Data for `groupby`

When you use `groupby`, you choose a *grouping column*. In the above example, we used the `'Album.debut'` column. This column was easy to work with, since (almost) every track has exactly one album; each row had exactly one *group name* (the album title).

This is not always the case, and for this reason you may have to tidy your data before being able to group it. Consider the following example:

Imagine you want to group by genre. Consider the song "Golden Slumbers", which has the genre `'Rock, Baroque Pop, Pop/Rock'`. Our ideal result is that Golden Slumbers is placed into **three** groups: one group for `'Rock'`, one for `'Baroque Pop'`, and one for `'Pop/Rock'`. However, if we try to group by genre without tidying the data, Golden Slumbers will be placed into a `'Rock, Baroque Pop, Pop/Rock'` group, containing **only songs with identical genres, written in the same order**. How can we fix this? Using `explode`!

As you learned in [Pandas: Tidy Data][pandas-tidy], you can `explode` a column containing several observations into several rows, each containing a single observation (e.g. one genre). 

<details><summary>Code to explode genre</summary>

```python
# clean the data before exploding
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.lower().str.strip().fillna('').str.split(', ')

# explode the data
beatles_billboard_exploded = beatles_billboard.explode('Genre').reset_index(drop=True)

# clean individual problems in the exploded data with str.replace() and str.strip()
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.strip('[')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('pop/rock', 'pop rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('r&b', 'rhythm and blues')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('rock and roll', 'rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('experimental music', 'experimental')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("children's music", "children's")
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("stage&screen", "stage and screen")
```
</details><br>

The result for Golden Slumbers would look like this:

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
      <th>154</th>
      <td>Golden Slumbers</td>
      <td>1969</td>
      <td>Abbey Road</td>
      <td>91</td>
      <td>5</td>
      <td>rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Golden Slumbers</td>
      <td>1969</td>
      <td>Abbey Road</td>
      <td>91</td>
      <td>5</td>
      <td>baroque pop</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Golden Slumbers</td>
      <td>1969</td>
      <td>Abbey Road</td>
      <td>91</td>
      <td>5</td>
      <td>pop/rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>

Now, when you use `groupby` on the `'Genre'` column, Golden Slumbers will be correctly placed into three groups: `'rock'`, `'baroque pop'`, and `'pop/rock'`.

This example demonstrates the importance of **tidying your data** whenever appropriate for a specific operation (like `groupby`). Your *grouping column* should contain exactly one *group name* per row. Refer to the techniques in [Pandas: Clean Data][pandas-clean] and [Pandas: Tidy Data][pandas-tidy] for instructions and examples.

### Examples using `groupby`

**`groupby`** functions allow you to organize and analyze data that share certain features.  For instance, we could find the **number of songs per album**:

```python
beatles_billboard.groupby("Album.debut")["Title"].count()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                                         17
Anthology 1                                                        21
Anthology 2                                                         4
Anthology 3                                                         9
Help!                                                               7
Let It Be                                                          12
Let It Be... Naked - Fly on the Wall bonus disc                     4
Live at the BBC                                                    31
Live! at the Star-Club in Hamburg, Germany; 1962                    1
Magical Mystery Tour                                               11
On Air - Live at the BBC Volume 2                                   2
Revolver                                                           11
Rock 'n' Roll Music                                                 1
Rubber Soul                                                        10
Sgt. Pepper's Lonely Hearts Club Band                              13
The Beatles                                                        30
The Beatles Bootleg Recordings 1963                                 2
The Beatles' Christmas Album                                        1
UK: 1967-1970 US: Hey Jude                                          6
UK: A Collection of Beatles Oldies US: 1962-1966                    1
UK: A Collection of Beatles Oldies US: Beatles '65                  1
UK: A Collection of Beatles Oldies US: Beatles VI                   1
UK: A Collection of Beatles Oldies US: Hey Jude                     1
UK: A Collection of Beatles Oldies US: Meet The Beatles!            1
...
UK: Rock 'n' Roll Music US: The Beatles Second Album                1
UK: Rubber Soul US: Yesterday and Today                             4
UK: With the Beatles US: Meet The Beatles!                          9
UK: With the Beatles US: The Beatles Second Album                   5
Yellow Submarine                                                    4
Name: Title, dtype: int64
</pre>
</details>

<br>

Or focus on the relative activity of Lennon and McCartney across the years, first by filtering to work that is theirs exclusively:

```python
beatles_jl_pm = beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```

> Note this excludes tracks they did not write independently. `.isin()` searches for exact matches, so for example, `'Lennon and Harrison'` would not be included.

Then find the 'groups':

```python
grouped = beatles_jl_pm.groupby("Songwriter")

list(grouped.groups.keys())
```

<details><summary>Output</summary><pre>
['Lennon', 'McCartney']
</pre>
</details>

<br>

And inspect a single "group":

```python
grouped.get_group("Lennon")
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
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
      <th>2</th>
      <td>A Hard Day's Night</td>
      <td>1964</td>
      <td>UK: A Hard Day's Night US: 1962-1966</td>
      <td>152</td>
      <td>35</td>
      <td>Rock, Electronic, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon, with McCartney</td>
      <td>8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Across the Universe</td>
      <td>1968</td>
      <td>Let It Be</td>
      <td>230</td>
      <td>19</td>
      <td>Psychedelic folk, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>All I've Got to Do</td>
      <td>1963</td>
      <td>UK: With the Beatles US: Meet The Beatles!</td>
      <td>124</td>
      <td>9</td>
      <td>Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>All You Need Is Love</td>
      <td>1967</td>
      <td>Magical Mystery Tour</td>
      <td>237</td>
      <td>25</td>
      <td>Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>15</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Bad to Me</td>
      <td>1963</td>
      <td>The Beatles Bootleg Recordings 1963</td>
      <td>142</td>
      <td>0</td>
      <td>Beat, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
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
    <tr>
      <th>295</th>
      <td>Yer Blues</td>
      <td>1968</td>
      <td>The Beatles</td>
      <td>241</td>
      <td>11</td>
      <td>Blues Rock, Hard Rock, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>296</th>
      <td>Yes It Is</td>
      <td>1965</td>
      <td>UK: Rarities US: Beatles VI</td>
      <td>161</td>
      <td>16</td>
      <td>Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon, McCartney and Harrison</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>298</th>
      <td>You Can't Do That</td>
      <td>1964</td>
      <td>UK: A Hard Day's Night US: The Beatles Second ...</td>
      <td>157</td>
      <td>25</td>
      <td>Rock and Roll, R&amp;B, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>305</th>
      <td>You're Going to Lose That Girl</td>
      <td>1965</td>
      <td>Help!</td>
      <td>140</td>
      <td>6</td>
      <td>Rock, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>306</th>
      <td>You've Got to Hide Your Love Away</td>
      <td>1965</td>
      <td>Help!</td>
      <td>131</td>
      <td>12</td>
      <td>FolkPop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>65 rows × 9 columns</p>
</details>

<br>

And finally to compare the outputs by grouping via two columns, songwriter and year.

"Size" considers *all* the rows (even ones with `NaN`s).

```python
beatles_jl_pm.groupby(['Songwriter','Year']).size()
```

<details><summary>Output</summary><pre>
Songwriter  Year
Lennon      1960     1
            1962     2
            1963     6
            1964    12
            1965     7
            1966     5
            1967     3
            1968    17
            1969    12
McCartney   1960     1
            1962     4
            1963     2
            1964     7
            1965     8
            1966     9
            1967     7
            1968    14
            1969    15
dtype: int64
</pre>
</details>

<br>

"Count" includes only the rows with valid data.

```python
beatles_jl_pm.groupby(['Songwriter','Year']).count()
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Title</th>
      <th>Album.debut</th>
      <th>Duration</th>
      <th>Other.releases</th>
      <th>Genre</th>
      <th>Lead.vocal</th>
      <th>Top.50.Billboard</th>
    </tr>
    <tr>
      <th>Songwriter</th>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="9" valign="top">Lennon</th>
      <th>1960</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1962</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1963</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1964</th>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1965</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1966</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1967</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1968</th>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1969</th>
      <td>12</td>
      <td>10</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th rowspan="9" valign="top">McCartney</th>
      <th>1960</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1962</th>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1963</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1964</th>
      <td>7</td>
      <td>6</td>
      <td>7</td>
      <td>7</td>
      <td>6</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1965</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1966</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1967</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1968</th>
      <td>14</td>
      <td>12</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1969</th>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</details>

<br>

There are many other functions that can be applied to aggregate, filter and transform data within groups!  See the essay above for a guide.

A count of track titles per album:

```python
beatles_billboard.groupby("Album.debut")["Title"].count()
```

Group by Songwriter and Year, showing counts for each:

<details><summary>Output</summary><pre>
Songwriter  Year
Lennon      1960     1
            1962     2
            1963     6
            1964    12
            1965     7
            1966     5
            1967     3
            1968    17
            1969    12
McCartney   1960     1
            1962     4
            1963     2
            1964     7
            1965     8
            1966     9
            1967     7
            1968    14
            1969    15
dtype: int64
</pre></details>

<br>

### A brief `groupby` reference

Since `groupby` is such a powerful but complex tool, it may be helpful to learn more about the various ways to use it.

In order to use `groupby`, you need:

* A *grouping column* (or several!)
* Each row in the *grouping column* should contain exactly one *group name* (i.e. a clean and tidy dataset)

Perform the `groupby` operation:

```python
grouped = beatles_billboard.groupby('Album.debut')
```

<blockquote><details><summary>What if I want to <code>groupby</code> on several columns?</summary>

Performing a `groupby` operation on several columns at once if you want to create subgroups within a group. For example:

```python
album_vocal = beatles_billboard.groupby(['Album.debut', 'Lead.vocal'])
```

Then any operation you perform will be performed on the subgroup of `'Lead.vocal'` within the larger `'Album.debut'` group.

Note that using `groupby` with several grouping columns will complicate the operations you perform later. Use the documentation!

</details></blockquote>

<br>

The result of the `groupby` operation has been stored in the variable `grouped`. The result is called a "`groupby` object" - not a dataframe, but a collection of several dataframes, one for each group. This is more difficult to represent visually, and in fact Pandas won't display `grouped` when you just use the variable name:

```python
grouped
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
&lt;pandas.core.groupby.generic.DataFrameGroupBy object at 0x12a634af0&gt;</pre>
        </td>
    </tr>
</table>

One way to get around this is using `.value_counts()`. Since almost every item is unique, when displaying the number of occurences of each item, `.value_counts()` will display each distinct item, with just `1` occurence as noted in the far-right column.

```python
grouped.value_counts()
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre style="white-space: pre;"><details><summary>Show output</summary>
Album.debut                                        Title                           Year  Duration  Other.releases  Genre                                  Songwriter              Lead.vocal                                    Top.50.Billboard
Abbey Road                                         Because                         1969  165       11              Pop/Rock                               Lennon                  Lennon, McCartney, Harrison                   -1                  1
                                                   Carry That Weight               1969  96        5               Symphonic Rock, Pop/Rock               McCartney               McCartney, with Lennon, Harrison and Starkey  -1                  1
                                                   Come Together                   1969  258       17              Blues Rock, Pop/Rock                   Lennon                  Lennon                                         6                  1
                                                   Golden Slumbers                 1969  91        5               Rock, Baroque Pop, Pop/Rock            McCartney               McCartney                                     -1                  1
                                                   Her Majesty                     1969  23        8               Music Hall, Folk, Pop/Rock             McCartney               McCartney                                     -1                  1
                                                                                                                                                                                                                                                   ..
UK: With the Beatles US: The Beatles Second Album  You've Really Got a Hold on Me  1963  182       2               Soul, Pop/Rock                         Robinson                Lennon and Harrison                           -1                  1
Yellow Submarine                                   All Together Now                1967  130       8               Skiffle, Pop/Rock                      McCartney, with Lennon  McCartney, with Lennon                        -1                  1
                                                   Hey Bulldog                     1968  194       12              Psychedelic Rock, Hard Rock, Pop/Rock  Lennon                  Lennon                                        -1                  1
                                                   It's All Too Much               1967  388       11              Psychedelic Rock, Acid Rock, Pop/Rock  Harrison                Harrison                                      -1                  1
                                                   Only a Northern Song            1967  207       9               Psychedelic Rock, Pop/Rock             Harrison                Harrison                                      -1                  1
Name: count, Length: 282, dtype: int64</pre></details>
        </td>
    </tr>
</table>

> By default, Pandas only displays 10 rows. If you want to see the entire object, you can change this setting, but be careful: your computer could run slowly or crash if it tries to display too many rows!
>
> To increase the limit, create a new code block with the following code, run it, and then run the code to display your data.
> 
> ```python
> # sets maximum number of rows to display
> pd.set_option('display.max_rows', None) # you can replace None with a number
> ```
> 
> After displaying your data, you should reset the setting. You could just set the option back to 10, or use `reset_option`:
>
> ```python
> pd.reset_option('display.max_rows')
> ```

Now you've created a **groupby object**, what can you do with it?

Each group is represented as its own dataframe, and all of the groups are contained in the groupby object. You can work with all the groups at once, or just one group at a time.

#### Working With All Groups

When you work with all groups simultaneously, there are a number of possible operations you can perform.

##### See the size (number of rows) of each group

```python
grouped.size()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              17
Anthology 1                                             21
Anthology 2                                              4
Anthology 3                                              9
Help!                                                    7
                                                        ..
UK: Rock 'n' Roll Music US: The Beatles Second Album     1
UK: Rubber Soul US: Yesterday and Today                  4
UK: With the Beatles US: Meet The Beatles!               9
UK: With the Beatles US: The Beatles Second Album        5
Yellow Submarine                                         4
Length: 54, dtype: int64</pre>
</details>

##### See the number of rows, **excluding those with missing values**, in each *column* of each group

```python
grouped.count()
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Other.releases</th>
      <th>Genre</th>
      <th>Songwriter</th>
      <th>Lead.vocal</th>
      <th>Top.50.Billboard</th>
    </tr>
    <tr>
      <th>Album.debut</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abbey Road</th>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Anthology 1</th>
      <td>21</td>
      <td>21</td>
      <td>21</td>
      <td>21</td>
      <td>21</td>
      <td>21</td>
      <td>19</td>
      <td>21</td>
    </tr>
    <tr>
      <th>Anthology 2</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Anthology 3</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Help!</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
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
    </tr>
    <tr>
      <th>UK: Rock 'n' Roll Music US: The Beatles Second Album</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>UK: Rubber Soul US: Yesterday and Today</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: Meet The Beatles!</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: The Beatles Second Album</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Yellow Submarine</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>54 rows × 8 columns</p>
</details>

##### See the number of unique rows in each *column* of each group

```python
grouped.nunique()
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Other.releases</th>
      <th>Genre</th>
      <th>Songwriter</th>
      <th>Lead.vocal</th>
      <th>Top.50.Billboard</th>
    </tr>
    <tr>
      <th>Album.debut</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abbey Road</th>
      <td>17</td>
      <td>1</td>
      <td>17</td>
      <td>9</td>
      <td>12</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Anthology 1</th>
      <td>21</td>
      <td>7</td>
      <td>14</td>
      <td>3</td>
      <td>14</td>
      <td>19</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Anthology 2</th>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Anthology 3</th>
      <td>9</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
      <td>7</td>
      <td>6</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Help!</th>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
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
    </tr>
    <tr>
      <th>UK: Rock 'n' Roll Music US: The Beatles Second Album</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>UK: Rubber Soul US: Yesterday and Today</th>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: Meet The Beatles!</th>
      <td>9</td>
      <td>1</td>
      <td>8</td>
      <td>8</td>
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: The Beatles Second Album</th>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Yellow Submarine</th>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>54 rows × 8 columns</p>
</details><br>

Now that you have a better sense of what the data looks like, you can begin to perform operations on it. These operations should be performed on a specific column, or just a few columns. For example, while it makes sense to compute the `mean` of the `'Duration'` column, it doesn't make sense to compute the `mean` of the `'Title'` column (and in fact you can't)!

You can select columns to operate on the same way you would with a regular dataframe, using square brackets: `grouped['column_name']` or `grouped[['column_1', 'column_2']]`.

You can perform the same counting operations (`.size()`, `.count()`, `.nunique()`):

##### See the size (number of rows), *in the specified column(s)*, for each group

```python
grouped['Duration'].size()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              17
Anthology 1                                             21
Anthology 2                                              4
Anthology 3                                              9
Help!                                                    7
                                                        ..
UK: Rock 'n' Roll Music US: The Beatles Second Album     1
UK: Rubber Soul US: Yesterday and Today                  4
UK: With the Beatles US: Meet The Beatles!               9
UK: With the Beatles US: The Beatles Second Album        5
Yellow Submarine                                         4
Name: Duration, Length: 54, dtype: int64
</pre></details>

##### See the number of rows without missing data, *in the specified column(s)*, for each group

```python
grouped[['Title', 'Lead.vocal']].count()
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Lead.vocal</th>
    </tr>
    <tr>
      <th>Album.debut</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abbey Road</th>
      <td>17</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Anthology 1</th>
      <td>21</td>
      <td>19</td>
    </tr>
    <tr>
      <th>Anthology 2</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Anthology 3</th>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Help!</th>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>UK: Rock 'n' Roll Music US: The Beatles Second Album</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>UK: Rubber Soul US: Yesterday and Today</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: Meet The Beatles!</th>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: The Beatles Second Album</th>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Yellow Submarine</th>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>54 rows × 2 columns</p>
</details>

##### See the number of unique rows, *in the specified column(s)*, for each group

```python
grouped['Other.releases'].nunique()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              9
Anthology 1                                             3
Anthology 2                                             2
Anthology 3                                             1
Help!                                                   7
                                                       ..
UK: Rock 'n' Roll Music US: The Beatles Second Album    1
UK: Rubber Soul US: Yesterday and Today                 4
UK: With the Beatles US: Meet The Beatles!              8
UK: With the Beatles US: The Beatles Second Album       5
Yellow Submarine                                        4
Name: Other.releases, Length: 54, dtype: int64
</pre></details>

##### See the sum of the specified column(s) for each group

> This will work with textual data, but it doesn't make sense! All the text entries in a column will be combined into one string. `sum` is best used with numerical data.

```python
grouped['Duration'].sum()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              2829
Anthology 1                                             3100
Anthology 2                                              725
Anthology 3                                             1631
Help!                                                   1024
                                                        ... 
UK: Rock 'n' Roll Music US: The Beatles Second Album     130
UK: Rubber Soul US: Yesterday and Today                  625
UK: With the Beatles US: Meet The Beatles!              1157
UK: With the Beatles US: The Beatles Second Album        820
Yellow Submarine                                         919
Name: Duration, Length: 54, dtype: int64
</pre></details>

##### See the maximum value in the specified column(s) for each group

> Only works with numerical data

```python
grouped['Top.50.Billboard'].max()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              30
Anthology 1                                             45
Anthology 2                                             47
Anthology 3                                             -1
Help!                                                   17
                                                        ..
UK: Rock 'n' Roll Music US: The Beatles Second Album    -1
UK: Rubber Soul US: Yesterday and Today                 27
UK: With the Beatles US: Meet The Beatles!              -1
UK: With the Beatles US: The Beatles Second Album       -1
Yellow Submarine                                        -1
Name: Top.50.Billboard, Length: 54, dtype: int64
</pre></details>

##### See the minimum value in the specified column(s) for each group

> Only works with numerical data

```python
grouped[['Other.releases', 'Top.50.Billboard']].min()
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Other.releases</th>
      <th>Top.50.Billboard</th>
    </tr>
    <tr>
      <th>Album.debut</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abbey Road</th>
      <td>5</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>Anthology 1</th>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>Anthology 2</th>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>Anthology 3</th>
      <td>0</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>Help!</th>
      <td>6</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>UK: Rock 'n' Roll Music US: The Beatles Second Album</th>
      <td>35</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>UK: Rubber Soul US: Yesterday and Today</th>
      <td>9</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: Meet The Beatles!</th>
      <td>9</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>UK: With the Beatles US: The Beatles Second Album</th>
      <td>2</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>Yellow Submarine</th>
      <td>8</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>54 rows × 2 columns</p>
</details>

##### See the average value in the specified column(s) for each group

> Only works with numerical data

```python
grouped['Top.50.Billboard'].mean()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                               1.235294
Anthology 1                                              5.095238
Anthology 2                                             11.000000
Anthology 3                                             -1.000000
Help!                                                    3.714286
                                                          ...    
UK: Rock 'n' Roll Music US: The Beatles Second Album    -1.000000
UK: Rubber Soul US: Yesterday and Today                  6.000000
UK: With the Beatles US: Meet The Beatles!              -1.000000
UK: With the Beatles US: The Beatles Second Album       -1.000000
Yellow Submarine                                        -1.000000
Name: Top.50.Billboard, Length: 54, dtype: float64
</pre></details>

##### See the standard deviation in the specified column(s) for each group

> Only works with numerical data

```python
grouped['Duration'].std()
```

<details><summary>Output</summary><pre>
Album.debut
Abbey Road                                              100.616884
Anthology 1                                              33.071855
Anthology 2                                              38.482680
Anthology 3                                              81.551790
Help!                                                    21.592547
                                                           ...    
UK: Rock 'n' Roll Music US: The Beatles Second Album           NaN
UK: Rubber Soul US: Yesterday and Today                  12.816006
UK: With the Beatles US: Meet The Beatles!               16.432522
UK: With the Beatles US: The Beatles Second Album        13.247641
Yellow Submarine                                        110.738054
Name: Duration, Length: 54, dtype: float64
</pre>
<blockquote>Note that one of the standard deviations is <code>NaN</code>! Can you guess why?
<br><br>
<em>Hint: can you find how many rows are in that group?</em>
</details>

#### Working With a Single Group

Another way to make use of a `groupby` object is to examine one group in particular.

##### See the list of groups

```python
list(grouped.groups.keys())
```

<blockquote><details><summary>What's going on here?</summary>
`grouped.groups` returns a dictionary, wherein each **key** is a group name and each **value** is a list. The list contains the indices of each item from the original dataframe that is in that group.

If we want to see all of the group names, we only need the **keys** of this dictionary. However, `grouped.groups.keys()` comes out in a weird format. We can fix this by converting the output to a list, using `list()`. The result is a nicely formatted list of every group name in the `groupby` object.
</details></blockquote>

<br>

<details><summary>Output</summary><pre>
['Abbey Road',
 'Anthology 1',
 'Anthology 2',
 'Anthology 3',
 'Help!',
 ...
 "UK: Rock 'n' Roll Music US: The Beatles Second Album",
 'UK: Rubber Soul US: Yesterday and Today',
 'UK: With the Beatles US: Meet The Beatles!',
 'UK: With the Beatles US: The Beatles Second Album',
 'Yellow Submarine']
</pre>
</details>

##### Check the number of groups

```python
grouped.ngroups
```

<details><summary>Output</summary><pre>
54
</pre>
</details>

##### See the contents of a group

```python
help = grouped.get_group('Help!')

# see the group
help
```

<details><summary>Output</summary>
<table border="1">
  <thead>
    <tr style="text-align: right;">
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
      <th>16</th>
      <td>Another Girl</td>
      <td>1965</td>
      <td>Help!</td>
      <td>124</td>
      <td>9</td>
      <td>Country Rock, Pop/Rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Help!</td>
      <td>1965</td>
      <td>Help!</td>
      <td>138</td>
      <td>34</td>
      <td>Folk Rock, Pop/Rock</td>
      <td>Lennon, with McCartney</td>
      <td>Lennon</td>
      <td>14</td>
    </tr>
    <tr>
      <th>114</th>
      <td>I Need You</td>
      <td>1965</td>
      <td>Help!</td>
      <td>148</td>
      <td>11</td>
      <td>Pop/Rock</td>
      <td>Harrison</td>
      <td>Harrison</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>261</th>
      <td>The Night Before</td>
      <td>1965</td>
      <td>Help!</td>
      <td>153</td>
      <td>13</td>
      <td>Electronic Pop/Rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>270</th>
      <td>Ticket to Ride</td>
      <td>1965</td>
      <td>Help!</td>
      <td>190</td>
      <td>31</td>
      <td>Power Pop, Jangle Pop, Folk Rock, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon, with McCartney</td>
      <td>17</td>
    </tr>
    <tr>
      <th>305</th>
      <td>You're Going to Lose That Girl</td>
      <td>1965</td>
      <td>Help!</td>
      <td>140</td>
      <td>6</td>
      <td>Rock, Pop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>306</th>
      <td>You've Got to Hide Your Love Away</td>
      <td>1965</td>
      <td>Help!</td>
      <td>131</td>
      <td>12</td>
      <td>FolkPop/Rock</td>
      <td>Lennon</td>
      <td>Lennon</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
</details>

<br>

The result stored in `help` is a dataframe! You could perform any operation on `help` that you would on a dataframe.

| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | **Filtering, Finding, and Grouping** | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

[pandas-basics]: 04_Pandas_Basics.md
[pandas-clean]: 05_Pandas_Clean_Data.md
[pandas-tidy]: 06_Pandas_Tidy_Data.md
[pandas-graphs]: 08_Pandas_Graphs_and_Charts.md
[pandas-networks]: 09_Pandas_Networks.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
[pandas-cut]: https://pandas.pydata.org/docs/reference/api/pandas.cut.html
[pandas-tutor-groupby-1]: https://pandastutor.com/vis.html#code=import%20pandas%20as%20pd%0Aimport%20io%0A%0Acsv%20%3D%20'''%0ATitle,Album.debut,Duration%0AAnother%20Girl,Help!,124%0AEleanor%20Rigby,Revolver,128%0AFor%20No%20One,Revolver,121%0AGirl,Rubber%20Soul,153%0AGood%20Day%20Sunshine,Revolver,129%0AGot%20to%20Get%20You%20into%20My%20Life,Revolver,147%0AHelp!,Help!,138%0A%22Here,%20There%20and%20Everywhere%22,Revolver,145%0AI%20Need%20You,Help!,148%0AI%20Want%20to%20Tell%20You,Revolver,149%0AI'm%20Looking%20Through%20You,Rubber%20Soul,147%0AIn%20My%20Life,Rubber%20Soul,148%0ALove%20You%20To,Revolver,181%0AMichelle,Rubber%20Soul,160%0ANorwegian%20Wood%20%28This%20Bird%20Has%20Flown%29,Rubber%20Soul,125%0ARun%20for%20Your%20Life,Rubber%20Soul,138%0AShe%20Said%20She%20Said,Revolver,157%0ATaxman,Revolver,159%0AThe%20Night%20Before,Help!,153%0AThe%20Word,Rubber%20Soul,161%0AThink%20for%20Yourself,Rubber%20Soul,138%0ATicket%20to%20Ride,Help!,190%0ATomorrow%20Never%20Knows,Revolver,178%0AWait,Rubber%20Soul,136%0AYellow%20Submarine,Revolver,158%0AYou%20Won't%20See%20Me,Rubber%20Soul,202%0AYou're%20Going%20to%20Lose%20That%20Girl,Help!,140%0AYou've%20Got%20to%20Hide%20Your%20Love%20Away,Help!,131%0A'''%0A%0Asongs%20%3D%20pd.read_csv%28io.StringIO%28csv%29%29%0Asongs%20%3D%20songs%5B%5B'Title',%20'Album.debut',%20'Duration'%5D%5D.sort_values%28'Album.debut'%29%0A%0Asongs.groupby%28'Album.debut'%29%5B'Duration'%5D.mean%28%29&d=2024-07-26&lang=py&v=v1