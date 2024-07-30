# Common Considerations for Pandas

## Using this document

### Finding the right FAQ

`^ Ctrl`+`F` (Windows) and `⌘ Cmd`+`F` (Mac) are your friends in this document! Use them to find an FAQ that could help you.

Each FAQ is titled with an **objective** - a task you might want to accomplish. Each also has an example of why that task might be necessary.

### Using links in the FAQ

In this document, any internal links (those pointing to another file) also include header information. When you first click the link, you'll just be taken to the top of the page. **Reload the page** after clicking any link in this FAQ to be directed to the appropiate section of the page.

### Don't forget the official documentation

Read the official Pandas [documentation][pandas-documentation].

Find tutorials at [W3Schools][w3schools].

A helpful [Pandas Cheat Sheet][pandas-cheat-sheet].

## When I want to…

<details>
<summary>
<strong>…find all the entries in a dataframe containing specific text</strong>
<blockquote style="margin-left: 13px;"><em>Ex: Find all the songs written by John Lennon</em></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="07_Pandas_Filter_Find_Group.md#searching-for-strings-and-substrings">filter</a> ("searching for strings and substrings") in our documentation</li>
</ul>
</details>

<details>
<summary>
<strong>…deal with missing data</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Identify all albums without a release date</em></blockquote>
</summary>
<ul>
    <li>See Pandas <code><a href="05_Pandas_Clean_Data.md#finding-missing-data">.isna()</a></code> for checking whether a cell is empty</li>
    <li>Create a <a href="07_Pandas_Filter_Find_Group.md#using-filters">filter</a> using a condition with <code>.isna()</code>. For example:<br>
<pre><code>beatles_billboard[beatles_billboard['Album.debut'].isna()]
</code></pre></li>
    <li>See Pandas <code><a href="05_Pandas_Clean_Data.md#filling-missing-data">.fillna()</a></code> for replacing missing information with something more meaningful<br>
    <blockquote><em>Ex: Replace </em><code>NaN</code><em> with </em><code>"unreleased"</code><em> for albums without a release date</em></blockquote>
</ul>
</details>

<details>
<summary>
<strong>…find all the rows in my dataframe meeting a specific condition</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Identify all the albums that reached Top 10 in the Billboard charts</em></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="07_Pandas_Filter_Find_Group#using-filters">filter</a> for finding rows based on information about the row</li>
</ul>
</details>

<details>
<summary>
<strong>…separate the data into subsets and create statistics on those subsets</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Create a subset of the data for each album and find average duration for each album</em></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="07_Pandas_Filter_Find_Group#groupby-functions">groupby</a> for separating a dataset into several groups based on certain criteria, then applying a function to each group independently</li>
</ul>
</details>

<details>
<summary>
<strong>…combine two datasets that have the exact same columns</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Combine two datasets containing data about albums that are formatted in the same way, just containing different albums</em></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="04_Pandas_Basics#combining-joining-and-merging-dataframes">concatenate</a> for combining two datasets with the same columns</li>
</ul>
</details>

<details>
<summary>
<strong>…combine two datasets that have different columns</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Combine billboard data and spotify data about the same tracks into one dataframe</em></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="04_Pandas_Basics#combining-joining-and-merging-dataframes">merging</a> for combining two datasets with the mostly different columns</li>
</ul>
</details>

<details>
<summary>
<strong>…get data from a file or other external source</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Import your Google Sheet into Pandas</em></blockquote>
</summary>
<ul>
    <li>
        If you want to access a Google Sheet in Pandas, you first need to publish it to the web as a CSV. Open the Google Sheet, then click <code>File -> Share -> Publish to web</code>. Change the option from "Entire document" to just the sheet (spreadsheet tab) you need. Change the option from "Web page" to "Comma-separated values (.csv)". Then copy the link and hit "Publish".
    </li>
    <li>See <code><a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html">pd.read_csv()</a></code> for detailed documentation on importing CSVs.<br>
<pre><code>df = pd.read_csv(file)
</code></pre></li>
<li>If the csv is stored locally, use a file path</li>
    <li>If using a google sheet, paste the URL</li>
    <li>Use quotation marks in both cases</li>
</ul>
</details>

