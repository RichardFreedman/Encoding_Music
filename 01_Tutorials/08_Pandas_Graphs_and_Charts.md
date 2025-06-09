| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | **Graphs and Charts** | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

# Charts and Plots with Plotly Express

Our main resource is the [Plotly Express](https://plotly.com/python/plotly-express) library, which allows for interactive visualizations and more complex/powerful graphs with less code. . The Plotly Express documentation details the very wide range of bar charts, histograms, scatter plots, heat maps, polar (radar) figures you can create, and various ways of adding captions, legends, colors, etc.

![Alt text](images/plotlyexp.png)

|     | Contents of this Tutorial               | 
|-----|-----------------------------------------|
| 1.  | [**Bar Charts**](#bar-charts) |
| 2.  | [**Histograms**](#histograms) |
| 3.  | [**Scatter Plots**](#scatter-plots) |
| 4.  | [**Radar or Spider Plots**](#radar-or-spider-plots) |
| 5.  | [**Correlation Plots and Heatmaps**](#correlation-plots-and-heatmaps) |
| 6.  | [**Correlation Does Not Equal Causation**](#correlation-does-not-equal-causation) |
| 7.  | [**Adjusting Chart Size**](#adjusting-size-of-the-image) |
| 8.  | [**Pick Custom Color Scheme**](#pick-custom-color-scheme) |
| 9.  | [**Adjusting Axes**](#axis-scaling-linear-or-logarithmic) |
| 10. | [**Adding a Title**](#adding-a-title) |
| 11. | [**Labels and Legends**](#labels-and-legends) |
| 12. | [**X and Y Axis Tickmarks**](#x-and-y-axis-tickmarks) |
| 13. | [**Hover Data**](#hover-to-show-data-points) |

---

The first step is always to import the relevant library. 


```python
# Import libraries
import pandas as pd
import plotly.express as px
```

From here you will normally:

- Define a figure by passing a dataframe to a method (such as `fig = px.histogram(df_hist(df)`)
- Specify special labels, formatting, or other features
- Show the figure with `fig.show()`, or specify a file name if you would prefer to save it.

## Bar Charts

Bar charts are used to display categorical data. They consist of vertical or horizontal bars that represent different categories and their corresponding values. Bar charts are excellent for comparing data across different categories.  Learn more at [Plotly Express](https://plotly.com/python/bar-charts/)

Here's an example of a bar chart showing mean values for selected Spotify features, by album:

<details><summary>Bar Chart Code</summary>

```python
# Group data by year and album, calculating the mean for selected audio features
grouped_data = beatles_spotify.groupby(['year', "album"])[['danceability', 'energy', 'acousticness']].mean().copy()
grouped_data = grouped_data.reset_index()

<details><summary>Bar Chart Code</summary>

fig = px.bar(grouped_data,
             x='album',
             y=['danceability', 'energy', 'acousticness'], # If you wanted a simpler bar chart, you could use a single feature
             labels={'danceability': 'Danceability', 'energy': 'Energy', 'acousticness': 'Acousticness'},
             title='Figure 1: Compararive Beatles Album Scores for Selected Audio Features')

fig.update_layout(barmode='group') # Set bar mode to group for side-by-side comparison, rather than stacked

# Show the figure
fig.show()
```

</details>

<br>
    
![png](images/bar_chart.png)
    
<br>


## Histograms
Histograms are used to display the distribution of numerical data. They consist of a series of adjacent rectangles (bins) that represent the frequency or proportion of data falling within specific intervals. Histograms help us understand the shape and spread of data.  Learn more at [Plotly Express](https://plotly.com/python/histograms/)

Let's use one to see how energetic Beatles songs tend to be!

<details><summary>Histogram Code</summary>

```python
 # Create histogram of song energy
fig = px.histogram(
    beatles_spotify,
    x='energy',
    nbins=20, ## Number of bins in the histogram
    title='Distribution of Energy in Beatles Songs',
    labels={'energy': 'Energy (0 = calm, 1 = intense)'},
)

fig.show()
```
</details>

![png](images/histogram_example.png)

<br>

## Scatter Plots
Scatter plots are used to display the relationship between two numerical variables. Each point on the plot represents the values of the variables. Scatter plots are useful for identifying patterns, trends, and outliers in the data.  Learn more at [Plotly Express](https://plotly.com/python/line-and-scatter/)

Here's an example of a scatter plot showing the relationship between energy and danceability. You may notice that the graph is a little hard to read, since it is stretched out sideways. We'll change this later, when we learn how to customize graphs and charts.

<details><summary>Scatter Plot Code</summary>

```python
fig = px.scatter(
    beatles_spotify,
    x='danceability',
    y='energy',
    color='album',
    title='Scatter Plot: Danceability vs Energy in Beatles Songs',
    labels={'danceability': 'Danceability (0 = low, 1 = high)', 'energy': 'Energy (0 = calm, 1 = intense)'},
)

fig.show()

```

</details>

![png](images/scatter_example1.png)

<br>

### Scatter Plot with Variable Marker Size

Here we combine several data features to make a more interesting kind of Scatter Plot, showing the changing representation of various places over time.  The examples draw from RILM Abstracts, the leading database of writings about music, all over the world.  In this case we searched for the terms "travel explorations", "explorers and travelers", and "travel writings" in the RILM Database.  We also restricted our results to only those subject entries that concerned "places" (the "G" category in the RILM Term taxonomy). This resulted in the following dataframe:


![alt text](images/rilm_g_df.png)

<br>

This was in turn passed to the our scatterplot function. The occurences of the place names (the Y axis) are plotted over time (X axis).  The size of the marker reflects the relative number of occurences of that term in that year (the minimum is set with the 'term_threshold' argument).  Terms that occur in the work of the same author are given the same color (we can show or hide these with the 'legend' argument).  The title of the image is set with the 'title' argument.  We can also set the heighth and width of the image with two other variables




```python
final_results = final_results
term_threshold = 5
legend = False
title = 'Travelogue Places'
scatter_plot(final_results, term_threshold=term_threshold, legend=legend, title=title)
```

With the following result:

![alt text](images/rilm_g_scatter.png)

<br>

Here is the code to do it:

<Details>

<Summary>Code for ScatterPlot with Variable Markers</Summary>


```python
# scatter plot shows terms over time
def scatter_plot(final_results, term_threshold=5, legend=True, height=600, width=800, title=None):
    # Filter out terms appearing less frequently than term_threshold
    filtered_df = final_results.groupby('term').filter(lambda x: len(x) > term_threshold)
    
    # Calculate the size of markers based on term occurrence per year
    value_counts = filtered_df.groupby(['term', 'year']).size().reset_index(name='marker_size')
    
    # Merge filtered_df with value_counts to ensure marker_size is correctly aligned
    filtered_df = pd.merge(filtered_df, value_counts, on=['term', 'year'], how='left')
    
    # Create scatter plot
    fig_scatter = px.scatter(filtered_df,
                             x='year', y='term',
                             hover_data=['author'],
                             color='author',
                             labels={'term': "Term", "author": "Author", "year": "Publication Year"},
                             size='marker_size',
                             height=height,
                             width=width,
                             title=title)
    
    # Customize layout
    fig_scatter.update_layout(height=800)
    fig_scatter.update_layout(showlegend=legend)
    fig_scatter.update_yaxes(categoryorder='category descending')
    
    # Show plot
    fig_scatter.show()
```

</Details>



## Radar or Spider Plots

Radar (or Polar) plots are a useful way to represent multiple variables at once, putting each of several variables around a central point:  the distance from the center indicates the strength of that feature.  There are many types of polar (radar) plots available in Plotly Express.  Here we use the `line_polar` plot.  Read more about the various features via [Plotly Express](https://plotly.com/python/radar-chart/).  

It is helpful in this instance to use the Pandas `melt` method to transform our 'wide' data (with multiple columns for the individual audio features) into 'long' form data (with each feature represented as an individual row: 


```python
pd.melt(sample, id_vars=['track_title'], value_vars=feature_list)
```

![Alt text](images/melt_df.png)

The [Plotly Express](https://plotly.com/python/polar-chart/#polar-chart-with-plotly-express) `line_polar` method in turn can easily read these long-form data to produce the feature-based plots. Here we define a function that takes in the original dataframe of audio features, a list of feature columns to plot, and a name for the final chart.  

<Details>
<Summary>Sample Radar Plot Code</Summary>

```python
# first declare feature list:
# feature_list = ["danceability", "energy", "speechiness", "liveness", "instrumentalness", "acousticness", "valence", "danceability"]
# note that you will need to make sure all these features are in your dataset!

def audio_feature_radar(audio_feature_data, feature_list, chart_title):
    melted_data = pd.melt(audio_feature_data, id_vars=['title'], value_vars=feature_list)
    closed_data = melted_data.copy()
    closed_data.loc[len(closed_data)] = closed_data.iloc[0]
    closed_data = closed_data.sort_values(['title', 'variable'])
    fig = px.line_polar(closed_data, 
                        r='value', 
                        theta='variable', 
                        color='title', 
                        labels={'title': "Track Title"},
                        line_close=True)  # Add this line
    
    fig.update_layout(title=chart_title)
    
    return fig  
```
</Details>

<br>

Typical usage:

```python
feature_list = ["danceability", "energy", "speechiness", "liveness", "instrumentalness", "acousticness", "valence", "danceability"]
spotify_tools.audio_feature_radar(audio_feature_data, feature_list, "My Radar Plot")
```


<br>


![Alt text](images/radar_px.png)


<br>


## Correlation Plots and Heatmaps

Correlation plots are used to visualize the strength and direction of the relationship between two numerical variables. They provide a numerical measure called the correlation coefficient, which ranges from -1 to 1. A value close to -1 indicates a strong negative correlation, a value close to 1 indicates a strong positive correlation, and a value close to 0 indicates no or weak correlation.

One way to do this is via the `scatter_matrix` function in Plotly Express, which produces an individual scatterplot of all pairs of values in each pair of variables in your data.  Here is an example using audio feature data from Spotify.   Learn more at [Plotly Express](https://plotly.com/python/splom/)

Note that to show trend lines as noted above, you would need to produce an individual scatterplot for each pair of variables.


<Details>
<Summary> Sample Correlation Plot Code </Summary>

```python
import pandas as pd
import plotly.express as px

audio_features = {
    'danceability': [0.227, 0.832, 0.689, 0.654, 0.442, 0.351, 0.576, 0.352, 0.607, 0.664],
    'energy': [0.431, 0.346, 0.676, 0.285, 0.527, 0.903, 0.759, 0.424, 0.411, 0.283],
    'acousticness': [0.0432, 0.036, 0.288, 0.0375, 0.0314, 0.0681, 0.0599, 0.0394, 0.0414, 0.0498],
    'instrumentalness': [0.575, 0.688, 0.865, 0.148, 0.453, 0.354, 0.501, 0.141, 0.412, 0.558],
    'speechiness': [0.126, 0.0945, 0.0481, 0.105, 0.297, 0.252, 0.121, 0.0664, 0.103, 0.345]
}
audio_feature_df = pd.DataFrame(audio_features)

# create matrix (and ignore non-numerical columns if they exist)
correlation_matrix = audio_feature_df.corr(numeric_only=True)

# fig = px.scatter_matrix(correlation_matrix)
fig = px.scatter_matrix(audio_feature_df, dimensions=audio_feature_df.columns)

# fig.update_yaxes(tickangle=90)
fig.update_layout(title=f'Audio Feature Correlation: {correlation:.2f}')
fig.show()

```

</Details>

<br>

![Alt text](images/corr_matrix_chart.png)



Another way to get a good sense of the high-level correlations among variables is by first making a correlation matrix with Pandas (that is:  `correlation_matrix = data_to_correlate.corr()`) and then passing that result to the Plotly Express `imshow()` method, as seen below.  Learn more at [Plotly Express](https://plotly.com/python/heatmaps/)


<Details>
<Summary> Sample Code to Show Correlation Matrix as Plotly Heatmap </Summary>

```python
import pandas as pd
import numpy as np
import plotly.express as px

data = {
    'danceability': [0.227, 0.832, 0.689, 0.654, 0.442, 0.351, 0.576, 0.352, 0.607, 0.664],
    'energy': [0.431, 0.346, 0.676, 0.285, 0.527, 0.903, 0.759, 0.424, 0.411, 0.283],
    'acousticness': [0.0432, 0.036, 0.288, 0.0375, 0.0314, 0.0681, 0.0599, 0.0394, 0.0414, 0.0498],
    'instrumentalness': [0.575, 0.688, 0.865, 0.148, 0.453, 0.354, 0.501, 0.141, 0.412, 0.558],
    'speechiness': [0.126, 0.0945, 0.0481, 0.105, 0.297, 0.252, 0.121, 0.0664, 0.103, 0.345]
}
data_to_correlate = pd.DataFrame(data)

correlation_matrix = data_to_correlate.corr()

fig = px.imshow(correlation_matrix)

fig.update_layout(title=f'Correlation: {correlation:.2f}')
fig.show()

```

</Details>

<br>

![Alt text](images/corrheatmap.png)


### Correlation Does Not Equal Causation
It's crucial to understand that correlation does not imply causation. Just because two variables are correlated does not mean that one variable causes the other. Correlation measures the statistical relationship between variables but cannot determine cause and effect.

Always exercise caution when interpreting correlations and avoid making causal claims based solely on correlation. Other factors, such as confounding variables, might be influencing the observed relationship.

Remember, correlation is not causation!

For example: 
![Alt text](images/Correlation%20not%20Causation%20Example.png)
Image Source: [Spurious Correlations by Tyler Vigen](https://www.tylervigen.com/spurious-correlations)

Although these two are strongly correlated, married couples that eat more margarine are not guaranteed to get divorced.

## Adjusting the Size, Title, Color, and Labels in Plotly Express Charts

In Plotly Express there are various ways to change the size of your final image, provide a title, adjust the scale of the X and Y axes, and provide special labels for the items noted each axis.  It's also possibe to provide additional data in 'pop-up' lists that appear when the user hovers over individual points on the chart.

The Plotly Express documentation explains the main options.  Here we summarize a few of the most important.



### Adjusting Size of the Image

Remember the scatterplot that was hard to read because of the layout size? Here, we are going to try to fix it by setting the x and y dimensions to values that makes sense, prevent stretching of the axes. Generally, 800 x 600 is a good place to start.

Adjust the size by adding `fig.update_layout(width=x, height=y)` on the penultimate line of your chart code (immediately before `fig.show()`.  The values for width and height are expressed in pixels. Of course, remember to replace x and y with actual values! Learn more at [Plotly Express](https://plotly.com/python/setting-graph-size/).

<details><summary>Code for altering size</summary>

```python
# Create the original scatter plot of danceability vs energy
fig = px.scatter(
    beatles_spotify,
    x='danceability',
    y='energy',
    color='album',
    title='Scatter Plot: Danceability vs Energy in Beatles Songs',
    labels={'danceability': 'Danceability (0 = low, 1 = high)', 'energy': 'Energy (0 = calm, 1 = intense)'},
)

# Adjust size
fig.update_layout(
    width=800,
    height=600,
)

# Show the figure
fig.show()
```

</details>

![png](images/size_example.png)

<br>

#### Adding a trend line

Now that we can read our plot a little better, lets add a basic trend line with `trendline="ols"`. It's worth noting that if you don't remove `color = 'album'`, it will create a trend line for each album - a jumbled mess. Also, see how we adjusted the size within the initial code.

<details><summary>Trend line code</summary>

```python
# Create the scatter plot of danceability vs energy
fig = px.scatter(
    beatles_spotify,
    x='danceability',
    y='energy',
    trendline="ols", # Adding a trendline for better analysis
    title='Scatter Plot: Danceability vs Energy in Beatles Songs',
    labels={'danceability': 'Danceability (0 = low, 1 = high)', 'energy': 'Energy (0 = calm, 1 = intense)'},
    width=800,
    height=700,
)

fig.show()
```

</details>

![png](images/trend_line.png)


### Pick Custom Color Scheme

You can select an overall color palette from among several options.  Here you need to add `color_discrete_sequence=px.colors.qualitative.Pastel` when you create the chart.  Learn more at [Plotly Express](https://plotly.com/python/discrete-color/)


<details><summary>Changing the color scheme</summary>

```python
# we also 'filter' the results to eliminate songs instances of just one song in the matching Year/Songwriter/Genre category

# First, create a 'song_count' column (since it doesn't exist in the DataFrame)
beatles_billboard['song_count'] = 1

author_counts = beatles_billboard.groupby(['Year', 'Songwriter', 'Genre'])['song_count'].sum().reset_index()

# filter out 'unique' genres (or focus on them!)
author_counts = author_counts[author_counts['song_count'] >= 2]

# Create the scatter plot
fig = px.scatter(
    author_counts,
    x='Year',
    y='Songwriter',
    size='song_count',
    color='Genre',
    hover_data=['song_count'],
    labels={
        'Year': 'Year',
        'Songwriter': 'Songwriter',
        'song_count': 'Number of Songs',
        'Genre': 'Genre'
    },
    title="Number of Songs by Songwriter Over Time",
    color_discrete_sequence = px.colors.qualitative.Pastel # Change the color scheme to a pastel palette
)

# Customize the plot
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Songwriter",
    showlegend=True,
    width=1200,  # Set width to 800px
    height=800,  # Set height to 800px
)

# Show the plot
fig.show()
```

</details>

![png](images/color_scheme.png)

<br>


### Axis Scaling:  Linear or Logarithmic?

Normally numerical values are shown on a linear scale.  But it's possible to use logarithmic scales, too.  To use a logarithmic scale on the y axis, for instance, pass the following argument to the function: `log_y=True`.  Learn more at [Plotly Express](https://plotly.com/python/log-plot/)

<Details>
<Summary> Sample Code to Adjust Axis Scaling </Summary>

```python
# This is a generic example, since we don't have anything logarithmic in our datasets.

fig = px.scatter(x=[1, 2, 3], y=[10, 100, 1000],
                log_y=True)
# Show the plot
fig.show()
```
![Alt text](images/log.png)

</Details>

<br>




### Adding Titles

To give your chart or graph an overall title, include `fig.update_layout(title_text="My Chart's Title")`. You can also customize your x and y-axis titles. Learn more via the [Plotly Express documentation](https://plotly.com/python/figure-labels/).


<details><summary>Add Titles</summary>

```python
 # Create histogram of song energy
fig = px.histogram(
    beatles_spotify,
    x='energy',
    nbins=5,
    labels={'energy': 'Energy (0 = calm, 1 = intense)'},
    template='plotly_white'
)

fig.update_layout(
    title_text = 'New Title: Distribution of Energy in Beatles Songs', # Changes the text that is displayed at the top of the plot
    xaxis_title = 'Energy (0 = calm, 1 = intense)', # Changes the x-axis title
    yaxis_title = 'Count', # Changes the y-axis title
    width=800,  # Set width to 800px
    height=600,  # Set height to 600px
)

fig.show()
```

</details>

![png](images/titles.png)

<br>

### Labels and Legends 

You can label data so that each point or category is identified with a particular color, which is then explained in a legend at the side of the chart. Learn more via the [Plotly Express documentation](https://plotly.com/python/figure-labels/).


<Details>
<Summary> Sample Code to Add Legend and Data Labels </Summary>

```python
import pandas as pd
import plotly.express as px
fig = px.scatter(data_df,
                x='energy', y = 'loudness',
                color = 'artist_name')

fig.show()
```
</Details>

<br>


![Alt text](images/legend.png)



### X and Y Axis Tickmarks

The content of the x and y axes are termined via variables passed in when you create your plot.  But the orientation, size and other graphical aspects of the scales themselves are determined via 'tickmark' adjustments.  One useful technique when dealing with song titles from Spotify information is to angle the X-axis tickmarks by updating the figure with `fig.update_xaxes(tickangle=45)
`. You can easily adjust many other aspects of the tickmarks and labelling style. See more at [Plotly Express](https://plotly.com/python/axes/)


<Details>
<Summary> Sample Code to Adjust Tickmark Angle </Summary>

```python
import pandas as pd
import plotly.express as px

# create figure using selected columns from the dataframe
fig = px.scatter(sample_df,
                 x="track_title", y='tempo')

# update layout of title labels for the x axis
fig.update_xaxes(tickangle=45)

# sort the titles alphabetically
fig.update_xaxes(categoryorder='category ascending')

fig.show()
```
</Details>

<br>


![Alt text](images/plotly_tick_angle.png)


### Hover to Show Data Points

Include a list of `hover_data` columns when you create the Plotly Express figure.  Learn more via the [Plotly Express documentation](https://plotly.com/python/hover-text-and-formatting/), and see the example below.


<Details>
<Summary> Sample Code to Add Hover Data </Summary>

```python
import pandas as pd
import plotly.express as px
fig = px.scatter(data_df,
                x='energy', y = 'loudness',
                hover_data = ['artist_name', 'track_title', 'track_id'])

fig.show()
```
</Details>
<br>

![Alt text](images/hover.png)


| [Pandas Basics][pandas-basics] | [Clean Data][pandas-clean] | [Tidy Data][pandas-tidy] | [Filtering, Finding, and Grouping][pandas-filter-find-group] | **Graphs and Charts** | [Networks][pandas-networks] |
|--------|--------|--------|--------|-------|-------|

[pandas-basics]: 04_Pandas_Basics.md
[pandas-clean]: 05_Pandas_Clean_Data.md
[pandas-tidy]: 06_Pandas_Tidy_Data.md
[pandas-filter-find-group]: 07_Pandas_Filter_Find_Group.md
[pandas-networks]: 09_Pandas_Networks.md
