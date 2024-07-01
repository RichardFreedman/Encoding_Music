# Common Considerations for Pandas

### When I need to…
<details>
<summary>
<b>…find all the entries in a dataframe containing specific text</b><br>
<blockquote style="margin-left: 13px;"><i>Ex: Find all the songs written by John Lennon</i></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="">filter</a></li>
</ul>
</details>

<details>
<summary>
<b>…deal with missing data</b><br>
<blockquote style="margin-left: 13px;"><i>Ex: Identify all albums without a release date</i></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="">.isna()</a> for checking whether a cell is empty</li>
    <li>See Pandas <a href="">filter</a> for removing rows based on information about the row</li>
    <li>See Pandas <a href="">.fillna()</a> for replacing missing information with something more meaningful<br>
    <blockquote><i>Ex: Replace </i><code>NaN</code><i> with </i><code>"unreleased"</code><i> for albums without a release date</i></blockquote>
</ul>
</details>

<details>
<summary>
<b>…find all the rows in my dataframe meeting a specific condition</b><br>
<blockquote style="margin-left: 13px;"><i>Ex: Identify all the albums that reached Top 10 in the Billboard charts</i></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="">filter</a> for removing rows based on information about the row</li>
</ul>
</details>

<details>
<summary>
<b>…separate the data into subsets and create statistics on those subsets</b><br>
<blockquote style="margin-left: 13px;"><i>Ex: Separate the dataset into songs with either high or low danceability, and find the average popularity of each</i></blockquote>
</summary>
<ul>
    <li>See Pandas <a href="">groupby</a> for separating a dataset into several groups based on certain criteria, then applying a function to each group independently<br>
    <pre><code class="language-python">code for this goes here
print("hello world")</code></pre<</li>
</ul>
</details>



<br><br><br><br>

**When I want to** *select data based on conditions*, I can use:

| Condition          | Command                                  |
|--------------------|------------------------------------------|
| Greater than 10    | `df[df['column'] > 10]`                  |
| Not equal to 5     | `df[df['column'] != 5]`                  |


<details>
<summary><b>How do I deal with <code>NaNs</code> (blank entries) in my data?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I copy a dataframe?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I import external data into Pandas?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I combine two dataframes together?</b></summary>
<ul>
    <li>Joining</li>
    <li>Merging</li>
</ul>
</details>

<details>
<summary><b>What practices will make my data easier to work with?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I filter a dataframe based on a condition?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I perform the same operation on an entire column, row, or dataframe?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I count the number of occurences of something in a dataframe?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<details>
<summary><b>How can I work with categorical data (using <code>groupby()</code>)?</b></summary>
<ul>
    <li>To do</li>
</ul>
</details>

<br><br><br>

Pandas - NaNs in data √

Naming these things:
* Dealing with NAs
* Copying dataframes
* Importing CSV file
    * JSONs
* Joining DFs
* Practical aspects of Tidying Data
    * also see Grouping
* Filter a data frame for certain conditions
* Apply - I need to process a data frame
    * Map
* Counting
* Grouping
    * GroupBy (understanding what a GroupBy object is)
    * Melt and Explode

Importing, merging, filtering, transforming (scalars into categoricals), grouping (by particular set)

What kind of visualization do I need?
Why a bar chart, scatter, regression, etc.?
How can I use size, color, labels, etc? - what story does it tell?
How do you do beyond two dimensions?

Tuple Trouble
Column that has a list of elements in it
Dates in Pandas