# Pandas:  Clean and Tidy Data

| Part A | Part B | Part C |
|--------|--------|--------|
| [Pandas Basics][part-a] | **Clean and Tidy Data** | [Finding and Grouping Data][part-c] |

<!--In this tutorial we explore various ways of cleaning data. We also explore ways to make your data follow the "Tidy Data" principles, which will vastly simplify other work. The key concept here is to *un-nest* the various cells that might contain multiple data points. "One observation or event per row" is the preferred format for Tidy Data.--><span style="color:red">Replace this ¶</span><br><br>

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

|    | Contents of this Tutorial                                                      | 
|----|--------------------------------------------------------------------------------|
| 0. | [**Defining Clean Data and its Uses**](#) |
| 1. | [**Clean and Tidy Principles**](#)                  |
| 5. | [**Wrong or Inconsistent Format**](#) |
| 2. | [**NaN Problem**](#)                                    |
| 3. | [**Duplicate Rowss**](#)                              |
| 4. | [**Wrong Data Type**](#)                                          |
| 6. | [**Incorrect Data**](#) |
| 7. | [**Nested Lists and Tuples in Cells**](#) |
| 8. | [**Tuple Trouble (and How to Cure It)**](#) |
| 9. | [**Explode, Melt, and Pivot**](#) |

### Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

### Meet the Beatles

We continue with our data about The Beatles:

* A set from **Spotify** that includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1CBiNbxqF4FHWMkFv-C6nl7AyOJUFqycrR-EvWvDZEWY/edit#gid=953807965).

* A set compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs:  author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts.  View these data on [Github]('https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv').

We will work with both of these sets, and in the process learn how to clean and 'tidy' the data in preparation for other operations.

Get the Spotify data:

```python
beatles_spotify_csv = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCv45ldJmq0isl2bvWok7AbD5C6JWA0Xf1tBqow5ngX7_ox8c2d846PnH9iLp_SikzgYmvdPHe9k7G/pub?output=csv'

beatles_spotify = pd.read_csv(beatles_spotify_csv)
```

and the Billboard data:

```python
beatles_billboard_csv = 'https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv'

beatles_billboard = pd.read_csv(beatles_billboard_csv)
```

## Intro Header

You will quickly run into all sorts of issues when working with data. Most, however, fall into two major categories: issues of **cleanliness** and issues of **organization**. Data that is both clean and organized is known as **Tidy Data**, and this is what we strive for when we use, manipulate, and create our data. This helps us understand our data better, and perhaps more importantly helps programs like Pandas perform better analysis on our data.

At the end of [Part A][part-a], we encountered two datasets that stored the same information (Beatles song titles) in different formats (lowercase/Title Case). This is an example of data that needs to be **cleaned** so we can more easily work with it.

In the Beatles Billboard dataset, you might notice that for certain songs, the column `Album.debut` contains information about different album names for UK and US releases when applicable, like in the below example for "All My Loving":

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
      <th>9</th>
      <td>All My Loving</td>
      <td>1963</td>
      <td>UK: With the Beatles US: Meet The Beatles!</td>
      <td>124</td>
      <td>32</td>
      <td>Pop/Rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>

It might be helpful to separate this into two different columns to simplify the data, like below:

<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Year</th>
      <th>Album.debut.UK</th>
      <th>Album.debut.US</th>
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
      <th>9</th>
      <td>All My Loving</td>
      <td>1963</td>
      <td>With the Beatles</td>
      <td>Meet The Beatles!</td>
      <td>124</td>
      <td>32</td>
      <td>Pop/Rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>

This is an example that could be organized differently, and perhaps better.

In the remainder of this document, you will learn about some common cases where data needs to be better cleaned or organized in the pursuit of Tidy Data.

## Clean and Tidy Data Principles

[TODO] As we work with use, manipulate, and create data in this course, it would be useful to have a standardized method to organize that data. Moreover, using a consistent format benefits the programs we run to parse our data. As you work with Pandas, you will learn that its tools are designed to work best on data formatted in a particular way. Following the principles of [Tidy Data](#) will allow us to standardize our data.

### Wrong or Inconsistent Format

For example when spelling or capitalization are different for the same item across many rows or columns.  There are Pandas methods to help with this process. 

## The NaN Problem

In Python there is a difference between a "0" and nothing.  The latter is a Null, which represents "no data at all."  Nulls will result in errors when you attempt to perform some operation on them.  You cannot add to or compare something to a Null.  Nor can you test whether a Null contains some set of characters or matches a word. 

* **Find the NaN's**:  `df[df.isna().any(axis=1)]`, or for the billboard data:  `beatles_billboard[beatles_billboard.isna().any(axis=1)]`.  

* **Fill the NaN's**. If you are performing mathematical operations, You can fill missing values with some default number or string. The solution will probably vary from one column to the next (since some are integers, some dates, and are text):  `beatles_billboard.fillna("-")` would fill *all NaN* with the same string.  But we could instead try something that would be more meaningful.  For example: `beatles_billboard['Album.debut'].fillna("unreleased", inplace=True)`
* If you are trying to filter a data frame by a particular keyword or condition, you can treat the Nulls as "False" and thereby ignore them.

### Duplicate Rows

Duplicate rows can also create errors, or distort your results.  Find them:  `duplicate = beatles_billboard[beatles_billboard.duplicated()]
duplicate` (in this case there are none).  Remove them automatically with `beatles.drop_duplicates()`

### Wrong Data Type

Wrong data type in a given column is another common error (particularly since Pandas attempts to guess the correct data type when importing from CSV or JSON).  In our beatles_spotify dataset, notice that the data type for 'energy' is `object`, which in the context of Pandas means it is a Python `string`.  As such we cannot perform mathematical operations on it. Change the data type with the `astype()` method:

```python
beatles_spotify['energy'] = beatles_spotify['energy'].astype(np.float64)
```

The same thing can happen with **date=time** information.  In our orignal datasets, the "Year" columms are in fact integers.  This works fine for basic sorting.  But Pandas has an intelligent format for working with date-time information that allows us to sort by month-day-year, or create 'bins' representing quarters, decades, centuries.  

So you will need to check the original data type, then convert to strings before converting to **date-time format**.  For example:

```python
beatles_billboard["Year"] = beatles_billboard["Year"].astype(str)
```

Then convert that string to **datetime** format (in this case, in a new column, for comparison):

```python
beatles_billboard["Year_DT"] = pd.to_datetime(beatles_billboard["Year"], format='%Y')
```
And then reorder the columns for clarity:

```python
beatles_billboard_sorted = beatles_billboard.iloc[:, [0, 1, 9, 3, 4, 5, 6, 7, 8]]
beatles_billboard_sorted.head()

```

### Incorrect Data

This is more difficult, since you will need to know the details of the errors, and how to correct them.  But Python and Pandas can help you automate the process.

See more [here](https://towardsdatascience.com/simplify-your-dataset-cleaning-with-pandas-75951b23568e).
 

## Cleaning Data with Functions

Let's imagine that you have a dataset in which a particular column contains data that are inconsistent: in some places for the name of an artist you have `John Lennon`, and other places `John Lenin`.  You could correct them by hand in a Spreadsheet. But there is an easier way with a Python **function**.

You will first want to understand all the values you are trying to correct.  So here you would use Pandas/Python **set** method on all the values of the df["column"] in question: `set(df["Artist"])`.

Now that you know what the problem values are, write a **function** that corrects `John Lenin` to `John Lennon`.  If you don't recall **functions** see **Python Basic Notebook**!

```python
def name_check:
    if df["Artist"] == "John Lenin":
        return "John Lennon"
```
In this case the **return** statement makes the result available for the next step in the process.

But how to run this over **all rows** of a data frame?  We can easily do this with the **apply** method. In effect it **apply** allows us to automatically pass over all rows in the data frame, transforming only the column we select.  

```python
df['column'] = df['column'].apply(name_check)
```

Note that we could use this approach not only for correcting data, but for creating **new columns** based on **existing columns**.  For example:  a Boolean column (True/False) based on the result of the contents of another column.  Here the new column will report True for any row where the column "artist" contains the string "Lennon".  

```python
df['By_Lennon'] = df['artist'].str.contains("Lennon")
```

We can then use the Boolean column to filter the entire frame (see below).

Try some out:

**NANs anywhere:**

```python
beatles_billboard[beatles_billboard.isna().any(axis=1)]
```

**Replace NA's in Album column with 'unreleased'**

```python
beatles_billboard['Album.debut'].fillna("unreleased", inplace=True)
beatles_billboard.head(25)
```

**Convert the year column to an integer, then use the Pandas "year" format to make an intelligent date out of it, and sort the columns according to their `index` positions:**

```python
beatles_billboard["Year"] = beatles_billboard["Year"].astype(int)
beatles_billboard["Year_DT"] = pd.to_datetime(beatles_billboard["Year"], format='%Y')
beatles_billboard_sorted = beatles_billboard.iloc[:, [0, 1, 9, 3, 4, 5, 6, 7, 8]]
beatles_billboard_sorted.head()
```

You can think of some others!

## Nested Lists and Tuples in Cells

### Split String into List

In some cases you might find that cells in your colum a list of terms as a single string, like `'Psychedelic Rock, Art Rock, Pop/Rock'`.  Note that this is *not* the same thing as a Python list!  It's just a single string.  The second cell of the "Genre" column in the Beatles Billboard data contains just such a problem:

```python
beatles_billboard['Genre'][1]
'Psychedelic Rock, Art Rock, Pop/Rock'
```

But we can `split` the list with a built-in Python function.  In this instance simply chain the Python functions and apply them to the column: 

```python
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.split(', ')
```

And now the cell looks like a proper Python list:

```python
beatles_billboard['Genre'][1]
['Psychedelic Rock', 'Art Rock', 'Pop/Rock']
```

Of course, this is "Tidy Data".  For that we would prefer to have each of these terms in its own row (and allow the rest of the data to repeat).  This format will allow us to perform grouping operations much more easily than if the 'Genre' values remain nested in this way.

## Tuple Trouble (and How to Cure It)

```python
# define the function to convert tuples to strings
def convertTuple(tup):
    out = ""
    if isinstance(tup, tuple):
        out = '_'.join(tup)
    return out  
# clean the tuples
df['ngram'] = df['ngram'].apply(convertTuple)
```

# [-------- FIND A PLACE FOR THIS
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
            <pre>'Lennon, McCartney, Harrison and Starkey: 12-Bar Original'</pre>
        </td>
    </tr>
</table>

# END SECTION THAT NEEDS TO BE PLACED -----]

# [ BEGIN NEW SECTION THAT NEEDS TO BE PLACE --------

## Cleaning and Checking Data

Missing data or data encoded as the wrong type will result in errors of various kinds.  See more [here](https://www.w3schools.com/python/pandas/pandas_cleaning.asp).

# ------------ END SECTION THAT NEEDS TO BE PLACED ]

[part-a]: 04_A_Pandas_Basics.md
[part-c]: 04_C_Pandas_Filter_Find_Group.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf