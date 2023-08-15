____________________
# Exploring (and Mining) XML with BeautifulSoup

**XML** stands for **eXtensible Markup Language**, and mainly serves to transport and store data. At its core, XML was designed to be **both machine- and human-readable**. 

XML is used widely on the web--**HTML** files are a kind of XML, in this case used for structured graphical representation of content. Read more about [**XML**](https://www.w3schools.com/xml/xml_syntax.asp).

In the case of music files, the common encoding standard is **MEI**, which stands for **Music Encoding Initiative** and is built on top of the XML framework. Read more about [**MEI**](https://music-encoding.org/).

**Beautiful Soup** is a Python library that allows us to interact with XML files--finding elements (the 'tags') and their attributes. Documentation: [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [here](https://tedboy.github.io/bs4_doc/index.html).

**Beautiful Soup** can be a good way to scrape data from web pages (especially tabular data).  It can also be a good way to learn about the structure of MEI files.

In this tutorial we will explore both possibilities.

------
## Setup: Importing Python Libraries


```python
import os
from bs4 import BeautifulSoup as bs
import optparse
import sys
from pathlib import Path
import requests
import pandas as pd
from lxml import etree
import re
from collections import Counter
import glob
import verovio
from IPython.display import SVG, HTML
import matplotlib.pyplot as plt
```

A list of all Beautiful Soup methods.  The most important for our work will be those that "find" elements and that 'get' the strings associated with various attributes and tags.


```python
dir(bs)
```


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



----
## Import Data (XML files!)

As your first and perhaps most important step, you'll have to go find some data. For this homework assignment, we will work with *these files*, which you can access *here*. Once you've picked your file and copied its URL, use the function provided below to **import it as a JSON object**.

The following function extras text as a JSON:


```python

def getXML(url):
    # request for xml document of given url
    response = requests.get(url)    
    # response will be provided in JSON format
    return response.text
```

**read in your file** and store it in the "xml_document" variable:



```python
xml_document = getXML('https://crimproject.org/mei/CRIM_Model_0008.mei')
```

Once you've imported a file, you should be able to **convert it into a Beautiful Soup Object**:


```python
my_soup_file = bs(xml_document, 'xml')
```

____________________
## Explore the XML File

The **MEI** framework tends to be easy to understand (as it is meant to be human-readable, too!) – and given some simple tools you should be able to successfully navigate your data.


First, let's take a look at the document as a whole. Make the cell below **print the "pretty"** version of your MEI file:

```python
print(my_soup_file.prettify())
```


```python
print(my_soup_file.prettify())
```

This is just the start ...



    <?xml version="1.0" encoding="utf-8"?>
    <?xml-model href="https://music-encoding.org/schema/4.0.1/mei-CMN.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
    <?xml-model href="https://music-encoding.org/schema/4.0.1/mei-CMN.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
    <mei meiversion="4.0.1" xml:id="m-1" xmlns="http://www.music-encoding.org/ns/mei">
     <meiHead xml:id="m-2">
      <fileDesc xml:id="m-3">
       <titleStmt>
        <title>
         Ave Maria
        </title>
        <respStmt>
         <persName auth="VIAF" auth.uri="http://viaf.org/viaf/100226284" role="composer">
          Josquin Des Prés
         </persName>
         <persName role="editor">
          Marco Gurrieri
         </persName>
         <persName role="editor">
          Vincent Besson
         </persName>
         <persName role="editor">
          Richard Freedman
         </persName>
        </respStmt>
       </titleStmt>

----

## Searching Elements and Attributes

The `find()` and `find(all)` methods are key ways of returning one or more tags in your XML file.  

`my_soup_file.persName()`, for example, will return the first instance of the `persName` tag in the MEI document we previously imported and named as the `my_soup_file` object. But it is also possible to do this in several other ways, with varied results:

- `my_soup_file.find('persName')` will find *the first* instance of a tag with that name.
- `my_soup_file.find_all('persName')` will find *all* the tags with that name and return them as a Python `list` object, across which you can iterate
- It is also possible to pass in lists (to return several different tags), regular expressions (to return tags matching various conditions), and even a dictionary (to match attributes of tags). Read more in the [Beautiful Soup documentation](https://tedboy.github.io/bs4_doc/6_searching_the_tree.html).
- We can *edit* tags and their attributes, and even *add or delete* tags.  For instance we might want to change or add the name of an editor in a certain file, or to update information about copyright in a folder of files.  Read more in the [Beautiful Soup documentation](https://tedboy.github.io/bs4_doc/7_modifying_the_tree.html).
- We can report the entire tag, or get just the text associated with it, then use that information in some subsequent report or process.  For instance, we could return a list of editors or sources for one or more files.  Or we could collect information about clefs and key signatures across a corpus of files, and 

As explained in the following section of this tutorial, these same basic concepts can be applied across the XML tree to look for children, parents and siblings of various tags.



----
## Family Matters:  Working with Children, Siblings, and Parents 

As you have probably noticed by now, MEI (and XML, generally) files follow a **tree-like structure**. Any document has its elements defined recursively, as its children. Intuitively, **children** are elements contained within a broader element (think section), also known as **parent**.  And **children** of the same parent tag are **siblings**.

In a way, the Title Statement ("\<titleStmt>") element is a wrapper for all things that define a Title Statement. Mainly, a typical MEI Title Statement describes the piece's title and the people involved with the piece in some capacity. It contains tags labelled `title`, and `respStmt` (which in turn contains a number of `persName` tags).
    

    
```python
print(my_soup_file.titleStmt.prettify())
```

It's possible to return these in turn, by chaining the elements together:
    
```python
print(my_soup_file.titleStmt.title.prettify())
```

Or
    
    
```python
print(my_soup_file.titleStmt.respStmt.prettify())
```
    
Or
  
```python
print(my_soup_file.titleStmt.respStmt.persName.prettify())
```
    
But once we reach `persName` we are stuck, since there are in fact several such tags, and the chained method will only return the **first instance** of each.  We need another way. This is where the **find_all** methods of Beautiful Soup come in.

### Looking Down:  Children

* First, let's find all **children** of the title Statement. The results are similar to what we found with other methods, but in this case we are searching for _all_ the elements nested within the titleStmt.


```python
children_of_title = my_soup_file.titleStmt.findChildren()
for child in children_of_title:
    print(child.prettify())
```

Here it's plain that the names of the individuals are in fact stated twice--once as part of the nested `restStmt` and again as part of the remainder of the `titleStmt`.  This is part of the MEI standard.


```python
children_of_title = my_soup_file.titleStmt.findChildren()
for child in children_of_title:
    print(child.prettify())
```

    <title>
     Veni speciosam
    </title>
    
    <respStmt>
     <persName auth="VIAF" auth.uri="http://viaf.org/viaf/42035469" role="composer">
      Johannes Lupi
     </persName>
     <persName role="editor">
      Marco Gurrieri
     </persName>
     <persName role="editor">
      Bonnie Blackburn
     </persName>
     <persName role="editor">
      Vincent Besson
     </persName>
     <persName role="editor">
      Richard Freedman
     </persName>
    </respStmt>
    <persName auth="VIAF" auth.uri="http://viaf.org/viaf/42035469" role="composer">
     Johannes Lupi
    </persName>
    
    <persName role="editor">
     Marco Gurrieri
    </persName>
    
    <persName role="editor">
     Bonnie Blackburn
    </persName>
    
    <persName role="editor">
     Vincent Besson
    </persName>
    
    <persName role="editor">
     Richard Freedman
    </persName>


### Looking Across: Siblings

Siblings are tags of the *same type* as a given tag.  

Thus `first_person = my_soup_file.titleStmt.persName` will find the **first element** of the `persName` type.

To find all the subsequent *siblings of the same type*, we use `findNextSiblings`:


`first_person.findNextSiblings()` will find all the siblings within that parent *after* the first element.

We could also do this in one line of code:

```python
sib_names = my_soup_file.titleStmt.persName.findNextSiblings()
sib_names
```


```python
first_person = my_soup_file.titleStmt.persName
first_person.findNextSiblings()
```




    [<persName role="editor">Marco Gurrieri</persName>,
     <persName role="editor">Bonnie Blackburn</persName>,
     <persName role="editor">Vincent Besson</persName>,
     <persName role="editor">Richard Freedman</persName>]

`findNext` will find the next element of the same type:

```python
first_person = my_soup_file.titleStmt.persName
first_person.findNext()
```

And this could be chained together with additional requests to `findNext`:


```python
second_person = my_soup_file.titleStmt.persName.findNext()
second_person
```

    <persName role="editor">Marco Gurrieri</persName>
### Looking Up:  Parents

Here we can find the tags going up from some lower level to find out the `parent` tag (and in turn discover other children of that parent), or parents of the parents.  For example here we find all the `parents` of one `note` in our mei file. **bottom level** of `note`:

```python
for parent in my_soup_file.note.find_parents():
    print(parent.name)
```


```python
for parent in my_soup_file.note.find_parents():
    print(parent.name)
```

    layer
    staff
    measure
    section
    score
    mdiv
    body
    music
    mei
    [document]


Knowing the **parent** of a given tag allows you to **add a sibling** of the same type:

```python
# The parent tag of persName 
people_involved_parent = my_soup_file.find("persName").parent
# create a new tag that will have the role of 'analyst':
new_person_tag = my_soup_file.new_tag("persName", role="Analyst")
# populate the text of that new tag with a string:
new_person_tag.string = "Oleh Shostak"
# add the new tag to the original parent found above
people_involved_parent.append(new_person_tag)
# and show the result
my_soup_file.find_all("persName")
```




```python
people_involved_parent = my_soup_file.find("persName").parent
new_person_tag = my_soup_file.new_tag("persName", role="Analyst")
new_person_tag.string = "Oleh Shostak"
people_involved_parent.append(new_person_tag)

my_soup_file.find_all("persName")
```




    [<persName auth="VIAF" auth.uri="http://viaf.org/viaf/42035469" role="composer">Johannes Lupi</persName>,
     <persName role="editor">Marco Gurrieri</persName>,
     <persName role="editor">Bonnie Blackburn</persName>,
     <persName role="editor">Vincent Besson</persName>,
     <persName role="editor">Richard Freedman</persName>,
     <persName role="Analyst">Oleh Shostak</persName>,
     <persName auth="VIAF" auth.uri="http://viaf.org/viaf/42035469" role="composer">Johannes Lupi</persName>,
     <persName auth="VIAF" auth.uri="http://viaf.org/viaf/59135590">Pierre Attaingnant</persName>]




By default, adding `children` to the request will **find all of the children** associated with that parent tag.  It returns them as a *list* (not as a slice of XML), and so to see them we need to iterate over them:

```python
for item in my_soup_file.titleStmt.children:
    print(item.prettify())
```

Here we see that the `titleStmt` contains both a `title` (the title of the work) and a `respStmt` (with the names of individuals and their roles:  composer and editors in this case.  

Each person in the `respStmt` is encoded with their own element (tag).  

The `role` attribute in each tag conveys the part each person played in this piece (and text).  

Other attributes are possible with the tag, as we see in the case of the composer, for whom we also have an `auth` file to identify them via a public key (the `auth.uri`).


```python
for item in my_soup_file.titleStmt.children:
    print(item.prettify())
```

    <title>
     Ave Maria
    </title>
    
    <respStmt>
     <persName auth="VIAF" auth.uri="http://viaf.org/viaf/100226284" role="composer">
      Josquin Des Prés
     </persName>
     <persName role="editor">
      Marco Gurrieri
     </persName>
     <persName role="editor">
      Vincent Besson
     </persName>
     <persName role="editor">
      Richard Freedman
     </persName>
    </respStmt>


## Finding All Tags of a Specific Type

We can **find all the tags of a specific type**, too, regardless of their 'parentage'.

* Note that in an XML document you can specify some part of the tree on the way to the individual child tag, or go directly to those tags.  This could be useful if some element is reused at different places in your XML schema.

```python
my_soup_file.titleStmt.find_all("persName")```

or

```python
my_soup_file.find_all("persName")```

Note that in the case of `find_all` BS will return a "list" of the relevant tags. 


```python
my_soup_file.titleStmt.find_all("persName")

```




    [<persName auth="VIAF" auth.uri="http://viaf.org/viaf/42035469" role="composer">Johannes Lupi</persName>,
     <persName role="editor">Marco Gurrieri</persName>,
     <persName role="editor">Bonnie Blackburn</persName>,
     <persName role="editor">Vincent Besson</persName>,
     <persName role="editor">Richard Freedman</persName>]



## Finding Tags by Attribute

And filter for those with a certain **attribute value**. 

* Note that the values are specified as a dictionary:  `{'your_key': 'your_value'}` along with the tag name.

Here for instance are all the `persName` tags with the string "editor" in the `role` attribute:

```python
my_soup_file.find_all("persName", {"role": "editor"})```


```python
my_soup_file.find_all("persName", {"role": "editor"})
```




    [<persName role="editor">Marco Gurrieri</persName>,
     <persName role="editor">Bonnie Blackburn</persName>,
     <persName role="editor">Vincent Besson</persName>,
     <persName role="editor">Richard Freedman</persName>]



## Return the Text of a Tag


Sometimes, you might be working for scraping/analysis tools and would want to access the **contents (text)** of individual tags:

```python
for tag in my_soup_file.find_all("persName", {"role": "editor"}):
    print(tag.text.strip())
```
    
The `.strip()` function assures that we remove whitespace and other useless code.

Note that the 'text' of a tag is not the same as its 'name':

`print(my_soup_file.titleStmt.persName.name)` will return the 'name' of the tag itself, in this case simply 'title'

`print(my_soup_file.titleStmt.persName.text)` will return the 'contents' of the tag itself, in this case simply 'Ave Maria'


```python

for tag in my_soup_file.find_all("persName", {"role": "editor"}):
    print(tag.text.strip())
```

    Marco Gurrieri
    Bonnie Blackburn
    Vincent Besson
    Richard Freedman


Similarly, we can easily access the composer:


```python
# the text of the composer element:
for tag in my_soup_file.find_all("persName", {"role": "composer"}):
    print(tag.text.strip())
```

    Johannes Lupi
    Johannes Lupi


And the title:


```python
# the text of the title element, more directly:
my_soup_file.title.text.strip()
```




    'Veni speciosam'

-----


-----
## Working with MEI `music`:  Measures, Staves, Notes

MEI (XML) files are normally thought of as rich encodings of musical scores and the editorial and source critical information that surround their production. But they can also be interrogated for music data.  This is despite the fact that those in Common Music Notation (the standard in use since the 18th century) are encoded 'measure by measure' and so it can be rather tricky to take stock of events that (for instance) are occuring at the same time in different staves.  

Advanced analysis of musical patterns is probably best done with Music21 or CRIM Intervals.  But a surprising among of relevant data about notes and editorial practice can be found with Beautiful my_soup_file.

### Staves

Information about the staves are contained in the `staffDef` tag. First, let's look at just the **first staff**:

```python
print(my_soup_file.staffDef.prettify())
```


```python
print(my_soup_file.staffDef.prettify())
```

    <staffDef clef.line="2" clef.shape="G" key.sig="1f" label="Superius" lines="5" n="1" xml:id="m-30">
     <label>
      Superius
     </label>
     <instrDef midi.channel="1" midi.pan="26" midi.volume="100" xml:id="m-32"/>
    </staffDef>
    


Next, **find all staves** with `find_all`:

* Notice that these are returned as a **list** object, so we can easily also run this with a **for** loop.  

```python
my_soup_file.find_all("staffDef")
```

* Beautiful Soup responses are "list ready".  Thus the first staff is `my_soup_file.find_all("staffDef")[0]`.  The last staff is `my_soup_file.find_all("staffDef")[-1]`.

```python
my_soup_file.find_all("staffDef")
```




    [<staffDef clef.line="2" clef.shape="G" key.sig="1f" label="Superius" lines="5" n="1" xml:id="m-30">
     <label>Superius</label>
     <instrDef midi.channel="1" midi.pan="26" midi.volume="100" xml:id="m-32"/>
     </staffDef>,
     <staffDef clef.line="2" clef.shape="G" key.sig="1f" label="Contratenor" lines="5" n="2" xml:id="m-33">
     <label>Contratenor</label>
     <instrDef midi.channel="1" midi.pan="46" midi.volume="100" xml:id="m-35"/>
     </staffDef>,
     <staffDef clef.dis="8" clef.dis.place="below" clef.line="2" clef.shape="G" key.sig="1f" label="PrimusTenor" lines="5" n="3" xml:id="m-36">
     <label>PrimusTenor</label>
     <instrDef midi.channel="1" midi.pan="81" midi.volume="100" xml:id="m-38"/>
     </staffDef>,
     <staffDef clef.dis="8" clef.dis.place="below" clef.line="2" clef.shape="G" key.sig="1f" label="SecundusTenor" lines="5" n="4" xml:id="m-39">
     <label>SecundusTenor</label>
     <instrDef midi.channel="1" midi.pan="81" midi.volume="100" xml:id="m-41"/>
     </staffDef>,
     <staffDef clef.dis="8" clef.dis.place="below" clef.line="2" clef.shape="G" key.sig="1f" label="Bassus" lines="5" n="5" xml:id="m-42">
     <label>Bassus</label>
     <instrDef midi.channel="1" midi.pan="81" midi.volume="100" xml:id="m-44"/>
     </staffDef>]



We can use the collection of Staves to figure out **what voices** are used in a piece:

- find ALL STAVES with a GIVEN CLEF by passing dictionary that specifies the requested type
- the final_all results are a Beautiful Soup list:

```python
# get all G-clef staves:
staves = my_soup_file.find_all("staffDef", {'clef.shape': "G"})
# print cleaned-up text of those tags--just the names
for staff in staves:
    print(staff.text.strip())
```


```python

# Get all G-clef staves:
staves = my_soup_file.find_all("staffDef", {'clef.shape': "G"})

# print cleaned-up text of those tags--just the names
for staff in staves:
    print(staff.text.strip())
```

    Superius
    Contratenor
    PrimusTenor
    SecundusTenor
    Bassus




### Counting Notes

We already know how to find the first note (of the first staff in the first bar):

```python
my_soup_file.note.get('pname')
```

But we can also:



```python
# gets just the first pitch
my_soup_file.note.get('pname')
```




    'g'




```python
# how many notes?
len(my_soup_file.find_all('note'))
```




    1933




```python
# find all the notes and print pitch names
for note in my_soup_file.find_all(name='note'):
    print(note.get('pname'))
```

    g
    d
    d
    c
    d
    f
    d
    e
    d
    c
    a
    g
    f
    b
    d
    c
    b
    g
    b
    a
    g
    b
    a
    g
    b
    a
    g
    f
    d
    e
    f
    g
    a
    g
    d
    b
    c
    a
    a
    d
    g
    f
    d
    c
    d
    f
    d
    g
    b
    a
    g
    f
    d
    f
    e
    d
    c
    a
    g
    f
    a
    g
    a
    e
    d
    e
    f
    e
    b
    d
    c
    g
    b
    a
    g
    f
    g
    a
    g
    d
    c
    b
    a
    b
    g
    d
    f
    e
    f
    g
    g
    d
    g
    f
    e
    f
    a
    g
    a
    d
    c
    d
    f
    e
    d
    e
    f
    g
    d
    c
    d
    f
    a
    a
    f
    g
    a
    d
    e
    d
    a
    b
    c
    b
    a
    b
    e
    d
    c
    a
    d
    a
    e
    d
    e
    f
    g
    f
    e
    d
    a
    b
    c
    c
    a
    c
    a
    b
    a
    a
    g
    e
    f
    b
    d
    a
    d
    c
    d
    e
    a
    f
    g
    a
    f
    a
    g
    f
    e
    d
    d
    b
    c
    d
    c
    b
    f
    d
    e
    d
    d
    a
    g
    f
    e
    d
    a
    d
    e
    d
    e
    f
    g
    a
    e
    f
    d
    d
    b
    c
    d
    c
    b
    a
    d
    d
    b
    c
    d
    f
    a
    g
    a
    b
    f
    e
    d
    a
    c
    b
    d
    f
    e
    e
    d
    d
    b
    a
    g
    f
    g
    g
    a
    b
    c
    d
    e
    d
    b
    c
    d
    c
    b
    d
    c
    b
    c
    d
    a
    c
    b
    f
    d
    e
    d
    a
    g
    g
    a
    b
    c
    d
    c
    g
    f
    d
    e
    g
    a
    d
    b
    c
    c
    b
    g
    a
    f
    g
    e
    d
    c
    g
    f
    d
    e
    d
    b
    a
    b
    c
    d
    a
    a
    b
    c
    d
    f
    g
    e
    d
    d
    g
    a
    g
    a
    b
    b
    a
    b
    c
    a
    d
    d
    e
    f
    g
    g
    f
    e
    d
    g
    d
    c
    b
    d
    c
    d
    c
    a
    g
    f
    g
    c
    b
    e
    d
    a
    g
    b
    a
    g
    d
    f
    e
    g
    a
    b
    c
    d
    c
    g
    f
    d
    e
    a
    b
    a
    g
    e
    d
    d
    c
    a
    g
    a
    b
    c
    c
    b
    g
    a
    f
    g
    e
    f
    d
    g
    f
    f
    e
    d
    c
    d
    g
    a
    b
    c
    a
    d
    c
    d
    g
    d
    c
    b
    a
    b
    g
    b
    a
    b
    c
    d
    g
    g
    d
    g
    g
    d
    d
    g
    d
    d
    c
    b
    a
    b
    g
    f
    e
    f
    g
    a
    f
    d
    c
    d
    f
    a
    d
    d
    a
    g
    f
    e
    f
    e
    d
    c
    d
    a
    g
    f
    a
    g
    a
    c
    d
    a
    b
    c
    d
    e
    f
    d
    e
    d
    c
    g
    b
    a
    g
    c
    b
    a
    a
    g
    f
    e
    d
    f
    d
    c
    d
    d
    f
    f
    g
    d
    e
    f
    g
    a
    c
    d
    a
    a
    e
    f
    e
    d
    c
    d
    a
    b
    c
    b
    a
    d
    a
    g
    e
    d
    c
    d
    a
    f
    e
    d
    c
    a
    b
    d
    c
    d
    f
    a
    c
    b
    a
    e
    d
    e
    f
    g
    c
    a
    g
    f
    e
    d
    c
    d
    g
    a
    e
    g
    a
    d
    c
    b
    a
    b
    c
    b
    g
    c
    a
    b
    c
    a
    b
    a
    b
    f
    e
    d
    a
    d
    c
    d
    f
    a
    e
    f
    d
    c
    d
    e
    d
    d
    a
    g
    a
    e
    d
    c
    d
    e
    g
    f
    d
    c
    d
    a
    d
    a
    e
    d
    a
    b
    g
    a
    b
    g
    f
    e
    d
    g
    d
    a
    c
    b
    a
    c
    b
    g
    f
    g
    f
    e
    c
    d
    g
    a
    b
    g
    a
    g
    a
    g
    e
    d
    e
    g
    f
    e
    a
    d
    c
    d
    e
    c
    f
    d
    e
    g
    d
    g
    b
    a
    b
    c
    d
    f
    e
    d
    e
    c
    g
    f
    e
    a
    f
    g
    c
    d
    d
    c
    d
    f
    e
    d
    d
    a
    g
    c
    b
    a
    b
    c
    d
    e
    c
    c
    d
    c
    c
    g
    a
    b
    g
    a
    g
    d
    g
    f
    c
    b
    a
    c
    b
    a
    g
    f
    e
    c
    e
    d
    c
    g
    g
    d
    e
    f
    g
    c
    b
    a
    g
    d
    g
    f
    e
    a
    b
    a
    g
    d
    e
    g
    b
    c
    d
    g
    c
    a
    b
    d
    g
    f
    g
    d
    d
    a
    g
    b
    d
    g
    f
    d
    c
    b
    a
    g
    c
    g
    b
    c
    f
    g
    e
    b
    a
    g
    f
    g
    d
    e
    c
    b
    g
    b
    g
    a
    b
    c
    d
    e
    d
    d
    c
    b
    g
    d
    f
    g
    g
    a
    f
    g
    d
    c
    b
    c
    d
    a
    a
    e
    d
    d
    d
    a
    d
    g
    a
    d
    d
    c
    d
    c
    a
    b
    g
    f
    g
    e
    a
    d
    g
    g
    f
    g
    d
    c
    b
    a
    g
    d
    d
    d
    c
    d
    f
    e
    d
    e
    f
    g
    a
    c
    c
    b
    b
    c
    b
    a
    b
    a
    g
    f
    d
    f
    g
    d
    g
    d
    c
    d
    e
    d
    f
    g
    e
    a
    d
    g
    g
    f
    d
    d
    c
    d
    e
    d
    d
    c
    a
    a
    g
    a
    g
    g
    f
    e
    a
    c
    b
    a
    d
    a
    b
    c
    a
    f
    f
    e
    d
    e
    d
    c
    a
    a
    d
    d
    c
    d
    b
    a
    g
    f
    d
    f
    e
    d
    g
    d
    c
    b
    b
    d
    g
    a
    a
    b
    b
    e
    f
    e
    d
    e
    c
    c
    b
    a
    g
    g
    f
    g
    a
    g
    a
    b
    c
    d
    f
    d
    g
    f
    c
    b
    a
    g
    d
    d
    f
    e
    d
    d
    c
    d
    g
    e
    d
    e
    g
    g
    b
    c
    b
    c
    g
    g
    a
    b
    c
    a
    b
    g
    b
    f
    f
    e
    d
    e
    c
    c
    b
    a
    g
    f
    g
    a
    g
    f
    f
    d
    e
    f
    e
    d
    c
    c
    b
    a
    g
    d
    d
    f
    e
    d
    g
    d
    g
    c
    c
    g
    b
    d
    e
    e
    c
    g
    b
    g
    a
    b
    g
    c
    g
    d
    e
    g
    g
    e
    c
    d
    g
    c
    b
    e
    e
    g
    e
    d
    c
    e
    f
    g
    e
    c
    g
    d
    g
    b
    g
    d
    d
    c
    d
    g
    d
    f
    g
    g
    f
    e
    d
    c
    b
    a
    g
    g
    g
    d
    c
    b
    b
    a
    g
    a
    d
    f
    g
    f
    e
    f
    g
    a
    b
    a
    d
    d
    e
    d
    c
    a
    g
    g
    f
    c
    d
    b
    a
    b
    g
    d
    g
    g
    b
    d
    d
    g
    g
    d
    c
    c
    b
    a
    g
    f
    e
    f
    e
    d
    f
    g
    a
    b
    g
    f
    g
    d
    d
    d
    d
    c
    b
    a
    g
    d
    g
    b
    a
    d
    a
    a
    g
    c
    d
    f
    e
    d
    c
    b
    a
    g
    f
    g
    f
    e
    d
    c
    d
    a
    a
    d
    f
    a
    g
    a
    b
    c
    a
    d
    e
    f
    g
    a
    f
    d
    c
    d
    g
    e
    f
    e
    d
    c
    b
    b
    c
    a
    f
    g
    a
    d
    e
    a
    f
    g
    a
    b
    c
    a
    b
    f
    e
    d
    e
    f
    g
    a
    d
    d
    a
    b
    a
    g
    f
    g
    f
    d
    e
    d
    d
    b
    c
    d
    c
    b
    a
    b
    a
    g
    d
    g
    d
    b
    c
    g
    f
    g
    e
    d
    b
    c
    f
    e
    f
    g
    a
    b
    g
    c
    d
    e
    d
    c
    d
    e
    g
    c
    b
    a
    b
    g
    e
    d
    c
    g
    e
    c
    e
    d
    c
    b
    g
    d
    f
    e
    b
    g
    a
    a
    d
    c
    b
    c
    a
    f
    e
    d
    e
    f
    g
    a
    d
    a
    f
    g
    a
    d
    d
    b
    c
    d
    e
    f
    b
    a
    b
    a
    g
    f
    d
    e
    d
    b
    c
    d
    g
    f
    a
    g
    f
    c
    b
    c
    d
    e
    d
    e
    d
    c
    b
    d
    f
    g
    a
    b
    d
    e
    f
    d
    d
    c
    b
    a
    g
    a
    b
    c
    b
    d
    g
    f
    g
    b
    a
    g
    f
    e
    f
    e
    d
    b
    c
    a
    g
    d
    g
    c
    d
    c
    d
    g
    g
    g
    d
    c
    b
    g
    e
    c
    g
    f
    e
    g
    f
    e
    c
    d
    c
    a
    d
    d
    c
    d
    e
    f
    d
    e
    b
    g
    a
    g
    a
    b
    g
    a
    b
    d
    a
    b
    c
    d
    c
    c
    g
    f
    c
    d
    e
    d
    d
    a
    g
    f
    d
    c
    b
    c
    a
    d
    c
    b
    e
    c
    d
    d
    c
    b
    c
    d
    e
    a
    g
    f
    e
    f
    d
    a
    f
    g
    a
    b
    c
    d
    f
    e
    d
    f
    g
    a
    b
    d
    e
    f
    g
    d
    c
    b
    g
    c
    e
    d
    d
    a
    a
    e
    c
    f
    g
    a
    g
    f
    e
    d
    d
    c
    d
    a
    d
    a
    c
    b
    a
    e
    d
    a
    d
    d
    g
    d
    f
    e
    d
    d
    c
    a
    d
    a
    c
    b
    d
    g
    b
    a
    g
    g
    f
    g
    f
    e
    g
    b
    g
    d
    g
    a
    g
    d
    c
    b
    c
    b
    d
    d
    b
    c
    d
    e
    f
    g
    g
    b
    a
    g
    a
    b
    c
    d
    g
    d
    f
    e
    d
    g
    f
    g
    d
    c
    d
    c
    b
    b
    d
    c
    a
    b
    b
    a
    d
    g
    f
    g
    f
    e
    d
    d
    f
    g
    a
    b
    c
    d
    c
    c
    d
    d
    a
    g
    f
    d
    e
    c
    g
    b
    e
    d
    g
    g
    a
    b
    g
    f
    d
    f
    e
    c
    f
    g
    a
    f
    g
    f
    a
    f
    c
    b
    a
    d
    e
    d
    c
    g
    f
    e
    d
    c
    b
    e
    c
    g
    f
    g
    c
    c
    g
    f
    e
    d
    c
    a
    g
    b
    a
    g
    e
    f
    g
    c
    b
    g
    b
    c
    d
    b
    g
    a
    c
    d
    c
    a
    c
    g
    f
    d
    f
    g
    g
    a
    d
    c
    c
    b
    g
    g
    f
    g
    e
    d
    d
    f
    d
    f
    g
    d
    g
    b
    c
    b
    a
    g
    d
    c
    a
    c
    d
    e
    a
    g
    f
    e
    g
    f
    e
    d
    a
    a
    b
    b
    a
    f
    d
    c
    d
    e
    f
    g
    a
    f
    g
    f
    e
    b
    g
    d
    e
    d
    f
    e
    d
    e
    f
    a
    g
    f
    g
    a
    b
    c
    d
    f
    e
    c
    f
    d
    d
    c
    a
    e
    d
    c
    b
    c
    b
    a
    g
    e
    f
    d
    c
    d
    b
    c
    a
    e
    e
    e
    f
    e
    a
    e
    f
    a
    f
    e
    c
    d
    c
    d
    e
    a
    a
    e
    c
    d
    e
    e
    d
    c
    b
    a
    g
    f
    e
    d
    a
    b
    a
    a
    d
    c
    a
    b
    a
    c
    d
    b
    c
    e
    f
    e
    a
    f
    g
    a
    d
    f
    e
    d
    c
    d
    f
    g
    a
    d
    a
    a
    b
    d
    d
    d
    c
    b
    a
    b
    g
    g
    f
    a
    f
    g
    a
    d
    e
    d
    b
    d
    b
    a
    g
    f
    b
    g
    d
    g
    a
    b
    c
    d
    b
    c
    d
    e
    d
    b
    b
    a
    g
    f
    d
    e
    d
    d
    c
    b
    a
    g
    d
    b
    c
    d
    g
    b
    c
    d
    g
    a
    g
    e
    d
    b
    c
    g
    g
    b
    c
    d
    b
    e
    g
    d
    g
    a
    b
    g
    c
    g
    c
    g
    e
    d
    e
    d
    g
    c
    b
    c
    e
    g
    c
    d
    g
    c
    b
    e
    g
    e
    d
    c
    e
    f
    g
    e
    c
    g
    d
    g
    b
    g


Using some of the familiar techniques, we can count **pitches** and put them in a **series** or **DataFrame**:


```python
# counts pitches all voices, now as dictionary
pitches = [n.get('pname') for n in my_soup_file.find_all('note')]
counted = Counter(pitches)


counted_notes = pd.Series(counted).to_frame('count').sort_index()
counted_notes
```




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
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>277</td>
    </tr>
    <tr>
      <th>b</th>
      <td>227</td>
    </tr>
    <tr>
      <th>c</th>
      <td>262</td>
    </tr>
    <tr>
      <th>d</th>
      <td>410</td>
    </tr>
    <tr>
      <th>e</th>
      <td>209</td>
    </tr>
    <tr>
      <th>f</th>
      <td>216</td>
    </tr>
    <tr>
      <th>g</th>
      <td>332</td>
    </tr>
  </tbody>
</table>
</div>




```python
# count pitches in one voice:

measures = my_soup_file.find_all('measure')
pitches = []
# here we assume the superius is the first staff
superius_bars = [my_soup_file.find_all('staff', {"n": "1"}) for measure in measures]
for superius in superius_bars[0]:
    notes = superius.find_all('note')
    for note in notes:
        pitch = note.get('pname')
        pitches.append(pitch)
pitches_counted = Counter(pitches)
superius_pitch_count = pd.Series(pitches_counted).to_frame('count').sort_index()
superius_pitch_count

```




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
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>67</td>
    </tr>
    <tr>
      <th>b</th>
      <td>64</td>
    </tr>
    <tr>
      <th>c</th>
      <td>70</td>
    </tr>
    <tr>
      <th>d</th>
      <td>99</td>
    </tr>
    <tr>
      <th>e</th>
      <td>29</td>
    </tr>
    <tr>
      <th>f</th>
      <td>27</td>
    </tr>
    <tr>
      <th>g</th>
      <td>46</td>
    </tr>
  </tbody>
</table>
</div>



And create a histogram


```python
counted_notes.plot(kind="bar", figsize=(15, 10))
plt.title("Pitch Distribution in My piece")
plt.xticks(rotation = 0)
plt.xlabel("Tone")
plt.ylabel("Count")
plt.show()

```


    
![png](output_47_0.png)
    


#### Working with Measures

It is oftentimes useful to look at **measures** – either all at once or specific ones. Here's an example:


```python
# last pitch in last measure, for each voice
measures = my_soup_file.find_all('measure')
last_measure = measures[-1]
for staff in last_measure.find_all('staff'):
        note = staff.find_all('note')[-1]
        print(note.get('pname'))

```

    g
    d
    g
    b
    g


Working with **Score Definitions** (scoreDef), it is possible to search for certain **events** within the piece. For example, find out where a **Time Signature change** occurs:


```python
scoredefs = my_soup_file.find_all('scoreDef')
for scoredef in scoredefs:
    print(scoredef.get('meter.count'))
    print(scoredef.get('meter.unit'))
    next_measure = scoredef.find_next('measure', )
    print("The first bar with this TS is " + next_measure.get('n'))
```

    4
    2
    The first bar with this TS is 1
    8
    2
    The first bar with this TS is 71
    4
    2
    The first bar with this TS is 72
    8
    2
    The first bar with this TS is 134


Finally, we can look for some very specific things, like **all notes with a particular duration, pitch, and octave**:

* Use dictionary of key/value pairs to specify particular attributes.

>`my_soup_file.find_all('note', {'dur': "4", 'pname': "g", 'oct': '3'})`


```python

my_soup_file.find_all('note', {'dur': "4", 'pname': "g", 'oct': '3'})
```




    [<note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-323"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-421"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-635"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-1200"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-1503">
     <verse n="1" xml:id="m-1553">
     <syl con="d" wordpos="m" xml:id="m-1554">
                 bi
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-1544"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-2519"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="55" stem.dir="up" xml:id="m-2539">
     <verse n="1" xml:id="m-2601">
     <syl con="d" wordpos="m" xml:id="m-2602">
                 sa
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-2667">
     <verse n="1" xml:id="m-2719">
     <syl con="d" wordpos="i" xml:id="m-2720">
                 ro
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3073"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3074">
     <verse n="1" xml:id="m-3079">
     <syl con="d" wordpos="m" xml:id="m-3080">
                 li
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3198">
     <verse n="1" xml:id="m-3253">
     <syl con="d" wordpos="m" xml:id="m-3254">
                 li
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="55" stem.dir="up" xml:id="m-3375">
     <verse n="1" xml:id="m-3460">
     <syl con="d" wordpos="i" xml:id="m-3461">
                 con
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="55" stem.dir="up" xml:id="m-3379"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3409">
     <verse n="1" xml:id="m-3416">
     <syl con="d" wordpos="m" xml:id="m-3417">
                 li
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3878"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3911"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-3922"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-4032"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-4056"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-4819">
     <verse n="1" xml:id="m-4828">
     <syl con="u" wordpos="t" xml:id="m-4829">
                 na,
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-4906"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-5041"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-5188"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-5502"/>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="55" stem.dir="up" xml:id="m-6123">
     <verse n="1" xml:id="m-6131">
     <syl con="u" wordpos="t" xml:id="m-6132">
                 ta?
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-6193">
     <verse n="1" xml:id="m-6206">
     <syl con="u" wordpos="t" xml:id="m-6207">
                 ta,
                </syl>
     </verse>
     </note>,
     <note dur="4" dur.ppq="256" oct="3" pname="g" pnum="43" stem.dir="up" xml:id="m-6197"/>]



### 4.0 Display your MEI with Verovio

* Verovio will render your piece directly in the Notebook.  It's the same library we use for CRIM.


```python


my_piece_url
response = requests.get(my_piece_url)
fetched_mei_string = response.text
# start the verovio toolkit and load the file there
tk = verovio.toolkit()
tk.loadData(fetched_mei_string)
tk.setScale(30)
tk.setOption( "pageHeight", "1500" )
tk.setOption( "pageWidth", "3000" )

tk.redoLayout()
# get the number of pages and display the music
count = tk.getPageCount()
for c in range(1, count + 1):
    music = tk.renderToSVG(c)
    display(SVG(music))
```

    [Warning] Unsupported data.PERCENT '100'
    [Warning] Unsupported data.PERCENT '100'
    [Warning] Unsupported data.PERCENT '100'
    [Warning] Unsupported data.PERCENT '100'
    [Warning] Unsupported data.PERCENT '100'
    [Warning] Unsupported '<line>' within <measure>
    [Warning] Unsupported '<line>' within <measure>



    
![svg](output_55_1.svg)
    



    
![svg](output_55_2.svg)
    



    
![svg](output_55_3.svg)
    



    
![svg](output_55_4.svg)
    



    
![svg](output_55_5.svg)
    



    
![svg](output_55_6.svg)
    



    
![svg](output_55_7.svg)
    



    
![svg](output_55_8.svg)
    



    
![svg](output_55_9.svg)
    



    
![svg](output_55_10.svg)
    



    
![svg](output_55_11.svg)
    



    
![svg](output_55_12.svg)
    



    
![svg](output_55_13.svg)
    



    
![svg](output_55_14.svg)
    



    
![svg](output_55_15.svg)
    



    
![svg](output_55_16.svg)
    



    
![svg](output_55_17.svg)
    



    
![svg](output_55_18.svg)
    



    
![svg](output_55_19.svg)
    



    
![svg](output_55_20.svg)
    



    
![svg](output_55_21.svg)
    



    
![svg](output_55_22.svg)
    



    
![svg](output_55_23.svg)
    



    
![svg](output_55_24.svg)
    



    
![svg](output_55_25.svg)
    



    
![svg](output_55_26.svg)
    


### 5.0 Save Revised XML document


```python
# regular expression to get CRIM Piece Id from URL:
title = re.findall("[^\\|/]+$", my_piece_url)[0]
# Save with that CRIM ID as part of title
f = open(title + '_' + 'rev' + '.mei', "w")
f.write(str(soup_mei))
f.close()
```
