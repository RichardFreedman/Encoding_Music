

---

# All About Networks

In this tutorial you will learn about networks, and how to build them with Python, Pandas, and Pyvis.

Note that for some of the demonstrations offered below you will be working with The Beatles Spotify and Billboard data. These are already available as CSV files.  For other projects you will need to bring your own data, either from Spotify or from some other project.

## Contents of this Tutorial

* [Networks:  Basic Concepts and Methods](#networks--basic-concepts-and-methods)
* [A Simple Network of Students](#a-simple-example--a-network-of-students)
* [Pyvis and NetworkX:  Python Tools for Networks](#pyvis-and-networkx--python-tools-for-networks)
* [Networks: From DataFrame to Edge Pairs with Groupby and Explode]()
* [Networks: Adjusting Pyvis Physics for Clarity](#adjust-physics)
* [Networks with Spotify Data](#networks-spotify)
* [Complex Networks:  Related Artists](#artist_networks)
* [Complex Networks:  Song Network](#song-network)
* [Louvain Community Detection:  The Ghost in the Machine](#louvain)




##  Networks:  Basic Concepts and Methods 

In the field of data science, networks (also known as graphs) are powerful tools used to represent and study relationships between entities. A network is composed of **nodes** (also called vertices) and **edges** (also called links). Each node represents an entity, while each edge represents a relationship between two entities.

### Nodes

**Nodes are the fundamental building blocks of a network.** Think of them as the entities or objects you want to study. In a social network, nodes could represent individuals, while in a transportation network, nodes could represent cities.  You could even have different **kinds** of nodes in the same network--for instance some nodes representing musical works and others representing the groups that performed them. These could be distinguished by color or shape.

### Edges

**Edges are the connections between nodes.** They show how the entities are related to each other. In a social network, edges could represent friendships, and in a transportation network, edges could represent roads connecting cities.

### Weights

**Edges can have an associated weight**. The weight of an edge represents the strength or intensity of the relationship between the connected nodes. For example, in a network of academic writings, the weights could represent the number of times authors cited each other. In the transporation network, the weights could represent the number of journeys taken between each pair of places. 

### How are Two Things more Related than Others?

Determining the strength of the relationship between two nodes depends on the context of the network. For example, in a social network, the frequency and duration of interactions, mutual friends, and common interests can help establish the strength of friendships. In other cases, such as a transportation network, the distance between nodes could be a factor in determining the weight of the edges.

### Centrality as a Key Concept in Networks

By design, network visualization tools arrange the nodes so that those with the greatest number of connections to other nodes appear at the center of a two-dimensional field.  Conversely nodes with only a few connections to other nodes wind up at the periphery. Such representations thus reveal "communities". And indeed, there are special algorithms, like *Louvain Community Detection*, that help us discover neighborhoods in complex networks.

### More about Network Theory

You can learn more about [Network Theory](https://en.wikipedia.org/wiki/Network_theory) and explore Network Graphs [here](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)).

## A Simple Example:  A Network of Students

![Network Example of Students](images/Network_resized.png)

In the Network graph above, the highlighted characteristics represent the differences between Haverford student A and every other student. We see that Haverford student A & B only have one difference, so the edge weight is strong and the nodes are closer together. Haverford student B and Bryn Mawr student A have two differences, so the edge weight is _relatively_ weaker. We also see a node in our graph that has no connection and has no similarity to the other three nodes.

Why is Bryn Mawr Student A connected and not Villanova Student A if they both have no similarities to Haverford Student A?

### Reason One

Bryn Mawr student A watches horror movies and Haverford student B also watches horror movies, so they are connected.

### Reason Two (less obvious without context)

Haverford and Bryn Mawr are part of the tri-co! Often in network graphs and in data science, machines find an abstract connection between vast amounts of data, often clustering data or nodes together, but that may not always mean that it is directly evident as to what these clusters or connections represent. For example, none of our node bullet points have "_is part of the tri-co_" as a characteristic, but perhaps there is some underlying bias or evidence that may not be evident to us that _is_ evident to machines which allows them to cluster or connect otherwise "different" data. 

## Pyvis and NetworkX:  Python Tools for Networks

Generally speaking, a network graph is a visual structure designed to emphasize connections between discrete entities. It consists of Nodes and Edges, which represent a system of connected or related elements, and is largely studied within Network Theory. 

We are lucky to have Python-friendly tools designed to help us create and display networks. Such work is in fact done in stages:  

* **NetworkX** is used to build up the list of nodes and edges as a "graph" object (see the excellent [tutorial for NetworkX](https://networkx.org/documentation/stable/tutorial.html) for more assistance).  
* **Pyvis** is used to display the graph, and we can in fact control this representation in various ways, each with its own mathematical basis for the physics that determines the placement of the nodes and edges.  Pyvis and NetworkX are normally used together.
* **Louvain Community Detection** can also be applied to help us partition the network into subgroups.  See more below.

Here is code that will **build, populate, and show a simple Network Graph** using **NetworkX** and **Pyvis**. This sample network consists of just two nodes and one edge to connect them.

```
#python
# import libraries
import pyvis
from pyvis import network as net
import networkx as nx

# create empty graph
G = nx.Graph()

# add nodes from a list of values
G.add_nodes_from(["John", "Paul"])

# add edges between any pair of nodes that are connected
G.add_edge("John", "Paul")

# render with pyvis
pyvis_graph = net.Network(notebook=True, width="800", height="800", bgcolor="white", font_color="black")
pyvis_graph.from_nx(G)
pyvis_graph.show('my_graph.html')
```

<Details>
<Summary>Image of the Network</Summary>

![Alt text](images/network_sample_1.png)

</Details>

<br>

#### Adding Nodes and Edges in One Step

Such a simple network graph above is not very informative:  of course we know that Lennon and McCartney are connected--they were collaborators and band mates! 

You could of course add any number of new nodes and edges to a given network using the same approach:  first make a list of notes, then pass along a series of tuples representing each edge.  But in fact it's possible to add nodes *at the same time you add the edges*, simply by passing a list of tuples that represent the edges.  The networkX graph object (`G = nx.Graph()`) has a method that allows us to do just this:  `G.add_edges_from()`.  For example:

```python
# define a list of tuples for the nodes and edges
# notice that repeating a node is fine; doing so simply adds another edge to the given node
my_edge_list = [("John", "Paul"), ("John", "Ringo"), ("John", "George")]

# create empty graph
G = nx.Graph()

# add the nodes and edges
G.add_edges_from(my_edge_list)

# render with pyvis
pyvis_graph = net.Network(notebook=True, 
width="800", 
height="800", 
bgcolor="white", 
font_color="black")

pyvis_graph.from_nx(G)
pyvis_graph.show('my_graph.html')
```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/network_sample2.png)

</Details>

<br>

And so with `G.add_edges_from()` it should be possible to easily transform tabular data (for instance, a pair of values in each row) as a list of tuples, and pass these directly to NetworkX.  

For additional information on adding attributes to nodes and edges (such as color, size, or pop ups, see the NetworkX documentation cited above.)

One convenient way to do this is to great a dataframe consisting of two columns: 

* a list of all the edges (and thus nodes), expressed as tuples
* the 'counts' of each tuple (which provides the edge weights) 

Imagine this:

![alt text](<images/tuples to network.png>)

*But how do we get from Pandas dataframes to a table of edge pairs and counts like this one?*  

----
##  From DataFrame to Edge Pairs:  Groupby and Explode


Deriving a table of edge pairs from your original dataframe takes some knowledge of several key Pandas and Python methods.  If you don't recall the first and second of these, review them in the relevant tutorial!

* **Groupby** (the 'groups' provide the basis of the edges, since all the items in a given group share some characteristic with each other)
* **Explode** (since once we aggregate the groups into a single new dataframe, and all of the tuples for each group into a single column, we need to 'tidy' them in order to simply the process of using `G.add_edges_from()`).
* **Combinations** (a method available in the 'itertools' library, which helps us build up pairs of all of the items in each group; these will be our tuples, and in turn our edges.)


Let's look at these steps in detail using the **Beatles Billboard** data. There are some 300 songs in this dataset, if we imagine a network with 300 nodes, it would almost certainly be too complex to interepret. But the Billboard dataset also includes some 'genre' labels, and it could be interesting to see how these genres fall into families. They might not reveal a lot about the songs, but they would definitely tell us something about the folks who assigned the labels in the first place!

##  Create a Notebook and Load the Pandas library 

```python
import pandas as pd
```


##  Meet the Beatles (Again) 

We continue with our data about The Beatles:

* A set from **Spotify** includes information about 193 songs, albums, years, plus other acoustic ratings that Spotify uses to characterize tracks. View these data as a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1CBiNbxqF4FHWMkFv-C6nl7AyOJUFqycrR-EvWvDZEWY/edit#gid=953807965).

* A set of **Billboard** data compiled by a team at the **University of Belgrade (Serbia)** that contains information about over 300 Beatles songs:  author(s), lead singer(s), album, musical genre(s), and standing in the Top 50 Billboard charts.  View these data on [Github]('https://github.com/inteligentni/Class-05-Feature-engineering/blob/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv').

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

## But Wait!  Are the Data Clean?

The first thing to notice, however, is that the individual cells of the 'Genre' column consist of long strings, such as `Psychedelic Rock, Art Rock, Pop/Rock`. Performing a groupby operation on these long strings will not reveal much, since all of the subgenre will be embedded in these long strings. So some data-cleaning is needed as a preliminary step. We need to *clean the data*, *split the lists*, and *regularize the terms* in order to make a useful network. So you might need to go back to Pandas Tutorial B and remind yourself of how to do this.

For purposes of this network demonstration, we can take care of these steps with the following code:

<Details>

<Summary> View Code for Initial Clean up and Tidy Functions <strong>THIS CODE DOESN'T WORK</strong></Summary>

```python
# make everything lowercase, remove leading/trailing spaces, and fill nas
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.lower().str.strip().fillna('')
# split the long strings into a list of strings in each cell
beatles_billboard['Genre'] = beatles_billboard['Genre'].str.split(',')
# explode the data
beatles_billboard_exploded = beatles_billboard.explode('Genre').reset_index(drop=True)
# and clean whitespace and odd characters again
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded

# clean individual problems in the exploded data with str.replace()
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('acid rock[', 'acid rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('pop/rock', 'pop rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('r&b', 'rhythm and blues')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('rock and roll', 'rock')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace('experimental music', 'experimental')
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("children's music", "children's")
beatles_billboard_exploded['Genre'] = beatles_billboard_exploded['Genre'].str.replace("stage&screen", "stage and screen")

```
</Details>

<br>

The result is a dataframe in which the "Genre" column contains just one label per row.  The song titles repeat, but this does not need to worry us:  Groupby will take care of the rest.

![alt text](images/nw_group_explode.png)


## Finding Pairs of Related Genres

So far we have **cleaned** up the data, and **exploded** the genre terms into manageable form. 

Now we need to find **every pair of genre terms that apply to a given song**, since these will form the **nodes** and **edges** of our genre network. 

Here is how to do it:

* **group** the tidy data by **song title**, and **return all of the genre labels as a list**. This might seem to have been already available to us after the `split(',')` operation above. But remember that we still had various issues with whitespaces, trailing characters, and variant spellings or terms! This will be a new dataframe.
* **from each list of genre labels create a new list of pairs of labels**.  These tuples will provide the basis of the nodes and edges. 
* **count** the occurences of each pair of labels, and return the results as a new dataframe:  pairs and counts.  This will be passed directly to networkX to populate the graph.

### 1: The Groupby Operation:

```python
# copy of our data, so we don't accidentally alter it
df = beatles_billboard_exploded

# select the columns to use
feature_to_groupby = 'Title' # <-- this is the original df column that will provide the basic control; could even be a list of columns
column_for_list_of_edges = 'Genre' # <-- this is the original df column that will contain the list of features that will become the nodes and edges

# Group by 'feature_to_groupby' and extract a 'column_for_list_of_edges'
grouped_feature_with_edges = df.groupby
```
From this we see that for each song title, we have a list of genre labels:

![alt text](images/new_nw_1.png)

### 2: Find the Combinations of Genre Labels for Each Group, and Count Them

For *each of these lists of titles*, we need to find all of the `pairs` of titles, which will serve as our network edges. This is easily done with a special Python library called `collections`, and within that the `combinations` method.

For "A Day in the Life", for instance (this is Index #1 in the dataframe), we find the following list of genre labels: `['psychedelic rock', 'art rock', 'pop rock']`

The `combinations` method will return a new list consisting of all the unique pairs of values in that list.  Each pair will be a tuple.  (Note:  three items in the list, we find the total combinations as `n(n-1)/2`.  five items will give us ten pairs since `(3*2)/2 = 3`).  

This is what this looks like for a single list of genre labels in one row:

```python
# make sure you have imported the relevant library, itertools
import itertools
# now a sample list and the resulting combinations
sample_list = ['psychedelic rock', 'art rock', 'pop rock']
pairs = list(combinations(sample_list, 2))
pairs

[('psychedelic rock', 'art rock'),
 ('psychedelic rock', 'pop rock'),
 ('art rock', 'pop rock')]
 ```

Running the `combinations` method over each row of the exploded dataframe, we in turn create a new dataframe with `all_pairs` of genres.  

```python
# make sure you have imported the relevant library, itertools
import itertools

# Generate all pairs edges for each group
all_pairs = []
for _, row in grouped_feature_with_edges.iterrows():
    pairs = list(combinations(row[column_for_list_of_edges], 2))
    all_pairs.append((row[feature_to_groupby], pairs))

# Create a new DataFrame with the results
edge_pair_name = column_for_list_of_edges + "_Pairs"
edge_pair_df = pd.DataFrame(all_pairs, columns=[feature_to_groupby, edge_pair_name])
# adjust for a threshold of genres per piece. should be > 0 
edge_pair_df_filtered = edge_pair_df[edge_pair_df[edge_pair_name].apply(len) > 0]

```


<Details>
<Summary>Image of Sample Output All Edges</Summary>


![alt text](images/new_nw_2.png)

</Details>

<br>

And this, in turn, we `explode` in order to create a dataframe of genre pairs for each title.  


```python
exploded_edge_pairs = edge_pair_df_filtered.explode(edge_pair_name)
```

<Details>
<Summary>Image of Sample Exploded Edges</Summary>


![alt text](images/new_nw_3.png)

</Details>

<br>


Finally, we will `count` the occurences of each edge pair, so that we can show a weighted network.


```python
# get the counts of each pair, which provides the basis of the weights
pair_counts = exploded_edge_pairs[edge_pair_name].value_counts()

# as a df, for clarity
pair_counts_df = pd.DataFrame(pair_counts).reset_index()
pair_counts_df.head()
```
<Details>
<Summary>Image of Sample Exploded Edges with Counts</Summary>

![alt text](images/new_nw_4.png)


</Details>

<br>




### 3: Make Network from the Edge Pairs

At last we are ready to build our network from the dataframe of edge pairs and their corresponding weights, which was our original goal! 

<Details>
<Summary>From List of Tuples to Weighted Edges and Nodes</Summary>


![alt text](<images/tuples to network.png>)

</Details>

<br>

<Details>
<Summary>Code to Create Network from Dataframe of Edge Tuples and Counts</Summary>


```python
# allow a filter for the number of times a given pair of genres occurs
# this works with the original series of pair counts, not the df

minimum_count_for_pair = 1

pair_counts_filtered = pair_counts[pair_counts >= 1]

# set graph options:
graph_height = 800
graph_width = 800
detect_louvain_communities = True
add_forceAtlas2Based_physics = True

# Create an empty NetworkX graph
G = nx.Graph()


# Add nodes and assign weights to edges
for pair, count in pair_counts_filtered.items():
    # Directly unpacking the tuple into node1 and node2
    node1, node2 = pair
    # Adding nodes if they don't exist already
    if node1 not in G.nodes:
        G.add_node(node1)
    if node2 not in G.nodes:
        G.add_node(node2)
    # Adding edge with weight
    G.add_edge(node1, node2, weight=count)

# Adjusting edge thickness based on weights
for edge in G.edges(data=True):
    edge[2]['width'] = edge[2]['weight']
    


# Adding Louvain Communities

if detect_louvain_communities == True:
    def add_communities(G):
        G = deepcopy(G)
        partition = community_louvain.best_partition(G)
        nx.set_node_attributes(G, partition, "group")
        return G
        
    G = add_communities(G)

# set display parameters
network_graph = Network(notebook=True,
                   width=graph_height,
                   height=graph_height,
                   bgcolor="black", 
                   font_color="white")

# Set the physics layout of the network

if add_forceAtlas2Based_physics == True:

    network_graph.set_options("""
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

network_graph.from_nx(G)
# # return the network
network_graph.show("network_graph.html")
```


</Details>

<br>


##### 3A. Basic Network

The simplest version of the NetworkX and Pyvis tools result in a rather dense (and thus difficult to interpret) network of genres:

![alt text](<images/nw no physics.png>)

##### 3B. Network with Updated Physics for Legibility

Adding some updated physics to the network spread things out so they are more legible, and includes the relative weights of the edges:

![alt text](<images/nw with physics.png>)

##### 3C. Network with Louvain Community Detection

Finally, we reveal 'communities' via color highlights, using the Louvain Community Detection Algorithm. Read more about this magic below!

![alt text](<images/nw with louvain.png>)


## The Complete Network Code

Here we assume that you have already cleaned and exploded your original dataframe as explained above.

You also need to know which column will serve as your `groupby` basis and which column will be used to build the `edge_pairs`.

There are also various settings that allow you to control the size and other features of the graph.


You will need to supply:

* a cleaned df
* feature to group by
* the column that will determine the edges
* option to select graph size, louvain, and advanced physics

#### Example A

df = beatles_spotify_binned

feature_to_groupby = 'danceability_q_binned' 

column_for_list_of_edges = 'song' 


#### Example B

df = beatles_billboard_exploded

feature_to_groupby = 'Title'

column_for_list_of_edges = 'Genre'





```python
# copy of our data, so we don't accidentally alter it


df = beatles_billboard_exploded

#  select the columns to use; these will be determined by your original df
feature_to_groupby = 'Title' # <-- this is the original df column that will provide the basic control; could even be a list of columns
column_for_list_of_edges = 'Genre' # <-- this is the original df column that will contain the list of features that will become the nodes and edges

# Group by 'feature_to_groupby' and extract a 'column_for_list_of_edges'
grouped_feature_with_edges = df.groupby(feature_to_groupby)[column_for_list_of_edges].unique().reset_index(name=column_for_list_of_edges)

# Generate all pairs edges for each group
all_pairs = []
for _, row in grouped_feature_with_edges.iterrows():
    pairs = list(combinations(row[column_for_list_of_edges], 2))
    all_pairs.append((row[feature_to_groupby], pairs))

# Create a new DataFrame with the results
edge_pair_name = column_for_list_of_edges + "_Pairs"
edge_pair_df = pd.DataFrame(all_pairs, columns=[feature_to_groupby, edge_pair_name])
# adjust for a threshold of genres per piece. should be > 0 
edge_pair_df_filtered = edge_pair_df[edge_pair_df[edge_pair_name].apply(len) > 0]

# explode the edge pair df
exploded_edge_pairs = edge_pair_df_filtered.explode(edge_pair_name)


# get the pair counts
pair_counts = exploded_edge_pairs[edge_pair_name].value_counts()


# allow a filter for the number of times a given pair of genres occurs
# this works with the original series of pair counts, not the df

minimum_count_for_pair = 1

pair_counts_filtered = pair_counts[pair_counts >= 1]

# set graph options:
graph_height = 800
graph_width = 800
detect_louvain_communities = True
add_forceAtlas2Based_physics = True

# Create an empty NetworkX graph
G = nx.Graph()


# Add nodes and assign weights to edges
for pair, count in pair_counts_filtered.items():
    # Directly unpacking the tuple into node1 and node2
    node1, node2 = pair
    # Adding nodes if they don't exist already
    if node1 not in G.nodes:
        G.add_node(node1)
    if node2 not in G.nodes:
        G.add_node(node2)
    # Adding edge with weight
    G.add_edge(node1, node2, weight=count)

# Adjusting edge thickness based on weights
for edge in G.edges(data=True):
    edge[2]['width'] = edge[2]['weight']
    


# Adding Louvain Communities

if detect_louvain_communities == True:
    def add_communities(G):
        G = deepcopy(G)
        partition = community_louvain.best_partition(G)
        nx.set_node_attributes(G, partition, "group")
        return G
        
    G = add_communities(G)

# set display parameters
network_graph = Network(notebook=True,
                   width=graph_height,
                   height=graph_height,
                   bgcolor="black", 
                   font_color="white")

# Set the physics layout of the network

if add_forceAtlas2Based_physics == True:

    network_graph.set_options("""
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

network_graph.from_nx(G)
# # return the network
network_graph.show("network_graph.html")
```

### 4: Interpreting Networks

Networks can *look* appealing, even mesmerizing.  But how do we interpret them?  One way is by exploring connections, and in turn thinking about the implications of things that are associated with each other (and things that are not).

Our Beatles Genre data are of course hardly objective:  they represent attributes made by others (the Belgrade team who first compiled the Billboard data?) about the objects in question.  But the genre tags associated with each other can in turn reveal something about their assumptions (and in turn ours).  Here are some 'communities' identified by our network.  Among the most creative aspects of the Beatles as a group was their capacity to 'mash up' genres of different kinds, or to cross boundaries in unexpected ways.  The community of tags in which pieces are *both psychedelic and vaudeville or music hall* is revealing, for it suggests that the old can be new, and even extreme, if treated in the right way:

![alt text](<images/nw vaudeville.png>)

On the other hand, we see a more obvious affinity among rock, the blues, and so-called 'progressive' rock, with it's influences from jazz, classical, and even avant-garde musics:


![alt text](<images/nw pro and blues.png>)




<!--- 
7/16/24>

The following are from 2022-23 and need work.  They are complex, and they don't yet use the Physics

On the other hand, the Louvain explanation is helpful!

--->
##  More Networks with Spotify Data</a>

In this part, we'll explore some ways of creating networks using Spotify's Artists and Songs based on Recommended and Related songs and artists.

Building onto these tools, we can create something more advanced – for example, **a diagram of user_1's playlists** (by iterating over *all_my_tracks*). We will scale the nodes (playlists) based on their size using Pyvis' **value** attribute of Nodes.

Here's how to do it (add this code to your Notebook)


```python
# Creating a Network with one center Node
playlists_network = net.Network(notebook=True, width=1000, height = 800)

playlists_network.add_node("user_1's Spotify", color="#fffff")

# As we want to record both playlist names and corresponding sizes, we need a Dictionary:
user_1_playlist_dictionary = {}
# replace "my_username" with the Spotify user ID of your choice
user_1s_playlists = pd.DataFrame(sp.user_playlists(my_username)["items"])

# Iterating over the playlists and recording Names and Sizes
for i in range(len(user_1s_playlists)):
    user_1_playlist_dictionary[user_1s_playlists.loc[i]["name"]] = user_1s_playlists["tracks"][i]["total"]

# Adding new Nodes and Edges based on the items in the Dictionary:
for item in user_1_playlist_dictionary:
    playlists_network.add_node(item, value=user_1_playlist_dictionary[item])
    playlists_network.add_edge("user_1's Spotify", item)

# Showing the Network Graph
playlists_network.show("playlists_diagram.html")
```

![Alt text](images/spot_25.png)
    

<br>

As expected, we can see the center node we added at first – which is now connected to 8 other nodes, which all correspond to user_1's playlists. These nodes are sized based on the playlists' sizes (number of tracks) and named based on the playlists' names. **This is a simple undirected network**.

----

##  <span style="color:olive">Complex Networks:  Related Artists </span> <a name="artist_networks"></a> 

Now, we'll get into slightly more complicated things.

Spotify API provides a way to **get related artists** given an Artist ID. According to Spotify, this method returns a collection of artists "similar to a given artist", and the **"similarity is based on analysis of the Spotify community's listening history"**.  Note that these connections are **social and collaborative**, and not based on the **audio feature** data explored above.

Learn more about Spotify's [Related Artists method](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-related-artists).

Reflecting this method, Spotipy conveniently has *spotipy_client.artist_related_artists*, which returns a collection of artists related to an artist. Making use of this method, one could think of a function that would go through a number of related artists (**limit**) and add graph Nodes and Edges corresponding to the newly discovered related artists. We will also **size nodes** based on popularity.

Here's what such a function could look like (add this to your Notebok):


```python
def add_related_artists(starting_artist_name, starting_artist_id, existing_graph, limit, spotipy_client, order_group=None):
    # get artists related to the current artist
    current_artist_related = pd.DataFrame(spotipy_client.artist_related_artists(starting_artist_id)["artists"])
    # loop through the related artists, add nodes and edges
    for i in range(limit):
        # check if node already exists
        if current_artist_related.loc[i]["name"] not in existing_graph.get_nodes():
            if order_group:
                existing_graph.add_node(current_artist_related.loc[i]["name"], value=int(current_artist_related.loc[i]["popularity"]), group=order_group)
            else:
                existing_graph.add_node(current_artist_related.loc[i]["name"], value=int(current_artist_related.loc[i]["popularity"]), group=(i + 1))
        # add edge
        existing_graph.add_edge(starting_artist_name, current_artist_related.loc[i]["name"])
```

    
#### Get Artist Albums

```python
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
artist_id = '7nwUJBm0HE4ZxD3f5cy5ok'

# pull all artists albums
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50})
d = r.json()

df = pd.DataFrame(d)
# df["items"][0]
```

#### Get Related Artists (for Multiple Generations)

In the cell below, we will make use of the function we just defined. Using this function and some basic information, we will **produce a Network Graph for two generations (circles) of artists related to The Beatles**. 

As noted, we will start with Beatles (Artist ID = "3WrFJ7ztbogyGnTHbHJFl2", Name = "The Beatles")


```python
## First, we need to record the information about The Beatles
center_artist_id = "3WrFJ7ztbogyGnTHbHJFl2"
center_artist_name = "The Beatles"
center_artist_popularity = 80

# # or, we need to record the information about Aretha
# center_artist_id = "6uRJnvQ3f8whVnmeoecv5Z"
# center_artist_name = "Berlin"
# center_artist_popularity = 100

# # or, we need to record the information about Aretha
# center_artist_id = "7nwUJBm0HE4ZxD3f5cy5ok"
# center_artist_name = "Aretha"
# center_artist_popularity = 100

# limit: how many related per generation are we interested in
limit = 5

center_artist_related = pd.DataFrame(sp.artist_related_artists(center_artist_id)["artists"]).loc[0:(limit-1)]

# setting up the Network
artist_network = net.Network(notebook=True, width=1000, height=800)
artist_network.add_node(center_artist_name, value=center_artist_popularity, color="#fffff", group=0)

# Getting the first circle of related artists:
add_related_artists(center_artist_name, center_artist_id, artist_network, limit, sp)

# artist_network.add_node("test")

# Showing the Network Graph
artist_network.show("artist_example.html")
```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/spot_26.png)

</Details>


<br>

In order to further complicate our lives, we can **add one more generation of related artists** (think friends of friends):


```python
# Running through the once-related artists
for i in range(limit):
    add_related_artists(center_artist_related.loc[i]["name"], center_artist_related.loc[i]["id"], artist_network, limit, sp, (i+1))

# Showing the Network Graph
artist_network.show("artist_example.html")


```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/spot_27.png)


</Details>

<br>


As you can see, the Network Graph above provides some very interesting information and prompts some very important thoughts. Think about: 
* Why are the nodes located the way they are located? 
* Who are the artists we've missed? 
* How are these people related?

<br>


##  <span style="color:olive"> Complex Networks:  A Network of Songs </span> <a name="song-network"></a>

Similarly to Related Artists, Spotify API has a way of **recommending songs** based on a "seed" of tracks. Acording to the API Documentation, "recommendations **are generated based on the available information for a given seed entity and matched against similar artists and tracks**".

You can read more about Spotify's Recommendations [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations).

This method is mirrored by Spotipy – specifically, in the *sp.recommendations* method. One could think of a function that would **get a generation of recommended songs and add them to a Network Graph** (scaled by popularity).

Add this to your Notebook:


```python
def add_related_songs(starting_song_name, starting_artist_name, starting_song_id, existing_graph, limit, spotipy_client, first_gen=True, order_group=None):
    current_song_related = pd.DataFrame(spotipy_client.recommendations(seed_tracks=[starting_song_id])["tracks"])
    for i in range(limit):
        if str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]) not in existing_graph.get_nodes():
            if order_group:
                existing_graph.add_node(str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]), value=int(current_song_related.loc[i]["popularity"]), group=order_group)
            else:
                existing_graph.add_node(str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]), value=int(current_song_related.loc[i]["popularity"]), group=(i+1))
        existing_graph.add_edge(str(starting_artist_name + ": " + starting_song_name), str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]))
    return current_song_related
```

In the cell below, we will make use of the function we just defined. Using this function and some basic information, we will **produce a Network Graph for two generations (circles) of recommended songs based on Ben E. King's Stand By Me**. 

As noted, we will start with Stand By Me (Song ID = "3SdTKo2uVsxFblQjpScoHy")


```python
# First, we need to record the information about Stand By Me
center_song = sp.track("3SdTKo2uVsxFblQjpScoHy")
# Or Mahler 1
# center_song = sp.track("7vZoMrrqsqfO96vortxxjn")

# Or Orlando di Lasso
# center_song = sp.track("4CAp8WXEotxJLE5A2c3Yup")

center_song_id = center_song["id"]
center_song_artist = center_song["artists"][0]["name"]
center_song_name = center_song["name"]
center_song_popularity = int(center_song["popularity"])

# limit: how many recommended songs per generation we are interested in
limit = 3

# Creating the Network graph and adding the center Node
song_network = net.Network(notebook=True, width=1000, height=800)
song_network.add_node(str(center_song_artist + ": " + center_song_name), value=center_song_popularity, color="#fffff", group=0)

# Getting the first circle of related artists:
recommended_songs = add_related_songs(center_song_name, center_song_artist, center_song_id, song_network, limit, sp)

# Showing the Network
song_network.show("song_network_short.html")

# Note that depending on your Jupyter Hub this network might not render directly in the Notebook.  Look for the named file in the folder where your Notebook is stored and open it there.
```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/spot_28.png)

</Details>

<br>

Similarly to Related Artists, we will further complicate our lives by **adding one more generation of recommended songs** (with no extra seed knowledge):


```python
# Getting the second generation of Recommended songs
for i in range(limit):
    add_related_songs(starting_song_name=recommended_songs.loc[i]["name"], 
                      starting_artist_name=recommended_songs.loc[i]["artists"][0]["name"], 
                      starting_song_id=recommended_songs.loc[i]["id"], 
                      existing_graph=song_network, 
                      limit=limit, 
                      spotipy_client=sp, 
                      first_gen=False, 
                      order_group=(i+1))
                      


# Showing the network
song_network.show("song_network.html")
```

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/spot_29.png)

</Details>

<br>

Interestingly, Spotify's recommendations for songs **change every time you run your code**. We encourage you to re-run  the previous two cells a few times! Just like the Related Artists graph, the Network Graph above provides some very interesting information and prompts some very important thoughts. Think about: 
* Why are the nodes located the way they are located? 
* Who are the artists we've missed? 
* How are these people related?

<br>

Finally, we can make one very slight tweak to our add_related_songs method. Previously, we only included one track as a seed track for running the GET Recommendations method. In the function below, we will define a new function that will essentially do the same thing as the one above, except it will **pass 5 random tracks (out of the tracks in the graph) as the recommendation seed** into the Recommendation function.


Add this to your Notebook:


```python
def add_related_songs_gen(starting_song_name, starting_artist_name, starting_song_id, existing_graph, limit, spotipy_client, first_gen=True, order_group=None):
    current_song_related = pd.DataFrame(sp.recommendations(seed_tracks=starting_song_id)["tracks"]).loc[0:(limit - 1)]
    for i in range(limit):
        if str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]) not in existing_graph.get_nodes():
            if order_group:
                existing_graph.add_node(str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]), value=int(current_song_related.loc[i]["popularity"]), group=order_group)
            else:
                existing_graph.add_node(str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]), value=int(current_song_related.loc[i]["popularity"]), group=(i+1))
        existing_graph.add_edge(str(starting_artist_name + ": " + starting_song_name), str(current_song_related.loc[i]["artists"][0]["name"] + ": " + current_song_related.loc[i]["name"]))
    return current_song_related
```

We will run this function for **two generations** for the same song (Stand By Me by Ben E. King):


```python
# Start the network
song_network = net.Network(notebook=False, width=1000, height=800)
song_network.add_node(str(center_song_artist + ": " + center_song_name), value=center_song_popularity, color="#fffff", group=0)

# First generation
recommended_songs = add_related_songs_gen(center_song_name, center_song_artist, [center_song_id], song_network, limit, sp)

# Second generation
for i in range(limit):
    add_related_songs_gen(recommended_songs.loc[i]["name"], recommended_songs.loc[i]["artists"][0]["name"], random.sample(list(recommended_songs["id"]), 3), song_network, limit, sp, False, (i+1))

# Show the network Graph
song_network.show("song_network.html")
```

Note that this graph looks a little different! What are **some of your observations**?  As a listener, do the recommendations make sense?

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/spot_30.png)

</Details>

<br>
----

##  <span style="color:olive">Louvain Community Detection:  The Ghost in the Machine </span> <a name="louvain"></a>


In the last part of this guide, we will briefly explore **Louvain Community Detection**. In short, this is a method that allows us to visually identify communities of discrete entities that share a common attribute. In simpler terms, it helps identify clusters or communities of related nodes.

You can learn more about the mathematics behind the Louvain algorithm [here](https://towardsdatascience.com/louvain-algorithm-93fde589f58c), explore its documentation [here](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html), read about its applications [here](https://towardsdatascience.com/louvains-algorithm-for-community-detection-in-python-95ff7f675306).


#### How the Louvain Algorithm Works

1. **Step 1: Initialization**
   - Each node is initially assigned to its own community.

2. **Step 2: Iterative Optimization**
   - The algorithm iteratively tries to improve the modularity of the network. Modularity is a measure of how well the nodes are grouped into communities.
   - It does this by attempting to move nodes between communities to increase the overall modularity.

3. **Step 3: Community Aggregation**
   - Once no more improvements can be made, the algorithm aggregates the communities found in the previous step and treats them as individual nodes in a new network.

4. **Step 4: Repeat**
   - The algorithm repeats steps 2 and 3 on the new network until a high modularity value is achieved.

### Why Modularity Matters
Modularity measures how well a network is divided into communities. Higher modularity values indicate better community structures. The Louvain algorithm aims to maximize the modularity by rearranging nodes into communities where they are more densely connected with each other and less connected with nodes in other communities.



### Example A:  Network of Artists Shared Among Five Related Spotify Playlists

In our first example, we will **identify Louvain communities of artists** within the playlists they belong to.  This approach is simply tracing common artists--it does not involve Spotify Audio Feature data.

<br>

At first, let's **pick 5 playlists** centered around a common theme. For example, let's choose "Rock". By searching on Spotify, we found and randomly picked these 5 playlists:
* [Rock Classics](https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U): "Rock legends & epic songs that continue to inspire generations", Spotify Playlist ID: "37i9dQZF1DWXRqgorJj26U"
* [Rock Mix](https://open.spotify.com/playlist/37i9dQZF1EQpj7X7UK8OOF): "Fleetwood Mac, Elton John, Steve Miller Band and more", Spotify Playlist ID: "37i9dQZF1EQpj7X7UK8OOF"
* [Classic Rock Drive](https://open.spotify.com/playlist/37i9dQZF1DXdOEFt9ZX0dh): "Classic rock to get your motor running. Cover: AC/DC", Spotify Playlist ID: "37i9dQZF1DXdOEFt9ZX0dh"
* [Rock Drive](https://open.spotify.com/playlist/37i9dQZF1DX7Ku6cgJPhh5): "Amp up your commute with these rock hits. Cover: Foo Fighters", Spotify Playlist ID: "37i9dQZF1DX7Ku6cgJPhh5"
* [Dad Rock](https://open.spotify.com/playlist/37i9dQZF1DX09NvEVpeM77): "Classic rock favorites. Cover: Bruce Springsteen", Spotify Playlist ID: "37i9dQZF1DX09NvEVpeM77"

<br>

Let's **put these playlists in a DataFrame**:

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
# Three Model Lists.  Two of them share only one.  Two of them share all except one.  
# What do we expect?
rock_playlists_dfs_list = []
PL_1 = '37i9dQZF1DWXRqgorJj26U'
PL_2 = '37i9dQZF1EQpj7X7UK8OOF'
PL_3 = '37i9dQZF1DXdOEFt9ZX0dh'
PL_4 = '37i9dQZF1DX7Ku6cgJPhh5'
PL_5 = '37i9dQZF1DX09NvEVpeM77'

rock_playlists_ids_list = [PL_1, PL_2, PL_3]

# # Create a list of playlists
# rock_playlists_dfs_list = []
# rock_playlists_ids_list = ["37i9dQZF1DWXRqgorJj26U",
#                           "37i9dQZF1EQpj7X7UK8OOF",
#                           "37i9dQZF1DXdOEFt9ZX0dh",
#                            "37i9dQZF1DX7Ku6cgJPhh5",
#                           "37i9dQZF1DX09NvEVpeM77"]

# Looping through the items and producing Audio Features DataFrames

for item in rock_playlists_ids_list:
  temp_playlist_df = pd.DataFrame(sp.playlist_items(item))
  temp_playlist_audio = spotify_tools.get_audio_features_df(temp_playlist_df, sp)
  temp_playlist_audio["playlist_name"] = sp.playlist(item)["name"]
  rock_playlists_dfs_list.append(temp_playlist_audio)
    
# Concatenating the Audio Features DataFrames
rock_playlists_df = pd.concat(rock_playlists_dfs_list)
rock_playlists_df

# Our new Rock Playlists DataFrame contains 400 tracks gathered across the 5 playlists. As we don't want to overwhelm our Network, we will **choose a random sample** of 100 tracks out of this DataFrame:

input_data_rock_df = rock_playlists_df.reset_index()
our_sample = input_data_rock_df.sample(100)
```

</Details>

<br>

Now, let's **define the Louvain Community Algorithm methods**.

**Create nodes** (courtesy of Daniel Russo Batterham and Richard Freedman).  See the code below, or just run this with the `rock_playlists_df`

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
# Creating an HTML node
def create_node_html(node: str, source_df: pd.DataFrame, node_col: str):
    rows = source_df.loc[source_df[node_col] == node].itertuples()
    html_lis = []
    for r in rows:
        html_lis.append(f"""<li>Artist: {r.artist}<br>
                                Playlist: {r.playlist_name}<br>"""
                       )
    html_ul = f"""<ul>{''.join(html_lis)}</ul>"""
    return html_ul
```

</Details>

<br>

**Add nodes from edge list** (courtesy of Daniel Russo Batterham and Richard Freedman):

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
# Adding nodes from an Edgelist
def add_nodes_from_edgelist(edge_list: list, 
                               source_df: pd.DataFrame, 
                               graph: nx.Graph,
                               node_col: str):
    graph = deepcopy(graph)
    node_list = pd.Series(edge_list).apply(pd.Series).stack().unique()
    for n in node_list:
        graph.add_node(n, title=create_node_html(n, source_df, node_col), spring_length=1000)
    return graph
```

</Details>
<br>

**Find Louvain Communities** (courtesy of Daniel Russo Batterham and Richard Freedman):

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
# Adding Louvain Communities
def add_communities(G):
    G = deepcopy(G)
    partition = community_louvain.best_partition(G)
    nx.set_node_attributes(G, partition, "group")
    return G
```
</Details>
<br>

**Produce a Network of pairs**, which we'll run the add_communities method on, marking the Louvain communities:

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
def choose_network(df, chosen_word, output_file_name, output_width=800):
    
    # creating unique pairs
    output_grouped = df.groupby(['tags'])[chosen_word].apply(list).reset_index()
    pairs = output_grouped[chosen_word].apply(lambda x: list(combinations(x, 2)))
    pairs2 = pairs.explode().dropna()
    unique_pairs = pairs.explode().dropna().unique()
    
    # creating a new Graph
    pyvis_graph = net.Network(notebook=True, width=output_width, height="1000", bgcolor="black", font_color="white")
    G = nx.Graph()
    # adding nodes
    try:
        G = add_nodes_from_edgelist(edge_list=unique_pairs, source_df=df, graph=G, node_col=chosen_word)
    except Exception as e:
        print(e)
    # add edges
    G.add_edges_from(unique_pairs)
    # find communities
    G = add_communities(G)
    pyvis_graph.from_nx(G)
    pyvis_graph.show(output_file_name)
```

</Details>
<br>

**Detect Louvain Communities** of artists within the playlists they belong to:

<Details>
<Summary>See the Code (and Copy to Your Notebook)</Summary>

```python
louvain_network = choose_network(input_data_rock_df.sample(50), 'artist', 'modified_rock.html')
louvain_network.show("modified_rock.html")
```

</Details>
<br>

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/louvain.png)


</Details>


### Example B:  Networks Using Audio Feature Data 

In our second example, we will **identify Louvain communities of using Spotify Audio Feature data**.  We do this in several steps:

**Create Categorical Bins from Scalar Audio Feature Data.**

Spotify Audio Feature data are of course scalars.  And so to find 'similar' tracks it is helpful to transform these as categorical data types (for instance:  `low, middle, high, very high` for `danceability`).  This is easily done with Pandas `cut` and `qcut` methods.  Here we use the latter, creating four bins, each with its own label:

<Details>
<Summary>Code to Use</Summary>

```python

# select the columns to categorize:
binned_cols = ['danceability',
 'energy',
 'key',
 'loudness',
 'speechiness',
 'liveness',
 'valence',
 'tempo',
 'duration_ms']

# copy the original dataframe, define labels and create new binned/categorized columns based on the originals
our_data_q_binned = our_data.copy()
labels = ['l', 'm', 'h', 's']
bin_count = len(labels)
for column in binned_cols:
    our_data_q_binned[f"{column}_q_binned"] = pd.qcut(our_data_q_binned[column], 
                                                 q=bin_count,
                                                labels = labels,
                                                 duplicates='drop')
```
</Details>

<br>

**Create 'Tags' that Combine Categories as Distinctive Types**.  Using python `join` we next link up the various categorical labels into distinctive 'tags' (like `L_L_M_H_L` which represent the values for several different Audio Features at once.

<Details>
<Summary>Code to Use</Summary>

```python
# select some useful set of columns to combine
q_bin_tag_cols = ['danceability_q_binned',
 'energy_q_binned',
 'speechiness_q_binned',
 'liveness_q_binned',
 'valence_q_binned']

# join them into a new column:

our_data_q_binned['tags'] = our_data_q_binned[q_bin_tag_cols].apply(lambda row : "_".join(row), axis='columns')
```

</Details>

<br>

**Create the Louvain Communities Networks from the Binned and Tagged Audio Feature Data**.  Below we detail the functions used to create the Louvain Communnities Network:


<Details>
<Summary>Code to use in Notebooks</Summary>

```python
# Adding nodes from an Edgelist
def add_nodes_from_edgelist(edge_list: list, 
                               source_df: pd.DataFrame, 
                               graph: nx.Graph,
                               node_col: str):
    graph = deepcopy(graph)
    node_list = pd.Series(edge_list).apply(pd.Series).stack().unique()
    for n in node_list:
        graph.add_node(n, spring_length=1000)
    return graph
# Adding Louvain Communities
def add_communities(G):
    G = deepcopy(G)
    partition = community_louvain.best_partition(G)
    nx.set_node_attributes(G, partition, "group")
    return G

def choose_network(df, chosen_word, output_file_name, output_width=800):
    
    # creating unique pairs
    output_grouped = df.groupby(['tags'])[chosen_word].apply(list).reset_index()
    pairs = output_grouped[chosen_word].apply(lambda x: list(combinations(x, 2)))
    pairs2 = pairs.explode().dropna()
    unique_pairs = pairs.explode().dropna().unique()
    
    # creating a new Graph
    pyvis_graph = net.Network(notebook=True, width=output_width, height="1000", bgcolor="black", font_color="white")
    G = nx.Graph()
    # adding nodes
    try:
        G = add_nodes_from_edgelist(edge_list=unique_pairs, source_df=df, graph=G, node_col=chosen_word)
    except Exception as e:
        print(e)
    # add edges
    G.add_edges_from(unique_pairs)
    # find communities
    G = add_communities(G)
    pyvis_graph.from_nx(G)
    pyvis_graph.show(output_file_name)

```

</Details>

</br>

**Create the Network**.  With all the code above in place, create the network:

```python
louvain_network = choose_network(our_data_q_binned, 'artist_name', 'artist_net.html')
```

The Result Tells us How Tracks (or Artists, or Playlists) are connected according to Audio Features:


![Alt text](images/louvain_audio.png)


#### Background on the Louvain Network is Created: How the Edges and Nodes are Formed: The "Grouped" Playlists


```python
output_grouped = input_data_rock_df.groupby(['playlist_name'])['artist'].apply(set).reset_index()
pairs = output_grouped['artist'].apply(lambda x: list(combinations(x, 2)))
pairs2 = pairs.explode().dropna()
unique_pairs = pairs.explode().dropna().unique()

```

#### Here is the `output_grouped`:

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/louvain_group.png)

</Details>

#### And the `Pairs` in each List:

<Details>
<Summary>Image of Sample Output</Summary>

![Alt text](images/louvain_pairs.png)

</Details>

Pairs are produced via combinations of all items in a set:

list(combinations(["paul", "john", 'george'], 2))
```
    [('paul', 'john'), ('paul', 'george'), ('john', 'george')]

```
Note the same thing as permutations (which considers all orderings)

from itertools import permutations
list(permutations(["paul", "john", 'george'], 3))
```
    [('paul', 'john', 'george'),
     ('paul', 'george', 'john'),
     ('john', 'paul', 'george'),
     ('john', 'george', 'paul'),
     ('george', 'paul', 'john'),
     ('george', 'john', 'paul')]

```
Each item in series is a list of tuples. the tuples will be the edges!

```

    0    [(Jimi Hendrix, Ben E. King), (Jimi Hendrix, A...
    1    [(Jimi Hendrix, Ben E. King), (Jimi Hendrix, A...
    2    [(Etta James, Patsy Cline), (Etta James, The B...
    Name: artist, dtype: object

```

Here we un-nest all the lists with `explode`.  Now the `len(pairs)` is 856!


```
pairs.explode().apply(sorted)
    0           [Ben E. King, Jimi Hendrix]
    0       [Aretha Franklin, Jimi Hendrix]
    0          [Howlin' Wolf, Jimi Hendrix]
    0       [Jimi Hendrix, The Temptations]
    0             [Jimi Hendrix, Sam Cooke]
                        ...                
    2       [Janis Joplin, Louis Armstrong]
    2         [Frank Sinatra, Janis Joplin]
    2    [Ella Fitzgerald, Louis Armstrong]
    2      [Ella Fitzgerald, Frank Sinatra]
    2      [Frank Sinatra, Louis Armstrong]
    Name: artist, Length: 135, dtype: object

```

There are nevertheless duplicate edges!  We could keep them for figuring weights!

### The Ghost In the Machine:

The key thing is that **Louvain does NOT know about the lists**!  It creates the commmunities **only on the basis of edges**!


```

# pairs2 = pairs.explode().dropna()

# do not need drop na!

# Note that the original lists are NOT here!

# could have other attributes added to data structure--weights, for instance!
unique_pairs = pairs.explode().unique()
unique_pairs
```
    array([('Jimi Hendrix', 'Ben E. King'),
           ('Jimi Hendrix', 'Aretha Franklin'),
           ('Jimi Hendrix', "Howlin' Wolf"),
           ('Jimi Hendrix', 'The Temptations'), ('Jimi Hendrix', 'Sam Cooke'),
           ('Jimi Hendrix', 'Donovan'),
           ('Jimi Hendrix', 'Jefferson Airplane'),
           ('Jimi Hendrix', 'Leonard Cohen'),
           ('Jimi Hendrix', 'Simon & Garfunkel'),
           ('Ben E. King', 'Aretha Franklin'),
           ('Ben E. King', "Howlin' Wolf"),
           ('Ben E. King', 'The Temptations'), ('Ben E. King', 'Sam Cooke'),
           ('Ben E. King', 'Donovan'), ('Ben E. King', 'Jefferson Airplane'),
           ('Ben E. King', 'Leonard Cohen'),
           ('Ben E. King', 'Simon & Garfunkel')])
          

### Adding Weighted Edges

We can count Tuples, which are the edges, so this would help us make a dict of value counts, and these could serve as the edge weights in the graph.


```
pairs.explode().value_counts()
```

    (Jimi Hendrix, Aretha Franklin)                      2
    (Aretha Franklin, The Temptations)                   2
    (Aretha Franklin, Simon & Garfunkel)                 2
    (Donovan, Leonard Cohen)                             2
    (Howlin' Wolf, Simon & Garfunkel)                    2
                                                        ..
    (Louis Armstrong, Frank Sinatra)                     1
    (Smokey Robinson & The Miracles, Louis Armstrong)    1
    (Etta James, Smokey Robinson & The Miracles)         1
    (Otis Redding, Howlin' Wolf)                         1
    (Patsy Cline, Ella Fitzgerald)                       1
    Name: artist, Length: 99, dtype: int64


In the Network Graph above, you can see the 3 **communities** of artists that are detected based on what playlist they belong to. Note: *we didn't pass the playlist information into the Network*!

\