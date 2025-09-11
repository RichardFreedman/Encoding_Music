| **Pandas Basics** | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|

# Pandas: Basics

*Pandas: The Python library for Data Analysis*

Pandas is a Python library which allows for the creation and manipulation of DataFrames, which are two dimensional objects designed to store data. Below are a few of the many ways in which pandas DataFrames can be modified, filtered, or transformed:

* High-performance manipulation of text, integers, numbers, dates
* Data alignment, reshaping, pivoting
* Intelligent slicing, grouping, and subsetting
* Merging and joining of sets
* Integrated modules for analysis, plots, visualizations, maps, networks

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

|    | Contents of this Tutorial                                                      | 
|----|--------------------------------------------------------------------------------|
| 1. | [**Introduction to DataFrames**](#introduction-to-dataframes)                  |
| 2. | [**Working with Rows**](#working-with-rows)                                    |
| 3. | [**Working with Columns**](#working-with-columns)                              |
| 4. | [**Sort and Count**](#sort-and-count)                                          |
| 5. | [**Combine and Merge Data Frames**](#combining-joining-and-merging-dataframes) |
| 6. | [**Making the Most of Pandas**](#making-the-most-of-pandas)                    |

## Introduction to DataFrames

Pandas **data frames** are the basic unit upon which all operations take place. Dataframes are like spreadsheets, with columns and rows.

Indeed, Pandas can easily import spreadsheets in **CSV** (comma separated values) format. We will also import data from databases in **JSON** format (Java Script Object Notation), similar to a Python dictionary. There are special scripts for working with JSON, too.

Pandas can export as well as import these formats (among others).

### Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

### Meet the Beatles

The Pandas library has a vast array of tools for sorting, filtering, grouping, analyzing, and even visualizing tabluar data of various kinds: strings, booleans, integers, floats, dates, and so on.  We begin with data about the albums and songs issued by the Beatles. The data are drawn from two sources:

* A set from **Spotify** that includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet][beatles-spotify-spreadsheet].

* A set compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs: author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts. View these data on [Github][beatles-billboard-spreadsheet].

We will work with both of these sets, and in the process learn how to inspect, clean, combine, filter, group, and analyze the information they contain.

We give the URL of the CSV file a name (simply for convenience), then pass that name to the `read_csv('source_file_name')` method, and name the resulting data frame.

```python
beatles_spotify_csv = 'https://docs.google.com/spreadsheets/d/1j_Be1iDDdmvGXfiSUIbSpJrkzKVg3fkWD5PiFJE2m7s/edit?gid=742074147#gid=742074147'

beatles_spotify = pd.read_csv(beatles_spotify_csv)
```

and 

```python
beatles_billboard_csv = 'https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv'

beatles_billboard = pd.read_csv(beatles_billboard_csv)
```

### Inspect the Data Frame

A quick look at the file as a dataframe using the `head()` method:

```python
beatles_billboard.head(15)  # Shows the first 15 rows
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <table border="1" class="dataframe">
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
                        <th>1</th>
                        <td>A Day in the Life</td>
                        <td>1967</td>
                        <td>Sgt. Pepper's Lonely Hearts Club Band</td>
                        <td>335</td>
                        <td>12</td>
                        <td>Psychedelic Rock, Art Rock, Pop/Rock</td>
                        <td>Lennon and McCartney</td>
                        <td>Lennon and McCartney</td>
                        <td>-1</td>
                    </tr>
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
                        <th>3</th>
                        <td>A Shot of Rhythm and Blues</td>
                        <td>1963</td>
                        <td>Live at the BBC</td>
                        <td>104</td>
                        <td>0</td>
                        <td>R&amp;B, Pop/Rock</td>
                        <td>Thompson</td>
                        <td>Lennon</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>4</th>
                        <td>A Taste of Honey</td>
                        <td>1963</td>
                        <td>UK: Please Please Me US: The Early Beatles</td>
                        <td>163</td>
                        <td>29</td>
                        <td>Pop/Rock, Jazz, Stage&amp;Screen</td>
                        <td>Scott, Marlow</td>
                        <td>McCartney</td>
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
                        <th>11</th>
                        <td>All Together Now</td>
                        <td>1967</td>
                        <td>Yellow Submarine</td>
                        <td>130</td>
                        <td>8</td>
                        <td>Skiffle, Pop/Rock</td>
                        <td>McCartney, with Lennon</td>
                        <td>McCartney, with Lennon</td>
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
                        <th>13</th>
                        <td>And I Love Her</td>
                        <td>1964</td>
                        <td>UK: A Hard Day's Night US: Something New</td>
                        <td>152</td>
                        <td>29</td>
                        <td>Pop/Rock</td>
                        <td>McCartney, with Lennon</td>
                        <td>McCartney</td>
                        <td>37</td>
                    </tr>
                    <tr>
                        <th>14</th>
                        <td>And Your Bird Can Sing</td>
                        <td>1966</td>
                        <td>UK: Revolver US: Yesterday and Today</td>
                        <td>121</td>
                        <td>9</td>
                        <td>Power Pop, Psychedelic Pop, Pop/Rock</td>
                        <td>Lennon, with McCartney</td>
                        <td>Lennon</td>
                        <td>-1</td>
                    </tr>
                </tbody>
            </table>
            <p>15 rows × 9 columns</p>
        </td>
    </tr>
</table>

Now we can look at the data in various ways to see what is here. The first column is the `index` (and begins with "0").

* `beatles_spotify.info()` will show the names, number and data types of the columns
* `beatles_spotify.shape` will tell us the size of our frame:  how many **rows and columns**, like `(193, 11)`.  Note:  normally these methods are followed by `()`.  This one is not.
* `beatles_spotify.describe()` delivers basic statistical information about the set, such as count, average, mean, standard deviation, and basic percentiles.

<table border="0">
    <tr>
        <th>Method:</th>
        <td><code>beatles_spotify.info()</code></td>
        <td><code>beatles_spotify.shape</code></td>
        <td><code>beatles_spotify.describe()</code></td>
    </tr>
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
&#60;class&#160;'pandas.core.frame.DataFrame'>&#160;&#160;&#160;&#160;&#160;
RangeIndex: 193 entries, 0 to 192
Data columns (total 11 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   id            193 non-null    int64  
 1   year          193 non-null    int64  
 2   album         193 non-null    object 
 3   song          193 non-null    object 
 4   danceability  193 non-null    float64
 5   energy        193 non-null    float64
 6   speechiness   193 non-null    float64
 7   acousticness  193 non-null    float64
 8   liveness      193 non-null    float64
 9   valence       193 non-null    float64
 10  duration_ms   193 non-null    int64  
dtypes: float64(6), int64(3), object(2)
memory usage: 16.7+ KB</pre>
        </td>
        <td valign="top">
            <pre>(193, 11)</pre>
        </td>
        <td valign="top">
            <table border="1">
                <thead>
                    <tr style="text-align: right;">
                        <th></th>
                        <th>id</th>
                        <th>year</th>
                        <th>danceability</th>
                        <th>energy</th>
                        <th>speechiness</th>
                        <th>acousticness</th>
                        <th>liveness</th>
                        <th>valence</th>
                        <th>duration_ms</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>count</th>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                        <td>193.000000</td>
                    </tr>
                    <tr>
                        <th>mean</th>
                        <td>97.000000</td>
                        <td>1966.290155</td>
                        <td>0.519093</td>
                        <td>0.536891</td>
                        <td>0.046399</td>
                        <td>0.375964</td>
                        <td>0.228647</td>
                        <td>0.642191</td>
                        <td>163644.155440</td>
                    </tr>
                    <tr>
                        <th>std</th>
                        <td>55.858452</td>
                        <td>2.256647</td>
                        <td>0.138738</td>
                        <td>0.193026</td>
                        <td>0.035101</td>
                        <td>0.287539</td>
                        <td>0.200419</td>
                        <td>0.250929</td>
                        <td>57982.884527</td>
                    </tr>
                    <tr>
                        <th>min</th>
                        <td>1.000000</td>
                        <td>1963.000000</td>
                        <td>0.146000</td>
                        <td>0.090200</td>
                        <td>0.024700</td>
                        <td>0.000043</td>
                        <td>0.041400</td>
                        <td>0.035700</td>
                        <td>25987.000000</td>
                    </tr>
                    <tr>
                        <th>25%</th>
                        <td>49.000000</td>
                        <td>1964.000000</td>
                        <td>0.419000</td>
                        <td>0.413000</td>
                        <td>0.031400</td>
                        <td>0.097400</td>
                        <td>0.099400</td>
                        <td>0.473000</td>
                        <td>133507.000000</td>
                    </tr>
                    <tr>
                        <th>50%</th>
                        <td>97.000000</td>
                        <td>1966.000000</td>
                        <td>0.533000</td>
                        <td>0.537000</td>
                        <td>0.036400</td>
                        <td>0.339000</td>
                        <td>0.139000</td>
                        <td>0.690000</td>
                        <td>154200.000000</td>
                    </tr>
                    <tr>
                        <th>75%</th>
                        <td>145.000000</td>
                        <td>1968.000000</td>
                        <td>0.612000</td>
                        <td>0.660000</td>
                        <td>0.045300</td>
                        <td>0.629000</td>
                        <td>0.298000</td>
                        <td>0.835000</td>
                        <td>180213.000000</td>
                    </tr>
                    <tr>
                        <th>max</th>
                        <td>193.000000</td>
                        <td>1970.000000</td>
                        <td>0.880000</td>
                        <td>0.969000</td>
                        <td>0.342000</td>
                        <td>0.971000</td>
                        <td>0.922000</td>
                        <td>0.975000</td>
                        <td>502013.000000</td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
</table>

## Working with Rows

By default Pandas shows only the first and last five rows of any data frame. There are various ways to see others:

* **All rows**, set `pd.set_option('display.max_rows', None)` or `pd.options.display.max_rows = 9999` before you display the frame.
* **Head** rows (default of five from the start, but can be any number):  `beatles_spotify.head(20)`
* **Tail** rows (default of five from the end, but can be any number):  `beatles_spotify.tail(20)`
* **Sample** a random sample of rows (default of 1 , but can be any number):  `beatles_spotify.sample(20)`

### Selecting Rows: `loc` and `iloc` 

`df.loc` and `df.iloc` are *not* the same!

### iloc for Index-based slices

* **iloc**: to select rows by **index number** (the left-hand column) use `iloc`. A good way to remember this is that `iloc` will correspond to the *integer* value of the index (which starts with zero). The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`. 

Note the use of square brackets `[ ]`: square brackets indicate we are taking a *slice* (a section) of an item.

The first number is *inclusive* but the second is *exclusive*. So `beatles_spotify.iloc[10:15, 2:4]` will yield rows 10, 11, 12, 13, 14, and columns 2, 3, but *not* row 15 or column 4.

As a shortcut, you can omit the first number of a range to start at the first possible index, and omit the last number of a range to end at the last possible index. You can also omit the column range to retrieve all columns.

Thus rows 10-14 (and all columns) of our dataframe would be `beatles_spotify.iloc[10:15]` (or `beatles_spotify.iloc[10:15., :]`).

### loc for Label-based slices

* **loc**: to select rows by **label** of the left-hand column (as when you might have an index of strings), use `loc`. This is useful when our index is a string rather than a number. It is especially useful for working with columns.

Pandas Cheat Sheet: [here][pandas-cheat-sheet].

Try:

```python
beatles_spotify.iloc[10:15]
```

### Dropping Rows

You can remove (what Pandas calls 'dropping') rows by referencing their index numbers. For example, to remove rows 0, 1, 5, and 6 from `beatles_billboard`:

```python
beatles_billboard = beatles_billboard.drop([0, 1, 5, 6])
```

Your dataset will now be missing rows with those indices. You can reset the indices of the dataset (so they are again continuous from 0 to the end of the dataset) using `.reset_index(drop=True)`:

```python
beatles_billboard = beatles_billboard.reset_index(drop=True)
```

## Working with Columns

We now start to look more closely at the columns.

### iloc for Index-based slices

It's possible to select colulmns with `iloc`, as shown above for rows. The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  The first column (and all rows) would be `beatles_spotify.iloc[:, 0]`. Thus the first `five` columns (and all rows) of our dataframe would be `beatles_spotify.iloc[:, 0:6]`.  Note:  the first number is *inclusive* but the second is *exclusive*.

Want to count from the *end*?  `-1` is the *last* column. So `beatles_spotify.iloc[:, -1]`

### Working with Columns by Name (or 'label')

| | Things you can do with columns |
|--|------------------------------|
| 1.| [Show all the columns of a dataframe](#show-all-the-columns-of-a-dataframe) |
| 2. | [Add a column](#add-a-column) |
| 3. | [Drop a column](#drop-a-column) |
| 4. | [Rename a column (or columns)](#rename-a-column-or-columns) |
| 5. | [Show the data types of the columns](#show-the-data-types-of-the-columns) |
| 6. | [Reorder columns](#reorder-columns) |

#### Show all the columns of a dataframe

Show all the columns of a dataframe as a list (note the absence of `()`):

```python
beatles_billboard.columns
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
Index(['Title', 'Year', 'Album.debut', 'Duration', 'Other.releases', 'Genre', 'Songwriter', 'Lead.vocal', 'Top.50.Billboard'],
      dtype='object')</pre>
        </td>
    </tr>
</table>

You can also see the list of columns in alphabetical order:

```python
beatles_spotify.columns.sort_values()
```

#### Add a column

You can add a column based on another column. You assign a new column name to an expression that is then evaluated for each row:

```python
beatles_spotify['sad'] = beatles_spotify['valence'] < 0.2
```

This example creates a new column, `'sad'`, in `beatles_spotify`. In each row, the `'sad'` column will have the value of the Boolean expression `beatles_spotify['valence'] < 0.2`. This means if valence for that row is less than 0.2, `'sad'` will be `True`, and if not, `'sad'` will be `False`.

#### Drop a column

Note that these must be presented as a list, even if there is only one!

```python
beatles_billboard = beatles_billboard.drop(columns=['Album.debut'])
```

#### Rename a column (or columns)

You can rename a single column like this:

```python
# copy 'Album.debut' column to new 'album' column
beatles_billboard["album"] = beatles_billboard["Album.debut"]
# remove original 'Album.debut' column
beatles_billboard = beatles_billboard.drop(columns=['Album.debut'])
```

This is the same as adding a new column, `'album'`, where every entry is the same as in the `'Album.debut'` column. You then have to get rid of the redundant `'Album.debut'` column, hence the drop.

You can also rename columns by creating a dictionary that specifies which column names should be changed, and what they should be changed to:

```python
renaming_dict = {
    'Album.debut': 'album',
    'Title': 'song',
    'Year': 'release_date'
}

beatles_billboard.rename(columns = renaming_dict)
```

#### Show the data types of the columns

Each column has a data type, which tells Pandas what form the column's data is in. This affects what operations are possible on the column; if it is stored as a number, you can't use string methods on the column, and if it is stored as a string, you can't apply mathematical operations. You'll learn more about working with data types in [Pandas: Clean Data][pandas-clean].

```python
beatles_spotify.dtypes
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
id                int64
year              int64
album            object
song             object
danceability    float64
                 ...   
speechiness     float64
acousticness    float64
liveness        float64
valence         float64
duration_ms       int64
Length: 11, dtype: object</pre>
        </td>
    </tr>
</table>

Note you can learn similar information about your dataframe using `beatles_spotify.info()`.

#### Reorder columns

To reorder columns, you simply specify a new order of the existing columns in a list. You can omit columns to exclude them from the new dataframe.

```python
column_list = ['Year', 'Title', 'Album.debut', 'Duration', 'Other.releases' 'Genre', 'Songwriter', 'Lead.vocal', 'Top.50.Billboard']
beatles_billboard_reordered = beatles_billboard[column_list]
```

Note that this could also be done using the `index` values for the columns.

With this method, we can make a **new dataframe with just a subset of columns**.

```python
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <table border="1">
                <thead>
                    <tr style="text-align: right;">
                        <th></th>
                        <th>Title</th>
                        <th>Year</th>
                        <th>Album.debut</th>
                        <th>Genre</th>
                        <th>Songwriter</th>
                        <th>Top.50.Billboard</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>0</th>
                        <td>12-Bar Original</td>
                        <td>1965</td>
                        <td>Anthology 2</td>
                        <td>Blues</td>
                        <td>Lennon, McCartney, Harrison and Starkey</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>1</th>
                        <td>A Day in the Life</td>
                        <td>1967</td>
                        <td>Sgt. Pepper's Lonely Hearts Club Band</td>
                        <td>Psychedelic Rock, Art Rock, Pop/Rock</td>
                        <td>Lennon and McCartney</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>2</th>
                        <td>A Hard Day's Night</td>
                        <td>1964</td>
                        <td>UK: A Hard Day's Night US: 1962-1966</td>
                        <td>Rock, Electronic, Pop/Rock</td>
                        <td>Lennon</td>
                        <td>8</td>
                    </tr>
                    <tr>
                        <th>3</th>
                        <td>A Shot of Rhythm and Blues</td>
                        <td>1963</td>
                        <td>Live at the BBC</td>
                        <td>R&amp;B, Pop/Rock</td>
                        <td>Thompson</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>4</th>
                        <td>A Taste of Honey</td>
                        <td>1963</td>
                        <td>UK: Please Please Me US: The Early Beatles</td>
                        <td>Pop/Rock, Jazz, Stage&amp;Screen</td>
                        <td>Scott, Marlow</td>
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
                    </tr>
                    <tr>
                        <th>305</th>
                        <td>You're Going to Lose That Girl</td>
                        <td>1965</td>
                        <td>Help!</td>
                        <td>Rock, Pop/Rock</td>
                        <td>Lennon</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>306</th>
                        <td>You've Got to Hide Your Love Away</td>
                        <td>1965</td>
                        <td>Help!</td>
                        <td>FolkPop/Rock</td>
                        <td>Lennon</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>307</th>
                        <td>You've Really Got a Hold on Me</td>
                        <td>1963</td>
                        <td>UK: With the Beatles US: The Beatles Second Album</td>
                        <td>Soul, Pop/Rock</td>
                        <td>Robinson</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>308</th>
                        <td>Young Blood</td>
                        <td>1963</td>
                        <td>Live at the BBC</td>
                        <td>Pop/Rock</td>
                        <td>Leiber, Stoller</td>
                        <td>-1</td>
                    </tr>
                    <tr>
                        <th>309</th>
                        <td>Your Mother Should Know</td>
                        <td>1967</td>
                        <td>Magical Mystery Tour</td>
                        <td>Music Hall, Vaudeville Rock, Psychedelic Pop, ...</td>
                        <td>McCartney</td>
                        <td>-1</td>
                    </tr>
                </tbody>
            </table>
            <p>310 rows × 6 columns</p>
        </td>
    </tr>
</table>

### A Column is a Series

An individual column is called a **Series**, which we can perform various operations on.

* **One column** of the dataframe: `beatles_spotify["year"]`
    > You can also reference a column like this: `beatles_spotify.year`. However, this syntax is not as clear and does not work with some column names, such as those with spaces or special characters (it is good practice to name your columns without spaces or special characters for this reason). Most examples here will use the bracketed syntax.
* Show all the unique entries in a single column: `beatles_spotify["album"].unique()`
* Count the **number of unique values** in a single column: `beatles_spotify["album"].nunique()`

Pandas Cheat Sheet: [here][pandas-cheat-sheet].

## Sort and Count

Pandas affords many ways to take stock of your data, with built-in functions counts of values, means, averages, and other statistical information.  Many of these are detailed on the [Pandas Cheat Sheet][pandas-cheat-sheet]. But the following will be useful for us:

* Count the **number of entries** for each value in a column:  `beatles_spotify["album"].value_counts()`

### Sort Values

**Sort Values** in any column.  This ascending (alphabetically or numerically) by default, but can be reversed.  Example:  

```python
beatles_spotify.sort_values("danceability")
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <table border="1">
                <thead>
                    <tr style="text-align: right;">
                        <th></th>
                        <th>id</th>
                        <th>year</th>
                        <th>album</th>
                        <th>song</th>
                        <th>danceability</th>
                        <th>energy</th>
                        <th>speechiness</th>
                        <th>acousticness</th>
                        <th>liveness</th>
                        <th>valence</th>
                        <th>duration_ms</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>150</th>
                        <td>151</td>
                        <td>1968</td>
                        <td>The Beatles (white album)</td>
                        <td>good night</td>
                        <td>0.146</td>
                        <td>0.355</td>
                        <td>0.0352</td>
                        <td>0.865000</td>
                        <td>0.1140</td>
                        <td>0.1780</td>
                        <td>193760</td>
                    </tr>
                    <tr>
                        <th>143</th>
                        <td>144</td>
                        <td>1968</td>
                        <td>The Beatles (white album)</td>
                        <td>helter skelter</td>
                        <td>0.166</td>
                        <td>0.831</td>
                        <td>0.0894</td>
                        <td>0.000606</td>
                        <td>0.8110</td>
                        <td>0.2810</td>
                        <td>269787</td>
                    </tr>
                    <tr>
                        <th>152</th>
                        <td>153</td>
                        <td>1969</td>
                        <td>Yellow Submarine</td>
                        <td>only a northern song</td>
                        <td>0.175</td>
                        <td>0.731</td>
                        <td>0.0705</td>
                        <td>0.000341</td>
                        <td>0.0846</td>
                        <td>0.8010</td>
                        <td>204493</td>
                    </tr>
                    <tr>
                        <th>149</th>
                        <td>150</td>
                        <td>1968</td>
                        <td>The Beatles (white album)</td>
                        <td>revolution 9</td>
                        <td>0.208</td>
                        <td>0.615</td>
                        <td>0.3420</td>
                        <td>0.769000</td>
                        <td>0.8240</td>
                        <td>0.1010</td>
                        <td>502013</td>
                    </tr>
                    <tr>
                        <th>158</th>
                        <td>159</td>
                        <td>1969</td>
                        <td>Yellow Submarine</td>
                        <td>sea of time</td>
                        <td>0.237</td>
                        <td>0.096</td>
                        <td>0.0387</td>
                        <td>0.971000</td>
                        <td>0.2030</td>
                        <td>0.0629</td>
                        <td>180213</td>
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
                        <td>...</td>
                        <td>...</td>
                    </tr>
                    <tr>
                        <th>32</th>
                        <td>33</td>
                        <td>1964</td>
                        <td>A Hard Day's Night</td>
                        <td>And I Love Her</td>
                        <td>0.767</td>
                        <td>0.331</td>
                        <td>0.0337</td>
                        <td>0.640000</td>
                        <td>0.0681</td>
                        <td>0.6360</td>
                        <td>149693</td>
                    </tr>
                    <tr>
                        <th>90</th>
                        <td>91</td>
                        <td>1966</td>
                        <td>Revolver</td>
                        <td>good day sunshine</td>
                        <td>0.770</td>
                        <td>0.496</td>
                        <td>0.0468</td>
                        <td>0.719000</td>
                        <td>0.1230</td>
                        <td>0.5710</td>
                        <td>129293</td>
                    </tr>
                    <tr>
                        <th>125</th>
                        <td>126</td>
                        <td>1968</td>
                        <td>The Beatles (white album)</td>
                        <td>wild honey pie</td>
                        <td>0.792</td>
                        <td>0.763</td>
                        <td>0.0506</td>
                        <td>0.425000</td>
                        <td>0.7890</td>
                        <td>0.1520</td>
                        <td>52973</td>
                    </tr>
                    <tr>
                        <th>124</th>
                        <td>125</td>
                        <td>1968</td>
                        <td>The Beatles (white album)</td>
                        <td>obi-la -di, ob-la-da</td>
                        <td>0.818</td>
                        <td>0.728</td>
                        <td>0.0314</td>
                        <td>0.232000</td>
                        <td>0.2510</td>
                        <td>0.9750</td>
                        <td>188960</td>
                    </tr>
                    <tr>
                        <th>191</th>
                        <td>192</td>
                        <td>1970</td>
                        <td>Let It Be</td>
                        <td>for you blue</td>
                        <td>0.880</td>
                        <td>0.556</td>
                        <td>0.0855</td>
                        <td>0.240000</td>
                        <td>0.2400</td>
                        <td>0.9550</td>
                        <td>152213</td>
                    </tr>
                </tbody>
            </table>
            <p>193 rows × 11 columns</p>
        </td>
    </tr>
</table>

### Count Values

Pandas makes it easy to summarize the count of each value in any column.  For example: 

```python
beatles_billboard["Album.debut"].value_counts()
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>
Album.debut
Live at the BBC                                        31
The Beatles                                            30
Anthology 1                                            21
Abbey Road                                             17
Sgt. Pepper's Lonely Hearts Club Band                  13
                                                       ..
UK: Rarities US: Beatles '65                            1
UK: Rarities US: The Beatles Second Album               1
UK: Rarities US: Meet The Beatles!                      1
UK: Rarities US: Beatles VI                             1
UK: A Hard Day's Night US: The Beatles Second Album     1
Name: count, Length: 54, dtype: int64</pre>
        </td>
    </tr>
</table>

You may want to store the result of the `.value_counts()` method in a new dataframe:

```python
counts = pd.DataFrame(beatles_billboard["Album.debut"].value_counts())
```

## Combining, Joining, and Merging DataFrames

As you are working with multiple datasets, you might find it useful to combine several datasets. There are two main ways to combine datasets: merging and concatenating. First, we ask you to explore **concatenating DataFrames** using Pandas' built-in *pandas.concat*.

You can read more about Concatenation [here][pandas-concat].

While concatenating datasets usually means appending more entries that have the same features (columns), **merging DataFrames** enables appending new features (columns) for the same (or new) entries in your DataFrame. Here, we ask you to **merge two datasets** using Pandas' built-in *pandas.DataFrame.merge*.

You can read more about Merging [here][pandas-merge].

**Joining DataFrames** is similar to merging, but is much less versatile. With `join`, you combine datasets based on index only.

You can read more about Joining [here][pandas-join].

### Concatenation vs. Merging

Concatenation is the most simple operation. If your data have identical column names, then you concatenate.

If you have different numbers of columns, but otherwise share column names, you *might* be able to concatenate, assuming you don't mind lots of missing data in some places.

If your dataframes are quite different but share some common data, then you should merge.

### Merging Example

We can merge the two Beatles data frame on the basis of some shared columns.  It is not necessary for the columns to have the same name, but they need to share the same items (like 'songs').

* In this case the **song** column in the **Spotify data** corresponds to the **Title** column in the **Billboard data**
* In Pandas, the two frames to be joined are called "left" and "right"
* The `left_on` and `right_on` arguments specify the names of the shared columns.
* The `how` argument specifies which keys to include in the resulting dataframe. For an `inner` merge, only rows with matching keys in both dataframes are retained.
* The optional `suffixes` argument tells Pandas how to handle fields that are otherwise named identically in the source files

```python
beatles_combined = pd.merge(right=beatles_spotify, 
         left=beatles_billboard, 
         right_on="song", 
         left_on="Title", 
         how="inner")

beatles_combined
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
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
                        <th>id</th>
                        <th>year</th>
                        <th>album</th>
                        <th>song</th>
                        <th>danceability</th>
                        <th>energy</th>
                        <th>speechiness</th>
                        <th>acousticness</th>
                        <th>liveness</th>
                        <th>valence</th>
                        <th>duration_ms</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th>0</th>
                    <td>A Hard Day's Night</td>
                    <td>1964</td>
                    <td>UK: A Hard Day's Night US: 1962-1966</td>
                    <td>152</td>
                    <td>35</td>
                    <td>Rock, Electronic, Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon, with McCartney</td>
                    <td>8</td>
                    <td>29</td>
                    <td>1964</td>
                    <td>A Hard Day's Night</td>
                    <td>A Hard Day's Night</td>
                    <td>0.590</td>
                    <td>0.805</td>
                    <td>0.0371</td>
                    <td>0.137</td>
                    <td>0.0996</td>
                    <td>0.797</td>
                    <td>154200</td>
                </tr>
                <tr>
                    <th>1</th>
                    <td>All My Loving</td>
                    <td>1963</td>
                    <td>UK: With the Beatles US: Meet The Beatles!</td>
                    <td>124</td>
                    <td>32</td>
                    <td>Pop/Rock</td>
                    <td>McCartney</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    <td>17</td>
                    <td>1963</td>
                    <td>With The Beatles</td>
                    <td>All My Loving</td>
                    <td>0.416</td>
                    <td>0.563</td>
                    <td>0.0298</td>
                    <td>0.207</td>
                    <td>0.3430</td>
                    <td>0.900</td>
                    <td>127853</td>
                </tr>
                <tr>
                    <th>2</th>
                    <td>And I Love Her</td>
                    <td>1964</td>
                    <td>UK: A Hard Day's Night US: Something New</td>
                    <td>152</td>
                    <td>29</td>
                    <td>Pop/Rock</td>
                    <td>McCartney, with Lennon</td>
                    <td>McCartney</td>
                    <td>37</td>
                    <td>33</td>
                    <td>1964</td>
                    <td>A Hard Day's Night</td>
                    <td>And I Love Her</td>
                    <td>0.767</td>
                    <td>0.331</td>
                    <td>0.0337</td>
                    <td>0.640</td>
                    <td>0.0681</td>
                    <td>0.636</td>
                    <td>149693</td>
                </tr>
                <tr>
                    <th>3</th>
                    <td>Ask Me Why</td>
                    <td>1962</td>
                    <td>UK: Please Please Me US: The Early Beatles</td>
                    <td>144</td>
                    <td>24</td>
                    <td>Pop/Rock</td>
                    <td>Lennon, with McCartney</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    <td>6</td>
                    <td>1963</td>
                    <td>Please Please Me</td>
                    <td>Ask Me Why</td>
                    <td>0.605</td>
                    <td>0.394</td>
                    <td>0.0378</td>
                    <td>0.767</td>
                    <td>0.0967</td>
                    <td>0.597</td>
                    <td>146533</td>
                </tr>
                <tr>
                    <th>4</th>
                    <td>Baby It's You</td>
                    <td>1963</td>
                    <td>UK: Please Please Me US: The Early Beatles</td>
                    <td>162</td>
                    <td>17</td>
                    <td>Pop/Rock</td>
                    <td>Bacharach, David, Dixon</td>
                    <td>Lennon</td>
                    <td>-1</td>
                    <td>10</td>
                    <td>1963</td>
                    <td>Please Please Me</td>
                    <td>Baby It's You</td>
                    <td>0.608</td>
                    <td>0.494</td>
                    <td>0.0345</td>
                    <td>0.778</td>
                    <td>0.0926</td>
                    <td>0.879</td>
                    <td>160520</td>
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
                    <td>...</td>
                    <td>...</td>
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
                    <th>16</th>
                    <td>Please Please Me</td>
                    <td>1962</td>
                    <td>UK: Please Please Me US: The Early Beatles</td>
                    <td>120</td>
                    <td>35</td>
                    <td>Merseybeat, Rock and Roll, Pop/Rock</td>
                    <td>Lennon</td>
                    <td>Lennon, with McCartney</td>
                    <td>18</td>
                    <td>7</td>
                    <td>1963</td>
                    <td>Please Please Me</td>
                    <td>Please Please Me</td>
                    <td>0.527</td>
                    <td>0.480</td>
                    <td>0.0280</td>
                    <td>0.334</td>
                    <td>0.0702</td>
                    <td>0.706</td>
                    <td>120853</td>
                </tr>
                <tr>
                    <th>17</th>
                    <td>Roll Over Beethoven</td>
                    <td>1963</td>
                    <td>UK: With the Beatles US: The Beatles Second Album</td>
                    <td>168</td>
                    <td>31</td>
                    <td>Rock and Roll, Pop/Rock</td>
                    <td>Berry</td>
                    <td>Harrison</td>
                    <td>-1</td>
                    <td>22</td>
                    <td>1963</td>
                    <td>With The Beatles</td>
                    <td>Roll Over Beethoven</td>
                    <td>0.351</td>
                    <td>0.749</td>
                    <td>0.0312</td>
                    <td>0.289</td>
                    <td>0.0952</td>
                    <td>0.967</td>
                    <td>165467</td>
                </tr>
                <tr>
                    <th>18</th>
                    <td>There's a Place</td>
                    <td>1963</td>
                    <td>UK: Please Please Me US: Rarities</td>
                    <td>109</td>
                    <td>24</td>
                    <td>Merseybeat, Rock and Roll, Pop/Rock</td>
                    <td>Lennon and McCartney</td>
                    <td>Lennon and McCartney</td>
                    <td>-1</td>
                    <td>13</td>
                    <td>1963</td>
                    <td>Please Please Me</td>
                    <td>There's a Place</td>
                    <td>0.455</td>
                    <td>0.582</td>
                    <td>0.0292</td>
                    <td>0.629</td>
                    <td>0.1720</td>
                    <td>0.927</td>
                    <td>110493</td>
                </tr>
                <tr>
                    <th>19</th>
                    <td>Till There Was You</td>
                    <td>1963</td>
                    <td>UK: With the Beatles US: Meet The Beatles!</td>
                    <td>136</td>
                    <td>22</td>
                    <td>Pop/Rock</td>
                    <td>Willson</td>
                    <td>McCartney</td>
                    <td>-1</td>
                    <td>20</td>
                    <td>1963</td>
                    <td>With The Beatles</td>
                    <td>Till There Was You</td>
                    <td>0.727</td>
                    <td>0.338</td>
                    <td>0.0454</td>
                    <td>0.790</td>
                    <td>0.1050</td>
                    <td>0.646</td>
                    <td>133507</td>
                </tr>
                <tr>
                    <th>20</th>
                    <td>Twist and Shout</td>
                    <td>1963</td>
                    <td>UK: Please Please Me US: The Early Beatles</td>
                    <td>125</td>
                    <td>44</td>
                    <td>Rock and Roll, R&amp;B, Pop/Rock</td>
                    <td>Medley, Russell</td>
                    <td>Lennon</td>
                    <td>13</td>
                    <td>14</td>
                    <td>1963</td>
                    <td>Please Please Me</td>
                    <td>Twist and Shout</td>
                    <td>0.482</td>
                    <td>0.849</td>
                    <td>0.0452</td>
                    <td>0.641</td>
                    <td>0.0414</td>
                    <td>0.937</td>
                    <td>155227</td>
                </tr>
            </tbody>
        </table>
        <p>21 rows × 20 columns</p>
    </td>
</table>

This isn't very useful! There are so few rows in this combined dataset because Pandas could only merge data for columns where the song title was formatted in exactly the same way. For this to work better, we should format the song titles in both frames the same way - perhaps all lowercase - before performing the merge:

```python
beatles_billboard['Title'] = beatles_billboard['Title'].str.lower() # convert all titles in the "Title" column to lowercase
beatles_spotify['song'] = beatles_spotify['song'].str.lower() # convert all titles in the "song" column to lowercase
```

With the song titles updated, let's try that merge again:

```python
beatles_combined = pd.merge(right=beatles_spotify, 
         left=beatles_billboard, 
         right_on="song", 
         left_on="Title", 
         how="inner")

beatles_combined
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
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
                        <th>id</th>
                        <th>year</th>
                        <th>album</th>
                        <th>song</th>
                        <th>danceability</th>
                        <th>energy</th>
                        <th>speechiness</th>
                        <th>acousticness</th>
                        <th>liveness</th>
                        <th>valence</th>
                        <th>duration_ms</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>0</th>
                        <td>a day in the life</td>
                        <td>1967</td>
                        <td>Sgt. Pepper's Lonely Hearts Club Band</td>
                        <td>335</td>
                        <td>12</td>
                        <td>Psychedelic Rock, Art Rock, Pop/Rock</td>
                        <td>Lennon and McCartney</td>
                        <td>Lennon and McCartney</td>
                        <td>-1</td>
                        <td>110</td>
                        <td>1967</td>
                        <td>Sgt. Pepper's Lonely Hearts Club Band</td>
                        <td>a day in the life</td>
                        <td>0.364</td>
                        <td>0.457</td>
                        <td>0.0675</td>
                        <td>0.290</td>
                        <td>0.9220</td>
                        <td>0.175</td>
                        <td>337413</td>
                    </tr>
                    <tr>
                        <th>1</th>
                        <td>a hard day's night</td>
                        <td>1964</td>
                        <td>UK: A Hard Day's Night US: 1962-1966</td>
                        <td>152</td>
                        <td>35</td>
                        <td>Rock, Electronic, Pop/Rock</td>
                        <td>Lennon</td>
                        <td>Lennon, with McCartney</td>
                        <td>8</td>
                        <td>29</td>
                        <td>1964</td>
                        <td>A Hard Day's Night</td>
                        <td>a hard day's night</td>
                        <td>0.590</td>
                        <td>0.805</td>
                        <td>0.0371</td>
                        <td>0.137</td>
                        <td>0.0996</td>
                        <td>0.797</td>
                        <td>154200</td>
                    </tr>
                    <tr>
                        <th>2</th>
                        <td>across the universe</td>
                        <td>1968</td>
                        <td>Let It Be</td>
                        <td>230</td>
                        <td>19</td>
                        <td>Psychedelic folk, Pop/Rock</td>
                        <td>Lennon</td>
                        <td>Lennon</td>
                        <td>-1</td>
                        <td>184</td>
                        <td>1970</td>
                        <td>Let It Be</td>
                        <td>across the universe</td>
                        <td>0.257</td>
                        <td>0.412</td>
                        <td>0.0287</td>
                        <td>0.361</td>
                        <td>0.0702</td>
                        <td>0.858</td>
                        <td>228133</td>
                    </tr>
                    <tr>
                        <th>3</th>
                        <td>act naturally</td>
                        <td>1965</td>
                        <td>UK: Help! US: Yesterday and Today</td>
                        <td>139</td>
                        <td>14</td>
                        <td>Country, Pop/Rock</td>
                        <td>Russell, Morrison</td>
                        <td>Starkey</td>
                        <td>50</td>
                        <td>63</td>
                        <td>1965</td>
                        <td>Help!</td>
                        <td>act naturally</td>
                        <td>0.702</td>
                        <td>0.447</td>
                        <td>0.0308</td>
                        <td>0.366</td>
                        <td>0.1530</td>
                        <td>0.944</td>
                        <td>150373</td>
                    </tr>
                    <tr>
                        <th>4</th>
                        <td>all i've got to do</td>
                        <td>1963</td>
                        <td>UK: With the Beatles US: Meet The Beatles!</td>
                        <td>124</td>
                        <td>9</td>
                        <td>Pop/Rock</td>
                        <td>Lennon</td>
                        <td>Lennon</td>
                        <td>-1</td>
                        <td>16</td>
                        <td>1963</td>
                        <td>With The Beatles</td>
                        <td>all i've got to do</td>
                        <td>0.490</td>
                        <td>0.579</td>
                        <td>0.0344</td>
                        <td>0.217</td>
                        <td>0.0644</td>
                        <td>0.879</td>
                        <td>122573</td>
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
                        <td>...</td>
                        <td>...</td>
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
                        <th>124</th>
                        <td>yellow submarine</td>
                        <td>1966</td>
                        <td>Revolver</td>
                        <td>158</td>
                        <td>24</td>
                        <td>Children's Music, Folk, Pop/Rock</td>
                        <td>McCartney</td>
                        <td>Starkey</td>
                        <td>25</td>
                        <td>152</td>
                        <td>1969</td>
                        <td>Yellow Submarine</td>
                        <td>yellow submarine</td>
                        <td>0.605</td>
                        <td>0.536</td>
                        <td>0.0421</td>
                        <td>0.518</td>
                        <td>0.5280</td>
                        <td>0.688</td>
                        <td>159720</td>
                    </tr>
                    <tr>
                        <th>125</th>
                        <td>yesterday</td>
                        <td>1965</td>
                        <td>UK: Help! US: Yesterday and Today</td>
                        <td>123</td>
                        <td>33</td>
                        <td>Baroque Pop, Pop/Rock</td>
                        <td>McCartney</td>
                        <td>McCartney</td>
                        <td>12</td>
                        <td>68</td>
                        <td>1965</td>
                        <td>Help!</td>
                        <td>yesterday</td>
                        <td>0.332</td>
                        <td>0.179</td>
                        <td>0.0326</td>
                        <td>0.879</td>
                        <td>0.0886</td>
                        <td>0.315</td>
                        <td>125667</td>
                    </tr>
                    <tr>
                        <th>126</th>
                        <td>you like me too much</td>
                        <td>1965</td>
                        <td>UK: Help! US: Beatles VI</td>
                        <td>155</td>
                        <td>12</td>
                        <td>Pop/Rock</td>
                        <td>Harrison</td>
                        <td>Harrison</td>
                        <td>-1</td>
                        <td>65</td>
                        <td>1965</td>
                        <td>Help!</td>
                        <td>you like me too much</td>
                        <td>0.555</td>
                        <td>0.570</td>
                        <td>0.0302</td>
                        <td>0.415</td>
                        <td>0.1910</td>
                        <td>0.899</td>
                        <td>156867</td>
                    </tr>
                    <tr>
                        <th>127</th>
                        <td>you never give me your money</td>
                        <td>1969</td>
                        <td>Abbey Road</td>
                        <td>242</td>
                        <td>7</td>
                        <td>Rock, Pop/Rock</td>
                        <td>McCartney</td>
                        <td>McCartney</td>
                        <td>-1</td>
                        <td>173</td>
                        <td>1969</td>
                        <td>Abbey Road</td>
                        <td>you never give me your money</td>
                        <td>0.335</td>
                        <td>0.416</td>
                        <td>0.0348</td>
                        <td>0.345</td>
                        <td>0.1160</td>
                        <td>0.223</td>
                        <td>242973</td>
                    </tr>
                    <tr>
                        <th>128</th>
                        <td>your mother should know</td>
                        <td>1967</td>
                        <td>Magical Mystery Tour</td>
                        <td>149</td>
                        <td>13</td>
                        <td>Music Hall, Vaudeville Rock, Psychedelic Pop, ...</td>
                        <td>McCartney</td>
                        <td>McCartney</td>
                        <td>-1</td>
                        <td>115</td>
                        <td>1967</td>
                        <td>Magical Mystery Tour</td>
                        <td>your mother should know</td>
                        <td>0.698</td>
                        <td>0.293</td>
                        <td>0.0332</td>
                        <td>0.784</td>
                        <td>0.0936</td>
                        <td>0.724</td>
                        <td>148413</td>
                    </tr>
                </tbody>
            </table>
            <p>129 rows × 20 columns</p>
        </td>
    </tr>
</table>

The result is significantly more useful - Pandas correctly matched many more songs across the two frames. This is a great example of why it is so important to **clean** our data - it is vital to ensure we get the results we expect and want. As you may have noticed, even this change was not enough for Pandas to correctly match every song in the `beatles_spotify` dataframe. Read more about cleaning data with Pandas in the [next section][pandas-clean].

## Making the Most of Pandas

Pandas is a powerful library that makes complex data science easier. There are myriad features designed to handle an almost infinite set of applications. However, especially to those with prior experience in Python, it can feel easier to revert to Python code you already know how to write for complex tasks. This takes away from a crucial element of Pandas - you don't need to reinvent the wheel! For example, you almost never need to write for loops in Pandas, because there are built-in methods that will apply an operation to an entire column or dataframe. To make sure you take full advantage of the benefits Pandas provides, be sure to search the [documentation][pandas-documentation] using the search bar whenever you're attempting something new. You can also check the [cheatsheet][pandas-cheat-sheet] or [W3Schools][w3schools]. Chances are, Pandas has a built-in way to accomplish your goal that will make your life easier.

| **Pandas Basics** | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

[pandas-clean]: 05_Pandas_Clean_Data.md
[pandas-tidy]: 06_Pandas_Tidy_Data.md
[pandas-filter-find-group]: 07_Pandas_Filter_Find_Group.md
[pandas-graphs]: 08_Pandas_Graphs_and_Charts.md
[pandas-networks]: 09_Pandas_Networks.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
[beatles-spotify-spreadsheet]: https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/refs/heads/main/02_Lab_Data/Beatles/M_255_Beatles_Spotify_2025.csv
[beatles-billboard-spreadsheet]: https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv
[pandas-concat]: https://pandas.pydata.org/docs/reference/api/pandas.concat.html
[pandas-merge]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
[pandas-join]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html