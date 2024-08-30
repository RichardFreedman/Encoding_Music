____________________
# Music 255: Beautiful Soup and Billboard

A Notebook for scraping Billboard Chart Data.


**XML** stands for **eXtensible Markup Language**, and mainly serves to transport and store data. At its core, XML was designed to be **both machine- and human-readable**. 

XML is used widely on the web--**HTML** files are a kind of XML, in this case used for structured graphical representation of content. Read more about [**XML**](https://www.w3schools.com/xml/xml_syntax.asp).

**Beautiful Soup** is a Python library that allows us to interact with XML files--finding elements (the 'tags') and their attributes. Documentation: [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [here](https://tedboy.github.io/bs4_doc/index.html).

**Beautiful Soup** can also be a good way to harvest information from structured webpages. In this tutorial we will explore the possibilities.

------

|    | Contents of this Tutorial               | 
|----|-----------------------------------------|
| 1. | [**Setup: Importing Python Libraries**](#setup-importing-python-libraries) |
| 2. | [**All Beautiful Soup Methods**](#all-beautiful-soup-methods) |
| 3. | [**Working with Billboard Data:  One Artist**](#working-with-billboard-data--one-artist) |
| 4. | [**Scraping Tabular Data**](#scraping-tabular-data) |
| 5. | [**One Artist vs Top 100 Lists**](#one-artist-vs-top-100-lists) |


## Setup: Importing Python Libraries

```python
import os
from bs4 import BeautifulSoup as bs
import optparse
import sys
from pathlib import Path
import requests
import pandas as pd
import re
from collections import Counter
import glob

```

## All Beautiful Soup Methods

A list of all Beautiful Soup methods.  The most important for our work will be those that "find" elements and that 'get' the strings associated with various attributes and tags.


```python
dir(bs)
```

<Details>

<Summary>Read the List of Soup Methods</Summary>


    ['ASCII_SPACES',
     'DEFAULT_BUILDER_FEATURES',
     'DEFAULT_INTERESTING_STRING_TYPES',
     'NO_PARSER_SPECIFIED_WARNING',
     'ROOT_TAG_NAME',
     '__bool__',
     '__call__',
     '__class__',
     '__contains__',
     '__copy__',
     '__delattr__',
     '__delitem__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattr__',
     '__getattribute__',
     '__getitem__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__unicode__',
     '__weakref__',
     '_all_strings',
     '_decode_markup',
     '_feed',
     '_find_all',
     '_find_one',
     '_is_xml',
     '_lastRecursiveChild',
     '_last_descendant',
     '_linkage_fixer',
     '_markup_is_url',
     '_markup_resembles_filename',
     '_popToTag',
     '_should_pretty_print',
     'append',
     'childGenerator',
     'children',
     'clear',
     'decode',
     'decode_contents',
     'decompose',
     'decomposed',
     'default',
     'descendants',
     'encode',
     'encode_contents',
     'endData',
     'extend',
     'extract',
     'fetchNextSiblings',
     'fetchParents',
     'fetchPrevious',
     'fetchPreviousSiblings',
     'find',
     'findAll',
     'findAllNext',
     'findAllPrevious',
     'findChild',
     'findChildren',
     'findNext',
     'findNextSibling',
     'findNextSiblings',
     'findParent',
     'findParents',
     'findPrevious',
     'findPreviousSibling',
     'findPreviousSiblings',
     'find_all',
     'find_all_next',
     'find_all_previous',
     'find_next',
     'find_next_sibling',
     'find_next_siblings',
     'find_parent',
     'find_parents',
     'find_previous',
     'find_previous_sibling',
     'find_previous_siblings',
     'format_string',
     'formatter_for_name',
     'get',
     'getText',
     'get_attribute_list',
     'get_text',
     'handle_data',
     'handle_endtag',
     'handle_starttag',
     'has_attr',
     'has_key',
     'index',
     'insert',
     'insert_after',
     'insert_before',
     'isSelfClosing',
     'is_empty_element',
     'new_string',
     'new_tag',
     'next',
     'nextGenerator',
     'nextSibling',
     'nextSiblingGenerator',
     'next_elements',
     'next_siblings',
     'object_was_parsed',
     'parentGenerator',
     'parents',
     'parserClass',
     'popTag',
     'prettify',
     'previous',
     'previousGenerator',
     'previousSibling',
     'previousSiblingGenerator',
     'previous_elements',
     'previous_siblings',
     'pushTag',
     'recursiveChildGenerator',
     'renderContents',
     'replaceWith',
     'replaceWithChildren',
     'replace_with',
     'replace_with_children',
     'reset',
     'select',
     'select_one',
     'setup',
     'smooth',
     'string',
     'string_container',
     'strings',
     'stripped_strings',
     'text',
     'unwrap',
     'wrap']


</Details>


## Working with Billboard Data:  One Artist

Let's look at one artist's page in Billboard.  We will star with Mile Davis.

```python

# Replace this with the URL of the artist or chart you are trying to scrape.  In the case of individual artists, remember to include the full URL shown here (including the `chart-history`)
url = "https://www.billboard.com/artist/miles-davis/chart-history/tlp/"  

# example of top 100:
# url = 'https://www.billboard.com/charts/hot-100/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')


```

## Scraping Tabular Data

Scraping tabular data from pages of the sort created by Billboard requires some careful attention to the structure of the XML.  Billoard has a lot of distracting ads, so a first step is to hide as many of those as possible.

![Alt text](images/bs_3.png)

Now with the clean view, use your browser menu to find the "inspect elements" option in your View or Developer tools.  This will show you the blocks of HTML that correspond to what you are seeing in the table.

The individual rows will be one HTML 'class' or identifier.  Take note of the name.  In the case of Billoard Artist View, it's called `o-chart-results-list-row`.

![Alt text](images/bs_4.png)

Hover over each of the columns you want to capture (such as "This Week", or "Last Week", or the "Artist Name" or "Track Title"). As you do, take note of the class. 

 - The artist and title are `h3` tags.  We can treat these as siblings, and use the `find_next` method to locate successive `h3` tags.
 - The ranking and date information columns are of the class `o-chart-results-list__item`.  Here we can use `find_all` (thus a list of items) and then work through them in succession to return the required values using `find_next`.

![Alt text](images/bs_5.png)


We now translate each of these into Beautiful Soup requests. 

Each song will begin with a tag of that has the class attribute 'o-chart-results-list-row'.  So a list of all songs would be:

```python
all_songs = soup.find_all(attrs={'class' : 'o-chart-results-list-row'})
```
We iterate over all the songs in the chart, saving each row/cell as a variable:

```python
for this_song in all_songs:
    title = this_song.h3.get_text(strip=True)
    author = this_song.h3.find_next('span').get_text(strip=True)
    this_song_details = this_song.find_all(attrs={'class': 'o-chart-results-list__item'})
    release_date = this_song_details[0].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
    peak_weeks = this_song_details[1].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
    peak_date = this_song_details[2].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
    total_weeks = this_song_details[3].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
```

And save the results as dictionary, which is in turn saved to a list of dictionaries, each representing the required data for one row:

```python
chart_data.append({
            'title': title,
            'author': author,
            'release_date': release_date,
            'peak_weeks': peak_weeks,
            'peak_date': peak_date,
            'total_weeks': total_weeks,
        })
```

<br>

Finally the list of dictionaries becomes a dataframe:

<br>

```python
df = pd.DataFrame(chart_data)
df
```



## One Artist vs Top 100 Lists

The tables for Artist and Top 100 charts are slightly different in their arrangement.  The code below checks the URL to which you have selected, and creates the tables accordingly.




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>author</th>
      <th>release_date</th>
      <th>peak_weeks</th>
      <th>peak_date</th>
      <th>total_weeks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bitches Brew</td>
      <td>Miles Davis</td>
      <td>05.16.70</td>
      <td>3512 Wks</td>
      <td>07.04.70</td>
      <td>29</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Man With The Horn</td>
      <td>Miles Davis</td>
      <td>07.25.81</td>
      <td>5312 Wks</td>
      <td>09.12.81</td>
      <td>18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Seven Steps To Heaven</td>
      <td>Miles Davis</td>
      <td>09.14.63</td>
      <td>6212 Wks</td>
      <td>10.05.63</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Live--Evil</td>
      <td>Miles Davis</td>
      <td>12.25.71</td>
      <td>12512 Wks</td>
      <td>02.12.72</td>
      <td>14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>You're Under Arrest</td>
      <td>Miles Davis</td>
      <td>06.01.85</td>
      <td>11112 Wks</td>
      <td>06.29.85</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Miles Davis At Fillmore</td>
      <td>Miles Davis</td>
      <td>12.12.70</td>
      <td>12312 Wks</td>
      <td>01.02.71</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>On The Corner</td>
      <td>Miles Davis</td>
      <td>11.18.72</td>
      <td>15612 Wks</td>
      <td>12.09.72</td>
      <td>11</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Decoy</td>
      <td>Miles Davis</td>
      <td>06.30.84</td>
      <td>16912 Wks</td>
      <td>07.28.84</td>
      <td>11</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Tutu</td>
      <td>Miles Davis</td>
      <td>10.25.86</td>
      <td>14112 Wks</td>
      <td>11.15.86</td>
      <td>10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Miles Davis In Europe</td>
      <td>Miles Davis</td>
      <td>09.26.64</td>
      <td>11612 Wks</td>
      <td>11.21.64</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>My Funny Valentine: Miles Davis In Concert</td>
      <td>Miles Davis</td>
      <td>04.24.65</td>
      <td>13812 Wks</td>
      <td>06.05.65</td>
      <td>9</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Quiet Nights</td>
      <td>Miles Davis</td>
      <td>04.11.64</td>
      <td>9312 Wks</td>
      <td>05.23.64</td>
      <td>9</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Tribute To Jack Johnson</td>
      <td>Miles Davis</td>
      <td>04.24.71</td>
      <td>15912 Wks</td>
      <td>06.05.71</td>
      <td>8</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Get Up With It</td>
      <td>Miles Davis</td>
      <td>01.04.75</td>
      <td>14112 Wks</td>
      <td>02.08.75</td>
      <td>8</td>
    </tr>
    <tr>
      <th>14</th>
      <td>In Concert</td>
      <td>Miles Davis</td>
      <td>05.05.73</td>
      <td>15212 Wks</td>
      <td>06.09.73</td>
      <td>8</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Star People</td>
      <td>Miles Davis</td>
      <td>05.21.83</td>
      <td>13612 Wks</td>
      <td>06.18.83</td>
      <td>7</td>
    </tr>
    <tr>
      <th>16</th>
      <td>We Want Miles</td>
      <td>Miles Davis</td>
      <td>05.29.82</td>
      <td>15912 Wks</td>
      <td>06.19.82</td>
      <td>7</td>
    </tr>
    <tr>
      <th>17</th>
      <td>In A Silent Way</td>
      <td>Miles Davis</td>
      <td>09.06.69</td>
      <td>13412 Wks</td>
      <td>09.06.69</td>
      <td>6</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Agharta</td>
      <td>Miles Davis</td>
      <td>03.13.76</td>
      <td>16812 Wks</td>
      <td>04.03.76</td>
      <td>5</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Amandla</td>
      <td>Miles Davis</td>
      <td>06.17.89</td>
      <td>17712 Wks</td>
      <td>07.08.89</td>
      <td>5</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Big Fun</td>
      <td>Miles Davis</td>
      <td>06.08.74</td>
      <td>17912 Wks</td>
      <td>07.06.74</td>
      <td>5</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Doo-Bop</td>
      <td>Miles Davis</td>
      <td>07.25.92</td>
      <td>19012 Wks</td>
      <td>08.08.92</td>
      <td>4</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Basic Miles - The Classic Performances Of Mile...</td>
      <td>Miles Davis</td>
      <td>10.13.73</td>
      <td>18912 Wks</td>
      <td>10.20.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Directions</td>
      <td>Miles Davis</td>
      <td>04.11.81</td>
      <td>17912 Wks</td>
      <td>04.11.81</td>
      <td>2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Water Babies</td>
      <td>Miles Davis</td>
      <td>05.07.77</td>
      <td>19012 Wks</td>
      <td>05.07.77</td>
      <td>2</td>
    </tr>
    <tr>
      <th>25</th>
      <td>LIVE In Europe 1967: The Bootleg Series Vol. 1</td>
      <td>The Miles Davis Quintet</td>
      <td>10.08.11</td>
      <td>17112 Wks</td>
      <td>10.08.11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Miles at the Fillmore: Miles Davis 1970 - The ...</td>
      <td>Miles Davis</td>
      <td>04.12.14</td>
      <td>18912 Wks</td>
      <td>04.12.14</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Everything's Beautiful</td>
      <td>Miles Davis &amp; Robert Glasper</td>
      <td>06.18.16</td>
      <td>15212 Wks</td>
      <td>06.18.16</td>
      <td>1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>The Final Tour: The Bootleg Series, Vol. 6</td>
      <td>Miles Davis &amp; John Coltrane</td>
      <td>04.07.18</td>
      <td>18712 Wks</td>
      <td>04.07.18</td>
      <td>1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Champions: Rare Miles From The Complete Jack J...</td>
      <td>Miles Davis</td>
      <td>07.31.21</td>
      <td>16112 Wks</td>
      <td>07.31.21</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

<br>


<Details>

<Summary>Get the Code</Summary>


```python

if 'artist' in url:
    chart_data = []
    all_songs = soup.find_all(attrs={'class' : 'o-chart-results-list-row'})
    # iterate over all the songs in the chart
    for this_song in all_songs:
        title = this_song.h3.get_text(strip=True)
        author = this_song.h3.find_next('span').get_text(strip=True)
        this_song_details = this_song.find_all(attrs={'class': 'o-chart-results-list__item'})
        release_date = this_song_details[0].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
        peak_weeks = this_song_details[1].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
        peak_date = this_song_details[2].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
        total_weeks = this_song_details[3].find_next(attrs={'class': 'o-chart-results-list__item'}).get_text(strip=True)
        chart_data.append({
            'title': title,
            'author': author,
            'release_date': release_date,
            'peak_weeks': peak_weeks,
            'peak_date': peak_date,
            'total_weeks': total_weeks,
        })

    df = pd.DataFrame(chart_data)
    df

elif 'charts' in url:
    data = []
    for e in soup.find_all(attrs={'class':'o-chart-results-list-row-container'}):
        # spans = e.find_all('span')
        this_week = e.span.get_text(strip=True)
        last_week = e.h3.find_next('span').find_next('span').get_text(strip=True)
        peak_position = e.h3.find_next('span').find_next('span').find_next('span').get_text(strip=True)
        weeks_on_chart = e.h3.find_next('span').find_next('span').find_next('span').find_next('span').get_text(strip=True)
        data.append({
            'title':e.h3.get_text(strip=True),
            'author':e.h3.find_next('span').get_text(strip=True),
            'this_week' : this_week,
            'last_week': last_week,
            'peak_position': peak_position,
            'weeks_on_chart': weeks_on_chart
        })
    df = pd.DataFrame(data)
    df
    
df

df.to_csv("Miles_Davis_Billboard.csv")
```

</Details>