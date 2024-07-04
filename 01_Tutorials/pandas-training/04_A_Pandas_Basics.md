# Pandas Basics:  Python for Data Analysis

*Pandas = Python for Data Analysis*

Pandas is a Python library which allows for the creation and manipulation of DataFrames, which are two dimensional objects designed to store data. Below are a few of the many ways in which pandas DataFrames can be modified, filtered, or transformed:

* High-performance manipulation of text, integers, numbers, dates

* Data alignment, reshaping, pivoting

* Intelligent slicing, grouping, and subsetting

* Merging and joining of sets

* Integrated modules for analysis, plots, visualizations, maps, networks

Read the [official documentation](https://pandas.pydata.org/about/).

Find tutorials at [W3Schools](https://www.w3schools.com/python/pandas/default.asp).

A helpful [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

| | Contents of this Tutorial |
|---|---|
| 1. | [**Introduction to DataFrames**](#introduction-to-dataframes-1) |
| 2. | [**Working with Rows**]() |
| 3. | [**Working with Columns**]() |
| 4. | [**Cleaning and Checking Data**]() |
| 5. | [**Sort, Count, and Filter**]() |
| 6. | [**Combine and Merge Data Frames**]() |

# Introduction to DataFrames

Pandas **data frames** are the basic unit upon which all operations take place.  Data frames are like spreadsheets, with columns and rows.

Indeed, Pandas can easily import spreadsheets in **CSV** (comma separated values) format.  We will also import data from databases in **JSON** format (Java Script Object Notation), similar to a Python dictionary.  There are special scripts for working with JSON, too.

Pandas can export as well as import these formats (among others).

## Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

## Meet the Beatles

The Pandas library has a vast array of tools for sorting, filtering, grouping, analyzing, and even visualizing tabluar data of various kinds:  strings, booleans, integers, floats, dates, and so on.  We begin with data about the albums and songs issued by the Beatles. The data are drawn from two sources:

* A set from **Spotify** includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1CBiNbxqF4FHWMkFv-C6nl7AyOJUFqycrR-EvWvDZEWY/edit#gid=953807965).

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

## Inspect the Data Frame

A quick look at the file as a dataframe using the `head()` method:

```python
beatles_billboard.head(25)  # Shows the first 25 rows
```

Now we can look at the data in various ways to see what is here. The first column is the `index` (and begins with "0").


* `beatles_spotify.info()` will show the names, number and data types of the columns
* `beatles_spotify.shape` will tell us the size of our frame:  how many **rows and columns**, like `(193, 11)`.  Note:  normally these methods are followed by `()`.  This one is not.
* `beatles_spotify.describe()` delivers basic statistical information about the set, such as count, average, mean, standard deviation, and basic percentiles.

![Alt text](<images/pd 1-1.png>)

## Working with Rows

By default Pandas shows only the first and last five rows of any data frame.  There are various ways to see others:

* **All rows**, set `pd.set_option('display.max_rows', None)` or `pd.options.display.max_rows = 9999` before you display the frame.
* **Head** rows (default of five from the start, but can be any number):  `beatles_spotify.head(20)`
* **Tail** rows (default of five from the end, but can be any number):  `beatles_spotify.tail(20)`
* **Sample** a random sample of rows (default of 1 , but can be any number):  `beatles_spotify.sample(20)`


### Selecting Rows:  `loc` and `iloc` 

`df.loc` and `df.iloc` are _not_ the same!

#### iloc for Index-based slices

* **iloc**: to select rows by **index number** (the left-hand column) use `iloc`. A good way to remember this is that `iloc` will correspond to the *integer* value of the index (which starts with zero). The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  Thus rows 10-15 (and all columns) of our dataframe would be `beatles_spotify.iloc[10:15, :]`.  

Note:  the first number is *inclusive* but the second is *exclusive*.  So `10:15` will yield rows 10, 11, 12, 13, 14, but *not* 15.

#### loc for Label-based slices

* **loc**: to select rows by **label** of the left-hand column (as when you might have an index of strings), use `loc`.  This is useful when our index is a string rather than a number.  It is especially useful for working with columns.

Pandas Cheat Sheet:  [here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Try:

```python
beatles_spotify.iloc[10:15,]
```

## Working with Columns

We now start to look more closely at the columns.

#### iloc for Index-based slices

It's possible to select colulmns with `iloc`, as shown above for rows. The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  The first column (and all rows) would be `beatles_spotify.iloc[:, 0]`. Thus the first `five` columns (and all rows) of our dataframe would be `beatles_spotify.iloc[:, 0:6]`.  Note:  the first number is *inclusive* but the second is *exclusive*.

Want to count from the *end*?  `-1` is the *last* column. So `beatles_spotify.iloc[:, -1]`

#### Working with Columns by Name (or 'label')

* **column names** as a list:  `beatles_spotify.columns`
* **rename a column**:  `beatles_billboard["album"] = beatles_billboard["Album.debut"]` or `beatles_billboard.rename(columns = {'Album.debut':'album'})`
* **drop a column**: `beatles_billboard.drop(columns=['Album.debut'])`.  Note that these must be presented as a list, even if there is only one!
* **add a column**; in this case we might want to create a column based on condition in another (like "Instrumental" as a Boolean ):   
* **data types** of the columns:  `beatles_spotify.dtypes`.  Note that we can do something similar with `beatles_spotify.info()`.  To change data type, see [Cleaning and Checking Data](), in Part B.
* **sort the columns** alphabetically:  `beatles_spotify.columns.sort_values()`
* **move or reorganize columns** by specifying a new order; this would also work to drop certain columns ommitted from the list:

```python
column_list = ['Year', 'Title', 'Album.debut', 'Duration', 'Other.releases' 'Genre', 'Songwriter', 'Lead.vocal', 'Top.50.Billboard']
beatles_billboard_reordered = beatles_billboard[column_list]

beatles_billboard_reordered
```

Note that this could also be done using the `index` values for the columns.

#### A Column is a Series

An individual column is called a **Series**
* **One column**: `beatles_spotify["year"]`
* Show all the unique entries in a single column: `beatles_spotify["album"].unique()`
* Count the **number of unique values** in a single column: `beatles_spotify["album"].nunique()`
* Count the **number of entries** for each value in a column:  `beatles_spotify["album"].value_counts()`

Pandas Cheat Sheet:  [here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Show the columns of our df:

```python
beatles_billboard.columns
```

Or the data types for each column:

```python
beatles_spotify.dtypes
```

Or show the column names sorted in a list:

```python
beatles_spotify.columns.sort_values()
```

Make a new df with just a subset of columns.  We first make a `list` of the required columns, then we pass that list inside `[]` against the original df.  In effect we are saying: `billboard` where `[these columns]` are `True`.

```python
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```

![Alt text](<images/pdf 2.png>)

[deleted something about an individual column being a series because it was redundant, leaving note to explain image below, since I can't see it yet]

![Alt text](<images/pd 3.png>)

## Sort and Count

Pandas affords many ways to take stock of your data, with built-in functions counts of values, means, averages, and other statistical information.  Many of these are detailed on the [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf). But the following will be useful for us:

### Sort Values

**Sort Values** in any column.  This ascending (alphabetically or numerically) by default, but can be reversed.  Example:  

```python
beatles_spotify.sort_values("danceability")
```

### Count Values

**Count Values** in any column.  For example: 

```python
beatles_billboard["Album.debut"].value_counts()
```

### Subset or Slice of Rows or Columns

It is also possible to **select some slice of rows or columns** by name or index position using `df.loc()`, or `df.iloc()`.  See above, and the [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

## Combining and Spliting Columns

Sometimes it is necessary to combine related columns into a new column, with values stored as a *list*. Conversely sometimes it might be necessary to split the values stored in one column into several columns (for example, if a column has first and last names, you may want one column for first names and one column for last names). This is easily done with Pandas and Python.

### Combine Two Columns as String

Two columns can be combined into a single one with a lambda function and `apply` (which runs the function on each row in turn):

```python
combine_cols = lambda row: row['Songwriter'] + ": "  + row['Title'] 
beatles_billboard['Author-Title'] = beatles_billboard.apply(combine_cols, axis=1)

beatles_billboard['Author-Title'][0]
```
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<div>
<pre>'Lennon, McCartney, Harrison and Starkey: 12-Bar Original'</pre>
</div></table>

## Combining, Joining, and Merging DataFrames

As you are working with multiple datasets, you might find it useful to combine several datasets. There are two main ways to combine datasets: merging and concatenating. First, we ask you to explore **concatenating DataFrames** using Pandas' built-in *pandas.concat*.

You can read more about Concatenation [here](https://pandas.pydata.org/docs/reference/api/pandas.concat.html).

While concatenating datasets usually means appending more entries that have the same features (columns), **merging DataFrames** enables appending new features (columns) for the same (or new) entries in your DataFrame. Here, we ask you to **merge two datasets** using Pandas' built-in *pandas.DataFrame.merge*.

You can read more about Merging [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html).

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

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<div>
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
</div>
</td>
</table>
</div>

This isn't very useful! There are so few rows in this combined dataset because Pandas could only merge data for columns where the song title was formatted in exactly the same way. For this to work better, we should format the song titles in both frames the same way - perhaps all lowercase - before performing the merge:

```python
beatles_billboard["Title"] = beatles_billboard['Title'].str.lower() # convert all titles in the "Title" column to lowercase
beatles_spotify['song'] = beatles_spotify['song'].str.lower() # convert all titles in the "song" column to lowercase
```

Let's try that merge again:

```python
beatles_combined = pd.merge(right=beatles_spotify, 
         left=beatles_billboard, 
         right_on="song", 
         left_on="Title", 
         how="inner")
beatles_combined
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<div>
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
</div>
</td>
</table>
</div>

The result is significantly more useful - Pandas correctly matched many more songs. This is a great example of why it is so important to **clean** our data - it is vital to ensure we get the results we expect and want. As you may have noticed, even this change was not enough for Pandas to correctly match every song in the `beatles_spotify` dataframe. Read more about cleaning data with Pandas in the [next section][part-b].

<span style="color: red">
[ --- deleting the section because it's been replaced by the above example -- ]
<br><br>
 But instead we could use billboard data and find the *mean ranking* of those in the top 50 by year.

<pre>
top_50 = beatles_billboard[beatles_billboard["Top.50.Billboard"] > 0].sort_values('Year')
top_50.tail()
</pre>

![Alt text](<images/pd 5.png>)

[ --- end deleted section ---]</span>

[part-b]: #