# Encoding Music: Setting Up a Local Environment with Miniconda

Normally we will complete all assignments via the class [Jupyter Hub](https://encodingmusic.crimproject.org) using your assigned login.

But it is also possible to run all our notebooks (and also develop your own ideas) **on your own computer**. The steps below will show you how using **Miniconda** — a lightweight alternative to the full Anaconda Navigator that gives you the same core tools with a smaller footprint.

Why **conda**?  Because it helps us managed **virtual environments** were we can install specified **Python requirements** for our project.  CRIM Intervals (and related software we use) require **specific versions** of individual libraries:  **dependencies** as they are called.  A **virtual environment** (also called `venv`) is the way to keep things clean, and avoid **dependency conflict**.   


Before doing anything else, check whether you have conda already installed!

Open a new terminal and type: `conda --version`.  If conda is already installed you should see something like `conda 24.5.0`

If you see this, then SKIP STEP 1 and go on to STEP 2!

---

## Step 1: Install Miniconda

**NOTE!  Remember to check whether you **already have conda** on your computer!**



Miniconda is a minimal installer that gives you Python and the `conda` package manager without the full Anaconda suite. Download the correct installer for your operating system from the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).

### On macOS

Download the correct installer for your Mac. If you have an **Apple Silicon** Mac (M1, M2, M3), use the `arm64` version. If you have an older **Intel** Mac, use the `x86_64` version. When in doubt, go to **Apple menu > About This Mac** to check.

Open a Terminal window and run:

```bash
# Apple Silicon (M1/M2/M3)
# downloads
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
# now installs
bash Miniconda3-latest-MacOSX-arm64.sh

# Intel Mac
# this downloads
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# and this installs
bash Miniconda3-latest-MacOSX-x86_64.sh
```

Follow the prompts. When asked **"Do you wish the installer to initialize Miniconda3?"**, type `yes`. This is important — it configures your shell so that `conda` commands work in any terminal window.

When the installer finishes, close your Terminal and open a new one for the changes to take effect.

### On Windows

Download the **Windows 64-bit** `.exe` installer from the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html) and run it.

During installation, on the **Advanced Options** screen, check the box for **"Add Miniconda3 to my PATH environment variable"**. This allows you to use `conda` from a standard terminal. Then complete the installation.

After installation, open a new **Command Prompt** or **PowerShell** window and run:

```powershell
conda init powershell
```

Close and reopen the window. You should now see `(base)` at the start of your prompt, confirming conda is active.

### Verify the Installation

On either platform, confirm that conda is working:

```bash
conda --version
```

You should see something like `conda 24.x.x`.

---

## Step 2: Create a New Virtual Environment

A virtual environment keeps your Encoding Music libraries separate from anything else on your computer, ensuring the right versions of everything are installed without interfering with other projects.

Run the following in your terminal (Mac) or Command Prompt / PowerShell (Windows):

```bash
conda create -n encoding_music python=3.10
```

This creates an environment named `encoding_music` running Python 3.10. The name can be anything you like — just avoid spaces.

When prompted **"Proceed ([y]/n)?"**, type `y`.

---

## Step 3: Activate the Environment

You need to activate the environment before installing anything or running notebooks. You will do this every time you start a new session.

```bash
conda activate encoding_music
```

Your prompt will change to show the environment name in parentheses:

```
(encoding_music) your-computer-name ~ %
```

---

## Step 4: Install JupyterLab and VS Code Support

With the environment active, install JupyterLab and the kernel support needed to run notebooks in VS Code:

```bash
conda install -c conda-forge jupyterlab ipykernel
```

---

## Step 5: Install the Encoding Music Libraries

Now install the Encoding Music libraries and all their dependencies directly from GitHub:

```bash
pip install git+https://github.com/RichardFreedman/Encoding_Music.git
```

This may take a minute or two — you will see a long stream of output as packages are downloaded and installed. When the prompt returns, the installation is complete.

> **Note on LLM Tools:** Some of the dependencies used by our LangChain system for working with LLMs and OpenAI differ from those in the main Encoding Music tools. You may need to create a separate virtual environment for those notebooks. Follow the same steps above with a different environment name, such as `encoding_music_llm`.

---

## Step 6: Get the Notebooks

Download the Encoding Music notebooks from GitHub. Go to the [Encoding Music repository](https://github.com/RichardFreedman/Encoding_Music), click the green **Code** button, and select **Download ZIP**. Unzip the folder somewhere convenient on your computer.

Alternatively, if you use Git, you can clone the repository:

```bash
git clone https://github.com/RichardFreedman/Encoding_Music.git
```

Either way, it's good practice to **rename any notebook you plan to edit** (for example, add your initials as a suffix) so you don't overwrite the original.

---

## Step 7: Run a Notebook

### In JupyterLab

With your environment active, launch JupyterLab from the terminal:

```bash
jupyter lab
```

This opens JupyterLab in your browser. Navigate to the folder where you saved the notebooks and open one to get started.

### In VS Code

If you prefer VS Code, install it from [code.visualstudio.com](https://code.visualstudio.com) if you haven't already. Then open VS Code, open the folder containing your notebooks, and open any `.ipynb` file.

The first time you open a notebook, VS Code will ask you to select a **kernel**. Choose the interpreter that includes `encoding_music` in its path — this tells VS Code to use the environment you just created.

You may also be prompted to install the `ipykernel` extension the first time — go ahead and do so. You may also find the **Live Preview** extension useful for rendering figures and network diagrams.

---

## Useful conda Commands for Reference

```bash
# See all your environments
conda env list

# Activate your environment
conda activate encoding_music

# Deactivate when you're done
conda deactivate

# Update a package
conda update <package-name>

# Remove an environment entirely
conda remove -n encoding_music --all
```

---

## Credits and License

Resources from **Music 255: Encoding Music**, a course taught at Haverford College by Professor Richard Freedman.

Special thanks to Haverford College students Charlie Cross, Owen Yaggy, Harrison West, Edgar Leon and Oleh Shostak for indispensable help in developing the course, the methods and documentation.

Additional thanks to Anna Lacy and Patty Guardiola of the Digital Scholarship team of the Haverford College libraries, to Adam Portier, systems administrator in the IITS department, and to Dr Daniel Russo-Batterham, Melbourne University.

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
