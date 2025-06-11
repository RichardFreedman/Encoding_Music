# Introduction to Mermaid Diagrams in Markdown

**[Mermaid Markdown](https://mermaid.js.org/)** allows you to create diagrams and flowcharts in Markdown-style text. It can be a great tool for visually explaining your processes to the reader. Don't think of this as a coding tool to show your data visually like Plotly, rather a tool to explain your methods in your markdown cells. 


## How to Use Mermaid in Markdown

To create a Mermaid diagram, wrap your code block in triple backticks and specify `mermaid` as the language.
 
````
```mermaid
graph TD
  A[Start] --> B[Process]
  B --> C[End]
```
````

Important:
- Use a markdown cell, not a code or raw cell.
- Include three backticks at the top and bottom. Make sure they're backticks (`), not apostrophes (').
- Place "mermaid" touching the first three backticks, without a space.
- Make sure there are no special characters. Any attempt to write comments with # or include special characters in text boxes will result in an error.

You can choose the shape of each box:
- `[text]` = Rectangle
- `{text}` = Diamond
- `([text])` = Oval (stadium-shape)
- `[(text)]` = Cylinder
- `((text))` = Circle
- And many more. See a full list in the **[documentation](https://mermaid.js.org/syntax/flowchart.html)**.


### Common Diagram Types in Mermaid

| Diagram Type       | Mermaid Keyword    | Use Case Example                                 |
|--------------------|--------------------|--------------------------------------------------|
| Flowchart          | `graph TD`         | Visualize  steps                  |
| Pie Chart          | `pie`              | Show distributions                               |
| Sequence Diagram   | `sequenceDiagram`  | Illustrate sequences                             |
| Gantt Chart        | `gantt`            | Plan  timelines or schedules      |
| Class Diagram      | `classDiagram`     | Represent structures or  relationships |



## Example: Simple Data Flow for Music Analysis

````
```mermaid
graph TD   # Flowchart
  A[Spotify CSV] --> B[Load into pandas]
  B --> C{Tidy the data}    # Diamond Shape
  C --> D[(melt)]   # Cylinder
  C --> E((explode))   # Circle shape
  D --> F([Plot with Plotly])  # Oval / Stadium Shape
  E --> F

# DO NOT INCLUDE COMMENTS IN YOUR OWN CODE - IT WON'T RENDER!
```
````

```mermaid
graph TD
  A[Spotify CSV] --> B[Load into pandas]
  B --> C{Tidy the data}
  C --> D[(melt)]
  C --> E((explode))
  D --> F([Plot with Plotly])
  E --> F
```




## Example: Pie Chart of Audio Feature Importance

````
```mermaid
pie title Spotify Audio Feature Breakdown
  "Danceability" : 30
  "Energy" : 25
  "Valence" : 20
  "Liveness" : 15
  "Speechiness" : 10
```
````

```mermaid
pie title Spotify Audio Feature Breakdown
  "Danceability" : 30
  "Energy" : 25
  "Valence" : 20
  "Liveness" : 15
  "Speechiness" : 10
```

Though you have the ability to make pie charts in mermaid, you should use the Plotly library to make your actual data-backed visuals.



## Tips for Using Mermaid 

- You can include mermaid code directly in your markdown cells! Make sure the cell is markdown, not code.
- Use short, clear node labels to avoid clutter.
- Use `graph TD` for top-to-bottom diagrams, or `graph LR` for left-to-right.
- Use the `pie` chart for simple percentage-based data.
- Test and preview diagrams using the [Mermaid Live Editor](https://mermaid.live).
- Avoid special characters. In our first example, if we wrote melt() instead of melt, it would have thrown an error.
- View the Mermaid Markdown tutorials page [here](https://mermaid.js.org/ecosystem/tutorials.html).
