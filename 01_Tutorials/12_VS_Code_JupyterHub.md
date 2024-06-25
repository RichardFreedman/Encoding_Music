# Connecting Visual Studio Code to the Encoding Music JupyterHub Server

To run code in Jupyter Notebooks in VS Code, you need to have an environment set up with the right version of Python and all the necessary libraries installed. One easy way to do this is connecting directly to the Encoding Music JupyterHub server, which already has a fully set up environment.

## Install Jupyter Extension

If you haven't already, first install the Jupyter Extension in VS Code.

### Open the Extensions Menu

![Alt text](images/vs_jupyter_extension1.png)

### Search for Jupyter in the Extensions Marketplace

![Alt text](images/vs_jupyter_extension2.png)

### Install the Jupyter Extension

![Alt text](images/vs_jupyter_extension3.png)

## Connecting to the Encoding Music JupyterHub Server

First, open up a Jupyter notebook. If you don't already have one, you can create a new `.ipynb` file. Click on the "Select Kernel" button.

![Alt text](images/vs_jupyterhub1.png)

Then press "Select Another Kernel"

![Alt text](images/vs_jupyterhub2.png)

Press "Existing Jupyter Server"

![Alt text](images/vs_jupyterhub3.png)

Enter the **full** URL of the Encoding Music JupyterHub server, `https://encodingmusic.crimproject.org`

![Alt text](images/vs_jupyterhub4.png)

You should install the JupyterHub extension if prompted.

![Alt text](images/vs_jupyterhub5.png)

When prompted, enter your username and password for the Encoding Music server. You can then select the Encoding Music kernel, called "Python 3 (ipykernel).