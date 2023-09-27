# Pandas:  Python for Data Analysis

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

## Data Frames

Pandas **data frames** are the basic unit upon which all operations take place.  Data frames are like spreadsheets, with columns and rows.

Indeed, Pandas can easily import spreadsheets in **CSV** (comma separated values) format.  We will also import data from databases in **JSON** format (Java Script Object Notation), similar to a Python dictionary.  There are special scripts for working with JSON, too.

Pandas can export as well as import these formats (among others).

## Meet the Beatles

The Pandas library has a vast array of tools for sorting, filtering, grouping, analyzing, and even visualizing tabluar data of various kinds:  strings, booleans, integers, floats, dates, and so on.  We begin with data about the albums and songs issued by the Beatles. The data are drawn from two sources:

* A set from **Spotify** includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1CBiNbxqF4FHWMkFv-C6nl7AyOJUFqycrR-EvWvDZEWY/edit#gid=953807965).

* A set compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs:  author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts.  View these data on [Github]('https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv').

We will work with both of these sets, and in the process learn how to inspect, clean, combine, filter, group, and analyze the information they contain.

We give the URL of the CSV file a name (simply for convenience), then pass that name to the `read_csv('source_file_name')` method, and name the resulting data frame.

```
beatles_spotify_csv = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCv45ldJmq0isl2bvWok7AbD5C6JWA0Xf1tBqow5ngX7_ox8c2d846PnH9iLp_SikzgYmvdPHe9k7G/pub?output=csv'

beatles_spotify = pd.read_csv(beatles_spotify_csv)

```

and 

```
beatles_billboard_csv = 'https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv'

beatles_billboard = pd.read_csv(beatles_billboard_csv)
```

## Inspect the Data Frame

A quick look at the file as a dataframe:

```
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

`df.loc` and `dc.iloc` are _not_ the same!

* **iloc** to select rows by **index number** (the left-hand column) use `iloc`. The syntax puts rows before columns, as in `beatles_spotify.iloc[startrow:endrow, startcolumn:endcolumn]`.  Thus rows 10-15 (and all columns) of our dataframe would be `beatles_spotify.iloc[10:15, :]`.  Note:  the first number is *inclusive* but the second is *exclusive*.  So `10:15` will yield rows 10, 11, 12, 13, 14, but *not* 15.
* **loc** to select rows by **label** of the left-hand column (as when you might have an index of strings), use `loc`.  This is useful when our index is a string rather than a number.  It is especially useful for working with columns.

Pandas Cheat Sheet:  [here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).

Try:

    beatles_spotify.iloc[10:15,]

## Working with Columns


We now start to look more closely the columns.


* **column names** as a list:  `beatles_spotify.columns`
* **rename a column**:  `beatles_billboard["album"] = beatles_billboard["Album.debut"]` or `beatles_billboard.rename(columns = {'Album.debut':'album'})`
* **drop a column**: `beatles_billboard.drop(columns=['Album.debut'])`.  Note that these must be presented as a list, even if there is only one!
* **add a column**; in this case we might want to create a column based on condition in another (like "Instrumental" as a Boolean ):   
* **data types** of the columns:  `beatles_spotify.dtypes`.  Note that we can do something similar with `beatles_spotify.info()`.  To change data type, see Cleaning and Checking Data, below.
* **sort the columns** alphabetically:  `beatles_spotify.columns.sort_values()`
* **move or reorganize columns** by specifying a new order; this would also work to drop certain columns ommitted from the list:

```
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```


An individual column is called a **series**
* **One column**:  `beatles_spotify["year"]`
* Count the **number of unique values** in a single column: `beatles_spotify["album"].nunique()`
* Count the **number of entries** for each value in a column:  `beatles_spotify["album"].value_counts()`

Pandas Cheat Sheet:  [here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).


Show the columns of our df:

    beatles_billboard.columns

Or the data types for each column:

    beatles_spotify.dtypes

Or sort the column names as a list:

    beatles_spotify.columns.sort_values()

Make a new df with just a subset of columns.  We first make a `list` of the required columns, then we pass that list inside `[]` against the original df.  In effect we are saying: `billboard` where `[these columns]` are `True`.

```
column_list = ['Title', 'Year', 'Album.debut', 'Genre','Songwriter', 'Top.50.Billboard']
beatles_billboard_short = beatles_billboard[column_list]
beatles_billboard_short
```
![Alt text](<images/pdf 2.png>)

Meanwhile an individual column is represented as a "Series"

```
beatles_spotify["song"]

```
![Alt text](<images/pd 3.png>)


## Cleaning and Checking Data

Missing data or data encoded as the wrong type will result in errors of various kinds.  See more [here](https://www.w3schools.com/python/pandas/pandas_cleaning.asp).

### The NAN Problem

In Python there is a difference between a "0" and nothing.  The latter is a Null, which represents "no data at all."  Nulls will result in errors when you attempt to perform some operation on them.  You cannot add to or compare something to a Null.  Nor can you test whether a Null contains some set of characters or matches a word. 

* **Find the NaN's**:  `df[df.isna().any(axis=1)]`, or for the billboard data:  `beatles_billboard[beatles_billboard.isna().any(axis=1)]`.  

* **Fill the NaN's**. If you are performing mathematical operations, You can fill missing values with some default number or string. The solution will probably vary from one column to the next (since some are integers, some dates, and are text):  `beatles_billboard.fillna("-")` would fill *all NaN* with the same string.  But we could instead try something that would be more meaningful.  For example: `beatles_billboard['Album.debut'].fillna("unreleased", inplace=True)`
* If you are trying to filter a data frame by a particular keyword or condition, you can treat the Nulls as "False" and thereby ignore them.

### Duplicate Rows

Duplicate rows can also create errors, or distort your results.  Find them:  `duplicate = beatles_billboard[beatles_billboard.duplicated()]
duplicate` (in this case there are none).  Remove them automatically with `beatles.drop_duplicates()`

### Wrong Data Type

Wrong data type in a given column is another common error (particularly since Pandas attempts to guess the correct data type when importing from CSV or JSON).  In our beatles_spotify dataset, notice that the data type for 'energy' is `object`, which in the context of Pandas means it is a Python `string`.  As such we cannot perform mathematical operations on it. Change the data type with the `astype()` method:

```
beatles_spotify['energy'] = beatles_spotify['energy'].astype(np.float64)
```

The same thing can happen with **date=time** information.  In our orignal datasets, the "Year" columms are in fact integers.  This works fine for basic sorting.  But Pandas has an intelligent format for working with date-time information that allows us to sort by month-day-year, or create 'bins' representing quarters, decades, centuries.  

So you will need to check the original data type, then convert to strings before converting to **date-time format**.  For example:

```

beatles_billboard["Year"] = beatles_billboard["Year"].astype(str)

```

Then convert that string to **datetime** format (in this case, in a new column, for comparison):

```
beatles_billboard["Year_DT"] = pd.to_datetime(beatles_billboard["Year"], format='%Y')
```
And then reorder the columns for clarity:

```
beatles_billboard_sorted = beatles_billboard.iloc[:, [0, 1, 9, 3, 4, 5, 6, 7, 8]]
beatles_billboard_sorted.head()

```
### Wrong or Inconsistent Format

For example when spelling or capitalization are different for the same item across many rows or columns.  There are Pandas methods to help with this process. 

### Incorrect Data

This is more difficult, since you will need to know the details of the errors, and how to correct them.  But Python and Pandas can help you automate the process.

See more [here](https://towardsdatascience.com/simplify-your-dataset-cleaning-with-pandas-75951b23568e).
 

## Cleaning Data with Functions

Let's imagine that you have a dataset in which a particular column contains data that are inconsistent:  in some places for the name of an artist you have `John Lennon`, and other places `John Lenin`.  You could correct them by hand in a Spreadsheet.  But there is an easier way with a Python **function**.

You will first want to understand all the values you are trying to correct.  So here you would use Pandas/Python **set** method on all the values of the df["column"] in question:

`set(df["Artist"])`

Now that you know what the problem values are, write a **function** that corrects `John Lenin` to `John Lennon`.  If you don't recall **functions** see **Python Basic Notebook**!
```

def name_check:
    if df["Artist"] == "John Lenin":
        return "John Lennon"
```
In this case the **return** statement makes the result available for the next step in the process.

But how to run this over **all rows** of a data frame?  We can easily do this with the **apply** method. In effect it **apply** allows us to automatically pass over all rows in the data frame, transforming only the column we select.  

`df['column'] = df['column'].apply(name_check)`

Note that we could use this approach not only for correcting data, but for creating **new columns** based on **existing columns**.  For example:  a Boolean column (True/False) based on the result of the contents of another column.  Here the new column will report True for any row where the column "artist" contains the string "Lennon".  

`df['By_Lennon'] = df['artist'].str.contains("Lennon")`

We can then use the Boolean column to filter the entire frame (see below).

Try some out:

NANs anywhere:

    beatles_billboard[beatles_billboard.isna().any(axis=1)]

Replace NA's in Album column with 'unreleased'

```
beatles_billboard['Album.debut'].fillna("unreleased", inplace=True)
beatles_billboard.head(25)
```

Convert the year column to an integer, then use the Pandas "year" format to make an intelligent date out of it, and sort the columns according to their `index` positions:

```
beatles_billboard["Year"] = beatles_billboard["Year"].astype(int)
beatles_billboard["Year_DT"] = pd.to_datetime(beatles_billboard["Year"], format='%Y')
beatles_billboard_sorted = beatles_billboard.iloc[:, [0, 1, 9, 3, 4, 5, 6, 7, 8]]
beatles_billboard_sorted.head()
```

You can think of some others!

## Sort, Count and Filter

Pandas affords many ways to take stock of your data, with built-in functions counts of values, means, averages, and other statistical information.  Many of these are detailed on the [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).  But the following will be useful for us:

### Sort Values

**Sort Values** in any column.  This ascending (alphabetically or numerically) by default, but can be reversed.  Example:  

```
beatles_spotify.sort_values("danceability")
```

### Count Values
**Count Values** in any column.  For example: 

```
beatles_billboard["Album.debut"].value_counts()
```

### Subset or Slice of Rows or Columns

It is also possible to **select some slice of rows or columns** by name or index position using `df.loc()`, or `df.iloc()`.  See above, and the Pandas Cheat Sheet.

### Filter Rows

**Filter rows based on some logical condition or string** in one or more columns.  There are several possibilities.  

#### Logical Tests and Boolean Series

Testing a single column for a logical condition returns a Boolean series of True/False values for all 'rows':

```
beatles_billboard['Year'] > 1969
```

It is then possible to apply this Boolean series as a kind of 'mask' against the entire dataframe.  In effect we are asking for a slice of the dataframe where the given column is  `True`:

```
beatles_billboard[beatles_billboard['Year'] > 1969]
```

We can even *reverse* the Boolean values, thus returning a dataframe that matches everything *except* the rows matching the given condition (note the extra parenthesis to clarify the syntax):

```
beatles_billboard[~(beatles_billboard['Year'] > 1964)]
```


## Bins 

Another important tool is being able to categorize data. Oftentimes, this is done through "binning" -- assigning the entry to one of several discrete categories based on some continuous value. 

### Boolean Bins

In the following example, we will use the values in the "danceability" column (expressed as floats ranging from 0 to 1) to classify a track as a Dance Tune (0 => Not a Dance Tune; 1 => Definitely a Dance Tune). 

Here we are using the *Beatles_Spotify* data:

First, you need to think about picking a certain threshold value. Is Get Back by the Beatles (0.628 danceability rating) a Dance Tune? How about Doctor Robert (0.392 danceability score)? Use the code cell below to **pick your danceability threshold value** and save it as a variable. 

```
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.000, 0.500, "right"), "Dance Tune"] = 0
beatles_spotify.loc[beatles_spotify["danceability"].astype(float).between(0.510, 1.000, "right"), "Dance Tune"] = 1
beatles_spotify
```

### Categorical Bins

Sometimes, a simple True/False ranking isn't enough. For example, the "tempo" column provides the Beat Per Minute musical tempo value for a given track; this value typically ranges between 1 and ~500 bpm. While it is possible to classify tracks into Slow and Not Slow, it might be more useful to, for example, categorize them into "Slow", "Medium", and "Fast". 

Pandas and Python can easily do this with the `cut` method, which allows you to set the boundaries and labels of the bins either automatically:

```
# find the minimum and maximum value in the given column:
min_value = beatles_billboard['Duration'].min()
max_value = beatles_billboard['Duration'].max()
# create labels for the bins
labels = ['short', 'medium', 'long']

# Use the cut function to create three bins, and assign the results to a new column
beatles_billboard['Duration_Category'] = pd.cut(beatles_billboard['Duration'], bins=3, labels=labels, include_lowest=True)
beatles_billboard['Duration_Category']
0       short
1      medium
2       short
```
Or filter the results according to a logical condition:

```
beatles_billboard[beatles_billboard['Duration_Category'] == 'long']

