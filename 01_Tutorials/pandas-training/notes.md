- The [Linkedin course on Pandas](https://www.linkedin.com/learning/pandas-essential-training-24082178/) seems like a helpful resource
- Use `help(pd.read_csv)` to access documentation for a specific method
    + or `pd.read_csv?`
    + `help(pd.DataFrame.groupby)`
    + `pd.DataFrame.groupby?`
- Official Pandas documentation: [here](https://pandas.pydata.org/pandas-docs/stable/)

Why use Pandas?
- Pandas is great for large datasets that Excel or Google Sheets would struggle to open

Other observations:
* `df.shape` shows dimensionality of `df`
* `df.sample(5)` might be preferable to `df.head(5)`
* `df.info`
* `df.describe`
* `pd.get_option("display.max_rows")`
* `pd.set_option("display.max_rows", None)`
* `pd.set_option("display.max_rows", 60)`
* `pd.get_option("display.max_columns")`
* `pd.get_option("display.width")`

Show one column (Series) from a dataframe:
```python
oo["Discipline"]
```

Show all columns
```python
oo.columns
```

Show unique values in column `"Year"`
```python
oo['Year'].unique()
```

Shows frequency of each entry in a column appearing
```python
oo['Year'].value_counts()
```

Shows relative frequency (percentage) of each entry in a column appearing
```python
oo['Year'].value_counts(normalize=True)
```

Rename columns using a mapper

```python
mapper = {"Athlete Name": "Athlete_Name",
          "Event Gender": "Event_Gender"}

oo = oo.rename(columns=mapper)
```

Rename all columns at once:
```python
column_names = ['Year', 'City', 'Sport', 'Discipline', 'Athlete_Name', 'NOC', 'Gender',
       'Event', 'Event_Gender', 'Medal', 'Position']
oo.columns = column_names
```

Rename the columns as you import the CSV:
```python
oo = pd.read_csv(filename, skiprows=5, names=column_names, header=0``
```

`axis=0` means the axis is the index, or the columns. Therefore, the operation will be performed vertically, down the rows.

`axis=1` means the axis is the row. Therefore, the operation will be performed horizontally, across the columns.

Drop a column:
```python
oo = oo.drop('Position', axis=1)
```

A reason not to use `inplace=True` is because it makes it impossible to do chaining.

Either:
```python
oo = pd.read_csv(filename, skiprows=5).drop('Position', axis=1)
```

or:
```python
oo = (pd.read_csv(filename, skiprows=5)
      .drop('Position', axis=1)
)
```
(This format allows for better readability and debugging, since you can comment out an individual operation.)

Drop one row:
```python
oo = (pd.read_csv(filename, skiprows=5)
      .drop(2, axis=0)
)
```

Drop several rows at once:
```python
oo = (pd.read_csv(filename, skiprows=5)
      .drop([0, 1, 3], axis=0)
)
```

Drop several columns at once:
```python
oo = oo.drop(['City', 'Sport'], axis=1)
```

Another reason not to use `inplace=True` is because `merge`, `concat`, and `groupby` don't have `inplace=True` options. It also makes it harder to debug things, because you've lost the original dataframe.

There have also been discussions about deprecating `inplace=True`.

Operators and symbols in Python/Pandas:

|   Operator                    |   Symbol  |
|-------------------------------|-----------|
|   Equal                       |   ==      |
|   Not equal                   |   !=      |
|   Less than                   |   <       |
|   Less than or equal to       |   <=      |
|   Greater than                |   >       |
|   Greater than or eual to     |   >=      |
|   AND                         |   &       |
|   OR                          |   \|      |
|   NOT                         |   ~       |


Checking the type of something:
```python
type(item)
```

To get the type of data with a Pandas object, like a Series:
```python
oo['Year'].dtype
```

Filtering a dataframe:
```python
# Create a series with booleans for each index in the dataframe that are
# either True or False depending on the given condition
first_olympics = (oo['Year'] == 1896)

# Filter the dataframe to only show rows where first_olympics has True
# for the corresponding index
# i.e. only the rows where the column 'Year'
oo[first_olympics]
```

Shorthand for the same filter:
```python
oo[oo['Year'] == 1896]
```

Get datatypes for every column in a dataframe:
```python
oo.dtypes
```

Filter for multiple conditions at once:
```python
oo = oo[(oo['Year'] == 1896) | (oo['Year'] == 2004)]

# Now verify that the results are only from those two years
oo[(oo['Year'] == 1896) | (oo['Year'] == 2004)]['Year'].unique()
```

Specify the columns you want to see in your output:
```python
oo[(oo['Year'] == 1896) & (oo['Gender'] == 'Men') & (oo['Event'] == '100m')][["Year", "Athlete Name", "NOC", "Event", "Medal"]]
```

Viewing several columns at once from a dataframe:
```python
first_men_100m[["Year", "Athlete Name", "NOC", "Event", "Medal"]]
```

Use a string method on an entire column:
```python
oo['Event'] = oo['Event'].str.capitalize()
```

See the complete list of string methods available:
```python
dir(oo.Event.str)
```

Use string methods when filtering:
```python
oo[oo["Athlete Name"].str.contains("LATYNINA")]
```

Return a sorted version of a column
```python
oo["Athlete Name"].sort_values()
```

Sort the entire dataframe based on a single column
```python
oo.sort_values("Athlete Name")
```

Sort in reverse order
```python
oo.sort_values("Athlete Name", ascending=False)
```

Sort by one column first, then another
```python
oo.sort_values(by=["Year", "Athlete Name"], ascending=[False, True])
```

Change the datatype of a column
```python
oo.Medal = oo.Medal.astype("category")
```

Reorder categories
```python
medal_order = ["Bronze", "Silver", "Gold"]
oo['Medal'] = pd.Categorical(oo['Medal'], categories=medal_order, ordered=True)
```

** Note: ** Categoricals require significantly less memory than objects

Return the memory usage of a Series
```python
oo.Medal.memory_usage(deep=True)
```

You can change the data type of a Series to `String`, but it does not affect the memory usage. However, it is more explicit than the `object` datatype, so it is
best practice.
```python
oo["Athlete Name"] = oo["Athlete Name"].astype("string")
```

Map all columns to a new datatype:
```python
ordered_medals = pd.api.types.CategoricalDtype(categories=["Bronze", "Silver", "Gold"], ordered=True)

dtype_mapper = {"Year": "int64",
                "City": "string",
                "Sport": "string",
                "Discipline": "string",
                "Athlete Name": "string",
                "NOC": "string",
                "Gender": "category",
                "Event": "string",
                "Event_gender": "category",
                "Medal": ordered_medals}

oo = pd.read_csv(filename, skiprows=5, dtype=dtype_mapper)
```

It may be necessary to hard-code the data type for some Series, particularly categoricals, which tend to be finnicky.
```python
oo['Event Gender'] = oo['Event Gender'].astype("category")
```

Show the row indices
```python
oo.index
```

Check the value of a column (`"Event"`) in a specific row (`22719`)
```python
oo.loc[22719, "Event"]
```

Change the index to be the values in a particular column
```python
oo = oo.set_index("Athlete Name")
```

Use a string index to access the values of a column in rows with that index
```python
oo.loc["LEWIS, Carl", "Event"]
```

Use a string index to access the values of several columns in rows with that index
```python
oo.loc["LEWIS, Carl", ["Year", "Event", "Medal"]]
```

Do the same with all columns
```python
oo.loc["LEWIS, Carl", :]
```

You can also get data from all columns by omitting the `:`, but it is best practice
to be explicit about what you are looking for.
```python
oo.loc["LEWIS, Carl"]
```

Sort rows by index
```python
oo = oo.sort_index()
```

Return to the numerical index from before. This restores the column that was used as the index to a normal column.
```python
oo = oo.reset_index()
```

Access data using integer values of rows and columns
```python
oo.iloc[0, 5]
```

`iloc` can also be used to retrieve a range of values
```python
oo.iloc[0, :]
```

Again, the same result can be obtained without including the `:`, but it is best practice to be explicit and include it.
```python
oo.iloc[0]
```

### Best Practices

#### Get immediate feedback

Whenever creating a dataframe (or modifying one), include code to check a sample of that dataframe in the same code block.

```python
oo.sample(3)
```

#### Understand the basics of Python

Use list comprehension, built-in documentation, and regular expressions to search for a method that does what you need.

```python
import re
import pandas as pd

search_string = "excel"

[func for func in dir(pd) if re.search(rf"{search_string}", func, re.IGNORECASE)]
```

#### `head()` vs. `sample()`

Using `sample()` has some benefits over `head()` because it returns a different result every time.

#### Modify the data, not the original file

It's helpful to create a function, like `preprocess()`, that will read in the data to Pandas.

#### Using Python `assert`

Verify that the result is what you expect. This throws an error if the result is not what you "assert" that is should be.

```python
assert(oo[(oo.Year < 1896) & (oo.Year > 2004)].shape[0] == 0)
```

#### Chaining and splitting over several lines. No `inplace=True`.

Instead of having a separate line for each operation, like this:
```python
oo = pd.read_csv(filename, skiprows=5)
oo = oo.drop('Position', axis=1)
```

It's better to chain operations, with each new one on a separate line:
```python
oo = (pd.read_csv(filename, skiprows=5)
      .drop('Position', axis=1)
)
```

That way, it's easier to debug by commenting out just a specific part:
```python
oo = (pd.read_csv(filename, skiprows=5)
      #.drop('Position', axis=1)
)
```

#### Using the Python `.isin()` method

```python
years_of_interest = [1972, 1980, 1984, 1992, 2000, 2004]

oo[oo.Year.isin(years_of_interest)]
```

```python
oo[~oo.Year.isin(years_of_interest)]
```

#### Finding and dealing with missing values

`.info()` shows the number of non-null entries in each column.

```python
oo.info()
```

### Creating Series and Dataframes

One way to create a dataframe is to create a dictionary, with each `key` as a column header
and each `value` as a list representing all the entries in that column.

```python
city = ["London", "Rio", "Tokyo"]
start_date = ["27th Jul, 2012", "5th Aug, 2016", "23rd July, 2021"]

pd.DataFrame({"City": pd.Series(city),
              "Start Date": pd.Series(start_date)})
```

You can also convert a list to a Pandas Series.

```python
pd.Series(city)
```

Another way to create a dataframe is using the `zip()` method:

```python
pd.DataFrame(zip(city, start_date))
```

Pass column names using the `zip()` method:
```python
pd.DataFrame(zip(city, start_date), columns=["City", "Start Date"])
```

### Working with dates

```python
city = ["London", "Rio", "Tokyo"]
start_date = ["07-27-2012", "5th Aug, 2016", "23rd Jul, 2021"]
end_date = ["12th Aug, 2012", "21-08-2016", "8th Aug, 2021"]

games = pd.DataFrame(zip(city, start_date, end_date), columns=["City", "Start Date", "End Date"])

games["Start Date"] = pd.to_datetime(games["Start Date"], format='mixed')
games["End Date"] = pd.to_datetime(games["End Date"], format='mixed')
```

Dates can be subtracted
```python
games["End Date"] - games["Start Date"]
```

You can assign these new values to a new column:
```python
games = games.assign(duration=games["End Date"] - games["Start Date"])
```

### Combining DataFrames

Concatenate along the rows:

```python
start = pd.DataFrame({"city": ["London", "Rio", "Tokyo"],
                      "start_date": ["27th Jul, 2012", "5th Aug, 2016", "23rd July, 2021"]})

end = pd.DataFrame({"city": ["London", "Tokyo", "Paris"],
                    "end_date": ["12th Aug, 2012", "8th Aug, 2021", "11th Aug, 2024"]})

pd.concat([start, end], axis=0)
```

Inner join combines available data. Only data available in both `start` and `end` will be outputted here.

```python
pd.merge(left=start, right=end, on="city", how="inner")
```

Outer join will leave values as `NaN`s if they are missing for certain combinations of data.

```python
pd.merge(left=start, right=end, on="city", how="outer")
```

A left join will take the keys from the left dataframe and merge with the corresponding values in the right dataframe if they exist.

```python
pd.merge(left=start, right=end, on="city", how="left")
```

A right join will take the keys from the right dataframe and merge with the corresponding values in the left dataframe if they exist.

```python
pd.merge(left=start, right=end, on="city", how="right")
```

### Combining Datasets

You first have to pre-process the headers for each column in the two datasets, making sure they match exactly.

```python
pd.concat([oo, nw], axis=0)
```

### Working with Missing Data

Create a boolean Series showing whether each entry in the Series is `NaN`

```python
nw['City'].isna()
```

Check the number of `NaN`s in a Series

```python
nw['City'].isna().sum()
```

Check all the rows where a specific column has a `NaN` entry

```python
nw[nw['City'].isna()]
```

Fill `NaN`s with a desired value

```python
nw['City'] = nw['City'].fillna(value="Beijing")
```

Drop rows with `NaN`s

```python
nw.dropna(how="all", axis=0) # if all columns in a row are NaN, delete that row
nw.dropna(how="any", axis=0) # if any column in a row has a NaN, delete that row
```

Drop rows wth `NaN`s in specific columns

```python
nw.dropna(subset=['Sport', 'Discipline', 'Athlete Name', 'NOC', 'Gender',
       'Event', 'Event Gender', 'Medal'], how="all")
```

### Working with Duplicates

Check the rows with duplicates

```python
nw.loc[nw.duplicated(), :]
```

Drop the duplicate rows

```python
nw = nw.drop_duplicates()
```

### `GroupBy`

Use [Pandas Tutor](pandastutor.com) to visualize `groupby` objects.

Create a `groupby` object

```python
up.groupby("Year")
```

Show counts for each group

```python
up.groupby("Year").count()
```

Iterate through each group and show its contents

```python
for group_key, group_value in up.groupby('Year'):
    print(group_key)
    print(group_value)
```

Pass a list of columns to see counts when grouping by each column

```python
up.groupby(['Year']).count()
```

`.size()` can also be used, but it also includes null values.

```python
up.groupby("Year").size()
```

When passing several columns, groups will be created based on the first column, then subgroups will be created within those primary groups based on the second column.

```python
up.groupby(['Year','NOC']).count()
```

Check the count for just a specific column within these new groups

```python
up.groupby(['Year','NOC'])['Medal'].count()
```

You can then perform operations on the created groups

```python
up.groupby(['NOC'])['Year'].min()
up.groupby(['NOC'])['Year'].max()
```

Or perform several at once

```python
up.groupby(['NOC'])['Year'].agg(['min', 'max', 'count'])
```

### Reshaping data: Stacking, Unstacking and MultiIndex

Use [Pandas Tutor](pandastutor.com) to visualize `stack` and `unstack` operations.

```python
sp.unstack('Gender', fill_value=0)
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Men</th>
      <th>Women</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th>Event</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">JAM</th>
      <th>100m</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">TRI</th>
      <th>100m</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">USA</th>
      <th>100m</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</td>
</table>
</div>

```python
(sp
 .unstack('Gender', fill_value=0)
 .unstack('Event', fill_value=0)
)
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Gender</th>
      <th colspan="2" halign="left">Men</th>
      <th colspan="2" halign="left">Women</th>
    </tr>
    <tr>
      <th>Event</th>
      <th>100m</th>
      <th>200m</th>
      <th>100m</th>
      <th>200m</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>JAM</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>TRI</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>USA</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</td>
</table>
</div>

```python
sp.unstack(['Gender', 'Event'], fill_value=0)
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Gender</th>
      <th colspan="2" halign="left">Men</th>
      <th colspan="2" halign="left">Women</th>
    </tr>
    <tr>
      <th>Event</th>
      <th>100m</th>
      <th>200m</th>
      <th>100m</th>
      <th>200m</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>JAM</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>TRI</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>USA</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</td>
</table>
</div>

```python
sp = sprints.groupby(['NOC','Gender','Event']).size()
sp
```
<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>

<blockquote><pre>
NOC  Gender  Event
JAM  Men     100m     1
             200m     1
     Women   100m     3
             200m     2
TRI  Men     100m     1
             200m     0
     Women   100m     0
             200m     0
USA  Men     100m     1
             200m     2
     Women   100m     0
             200m     1
dtype: int64
</pre></blockquote>

</td></table></div>

```python
sp.unstack(level=1, fill_value=0)
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Men</th>
      <th>Women</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th>Event</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">JAM</th>
      <th>100m</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">TRI</th>
      <th>100m</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">USA</th>
      <th>100m</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>200m</th>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</td></table>
</div>

```python
sprints_table = sp.unstack(level=1, fill_value=0).unstack(level=1, fill_value=0)
sprints_table
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Gender</th>
      <th colspan="2" halign="left">Men</th>
      <th colspan="2" halign="left">Women</th>
    </tr>
    <tr>
      <th>Event</th>
      <th>100m</th>
      <th>200m</th>
      <th>100m</th>
      <th>200m</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>JAM</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>TRI</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>USA</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table></td></table>
</div>

```python
sprints_NOC = sprints_table.stack("Gender")
sprints_NOC
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event</th>
      <th>100m</th>
      <th>200m</th>
    </tr>
    <tr>
      <th>NOC</th>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">JAM</th>
      <th>Men</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Women</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">TRI</th>
      <th>Men</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Women</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">USA</th>
      <th>Men</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Women</th>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table></td></table>
</div>

```python
sprints_NOC.index
```

<div>
<table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<blockquote><pre>
MultiIndex([('JAM',   'Men'),
            ('JAM', 'Women'),
            ('TRI',   'Men'),
            ('TRI', 'Women'),
            ('USA',   'Men'),
            ('USA', 'Women')],
           names=['NOC', 'Gender'])
</pre></blockquote></td></table></div>

```python
sprints_NOC.loc[('JAM',   'Men'), :]
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td>
<blockquote><pre>
Event
100m    1
200m    1
Name: (JAM, Men), dtype: int64
</pre></blockquote></td></table></div>

```python
sprints_NOC.loc[('JAM',   'Men'), '100m']
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td><blockquote><pre>
np.int64(1)
</pre></blockquote></td></table></div>

```python
sprints_NOC.iloc[0, :]
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td><blockquote><pre>
Event
100m    1
200m    1
Name: (JAM, Men), dtype: int64
</pre></blockquote></td></table></div>

```python
sprints_NOC.iloc[0, 0]
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td><blockquote><pre>
np.int64(1)
</pre></blockquote></td></table></div>

### Finding desired functions

If you are trying to accomplish a specific action and are looking for a method to help you do it,
you can perform a search on the documentation of all available methods.

Using regular expressions, you can search for a specific string in all documentation.

```python
import re
import pandas as pd

search_string = "excel"

[func for func in dir(pd) if re.search(rf"{search_string}", func, re.IGNORECASE)]
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td><blockquote><pre>
['ExcelFile', 'ExcelWriter', 'read_excel']
</pre></blockquote></td></table></div>

```python
import re

search_string = "upper"

[func for func in dir(nw["Athlete Name"].str) if re.search(rf"{search_string}", func, re.IGNORECASE)]
```

<div><table border="0">
<tr>
  <th valign="top">Output:</th>
  <td><blockquote><pre>
['isupper', 'upper']
</pre></blockquote></td></table></div>