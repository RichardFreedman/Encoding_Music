# Pandas Basics:  Python for Data Analysis

Pandas is a Python library which allows for the creation and manipulation of DataFrames, which are two dimensional objects designed to store data. Below are a few of the many ways in which pandas DataFrames can be modified, filtered, or transformed. 

Pandas = Python for Data Analysis
* High-performance manipulation of text, integers, numbers, dates
* Data alignment, reshaping, pivoting
* Intelligent slicing, grouping, and subsetting
* Merging and joining of sets
* Integrated modules for analysis, plots, visualizations, maps, networks

[Read more](https://pandas.pydata.org/about/).

[Tutorials](https://www.w3schools.com/python/pandas/default.asp).

[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Contents of this Tutorial

### Introduction to Data Frames
### Working with Rows
### Working with Columns
### Cleaning and Checking Data
### Sort, Count, and Filter
### Combine and Merge Data Frames


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

A quick look at the file as a dataframe:

```python
beatles_billboard = pd.read_csv(beatles_billboard_csv)
beatles_billboard.head(25)
```

Now we can look at the data in various ways to see what is here. The first column is the `index` (and begins with "0").


* `beatles_spotify.info()` will show the names, number and data types of the columns
* `beatles_spotify.shape` will tell us the size of our frame:  how many **rows and columns**, like `(193, 11)`.  Note:  normally these methods are followed by `()`.  This one is not.
* `beatles_spotify.describe()` delivers basic statistical information about the set, such as count, average, mean, standard deviation, and basic percentiles.

![Alt text](<images/pd 1-1.png>)

## Working with Rows

By default Pandas shows only the first and last five rows of any data frame.  There are various ways to see others:

* **All rows**, set `pandas.set_option('display.max_rows', None)` or `pd.options.display.max_rows = 9999` before you display the frame.
* **Head** rows (default of five from the start, but can be any number):  `beatles_spotify.head(20)`
* **Tail** rows (default of five from the end, but can be any number):  `beatles_spotify.tail(20)`
* **Sample** a random sampling of x rows:  `beatles_spotify.sample(20)`


### Selecting Rows:  `loc` and `iloc` 

`df.loc` and `df.iloc` are _not_ the same!

#### iloc for Index-based slices
* **iloc** to select rows by **index number** (the left-hand column) use `iloc`. A good way to remember this is that `iloc` will correspond to the *integer* value of the index (which starts with zero). The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  Thus rows 10-15 (and all columns) of our dataframe would be `beatles_spotify.iloc[10:15, :]`.  

Note:  the first number is *inclusive* but the second is *exclusive*.  So `10:15` will yield rows 10, 11, 12, 13, 14, but *not* 15.

#### loc for Label-based slices
* **loc** to select rows by **label** of the left-hand column (as when you might have an index of strings), use `loc`.  This is useful when our index is a string rather than a number.  It is especially useful for working with columns.

Pandas Cheat Sheet:  [here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Try:

```python
beatles_spotify.iloc[10:15,]
```

## Working with Columns

We now start to look more closely the columns.

#### iloc for Index-based slices

It's possible to select colulmns with `iloc`, as shown above for rows. The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  The first column (and all rows) would be `beatles_spotify.iloc[:, 0]`. Thus the first `five` columns (and all rows) of our dataframe would be `beatles_spotify.iloc[:, 0:6]`.  Note:  the first number is *inclusive* but the second is *exclusive*.

Want to count from the *end*?  `-1` is the *last* column. So `beatles_spotify.iloc[:, -1]`

#### Working with Columns by Name (or 'label')

* **column names** as a list:  `beatles_spotify.columns`
* **rename a column**:  `beatles_billboard["album"] = beatles_billboard["Album.debut"]` or `beatles_billboard.rename(columns = {'Album.debut':'album'})`
* **drop a column**: `beatles_billboard.drop(columns=['Album.debut'])`.  Note that these must be presented as a list, even if there is only one!
* **add a column**; in this case we might want to create a column based on condition in another (like "Instrumental" as a Boolean ):   
* **data types** of the columns:  `beatles_spotify.dtypes`.  Note that we can do something similar with `beatles_spotify.info()`.  To change data type, see Cleaning and Checking Data, below.
* **sort the columns** alphabetically:  `beatles_spotify.columns.sort_values()`
* **move or reorganize columns** by specifying a new order; this would also work to drop certain columns ommitted from the list:

```python
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```
Note that this could also be done using the `index` values for the columns.

#### A Column is a Series

An individual column is called a **series**
* **One column**:  `beatles_spotify["year"]`
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

Or sort the column names as a list:

`python
beatles_spotify.columns.sort_values()
```

Make a new df with just a subset of columns.  We first make a `list` of the required columns, then we pass that list inside `[]` against the original df.  In effect we are saying: `billboard` where `[these columns]` are `True`.

```python
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```
![Alt text](<images/pdf 2.png>)

Meanwhile an individual column is represented as a "Series"

```python
beatles_spotify["song"]

```
![Alt text](<images/pd 3.png>)



## Sort and Count

Pandas affords many ways to take stock of your data, with built-in functions counts of values, means, averages, and other statistical information.  Many of these are detailed on the [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).  But the following will be useful for us:

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

It is also possible to **select some slice of rows or columns** by name or index position using `df.loc()`, or `df.iloc()`.  See above, and the Pandas Cheat Sheet.



## Combining and Spliting Columns

Sometimes it is necessary to combine related columns into a new column, with values stored as a *list*.  Conversely sometimes it might be necessary to take split values stored as a long string into a list of values.  This is easily done with Pandas and Python.


### Combine Two Columns as String

Two columns can be combined into a single one with a lambda function and `apply` (which runs the function on each row in turn):

```python
combine_cols = lambda row: row['Songwriter'] + ": "  + row['Title'] 
beatles_billboard['Author-Title'] = beatles_billboard.apply(combine_cols, axis=1)
beatles_billboard['Author-Title'][0]
'Lennon, McCartney, Harrison and Starkey: 12-Bar Original'
```

## Combining, Joining, and Merging DataFrames

As you are working with multiple datasets, you might find it useful to combine several datasets. There are two main ways to combine datasets: merging and concatenating. First, we ask you to explore **concatenating DataFrames** using Pandas' built-in *pandas.concat*.

You can read more about Concatenation [here](https://pandas.pydata.org/docs/reference/api/pandas.concat.html).

While concatenating datasets usually means appending more entries that have the same features (columns), **merging DataFrames** enables appending new features (columns) for the same (or new) entries in your DataFrame. Here, we ask you to **merge two datasets** using Pandas' built-in *pandas.DataFrame.merge*.

You can read more about Merging [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html).

We can merge the two Beatles data frame on the basis of some shared columns.  It is not necessary for the columns to have the same name, but they need to share the same items (like 'songs')

* In this case the **song** column in the **Spotify data** corresponds to the **Title** column in the **Billboard data**
* In Pandas, the two frames to be joined are called "left" and "right"
* The "suffixes" argument tells Pandas how to handle fields are otherwise named identically in the source files

```python
beatles_combined = pd.merge(right=beatles_spotify, 
         left=beatles_billboard, 
         right_on="song", 
         left_on="Title", 
         how="left")
beatles_combined
```

![Alt text](<images/pd 4.png>)

This is not very meaningful!  But instead we could use billboard data and find the *mean ranking* of those in the top 50 by year.

```python
top_50 = beatles_billboard[beatles_billboard["Top.50.Billboard"] > 0].sort_values('Year')
top_50.tail()
```

![Alt text](<images/pd 5.png>)