```


## Searching for Strings and SubStrings

Note the differences between `str.contains()`, which matches **full contents of cell** and `isin(["sub_string_1", "sub_string_2"])`, which matches **any number of shorter strings** within a cell.

#### `The str.contains()` Method

For example here we filter to tracks with "unreleased" in the `Album.debut` column. The **items within "[]" become a Boolean series**:

```
[beatles_billboard['Album.debut'].str.contains("unreleased")]
```

This is then used to **mask** the complete data trame (rows with "True" are retained), which happens when we append this list to the name of the dataframe itself.  In effect we are saying "return df where [these conditions] are True"

```
beatles_billboard[beatles_billboard['Album.debut'].str.contains("unreleased")]
```

But we can also **invert the Boolean series**, so that the string "unreleased" is **False**.  "~" (the tilde) is used to invert the mask:

```
beatles_billboard[~beatles_billboard['Album.debut'].str.contains("unreleased")]
```

Or we can **filter with two conditions** (the above, plus "Year < 1965".  Notice that in this case each condition (which will be a set of True/False values) is surrounded in `()`, and then together linked by `&` as part of the complete `[]` test.

```
beatles_billboard[(beatles_billboard['Album.debut'].str.contains("unreleased")) & (beatles_billboard['Year'] < 1965)]
```
#### The `isin()` Method

The **isin()** method works if you are looking for *one or more substrings in a given cell*.  Note that the strings must be presented as a "list", thus **`isin(["substring_1", "substring_2"])`**.  For example, this, which returns either "Lennon" OR "McCartney" (in any context within that column):

```
beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```



## Combining and Spliting Columns

Sometimes it is necessary to combine related columns into a new column, with values stored as a *list*.  Conversely sometimes it might be necessary to take split values stored as a long string into a list of values.  This is easily done with Pandas and Python.

### Split String into List

The column contains a list (just showing one cell for brevity):

```beatles_billboard['Genre'][1]
'Psychedelic Rock, Art Rock, Pop/Rock'
```

Split it (just showing one cell for brevity):

```
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.split(', ')
beatles_billboard['Genre'][1]
['Psychedelic Rock', 'Art Rock', 'Pop/Rock']
```

### Combine Two Columns as String

Two columns can be combined into a single one with a lambda function and `apply` (which runs the function on each row in turn):

```
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

```
beatles_combined = pd.merge(right=beatles_spotify, 
         left=beatles_billboard, 
         right_on="song", 
         left_on="Title", 
         how="left")
beatles_combined
```

![Alt text](<images/pd 4.png>)

This is not very meaningful!  But instead we could use billboard data and find the *mean ranking* of those in the top 50 by year.

```
top_50 = beatles_billboard[beatles_billboard["Top.50.Billboard"] > 0].sort_values('Year')
top_50.tail()
```

![Alt text](<images/pd 5.png>)



# Groupby Functions

Learn more about Groupby [here](https://medium.com/towards-data-science/pandas-groupby-aggregate-transform-filter-c95ba3444bbb).

**Groupby** functions allow you to organize and analyze data that share certain features.  For instance, we could find the **number of songs per album**:

```
beatles_billboard.groupby("Album.debut")["Title"].count()
```

![Alt text](<images/pd 6.png>)

Or focus on the relative activity of Lennon and McCartney across the years, first by filtering to only their work:

```
beatles_jl_pm = beatles_billboard[beatles_billboard['Songwriter'].isin(["Lennon", "McCartney"])]
```

Then find the 'groups':

```
grouped = beatles_jl_pm.groupby(["Songwriter"])
grouped.groups
```

And inspect a single "group":

```
grouped.get_group("Lennon")
```

And finally to compare the outputs by grouping via two columns, songwriter and year.

"Size" considers _all_ the rows (even ones with NaNs).

```
beatles_jl_pm.groupby(['Songwriter','Year']).size()
```

"Count" includes only the rows with valid data.

```
beatles_jl_pm.groupby(['Songwriter','Year']).count()
```

There are many other functions that can be applied to aggregate, filter and transform data within groups!  See the essay above for a guide.

A count of track titles per album:

```
beatles_billboard.groupby("Album.debut")["Title"].count()
```

Group by Songwriter and Year, showing counts for each:

```
beatles_jl_pm.groupby(['Songwriter','Year']).size()
```

![Alt text](<images/Pd 7.png>)


## Charts and Graphs

Through libraries like **matplot**, Pandas can quickly produce histograms, charts, and graphs of various kinds (these can even be saved as PNG files for publications).

For example: a histogram of the count of songs per albumn.

```
beatles_spotify["album"].hist(figsize=(10, 5), bins=100)
plt.xlabel("Album")
plt.xticks(rotation = 60) # Rotates X-Axis Ticks by 60-degrees
plt.ylabel("Song Count")
plt.show()
```

![Alt text](<images/pd 8.png>)


Various built-in math functions allow us to run basic statistics.  Libraries like `numpy` permit many more!



```
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