<details>
<summary>
<strong>…make changes to a dataframe without getting rid of the original data</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Filter a dataframe containing album data to only contain Billboard Top 10 albums, but maintain the original list of albums for comparison</em></blockquote>
</summary>
<ul>
    <li>Use Pandas <code><a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy">df.copy()</a></code> to create a copy of your original dataframe, then perform operations on this copy.<br>
<pre><code>copy_df = original_df.copy()
</code></pre></li>
<li>Now perform operations (like filtering) on <code>copy_df</code> without modifying <code>original_df</code></li>
</ul>
</details>

<details>
<summary>
<strong>…modify the way my data is formatted to make it more "tidy"</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Instead of a string of genres in each row, create one row for each genre</em></blockquote>
</summary>
<ul>
    <li>If all your data is in one column, and you want it to be split into several rows, use <code><a href="06_Pandas_Tidy_Data.md#fixing-multiple-observations-in-one-row-explode">explode()</a></code>. Note it is necessary to <a href="05_Pandas_Clean_Data.md">clean data</a> first.<br>
<pre><code>exploded_df = df.explode(column_name)
</code></pre></li>
    <li>
        If there are multiple observations in one row, each in a different column, and you want to have just one observation per row, use <code><a href="06_Pandas_Tidy_Data.md#fixing-multiple-observations-in-one-row-melt">melt()</a></code>. 
        In the below example, <code>'id_column'</code> is the name of a column that uniquely identifies each row. The column names listed in <code>value_vars</code> are the columns containing observations that you would prefer to be stored in separate rows.<br>
<pre><code>melted_df = pd.melt(original_df, id_vars=['id_column'], value_vars=["col_1", "col_2", "col_3"]).sort_values('id_column').reset_index(drop=True)
</code></pre>
    </li>
    <li>See more examples in <a href="06_Pandas_Tidy_Data.md">Pandas: Tidy Data</a>
</ul>
</details>

<details>
<summary>
<strong>…modify all the entries in a particular column or dataframe</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Replace every instance of the number </em><code>-1</code><em> with the number </em><code>0</code><em></em></blockquote>
</summary>
<ul>
    <li>See Pandas <code><a href="05_Pandas_Clean_Data.md#cleaning-data-with-functions">.apply()</a></code> to apply a custom operation (such as a function you wrote) on every entry in a row, column, or dataframe<br>
<pre><code>df['column_name'] = df['column_name'].apply(function_name)
</code></pre></li>
    <li>Learn more about <code>.apply()</code> in the Pandas <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas-dataframe-apply">documentation</a></li>
    <li>If the entries being changes are text, consider using <a href="05_Pandas_Clean_Data.md#wrong-or-inconsistent-format-or-values">string methods</a>
</ul>
</details>

<details>
<summary>
<strong>…count the occurences of specific data in a column or dataframe</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: Count the number of songs written by John Lennon</em></blockquote>
</summary>
<ul>
    <li>Use Pandas <code><a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count">.count()</a></code> on a <a href="">filtered</a> dataframe or series.<br>
<pre><code>df[filter_condition].count()
</code></pre>
<pre><code>df[filter_condition]['column_name'].count()
</code></pre></li>
</ul>
</details>

<details>
<summary>
<strong>…deal with data that I can't understand because it is too complex</strong><br>
<blockquote style="margin-left: 13px;"><em>Ex: I have no idea what my dataset even is!</em></blockquote>
</summary>
<ul>
    <li>Use Pandas methods that give you a better sense of the data</li>
    <li>Review sections 1-4 in <a href="04_Pandas_Basics.md">Pandas: Basics</a>
    <li>See <a href="04_Pandas_Basics.md#sort-and-count">Sort and Count</a> in <a href="04_Pandas_Basics.md">Pandas: Basics</a> in particular for info on your data using <code>.value_counts()</code> and <code>.sort_values()</code><br> 
    </li>
    <li>Learn about <a href="05_Pandas_Clean_Data.md#identifying-the-problem">identifying errors in your data</a></li>
</ul>
</details>

<!-- TODO: More information about what visualization fits what problem -->

[pandas-documentation]: https://pandas.pydata.org/about/
[w3schools]: https://www.w3schools.com/python/pandas/default.asp
[pandas-cheat-sheet]: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf