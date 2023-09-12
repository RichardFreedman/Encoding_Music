# Using Jupyter Notebooks and Pandas to Work with Data

## Introduction

**Jupyter Notebooks** allow anyone to run Python code in any browser, without the need to use the terminal or command line. The notebooks are saved with the `ipynb` extension. Notebooks are organized as 'cells', which can be commentary (static, written in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)), or Python code (which produce dyanmic output).  

**Navigate between cells** with the arrow keys on your computer, or just click in the cell you want to edit or run. 

To **run an individual cell**, use the arrow/run command at the top of the Notebook, or just press Shift + Enter on your keyboard.

The **sequence in which cells have been run** is tracked in the space to left of individual cells.  The succession often matters, since one cell will use the state of a variable or dataframe that has been created in a previous one.  This is important, since it is possible to alter in a subsequent cell something that has been established in a previous one.

It is also good practice to **copy and rename** any notebook you work on in order to preserve the original version of it.  See more below to learn how.

## Run the Notebooks in a Browser or VS Code

There are several ways to run, edit, and create notebooks. Students in Encoding Music can use the [Jupyter Hub](https://encodingmusic.haverford.edu/) created especially for this course. Log on with your **full Haverford user id** (including @haverford.edu and password--students from Bryn Mawr College will be given a special user account).  You *must* be on the Haverford College network, or VPN!

![Alt text](<images/nb 1.png>)

Your screen should  look like this on first log in.  You will always use the Encoding Music kernel (which is our Environment, including all required Python libraries)

![Alt text](<images/nb 23.png>)

You can also run the Notebooks in a local installation of Jupyter or VS Code on your own computer.  See [this guide](https://github.com/RichardFreedman/Encoding_Music/blob/main/01_Tutorials/02_VS_Code_Google_Collab.md) to learn how.


## First Steps:  Create a Folder, Create Your First NB

There will be times when we share certain draft Notebooks that you can adapt. These can be uploaded into this space from your computer or a URL link.

But in general you will **create your own notebook**, adding modular code found in the Encoding Music tutorials.



## The Kernel

Your notebook will only correctly if it is operating on the correct "Kernel", which is a version of Python (complete with all the relevant dependencies) that is available on the server or machine.  

In the Jupyter Hub you will always want to be sure that you are using the **Encoding Music** kernel!  From the Encoding Music hub, start the correct Kernel as shown here:

![Alt text](<images/nb 2.png>)

If your notebook will not work after opening it, you might want to **double check that you are on the Encoding Music Kernel**, as shown here:

![Alt text](<images/nb 8.png>)

If your Notebook becomes unresponsive, or you are simply stuck in some other way, one solution is to "Restart the Kernel" and begin again from the top.  Look for the "Kernel" menu or function.

## Make a Folder, Create a Notebook

You will want to make a folder for your work, and perhaps different folders for different assignments or projects.  Right+click to rename, delete, etc.

![Alt text](<images/nb 24.png>)

Now you can create a Notebook within that Folder.  Right+click will also allow you to move, rename, and export.

![Alt text](<images/nb 25.png>)

### Remember:  Always use the Encoding Music Kernel!

![Alt text](<images/nb 26.png>)

## Viewing and Saving Charts and Graphics

Normally, in the Encoding Music version and your local Anaconda Jupyter, all charts, graphs, and notation should render directly in the output cells for each code block.

In a local VS-Code version of the notebook, you might find that graphs and charts are saved to your working folder (at the left) as `.png` or `.html` files.  You will need to open these in a browser or other viewer.

If you would like to save a chart or graph to reuse in another publication (such as Google Slides or Docs), there are various solutions:

In the **Encoding Music** hub version of Jupyter, `right-click` on output of the cell in question, then select `copy to clipboard`.  Now you can paste this image directly into some other document.  The process is the same if you are running notebooks **locally in Anaconda Jupyter** 

![Alt text](<images/nb 19.png>)

In a local **Anaconda VS-Code** put your cursor in the output area of the cell (near the image).  You will then see three icons--the one on the right is to "Save" the image.  Follow the dialogue to name and save the PNG file, then use it some other document.

![Alt text](<images/nb 20.png>)

![Alt text](<images/nb 21.png>)

## Saving DataFrames as CSV Files (and Loading Datframes from CSV)

Dataframes can be saved as CSV files, which provide a good way of reusing them in other projects.  For instance a df called `beatles_hits` could be saved with:

	`beatles_hits.to_csv('beatles_hits_output.csv')`

Note that you must include `.csv` as part of name of the file, and that you must provide a name for the file in quotation marks.

Conversely, it's easy to *load* a csv file as a dataframe.  Either provide a url (such as the raw version of a github file, or a shared csv from Google drive), or a local path to the file on your computer). For example:

Name the file path some simple variable, then use `pd.read_csv` to import to Pandas:

We give the URL of the CSV file a name (simply for convenience), then pass that name to the `read_csv('source_file_name')` method, and name the resulting data frame.

```
beatles_spotify_csv = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCv45ldJmq0isl2bvWok7AbD5C6JWA0Xf1tBqow5ngX7_ox8c2d846PnH9iLp_SikzgYmvdPHe9k7G/pub?output=csv'

beatles_spotify = pd.read_csv(beatles_spotify_csv)

```

## Copy, Save, and Download Notebook

It's a good idea to make a Copy of your Notebook before you run or edit it.  Rename with "_dev" at the end, for instance, so you can distinguish it from the original.

In the **Encoding Music** hub version of Jupyter, `right-click` on the NB file, then pick "Duplicate".  Note that you can follow the same menu to `Download` your Notebook as ipynb to share or submit.

![Alt text](<images/nb 12.png>)

If you are running notebooks **locally in Anaconda Jupyter**, then `File>DownloadAs>Notebook`:

![Alt text](<images/nb 13.png>)

In a local **Anaconda VS-Code** you can simply find the ipynb file on your computer and copy or share it from there.

## Export to HTML or PDF

Saving your Notebook as HTML or PDF is the only way to share your work outside of the Jupyter environment. The process of creating HTML or PDF is slightly different (but equally tedious) in each platform.

From the **Encoding Music** hub or **Local Jupyter (on Anaconda)**, follow `File>Download` (or `File>DownloadAs`) and select **HTML** as the format.  Be sure to select HTML and *not* any of the PDF formats, which will not work! This will be saved to the 'downloads' area on your computer. Next,open the file in a browser, then use the `Print` dialogue to save it as PDF.  Be sure to name it according to the conventions!


![Alt text](<images/nb 14.png>)

From Local VS-Code (on Anaconda), look for the 'three dots' at the top right of your Notebook, then pick `Export`:


![Alt text](<images/nb 15.png>)

Now from the Export menu select 'HTML' (PDF will not work!). The HTML will be saved to the 'downloads' area on your computer. Open the file in a browser, then use the `Print` dialogue to save it as PDF.  Be sure to name it according to the conventions!

![Alt text](<images/nb 16.png>)










