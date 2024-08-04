## RILM:  The World's Writings on a World of Music

**RILM** is the **Répetoire Internationale de Littérature Musicale**.  It is the leading international database of writings about all forms of music, across time and place.  Based in New York, the RILM team includes dozens of librarians, musicologists, and information technologists around the globe who work to index writings about music in hundreds of journals, books, and other materials that appear annually. Their flagship product is called [**RILM Abstracts of Music Literature**](https://www.rilm.org/abstracts/), and currently includes over 1.6 million items published during the last 75 years.

Haverford, Bryn Mawr, and Swarthmore College subscribe to this database, which you can search via our EBSCO interface (visit the [Music Library Resources](https://guides.tricolib.brynmawr.edu/music) page to find it).


## What do RILM Abstracts Look Like?

Let's take a single entry in RILM as a point of departure.  What kinds of information do we find here?  Here is an item returned from a search for `symphonies, no. 9, op. 125`. 


It is an essay about an important commemorative performance of the Beethoven Ninth Symphony held a year after the attack on New York on September 11, 2001:

![alt text](../01_Tutorials/images/rilm_1.png)

The EBSCO interface presents the record as a series of nicely formatted blocks:

- **document** type (in this case an article in a periodical)
- **authors** (just one in the case: Peter Tregear) 
- **major subject heading** (it begins with a category number, then a description; it drawn from a 'controlled vocabulary' of terms that RILM maintains, so that they indexing is consistent)
- **a series of 'subject entries'** (more on these below)
- an **abstract** (a narrative description of the item; normally there are in English even if they publication is not)
- **publication date**
- the **'source' of the publication** (in this case: a periodical called Beethoven Forum; also volume and page information, since it is a periodical)
- **country and language of publication**
- a **url** (not all publications have these, but this is available online)
- something called the '**ISSN**' (the International Series number, which is a unique identifier for the Beethoven Forum)
- a **RILM 'accession' number** (their unique identifier for it in the RILM database; the first four numbers correspond to the year of publication)

#### Subject Entries Up Close

These RILM entries are rich with detail.  The **abstract** provides a great way to understand the gist of an article, even if you cannot read it in the original language.  But from the standpoint of our interest in data about music, the **subject entries** are particularly important.  In this case there six of them, each with a different 'top level' term:

- **Beethoven, Ludwig van** (the composer, of course!)
- **reception** (the general term for the kind of historical or critical study of how some idea or work of art is understood in different ways across time or place)
- wars and catastrophes (sadly, we know what these are, and music is often connected with them)
- **Adorno, Theodor W**. (an important German music philosopher and critic of the 20th century; he emigrated to the USA during the Nazi period)
- **Mann, Thomas** (an equally important German author of the 20th century; he also emigrated to the USA)
- **Taruskin, Richard** (a very important musicologist and critic; he taught for many years at the University of California, Berkeley)

Each of these top-level terms is in turn followed by a cascade of lower-level terms, each more specific than the next. In the first, for instance:

"Beethoven==>reception==>symphonies, no.9, op. 125==>relationship to 9/11 terrorist attacks"
Meanwhile the second is a slight variation on the first, switching the first two levels around, so that we move from 'reception' to 'Beethoven' and not the other way around. The point here is to understand each of these as a hierarchy of terms that would allow researchers starting at different points of entry to find their way not only to *this* item, but also to all the *other* items that might deal with a similar subject from a related perspective.

And to do this, the RILM team have devised what is called a **'controlled vocabulary'** of terms:  uniform ways of naming a particular person, work, place, or idea.  This is what makes RILM so powerful, and what will make our exploration of the relationship among these 'entities' so interesting.

## From RILM Search to DataFrame

We are fortunate that the RILM team (Freedman is a member of the Board of Directors) is also interested to see what students in Encoding Music can help them discover about their data:

- Looking for changing trends in musicological discourse
- Creating knowledge graphs that show the connections among different topics, people, and places

We manage all this via an 'key' (the 'Bearer Token') allows us to access their database directly via a special API that they have created for us. Your instructor will provide the key as needed in class for you to use.

Note that *this key is just for use in the context of our class, and not to be published or shared*.  

*DO NOT post the Bearer Token to any code you keep on Github or any public resource!*

In brief, our `get_query_data` function allows us to:

- post a request to the API
- return matching results as json 
- load the json as a dataframe
- clean up the RILM column names to something more useful

<Details>

<Summary>Code to Fetch Data from RILM API</Summary>

```python

AB_BASE = "https://ibis2.rilm.org/api/rilm_index/rilm_index_strings_by_term"


URLS = {
    # "year": AB_BASE + "rilm_index_RYs",
    # "terms": AB_BASE + "rilm_index_top_terms",
    "index": AB_BASE
}

# note that the Bearer_Token is NOT part of this document!
BEARER_TOKEN = "our_secret_token"

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# the api request function

def get_query_data(search_term):
    """ Returns the results of an API query for the given search term """
    # query the API
    params = {
        "termName": search_term,
        "includeAuthors": True
    }

    # and get the response
    response = requests.get(
        URLS["index"], 
        headers=HEADERS, 
        params=params
    )

    # get the data
    data = response.json()
    results = pd.DataFrame(data)
    results = results.fillna('')
    # # combines year and accession number to make unique id for each item
    results['full_acc'] = results.ry.apply(str) + "-"  + results.ac.apply(str)
    results.rename(columns = {'ry':'year', 'ac': 'item', 'ent' : 'entry', 'lvl': 'level', 'name': 'term', 'cat': 'category', 'full_acc': 'full_id'}, inplace=True)
    return results

# clean up column names and provide for a way to filter by year and categories of terms
def clean_query_data(results, year_list, categories):
    """
    Cleans the query results for a given a search term, list of years, and list of categories
    results : pandas dataframe containing the results from the API query
    year : list of ints
    category : list of strings
    """
    # parse results for corresponding entries
    if year_list is not None:
        results = results[results['year'].isin(year_list)]
    if categories is not None:
        # results = results[results['category'] == category]
        results = results[results['category'].isin(categories)]
    results = results.drop_duplicates(['term', 'full_id'])
    return results
```

</Details>

<br>

Our `get_query_data` function takes in a search term and two optional lists:  selected years, and selected categories (more about the latter below).  The `clean_query_data` function takes in the first function, and takes care of the cleanup of column names.  Here is what a search Beethoven's Ninth looks like without any filters for years or categories: 


```python
search_term = 'symphonies, no. 9, op. 125'
year_list = None
categories = None
results = clean_query_data(get_query_data(search_term), year_list, categories)
```

The resulting dataframe is more than 5,000 lines long! Of course there does not mean there are 5,000 individual writings about the Ninth.  

![alt text](../01_Tutorials/images/rilm_2.png)


We could figure that out by checking the `nunique()` of the 'full_id' column:

`results['full_id'].nunique()`

There are 416 unique items in this case!

Now let's have a look at *just* the article by Peter Tregear we discussed above.  We can find it this way:

```python
df = pd.DataFrame(data)
filtered_df = df[(df['ry'] == 2003) & (df['author'] == 'Tregear, Peter')]
filtered_df
```

<br>

![alt text](../01_Tutorials/images/rilm_3.png)

<br>

### A Guide to the RILM Column Headings


#### `year`, `item`, and `full_id`

These are the **year** of publication and a **RILM "item" number** for that year (these repeat from year to year). We also combine these to make a **full_id**, which is a unique identifier for each publication abstract.

#### `entry` and `level` values

Now we begin to understand how the data are organized.  Each 'row' corresponds to  *one level* of *one subject entry* for that article. And so if we further limit these results to only those where `ent` is 1, we will find a tiny dataframe that includes (in order) each of the successive "levels" (see the `lvl` colum for that entry).  

- An 'entry' can have more than one 'level'.  
- A given 'level' can only belong to one 'entry'.

<br>

```python
entry_1 = filtered_df[filtered_df['entry'] == 1]
entry_1
```

<br>

![alt text](../01_Tutorials/images/rilm_4.png)

<br>

Reading *down* the `level` column would allow us to reconstruct the entire subject entry:

"Beethoven==>reception==>symphonies, no.9, op. 125==>relationship to 9/11 terrorist attacks"


#### Controlled Vocabulary:  the `id` Value

The `id` column is not the identifier of the *article*, but instead the **unique identifier of the particular term in the controlled vocabulary**.  For example:

- The `id` for "reception" is 191504.  
- The `id` for Beethoven's Ninth is 358192.  

And so on.

#### Result String and Category:  the `term`  and `category` Values

The `term` column is the term for that particular level of a given entry. 

There is another important column associated with these:  `category`. As the title suggests, this is a 'categorical' that helps us understand the *kind* of information conveyed in the corresponding `term` field in the same row.  We can use these to refine our searches, or to perform various kinds of groupBy operations on the results.

Here are some of the typical `category` values you wil encounter (and what they mean): 
 

```
B = broadcasts, radio, TV, and podcasts
C = title of choreographic work
D = dictionary
E = ethnic group
F = films and videos
G = geographic name
I = instrument
L = literary work (poetry and prose)
M = margin
N = personal name
O = Organization (other than a school)
P =  periodical
Q = databases
R = treatise
S = school
T = topic
V = visual art
W = work title
```


The most important are probably:

- G = geographic name
- N = personal name
- W = work titleW
- T = topic

### Filtered Searches

Of course with Pandas it is possible to filter our search results in all kinds of ways using the various columns and rows.

But we can also use our original functions to limit the data in the first place.   Here we 'sample' the years of so that we take only every fifth year in the range between 1980 and 2021 (remember that the end number in these range functions is _exclusive_, so if we want to include 2020 we will to put our upper limit as 2021).

Meanwhile we also limit our search to only 

```python
search_term = 'symphonies, no. 9, op. 125'
year_list = [*range(1980, 2021, 5)]
categories = ['G', "N", "W", "T"]
results = clean_query_data(get_query_data(search_term), year_list, categories)
results
```

There are 610 rows and 416 abstracts.


## Charts and Networks with RILM Data


We can also render the results of our search in various kinds of charts and networks that will help us see the changing character of research.

Here, for instance we have the results of a function that will create a histogram of the "X" most frequently occuring terms in writings about the Beethoven Ninth.  In this case we produce three different charts: one for 1900-1950, one for 1950-2000 and one for 2000 to the present.  Here is how we run one of these:

```python
search_term = 'symphonies, no. 9, op. 125'
# set year range
year_list = [*range(2000, 2024, 1)]
# select categories
categories = ['G', "N", "W", "T"]
# number of terms to show in histogram
num_hist_terms = 20

# get results 
results = clean_query_data(get_query_data(search_term), year_list, categories)

# make the chart
term_hist(results, num_terms=num_hist_terms)
```

<br>

And the results:

<br>


![alt text](../01_Tutorials/images/rilm_5.png)

<br>

![alt text](../01_Tutorials/images/rilm_6.png)

<br>

![alt text](../01_Tutorials/images/rilm_7.png)

In these we can see the rise of terms like 'reception' and the relative decline of a concern for 'creative process'.



<br>



<Details>

<Summary> Code For RILM Histogram </Summary>

```python
def term_hist(cleaned_df, num_terms=5):
    """Creates, shows, and returns a histogram showing the number of times each term appears in the DataFrame using Plotly Express.
    
    @param cleaned_df: the cleaned DataFrame to count the term occurrences in
    @param num_terms: the number of terms to show on the histogram
    @return: the Plotly figure object of the histogram
    """
    # Count the occurrences of each term
    counts = dict(cleaned_df['term'].value_counts())
    # Create a DataFrame from the counts
    counts_frame = pd.DataFrame({'term': counts.keys(), 'occurences': counts.values()})
    # Sort the DataFrame by the number of occurrences in descending order
    counts_frame = counts_frame.sort_values(by='occurences', ascending=False)
    # Limit the DataFrame to the top num_terms terms
    counts_frame = counts_frame.head(num_terms)
    
    # Create the bar chart using Plotly Express
    fig = px.bar(counts_frame, x='term', y='occurences', title='Number of Occurences of Terms')
    
    # Update the layout to make the plot vertical and place the legend at the side
    fig.update_layout(
        legend=dict(orientation="v", yanchor="top", y=1.1, xanchor="right", x=1),
        autosize=True,
        margin=dict(l=50, r=50, t=50, b=100),
        height=600
    )

    return fig
```

</Details>

<br>

### A Network of Concepts, People, Places, and Works

Finally, we can also use networkX and Pyvis to create a revealing network of related terms.  Each top-level search term becomes a node.  Each time two of these top-level terms occur in the _same_ publication they are connected with an edge.  And each 'category' of term (People, Geographical entities, Works, and Terms [abstract concepts]) gets a distinctive color.

Note that in addition to filtering by years and categories, we also need to add a `weight_threshold` value, which represents the _proportion_ of that term among the graphed results.  1 is the default, but depending on how many results you return, this could be a very dense graph.

Here we look at just the years between 2000 and 2004, in order to take a measure of where our Tregear article fits in:



```python
search_term = 'symphonies, no. 9, op. 125'
year_list = [*range(2000, 2005, 1)]
categories = ['G', "N", "W", "T"]
weight_threshold=2
concept_map_name = "concept_map.html"

results = clean_query_data(get_query_data(search_term), year_list, categories)
create_concept_map(results, weight_threshold=weight_threshold).show(concept_map_name)
```

<br>

Here is the big picture:


<br>

![alt text](../01_Tutorials/images/rilm_8.png)

And the local area where our article is manifest as a series of connected 'nodes' relating to politics and reception:



<br>

![alt text](../01_Tutorials/images/rilm_9.png)

<br>

<Details>

<Summary>Code for Network of RILM Results</Summary>

```python
def create_concept_map(results, weight_threshold=1):
    """
    Creates a concept map given cleaned query results
    results : pandas dataframe containing the results from the API query cleaned for a given a search term, list of 
                years, and list of categories
    """
    
    # get dictionary with key=full_id, value=list of unique terms
    terms_dict = {}

    past_id = results.iloc[0]['full_id']
    terms_list = []
    for index, row in results.iterrows():
        curr_id = row['full_id']
        if curr_id == past_id:
            terms_list.append(row['term'])
        else:
            terms_dict[past_id] = terms_list
            past_id = curr_id
            terms_list = [row['term']]
    terms_dict[past_id] = terms_list

    # get list of all combinations of pairs for each entry
    pairs_list = []
    for key, value in terms_dict.items():
        pairs_list += list(combinations(value, 2))
        
    # get edge weights and unique nodes
    for i, p in enumerate(pairs_list):
        pairs_list[i] = tuple(sorted(p))
        
    if weight_threshold == 0:
        weighted_plist = [[elem, count] for elem, count, in Counter(pairs_list).items() if count >= weight_threshold]
        nodes = results['term'].unique()
    else:
        nodes = set()
        weighted_plist = []
        for ele, count in Counter(pairs_list).items():
            if count >= weight_threshold:
                weighted_plist.append([ele, count])
                if weight_threshold > 0:
                    nodes.add(ele[0])
                    nodes.add(ele[1])
                    
    # get the information about each unique node [category, list of years, number of years]
    nodes_dict = {}
    for node in nodes:
        node_info = []
        node_info.append(results[results['term'] == node]['category'].unique()[0])
        node_info.append(results[results['term'] == node]['year'].unique())
        node_info.append(len(node_info[1]))
        nodes_dict[node] = node_info

    # create network
    G = nx.Graph()
    # cmap = Network(notebook=True, width=1000, height = 800)
    
    cmap = Network(notebook=True,
                   width="1500px",
                          height="1500px",
                          bgcolor="black", 
                          font_color="white")
    # Set the physics layout of the network
    cmap.set_options("""
    {
    "physics": {
    "enabled": true,
    "forceAtlas2Based": {
        "springLength": 1
    },
    "solver": "forceAtlas2Based"
    }
    }
    """)
    
    for name, info in nodes_dict.items():
        years = f"years: {*info[1],}"
        
        G.add_node(name, value=info[2], group=info[0], title=years)
        
    for pair, weight in weighted_plist:

        G.add_edge(pair[0], pair[1], value=weight, title=str(weight))
    cmap.from_nx(G)
    # return the network
    
    return cmap
```

</Details>




