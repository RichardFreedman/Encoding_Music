# AI Tutorial: Structured Output with LangChain 

In your previous labs, you’ve worked with **structured data** — tidy CSV files with neat columns. In this tutorial, we’ll learn how to take **unstructured text** (like a scanned play) and turn it into structured data you can analyze with pandas.

We’ll use **Pydantic** to define exactly what we want the LLM to return, and **LangChain** to call the model in a way that enforces this structure. This is like telling the model: *“Here’s the table I want you to fill out — exactly in this shape.”*

---

## Step 0: Decide What You Want Back (Your Schema)

Before writing any code to process the text, we design our “table” — the fields we want for each musical moment. We do this with a Pydantic `BaseModel`.

**Why this matters:**

- Fields are the columns in your output.
- `description=` tells the LLM *exactly what to look for and where to find it in the text*.
- The model **must** return your type — or you’ll get a clear validation error.

**Think of it like:** Creating the header rows of your Pandas DataFrame before collecting any data.

**Pydantic quick-start:** If you’ve only used pandas so far, think of a `class` like a named set of columns. Pydantic adds *validation* to make sure the model fills those columns with the right data types.

Example schema for this project - notice that for act, we tell it *what it is*, and *where to find it* as mentioned above:

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class MusicalMoment(BaseModel):
    act: int = Field(description="Act number where this moment occurs — labeled at the top of the act or scene")
    scene: int = Field(description="Scene number where this moment occurs — labeled at the top of the scene")
    number: int = Field(description="Order of the musical moment in the scene (1, 2, 3...) ")
    characters: List[str] = Field(description="Name(s) of character(s) performing")
    dramatic_situation: str = Field(description="Brief description of what’s happening dramatically")
    air_or_melodie: str = Field(description="Title of the song (air/mélodie) as labeled in the text")
    poetic_text: str = Field(description="Only the sung words — no stage directions")
    rhyme_scheme: str = Field(description="Pattern of rhymes, e.g., AABB")
    poetic_form: str = Field(description="Form or structure, e.g., verse + refrain")
    end_of_line_accents: List[str] = Field(description="For each line: masculine or féminine")
    syllable_count_per_line: List[int] = Field(description="Number of syllables per line; watch for contractions/dialect")
    irregularities: Optional[str] = Field(description="Oddities or exceptions")
    stage_direction_or_cues: Optional[str] = Field(description="Stage directions or cues linked to the song")
    reprise: Optional[str] = Field(description="If it’s a reprise of an earlier number")

class VaudevillePlay(BaseModel):
    musicalMoments: List[MusicalMoment]
```

---

## Step 1: API Key, Model, and Prompt

Just like when you used the Spotify API key earlier in the course, you’ll need an OpenAI API key. It is super important not to paste the key into your python code. Rather, you should store it on your computer or server. See the API Tutorial for more information on how to acquire and store your key.

Next, we choose our chat model. For more complex tasks, choose a model like gpt-4o or gpt-5o. For simpler tasks, a model like gpt-4o-mini or gpt-5o-mini will do just fine, and costs a fraction of the price. 

Then, we create our system prompt. This step is *super* important. The system prompt tells the LLM who it is, and what its job is. 

```python
# Setting up our API Key
import getpass, os
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Choosing our chat model
llm = init_chat_model("gpt-4o", model_provider="openai")

# Binding the LLM to our desired output "table"
structured_llm = llm.with_structured_output(VaudevillePlay)

# Setting up our prompt - telling the LLM what it's job is
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a literary analyst of French Vaudeville. Return a VaudevillePlay object with all musical moments."),
    ("human", "Context:\n{context}\n\nExtract all musical moments.")
])
```

---

## Step 2: Load the Play Text

We’ll use LangChain’s PDF loader to read the file into a `Document`. This essentially saves our document as a python variable that we can reference to easily pass in as context.

By default, it loads it as a list of pages. If you want to use this as the natural split, ignore the last two lines of code. Otherwise, you can merge the pages together into one variable (`doc`). 

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

loader = PyPDFLoader("/path/to/play.pdf")
pages = loader.load()
full_text = "".join(p.page_content for p in pages)
doc = Document(page_content=full_text)
```

---

## Step 3: Optional — Split up your document

LLM's begin to struggle with too much content. Thus, if your document is more than a few pages, you need to split it up and pass it to the LLM as chunks. Most of the time, you can use LangChain's `RecursiveCharacterTextSplitter`. With this splitter, you can simply choose an arbitrary number of characters for each chunk. See more about it in the Retrieval Augmented Generation Tutorial.  Or, you could use the natural page breaks that occur when you load your document (LangChain's PDF loader returns a list of pages, rather than one large string).

&#x20;

In our case, we have to be really sure we don't split our text in the middle of a musical moment. Thus, we break it up into scenes. To do this, we use a mini structured output app (Yes, we used a structured output app within our structured output app) to have an LLM figure out how each scene is labeled. Then we can go through the whole text and split on each of these headers. This is pretty complex, so if you don't understand what's going on in the cell below, don't worry. 

```python
class Scene(BaseModel):
    act: int = Field(description="Act number as labeled in text")
    scene: int = Field(description="Scene number as labeled in text")
    header: str = Field(description="Exact scene header line, verbatim")

class FullPlay(BaseModel):
    all_scenes: List[Scene]
```

```python
scene_splitter_llm = llm.with_structured_output(FullPlay)
scene_index = scene_splitter_llm.invoke(f"Identify all scene headers in:\n{full_text}")

scene_docs = []
prev_end = 0
for i, sc in enumerate(scene_index.all_scenes):
    start = full_text.find(sc.header, prev_end)
    if i + 1 < len(scene_index.all_scenes):
        next_start = full_text.find(scene_index.all_scenes[i+1].header, start)
        end = next_start if next_start != -1 else len(full_text)
    else:
        end = len(full_text)
    scene_docs.append(Document(page_content=full_text[start:end], metadata={"act": sc.act, "scene": sc.scene, "header": sc.header}))
    prev_end = end
```

If you skip this step, it may be helpful to put your document into a single-item list, since the rest of the framework is built to work with a list of document chunks: `scene_docs = [doc]`

---

## Step 4: Extract Musical Moments

We now loop over each scene (or the whole play if not splitting) and run the model. You can set up a more complicated system with `LangGraph` if desired, but this is the simplest form. 

```python
all_moments = []
for scene in scene_docs:
    msg = prompt.invoke({"context": scene.page_content})
    result = structured_llm.invoke(msg)
    all_moments.extend(result.musicalMoments)
```

---

## Step 5: Convert to a Pandas DF

```python
import pandas as pd

df = pd.DataFrame([m.model_dump() for m in all_moments])

# Optionally, turn it into a CSV to export.
df.to_csv("vaudeville_moments.csv", index=False)
```

You can then export it as a CSV, if you want a spreadsheet of data. Or, start looking into your new structured data with Pandas.

```python
# Top characters by appearances
df.explode("characters")["characters"].value_counts().head()
```

---



**Helpful links:**

- Langchain Structured Output: [https://js.langchain.com/docs/concepts/structured\_outputs/](https://js.langchain.com/docs/concepts/structured_outputs/)
- Full Vaudeville Structured Output Notebook: [https://cwcross.github.io/Encoding-Music-Summer-2025/Vaudeville/Vaudeville\_structured.html](https://cwcross.github.io/Encoding-Music-Summer-2025/Vaudeville/Vaudeville_structured.html)


## Credits and License

Resources from **Music 255:  Encoding Music**, a course taught at Haverford College by Professor Richard Freedman.

Special thanks to Haverford College students Charlie Cross, Owen Yaggy, Harrison West, Edgar Leon and Oleh Shostak for indispensable help in developing the course, the methods and documentation.

Additional thanks to Anna Lacy and Patty Guardiola of the Digital Scholarship team of the Haverford College libraries, to Adam Portier, systems administrator in the IITS department, and to Dr Daniel Russo-Batterham, Melbourne University.

This work is licensed under CC BY-NC-SA 4.0 
