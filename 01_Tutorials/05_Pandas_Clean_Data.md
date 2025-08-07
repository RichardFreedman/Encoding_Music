| [Pandas Basics][pandas-basics] | **Clean Data** | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

# Pandas: Clean Data

Cleaning data is an important precursor to anlyzing data, and often represents the biggest part of a data analysis project. In this tutorial, we explore various ways in which data can be "messy" and how it can be subsequently cleaned.

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

A guide to cleaning data with Pandas on [Medium][towards-data-science-cleaning].

|    | Contents of this Tutorial                                                      | 
|----|--------------------------------------------------------------------------------|
| 1. | [**Identifying the Problem**](#identifying-the-problem) |
| 2. | [**Understanding Clean and Tidy Data**](#understanding-clean-and-tidy-data) |
| 3. | [**Wrong or Inconsistent Format or Values**](#wrong-or-inconsistent-format-or-values) |
| 4. | [**Using a Dictionary with Map to Clean Data**](#using-a-dictionary-with-map-to-clean-data) |
| 5. | [**Cleaning Data with Functions**](#cleaning-data-with-functions) |
| 6. | [**Missing Data**](#missing-data) |
| 7. | [**Duplicate Rows**](#duplicate-rows) |
| 8. | [**Wrong Data Type**](#wrong-data-type) |
| 9. | [**Data Cleaning Best Practices**](#data-cleaning-best-practices) |

### Create a Notebook and Load the Pandas library

```python
import pandas as pd
```

### Meet the Beatles

We continue with our data about The Beatles:

* A set from **Spotify** that includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Github](https://github.com/RichardFreedman/Encoding_Music/blob/main/02_Lab_Data/Beatles/M_255_Beatles_Spotify_2025.csv).

* A set compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs:  author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts.  View these data on [Github]('https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv').

We will work with both of these sets, and in the process learn how to clean and 'tidy' the data in preparation for other operations.

Get the Spotify data:

```python
beatles_spotify_csv = 'https://raw.githubusercontent.com/RichardFreedman/Encoding_Music/refs/heads/main/02_Lab_Data/Beatles/M_255_Beatles_Spotify_2025.csv'

beatles_spotify = pd.read_csv(beatles_spotify_csv)
```

and the Billboard data:

```python
beatles_billboard_csv = 'https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv'

beatles_billboard = pd.read_csv(beatles_billboard_csv)
```

## Understanding Clean and Tidy Data

You will quickly run into all sorts of issues when working with data. Most, however, fall into two major categories: issues of **cleanliness** and issues of **organization**. Data that is both clean and organized is known as **Tidy Data**, and this is what we strive for when we use, manipulate, and create our data. This helps us understand our data better, and perhaps most importantly helps programs like Pandas perform better analysis on our data.

At the end of [Pandas: Basics][pandas-basics], we encountered two datasets that stored the same information (Beatles song titles) in different formats (lowercase/Title Case). This is an example of data that needs to be **cleaned** so we can more easily work with it (see how in the [section on data formatting](#wrong-or-inconsistent-format)).

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

This is an example of data that could be **organized** differently, and perhaps better (see how in [Pandas: Tidy Data][pandas-tidy]).

In the remainder of this document, we will focus on data **cleaning**. Then, in [Pandas: Tidy Data][pandas-tidy], we will pivot to data **tidying** and **organization**.

## Identifying the Problem

We will often be working with large datasets where it is impossible to manually check every value to verify its accuracy and cleanliness. One tool we can use to quickly identify problems in a dataset is the Pandas `.sort_values().` method. This allows us to generate a list of every entry in a column, sorted alphabetically. This provides a decent snapshot into your data. Try the below code:

```python
list(beatles_billboard['Album.debut'].sort_values())
```

## Wrong or Inconsistent Format or Values

Many issues arise when data is stored as strings. Spelling and capitalization can vary across items that are meant to be the same. Often, the situation will be applying a **string method** to an entire column. You saw an example of the `.str.lower()` string method in [Pandas: Basics][pandas-basics]:

```python
beatles_billboard['Title'] = beatles_billboard['Title'].str.lower()
```

`lower()` replaces every string in a column with a completely lowercase version of that string. You can see the full list of string methods here: [Pandas string methods][pandas-string-methods].

Some particularly important string methods for cleaning data:

* `.str.replace(x, y)`: Replace any instance of `x` with `y`
  + For example, you might want to regularize:
    - `'rock & roll'` as `'rock'`
    'r&b' (as 'rhythm and blues' ?)
    'stage&screen' (as 'stage and screen')
    'experimental music' as 'experimental', or 'children's music' as 'children's' (since having 'music' in a list of music genres is not very useful)
* `.str.split(x)`: Replace a string with a list of strings. The original string is separated at every instance of the substring `x`. E.g.: applying `.split(', ')` to `'John, Paul, George, Ringo'` would result in `['John', 'Paul', 'George', 'Ringo']`
* `.str.strip()`: Remove the spaces from the beginning and end of a string. Can also be configured to remove other characters.
* `.str.upper()`: Convert a string to all uppercase.
* `.str.title()`: Convert a string to Title Case.

String methods can only be applied to one column at a time. To use string methods, follow the pattern below:

```python
df['column_name'] = df['column_name'].str.method_name()
```

Here are some examples of data you may want to regularize:

*  `'rock & roll'` and `'rock'` (could be the same?)
* `'r&b'` (as `'rhythm and blues'`?)
* `'stage&screen'` (as `'stage and screen'`)
* `'experimental music'` as `'experimental'`, or `"children's music"` as `"children's"` (since having 'music' in a list of music genres is not very useful)

> Use "double quotes" if your string contains a 'single quote' (like "children's") to avoid errors.

You may want to regularize the `'Genre'` column, since it's stored as a string, but is essentially a list. This would be a good use of the `.str.split(', ')` method:

```python
beatles_billboard['Genre'].str.split(', ')
```
## Using a Dictionary with Map to Clean Data

If you want to replace a specific value with another value, you can use the `.map()` method. This is particularly useful when you have a large number of values to replace, or when you want to replace values based on a mapping.  For example, you might first get all the unique values in a column with `beatles_billboard['genre'].unique()`. Then on the basis of that list, you can create a dictionary that maps each value to a new value.


```python
# Define dictionary mapping terms to labels
term_mapping_dict = {
    'rock n roll': 'rock',
    'rock and roll': 'rock',
    'rock & roll': 'rock'
}

# Add new column based on term mapping
beatles_billboard['clean_genre'] = beatles_billboard['genre'].map(term_mapping_dict).fillna('other')
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

As you will recall from [Pandas: Basics][pandas-basics], Pandas tries to simplify your work by providing a comprehensive suite of tools. In this instance, Pandas saves us from iterating through every row with the `.apply()` method:

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

The `.apply()` method also allows you to split the contents of one column into several columns. To do this, see an example in the section "[Fixing Multiple Variables in One Column](06_Pandas_Tidy_Data.md#fixing-multiple-variables-in-one-column)" in [Pandas: Tidy Data][pandas-tidy].

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

These are examples of **filters**, which you will lean more about in [Pandas: Filtering, Finding, and Grouping][pandas-filter-find-group].

### Filling Missing Data

In many cases, you might come up with some default number or string to take the place of `NaN`s. You can fill `NaN`s using the `.fillna()` method. But `beatles_billboard.fillna('-')` would fill *all* `NaN`s with the same string. Instead, the solution will probably vary from one column to the next (since some are integers, some dates, and are text). You can fill the missing values in just one column at a time:

```python
beatles_billboard['Album.debut'] = beatles_billboard['Album.debut'].fillna("unreleased")
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

You may decide to remove rows or columns with missing data, for instance if so much data is missing that the row/column is unusable. In Pandas, removing data is called **dropping** data. You learned how to drop entire rows and columns manually in [Pandas: Basics][pandas-basics].

When dropping rows with missing data, you can take advantage of the built-in Pandas method `.dropna()`, which will help you automatically drop rows/columns with missing data. `.dropna()` takes two key arguments:

* `how`:
  + `how='any'` will drop all rows/columns that contain *any* missing data
  + `how='all'` will drop all rows/columns that contain missing data in *every* entry in that row/column
* `axis`:
  + `axis=0` indicates dropping rows
  + `axis=1` indicates dropping columns

Put it all together:

```python
beatles_billboard = beatles_billboard.dropna(how='any', axis=0) # drops all rows with missing data in any entry
```

> As with most of the methods in this tutorial, Pandas provides many more arguments that allow you to customize the `.dropna()` method. Always check the [documentation][pandas-documentation] to see if Pandas provides pre-built tools for a specific task you're doing.

## Duplicate Rows

Duplicate rows can also create errors, or distort your results. Find them:  `duplicates = beatles_billboard[beatles_billboard.duplicated()]` (in this case there are none). Remove them automatically with `beatles_billboard = beatles_billboard.drop_duplicates()`

You can also specify removing rows only if they contain duplicates in a specific column with `beatles_billboard = beatles_billboard.drop_duplicates(subset=['Title'])`

## Wrong Data Type

Wrong data type in a given column is another common error (particularly since Pandas attempts to guess the correct data type when importing from CSV or JSON). In our `beatles_spotify` dataset, suppose that the data type for 'energy' is `object`, which is a general data type that could mean almost anything.  As such we cannot perform mathematical operations on it. Change the data type with the `astype()` method:

```python
beatles_spotify['energy'] = beatles_spotify['energy'].astype('float64')
```

The same thing can happen with **date-time** information.  In our orignal datasets, the "Year" columms are in fact integers.  This works fine for basic sorting.  But Pandas has an intelligent format for working with date-time information that allows us to sort by month-day-year, or create 'bins' representing quarters, decades, centuries.  

So you will need to check the original data type, then convert to **date-time format**. For example (in this case, in a new column, for comparison):

```python
beatles_billboard["Year_DT"] = pd.to_datetime(beatles_billboard["Year"], format='%Y')
```
And then reorder the columns for clarity:

```python
# Creates a copy of the dataframe including all row, with column 9 ("Year_DT") taking the place of column 2, and column 2 no longer being included
beatles_billboard_sorted = beatles_billboard.iloc[:, [0, 1, 9, 3, 4, 5, 6, 7, 8]]
```

You can see the full list of date format codes (like `'%Y'`) [here][datetime-format-codes].

Pandas also supports **categorical** data. This can be more complex to work with, but adds lots of powerful functionality. You can read the [Pandas categories documentation][pandas-documentation-categories].

## Data Cleaning Best Practices

As you work with data from various sources, you will inevitably encouter problems. It can be tempting to fix individual errors as you see them occur - for example, if you see "Lennon" mispelled as "Lenin", you might want to return to the original spreadsheet to correct the error. You might even use Pandas to change an individual cell. However, this contravenes a key principle of data science: **reproducibility**.

Whenever possible, take a **generalized** and **reproducible** approach to cleaning data. That means instead of manually correcting "Lenin" to "Lennon", use a string method to change **every** instance of "Lenin". Doing this in a Jupyter notebook, with explanation, means that someone else could take the same original dataset and produce the same result as you, following a single method documented in one place.

One good practice is to create a **function** that handles cleaning your data. Once you've figured out the best way to clean your data, you can put all the steps in a function, like this:

```python
def preprocess():
    # Read CSV
    beatles_billboard_df = pd.read_csv('https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv')

    # Fill missing entries in the 'Album.debut' column with 'unreleased'
    beatles_billboard_df['Album.debut'] = beatles_billboard_df['Album.debut'].fillna("unreleased")

    # Drop rows with missing data
    beatles_billboard_df = beatles_billboard_df.dropna(how='any', axis=0)

    # Change entries of -1 to 0 in 'Top.50.Billboard' column
    def normalize_billboard(entry):
        if entry == -1:
            return 0
        return entry
    beatles_billboard_df['Top.50.Billboard'] = beatles_billboard_df['Top.50.Billboard'].apply(normalize_billboard)

    # Change the 'Year' column to a datetime datatype
    beatles_billboard_df["Year"] = pd.to_datetime(beatles_billboard_df["Year"], format='%Y')

    # Return the cleaned dataframe
    return beatles_billboard_df
```

Now you can get a fresh, clean version of the dataset with just one line:

```python
beatles_billboard = preprocess()
```

This sets you up for the next step: **tidying** your data in [Pandas: Tidy Data][pandas-tidy].

| [Pandas Basics][pandas-basics] | **Clean Data** | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

[pandas-basics]: 04_Pandas_Basics.md
[pandas-tidy]: 06_Pandas_Tidy_Data.md
[pandas-filter-find-group]: 07_Pandas_Filter_Find_Group.md
[pandas-graphs]: 08_Pandas_Graphs_and_Charts.md
[pandas-networks]: 09_Pandas_Networks.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
[towards-data-science-cleaning]: https://towardsdatascience.com/simplify-your-dataset-cleaning-with-pandas-75951b23568e
[pandas-string-methods]: https://pandas.pydata.org/docs/user_guide/text.html#method-summary
[python-basics]: 03_Python_basics.md
[w3schools-functions]: https://www.w3schools.com/python/python_functions.asp
[datetime-format-codes]: https://docs.python.org/3/library/datetime.html#format-codes
[pandas-documentation-categories]: https://pandas.pydata.org/docs/user_guide/categorical.html
[tidy-data]: https://www.jstatsoft.org/article/view/v059i10