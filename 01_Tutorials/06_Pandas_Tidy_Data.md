| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | **Tidy Data** | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

# Pandas: Tidy Data

In this tutorial, we explore ways to make your data follow "Tidy Data" principles, which will vastly simplify other work. The key concept of Tidy Data is "one observation or event per row".

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

Read the famous [essay on Tidy Data][tidy-data].

|    | Contents of this Tutorial | 
|----|---------------------------|
| 1. | [**Data Organization Principles**](#data-organization-principles) |
| 2. | [**Fixing Multiple Variables in One Column**](#fixing-multiple-variables-in-one-column) |
| 3. | [**Fixing Multiple Observations in One Row: Explode**](#fixing-multiple-observations-in-one-row-explode) |
| 4. | [**Fixing Multiple Observations in One Row: Melt**](#fixing-multiple-observations-in-one-row-melt) |
| 5. | [**Tuple Trouble (and How to Cure It)**](#tuple-trouble-and-how-to-cure-it) |
| 6. | [**Combining Columns**](#combining-columns) |
| 7. | [**Stack and Unstack**](#stack-and-unstack) |

## Data Organization Principles

The next step to take with your data is making it **tidy**. The key concepts of Tidy Data are:

1. Each variable forms a column

    > In our `beatles_billboard` dataset, the `'Album.debut'` column contains *two* variables: the UK and the US release of each album. To fix this, we would have to create two columns, one for the UK release and one for the US release.
    
    As you will see in [Fixing Multiple Variables in One Column](#fixing-multiple-variables-in-one-column), the `.str.split()` method is a great way to solve this.

2. Each observation forms a row

    > In the `beatles_billboard` dataset, the `'Genre'` column often contains *several* genres. This is, in effect *several observations*. Tidy data would suggest creating a new row for each observation.

    As you will see in [Fixing Multiple Observations in One Row](#fixing-multiple-observations-in-one-row-explode), the `.explode()` method is a great way to solve this.

3. Each type of observational unit forms a table

    > Both `beatles_billboard` and `beatles_spotify` center around the observational unit of a *single song*. If we wanted to focus on a different unit, like observations about musical artists, it would be more organized to do so in a *new* dataframe, rather than our existing ones.

    In this course, we will largely work with the same type of data during a project, so this point is somewhat beyond our scope. However, even the distinction between the `beatles_spotify` and `beatles_billboard` datasets is a good example of separating tables that are making different observations.

You can read more in Hadley Wickham's paper on Tidy Data [here][tidy-data].

### What are the benefits of following Tidy Data principles?

Beyond having a largely standardized format for datasets, making your data "tidy" will massively simplify your work in Pandas. In [Pandas: Filtering, Finding, and Grouping][pandas-filter-find-group], you'll start working with your data in-depth. All of Pandas built-in tools to parse, analyze, and visualize your data will work best when your data is organized following these principles.

## Fixing Multiple Variables in One Column

As observed in the above section, many entries in the `'Album.debut'` column seem to contain *two* variables: the **UK** album debut and the **US** album debut, like below:

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

This violates the Tidy Data principle that **"Each variable forms a column"**, since the two variables (UK album release and US album release) are stored in the same column. There are also rows where there is no dinstinction between a UK and a US album release, so we can assume the release was the same in both regions.

This is a somewhat complex problem to solve. The data we need is stored in a string, with part of it coming after "UK: " (the UK release) and part of it coming after "US: " (the US release). Thankfully, there is a string method we can use to tidy data: `.str.split()`. We know the UK release will always be before " US: ", and the US after. So we can split on that string (including the spaces before and after): `beatles_billboard['Album.debut'].str.split(' US: ')`

This doesn't create a new column! To split a column, you can use the `expand` keyword for the `.str.split()` method. And since this splits the entry into two columns, we need to assign it to two columns. Put it together below:

```python
beatles_billboard[['Album.debut.UK', 'Album.debut.US']] = beatles_billboard['Album.debut'].str.split(' US: ', expand=True)
```

Then drop the original column, and reorder the columns:

```python
beatles_billboard = beatles_billboard.drop(columns=['Album.debut'])
beatles_billboard = beatles_billboard.iloc[:, [0, 1, 2, 8, 9, 3, 4, 5, 6, 7]]
```

You're left with most of the data in the right place, but you still have a bit of cleaning up to do. You need to deal with the text "UK: ":

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
      <td>UK: With the Beatles</td>
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

Let's use another string method, this time `.str.strip()`, to cut "UK: " out from the beginning of each entry in the column:

```python
beatles_billboard['Album.debut.UK'] = beatles_billboard['Album.debut.UK'].str.strip('UK: ')
```

Now you're almost done with the split!

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

The last case to handle is albums that didn't specifiy separate UK/US releases. In those rows, `.str.split(' US: ')` couldn't find the string " US: " to split on, so it just put the entire string in the `'Album.debut.UK'` column, and nulls in the `'Album.debut.US'` column, like so:

<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Year</th>
      <th>Album.debut.UK</th>
      <th>Album.debut.US</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>92</th>
      <td>Help!</td>
      <td>1963</td>
      <td>Help!</td>
      <td>None</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

 Remember, `None`, is another type of missing data. We can fix this using `.fillna()` to replace any missing data in the `'Album.debut.US'` column with the entry in the `'Album.debut.UK'` column for that row:

 ```python
 beatles_billboard['Album.debut.US'] = beatles_billboard['Album.debut.US'].fillna(beatles_billboard['Album.debut.US'])
 ```

 Now every song will be correctly split into two columns:

 <table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Year</th>
      <th>Album.debut.UK</th>
      <th>Album.debut.US</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>92</th>
      <td>Help!</td>
      <td>1963</td>
      <td>Help!</td>
      <td>Help!</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

If you have any problems, you may need to handle the missing data in the `'Album.debut'` column before trying to perform operations on it.

## Fixing Multiple Observations in One Row: `explode`

In the `'Genre'` column of the `beatles_billboard` dataset, there are often several genres listed. We can see this in Golden Slumbers:

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

 This violates the principle of Tidy Data that **"Each observation forms a row"**, since there are multiple observations (Golden Slumbers has genre **X**) in a single row. We want to expand this row into three rows, each with a different observed genre. Pandas allows us to do this in three key steps:

1. Clean the data

> This could include
> 
> * Converting all genres to lowercase to ensure uniform formatting
> * Stripping any superfluous spaces
> 
> This **must** include:
> 
> * Handling any missing data

2. Within the column, **"split"** the genres:

<blockquote><table>
  <tr>
    <td>
      <table>
        <tr>
          <th>Genre</th>
        </tr>
          <td><code>'Rock, Baroque Pop, Pop/Rock'</code></td>
        <tr>
      </table>
    </td>
    <td><strong>→</strong></td>
    <td>
      <table>
        <tr>
          <th>Genre</th>
        </tr>
          <td><code>['Rock', 'Baroque Pop', 'Pop/Rock']</code></td>
        <tr>
      </table>
    </td>
  </tr>
</table></blockquote>

 3. **"Explode"** the row into one row for each genre:
 
<blockquote><table>
  <tr>
    <td>
      <table>
        <tr>
          <th>Genre</th>
        </tr>
          <td><code>['Rock', 'Baroque Pop', 'Pop/Rock']</code></td>
        <tr>
      </table>
    </td>
    <td><strong>→</strong></td>
    <td>
      <table>
        <tr>
          <th>Genre</th>
        </tr>
          <td><code>'Rock'</code></td>
        <tr>
        </tr>
          <td><code>'Baroque Pop'</code></td>
        <tr>
        </tr>
          <td><code>'Pop/Rock'</code></td>
        <tr>
      </table>
    </td>
  </tr>
</table></blockquote>

### Cleaning the data

Since we are already familiar with these steps, let's clean the column by "chaining" three methods:

```python
# make everything lowercase, remove leading/trailing spaces, and fill NAs
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.lower().str.strip().fillna('')
```

### Splitting the data

To split the genres into an organized **list**, we use the string method `.str.split(', ')`:

```python
# split the long strings into a list of strings in each cell
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.split(', ')
```

### Exploding the data

Now we can split the row into several rows, one for each element of the list, using `df.explode('column_name')`, in this case `beatles_billboard.explode('Genre')`. Since this is such a big change, and we don't want to ruin our data, let's store the result in a new dataframe, `beatles_billboard_exploded`:

```python
# explode the data
beatles_billboard_exploded = beatles_billboard.explode('Genre')
```

"Exploded" rows maintain their original dataframe index. For example, since Golden Slumbers had the index `81`, and three genres, there are now three rows with the index `81`. Let's fix this using `.reset_index(drop=True)` (this removes the old index column):

```python
# clean up indices
beatles_billboard_exploded = beatles_billboard_exploded.reset_index(drop=True)
```

Now the entries for Golden Slumbers will have unique indices:

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

Remember you can chain methods in one line once you're comfortable with them, like this:

```python
beatles_billboard_exploded = beatles_billboard.explode('Genre').reset_index(drop=True)
```

In this way, you can more simply write all of the steps for exploding:

```python
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.lower().str.strip().fillna('').str.split(', ')
beatles_billboard_exploded = beatles_billboard.explode('Genre').reset_index(drop=True)
```

### Clean the result

You can now more easily access the individual genres, which you will need to clean using string methods like `.str.replace()`. 

The below code snippet provides an example of the methods you could apply in this scenario.

<details><summary>View code</summary>

```python
# clean individual problems in the exploded data with str.replace() and str.strip()
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.strip('[')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('pop/rock', 'pop rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('r&b', 'rhythm and blues')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('rock and roll', 'rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('experimental music', 'experimental')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("children's music", "children's")
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("stage&screen", "stage and screen")
```
</details>

You'll see an example of this in the [Networks tutorial][pandas-networks].

## Fixing Multiple Observations in One Row: `melt`

In `beatles_spotify`, we have six columns of feature data. In other words, there are six musical feature observations in each row. You may decide that a better method of organization is to only make one music feature observation in each row, like this:

<blockquote><table>
  <tr>
    <td>
      <table>
        <tr>
          <th>song</th>
          <td><code>'danceability'</code></td>
          <td><code>'energy'</code></td>
          <td><code>'speechiness'</code></td>
          <td><code>'acousticness'</code></td>
          <td><code>'liveness'</code></td>
          <td><code>'valence'</code></td>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>0.3320</code></td>
          <td><code>0.1790</code></td>
          <td><code>0.0326</code></td>
          <td><code>0.8790</code></td>
          <td><code>0.0886</code></td>
          <td><code>0.3150</code></td>
        <tr>
      </table>
    </td>
  </tr>
    <td><strong>↓</strong></td>
  <tr>
    <td>
      <table>
        <tr>
          <th>song</th>
          <th>variable</th>
          <th>value</th>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'danceability'</code></td>
          <td><code>0.3320</code></td>
        <tr>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'energy'</code></td>
          <td><code>0.1790</code></td>
        <tr>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'speechiness'</code></td>
          <td><code>0.0326</code></td>
        <tr>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'acousticness'</code></td>
          <td><code>0.8790</code></td>
        <tr>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'liveness'</code></td>
          <td><code>0.0886</code></td>
        <tr>
        </tr>
          <td><code>'yesterday'</code></td>
          <td><code>'valence'</code></td>
          <td><code>0.3150</code></td>
        <tr>
      </table>
    </td>
  </tr>
</table></blockquote>

This is where the Pandas `.melt()` method comes in. We can pass `.melt()` our dataframe, the column(s) that differentiate each row (`id_vars`), and the columns we want to be "melted" (`value_vars`).

This will create a new table, which we can save separately, and will *only* contain the information we have specifically passed to the `.melt()` method.

In this example, we also sort the songs after melting so all of a song's musical features are grouped together, and then reset the index (since we just rearranged everything).

```python
melted_feature_data = pd.melt(beatles_spotify, id_vars=['song'], value_vars=["danceability", "energy", "speechiness", "acousticness", "liveness", "valence"]).sort_values('song').reset_index(drop=True)
```

The resulting dataframe will look like this:

<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>song</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1110</th>
      <td>yesterday</td>
      <td>valence</td>
      <td>0.3150</td>
    </tr>
    <tr>
      <th>1111</th>
      <td>yesterday</td>
      <td>liveness</td>
      <td>0.0886</td>
    </tr>
    <tr>
      <th>1112</th>
      <td>yesterday</td>
      <td>acousticness</td>
      <td>0.8790</td>
    </tr>
    <tr>
      <th>1113</th>
      <td>yesterday</td>
      <td>energy</td>
      <td>0.1790</td>
    </tr>
    <tr>
      <th>1114</th>
      <td>yesterday</td>
      <td>speechiness</td>
      <td>0.0326</td>
    </tr>
    <tr>
      <th>1115</th>
      <td>yesterday</td>
      <td>danceability</td>
      <td>0.3320</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

## Tuple Trouble (and How to Cure It)

You may encounter data stored as tuples: `('this', 'is', 'a', 'tuple')`. As we've seen, it can be much easier to work with strings than tuples (for example, for the functionality of string methods). This function will help you convert tuples to strings:

```python
# define the function to convert tuples to strings
def convertTuple(tup):
    out = ""
    if isinstance(tup, tuple):
        out = '_'.join(tup)
    return out  

# clean the tuples
df['column_name'] = df['column_name'].apply(convertTuple)
```

## Combining Columns

As we've seen, making your data tidy can involve splitting a column into several columns. However, you may also want to combine several columns of related data into one. For example, you could take the `'Songwriter'` and `'Title'` columns from `beatles_billboard`, and combine them into a new `'Author-Title'` column with the format `'Songwriter: Title'`. This function will help you do that:

```python
# define the function using lambda
combine_cols = lambda row: row['Songwriter'] + ": "  + row['Title']

# use .apply() to apply the function to every row in the column
beatles_billboard['Author-Title'] = beatles_billboard.apply(combine_cols, axis=1)

# output a single row as an example
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

> Normally we've seen functions written like this: `def combine_cols(row):`. However, there is a shorthand for writing functions using `lambda`, which allows you to write functions in a single line. `lambda` functions are easier and cleaner to write, but at the expense of readbility. Learn more [here][lambda-functions].

## Stack and Unstack

`stack` and `unstack` provide new ways to reshape your data. They are more radical transformations than `explode` and `melt` because the result isn't necessarily a dataframe. While you are less likely to need these methods, you may encounter scenarios, such as a visualization tool requiring a specific data format, where they are beneficial. As such, the primary focus of this section is to expand your knowledge of the possibilities without delving into the specifics.

### `stack` Function

`stack` transforms your dataframe into a series. Each entry in the series represents a row in the original dataframe. You can think of this as converting your data from a "wide" format to a "long" format. For example:

```python
stacked_df = beatles_billboard.stack()

# show the first entry
stacked_df[0]
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre>Title                                       12-Bar Original
Year                                                   1965
Album.debut                                     Anthology 2
Duration                                                174
Other.releases                                            0
Genre                                                 Blues
Songwriter          Lennon, McCartney, Harrison and Starkey
Top.50.Billboard                                         -1
dtype: object</pre>
        </td>
    </tr>
</table>

One common way to `stack` dataframes is by first setting the index to one of the columns of the dataframe. That way, the resulting series has each title as an index, making it easy to quickly see information on a particular track.

```python
# create a stack with titles as indices
title_stack = beatles_billboard.set_index('Title').stack()

# show the result
title_stack
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre style="white-space: pre;">Title                                                                      
12-Bar Original                                            Year                                                             1965
                                                           Album.debut                                               Anthology 2
                                                           Duration                                                          174
                                                           Other.releases                                                      0
                                                           Genre                                                           Blues
                                                           Songwriter                    Lennon, McCartney, Harrison and Starkey
                                                           Top.50.Billboard                                                   -1
A Day in the Life                                          Year                                                             1967
                                                           Album.debut                     Sgt. Pepper's Lonely Hearts Club Band
                                                           Duration                                                          335
                                                           Other.releases                                                     12
                                                           Genre                            Psychedelic Rock, Art Rock, Pop/Rock
                                                           Songwriter                                       Lennon and McCartney
                                                           Lead.vocal                                       Lennon and McCartney
                                                           Top.50.Billboard                                                   -1
...</pre>
        </td>
    </tr>
</table>

This makes it much more intuitive to access information for a single track:

```python
title_stack['A Day in the Life']
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre style="white-space: pre;">Year                                                 1967
Album.debut         Sgt. Pepper's Lonely Hearts Club Band
Duration                                              335
Other.releases                                         12
Genre                Psychedelic Rock, Art Rock, Pop/Rock
Songwriter                           Lennon and McCartney
Lead.vocal                           Lennon and McCartney
Top.50.Billboard                                       -1
dtype: object</pre>
        </td>
    </tr>
</table>

You can also reference just a specific data point:

```python
title_stack['A Day in the Life']['Lead.vocal']
```

<table border="0">
    <tr>
        <th valign="top">Output:</th>
        <td>
            <pre style="white-space: pre;">'Lennon and McCartney'</pre>
        </td>
    </tr>
</table>

Use this code to check all of the possible index values:

```python
set(title_stack.index.get_level_values(0))
```

###  `unstack` Function

`unstack` is the inverse operation of `stack`.

The one crucial requirement for a successful `unstack` operation is that each index in the "stacked" (long form) data is unique. If it isn't, this should be resolved using `.drop_duplicates()`, `.reset_index()`, `.reset_index(drop=True)`, or another method, depending on your needs.

If each index in your stacked data is unique, you can simply use the `.unstack()` method to re-create the original dataframe, as it was before the `stack` was performed.

```python
reverted_df = stacked_df.unstack()
```

| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | **Tidy Data** | [Filtering, Finding, and Grouping][pandas-filter-find-group] | [Graphs and Charts][pandas-graphs] | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

[pandas-basics]: 04_Pandas_Basics.md
[pandas-clean]: 05_Pandas_Clean_Data.md
[pandas-filter-find-group]: 07_Pandas_Filter_Find_Group.md
[pandas-graphs]: 08_Pandas_Graphs_and_Charts.md
[pandas-networks]: 09_Pandas_Networks.md
[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
[tidy-data]: https://www.jstatsoft.org/article/view/v059i10
[lambda-functions]: https://www.w3schools.com/python/python_lambda.asp