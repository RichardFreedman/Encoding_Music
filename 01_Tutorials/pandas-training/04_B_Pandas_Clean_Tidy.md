# Pandas:  Clean and Tidy Data

| Part A | Part B | Part C |
|--------|--------|--------|
| [Pandas Basics][part-a] | **Clean and Tidy Data** | [Filtering, Finding, and Grouping][part-c] |

<!--In this tutorial we explore various ways of cleaning data. We also explore ways to make your data follow the "Tidy Data" principles, which will vastly simplify other work. The key concept here is to *un-nest* the various cells that might contain multiple data points. "One observation or event per row" is the preferred format for Tidy Data.--><span style="color:red">Replace this ¶</span><br><br>

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

|    | Contents of this Tutorial                                                      | 
|----|--------------------------------------------------------------------------------|
| x. | [**Defining Clean Data and its Uses**](#) |
| x. | [**Clean and Tidy Principles**](#)                  |
| x. | [**Wrong or Inconsistent Format**](#) |
| x. | [**Cleaning Data with Functions**](#) |
| x. | [**Missing Data**](#)                                    |
| x. | [**Duplicate Rows**](#)                              |
| x. | [**Wrong Data Type**](#)                                          |
| x. | [**Incorrect Data**](#) |
| x. | [**Nested Lists and Tuples in Cells**](#) |
| x. | [**Tuple Trouble (and How to Cure It)**](#) |
| x. | [**Explode, Melt, and Pivot**](#) |

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

## Understanding Tidy Data

You will quickly run into all sorts of issues when working with data. Most, however, fall into two major categories: issues of **cleanliness** and issues of **organization**. Data that is both clean and organized is known as **Tidy Data**, and this is what we strive for when we use, manipulate, and create our data. This helps us understand our data better, and perhaps most importantly helps programs like Pandas perform better analysis on our data.

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

This is an example of data that could be **organized** differently, and perhaps better.

In the remainder of this document, you will learn about some common cases where data can be cleaned or organized using Pandas in pursuit of Tidy Data.

<!--## Clean and Tidy Data Principles

[TODO] As we work with use, manipulate, and create data in this course, it would be useful to have a standardized method to organize that data. Moreover, using a consistent format benefits the programs we run to parse our data. As you work with Pandas, you will learn that its tools are designed to work best on data formatted in a particular way. Following the principles of [Tidy Data](#) will allow us to standardize our data.--><span style="color:red">Replace this ¶</span><br><br>

## Wrong or Inconsistent Format

Many issues arise when data is stored as strings. Spelling and capitalization can vary across items that are meant to be the same. Often, the situation will be applying a **string method** to an entire column. You saw an example of the `lower()` string method in Part A:

```python
beatles_billboard['Title'] = beatles_billboard['Title'].str.lower()
```

`lower()` replaces every string in a column with a completely lowercase version of that string. You can see the full list of string methods here: [Pandas string methods][pandas-string-methods].

Some particularly important string methods for cleaning data:

* `.replace(x, y)`: Replace any instance of `x` with `y`
* `.split(x)`: Replace a string with a list of strings. The original string is separated at every instance of the substring `x`. Ex: applying `.split(', ')` to `'John, Paul, George, Ringo` would result in `['John', 'Paul', 'George', 'Ringo']`
* `.strip()`: Remove the spaces from the beginning and end of a string. Can also be configured to remove other characters.
* `.upper()`: Convert a string to all uppercase.
* `.title()`: Convert a string to Title Case.

String methods can only be applied to one column at a time. To use string methods, follow the pattern below:

```python
df['column_name'] = df['column_name'].str.method_name()
```

## Cleaning Data with Functions

If string methods are not suffificent, or you're working with a different data type, you might need to create your own function that can be applied to the entire column.

Let's imagine that you want to get some statistics about the amount of time spent by Beatles songs on the Billboard Top 50. You can do this using `beatles_billboard['Billboard.Top.50'].describe()`. However, you first have to fix an important problem: handling unusual data. In several instances, the creators of the dataset made the decision to enter `-1` in the `'Billboard.Top.50'` column, as in the case of the song "Golden Slumbers":

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
  </tbody>
</table>

This is likely because these songs spent no time in the Top 50. However, values of `-1` will lead to strange results when calculating the average value of the column, for example. For our purposes, it is better to represent the number of weeks spent in the Top 50 as `0`, rather than `-1`. Let's write a function that replaces `-1` with `0`.

> The creators of this dataset did not document whether a value of `-1` indicates "no weeks spent in the Top 50" or "no data found indicating whether song made Top 50". It is likely safe to assume the former, but this is still an *assumption*. Be careful making assumptions about data, as this could lead to incorrect analysis. Always check the source of the data to learn more about it.

```python
def normalize_billboard(entry):
    if entry == -1:
        return 0
    return entry
```

If we pass a value of `-1` to the function, it will return a value of `0`. Otherwise, it will return the original value passed to it.

> *Note on Python Functions:* <br>
> Once a value is returned, the function is exited. Hence, there is no need for an `else` statement - no more than one value will ever be returned. Review Python functions at [W3Schools][w3schools-functions].

As you will recall from Part A, Pandas tries to simplify your work by providing a comprehensive suite of tools. In this instance, Pandas saves us from iterating through every row with the `.apply()` method:

```python
beatles_billboard['Top.50.Billboard'] = beatles_billboard['Top.50.Billboard'].apply(normalize_billboard)
```

This will pass every entry in the `'Top.50.Billboard'` column to the `normalize_billboard()` function, replacing the entry with the return value of the function. The updated row for "Golden Slumbers" will be:

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
      <th>81</th>
      <td>Golden Slumbers</td>
      <td>1969</td>
      <td>Abbey Road</td>
      <td>91</td>
      <td>5</td>
      <td>Rock, Baroque Pop, Pop/Rock</td>
      <td>McCartney</td>
      <td>McCartney</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

If for some reason you want to maintain the original column, you can do so by saving the result to a new column with a different name, for example:

```python
beatles_billboard['Top.50.Billboard.normalized'] = beatles_billboard['Top.50.Billboard'].apply(normalize_billboard)
```

<!-- I want to replace this example because it is covered by a string function

Let's imagine that you have a dataset in which a particular column contains data that are inconsistent: in some places for the name of an artist you have `John Lennon`, and other places `John Lenin`.  You could correct them by hand in a Spreadsheet. But there is an easier way with a Python **function**.

You will first want to understand all the values you are trying to correct.  So here you would use Pandas/Python **set** method on all the values of the df["column"] in question: `set(df["Artist"])`.

Now that you know what the problem values are, write a **function** that corrects `John Lenin` to `John Lennon`.  If you don't recall **functions** see [Python Basics Notebook][python-basics]!

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
-->

<!-- This is really weird. Seems to be a combination of filtering and NaN stuff.

Try some out:

**NANs anywhere:**

```python
beatles_billboard[beatles_billboard.isna().any(axis=1)]
```

**Replace NA's in Album column with 'unreleased'**

```python
beatles_billboard = beatles_billboard['Album.debut'].fillna("unreleased")
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
-->

## Missing Data

Another common problem in data is **missing data**. For example, see the row for a more obscure song "Circles" in the Beatles Billboard dataset:

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
      <th>42</th>
      <td>Circles</td>
      <td>1968</td>
      <td>NaN</td>
      <td>226</td>
      <td>0</td>
      <td>Hindustani Blues, Pop/Rock</td>
      <td>Harrison</td>
      <td>Harrison</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Missing data can be represented in many different ways in code. In this instance, the entry in the column `'Album.debut'` is `NaN`, meaning "Not a Number". You might also see missing data encoded as `null`, `None`, or `pd.NA`. All of these represent "no data at all".

Missing data can be incredibly troublesome. Most operations involving missing data will result in errors. For example, using a **string method** on a column with just a single missing value will cause the entire operation to fail. This is why it is crucial to **find** missing values and either **fill** or **remove** them.

> You might also decide you want to keep null values in your data. It is possible to work around the problems presented by missing data, but this makes work more complex. It is often simpler to replace missing data with some default value.

### Finding Missing Data

Before doing something about missing data, you should first get a clear picture of what data is missing.

* Show just the rows with missing data:
    + ```python
      beatles_billboard[beatles_billboard.isna().any(axis=1)]
      ```
* Show just rows with missing data in a specific column:
    + ```python
      beatles_billboard[beatles_billboard['Album.debut'].isna()]
      ```

These are examples of **filters**, which you will lean more about in [Part C][part-c].

### Filling Missing Data

In many cases, you might come up with some default number or string to take the place of `NaN`s. You can fill `NaN`s using the `.fillna()` method. But `beatles_billboard.fillna('-')` would fill *all* `NaN`s with the same string. Instead, the solution will probably vary from one column to the next (since some are integers, some dates, and are text). You can fill the missing values in just one column at a time:

```python
beatles_billboard = beatles_billboard['Album.debut'].fillna("unreleased")
```

Now the row for "Circles" will be:

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
      <th>42</th>
      <td>Circles</td>
      <td>1968</td>
      <td>unreleased</td>
      <td>226</td>
      <td>0</td>
      <td>Hindustani Blues, Pop/Rock</td>
      <td>Harrison</td>
      <td>Harrison</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

### Removing Missing Data

You may decide to remove rows or columns with missing data, for instance if so much data is missing that the row/column is unusable.

## Duplicate Rows

Duplicate rows can also create errors, or distort your results.  Find them:  `duplicate = beatles_billboard[beatles_billboard.duplicated()]
duplicate` (in this case there are none).  Remove them automatically with `beatles.drop_duplicates()`

## Wrong Data Type

Wrong data type in a given column is another common error (particularly since Pandas attempts to guess the correct data type when importing from CSV or JSON).  In our beatles_spotify dataset, notice that the data type for 'energy' is `object`, which in the context of Pandas means it is a Python `string`.  As such we cannot perform mathematical operations on it. Change the data type with the `astype()` method:

```python
beatles_spotify['energy'] = beatles_spotify['energy'].astype(np.float64)
```

The same thing can happen with **date-time** information.  In our orignal datasets, the "Year" columms are in fact integers.  This works fine for basic sorting.  But Pandas has an intelligent format for working with date-time information that allows us to sort by month-day-year, or create 'bins' representing quarters, decades, centuries.  

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

## Incorrect Data

This is more difficult, since you will need to know the details of the errors, and how to correct them.  But Python and Pandas can help you automate the process.

See more [here][towards-data-science-cleaning].

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

## Organization Principles

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

| Part A | Part B | Part C |
|--------|--------|--------|
| [Pandas Basics][part-a] | **Clean and Tidy Data** | [Filtering, Finding, and Grouping][part-c] |

[part-a]: 04_A_Pandas_Basics.md
[part-c]: 04_C_Pandas_Filter_Find_Group.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
[pandas-string-methods]: https://pandas.pydata.org/docs/user_guide/text.html#method-summary
[python-basics]: 03_Python_basics.md
[towards-data-science-cleaning]: https://towardsdatascience.com/simplify-your-dataset-cleaning-with-pandas-75951b23568e
[w3schools-functions]: https://www.w3schools.com/python/python_functions.asp