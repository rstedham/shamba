# SHAMBA guides

## End User guide

### Important note

>Before using Shamba, you need to follow the Developer guide first.

### Introduction

Shamba can be used as:

* a command line application
* a GUI application

>Disclaimer : The two applications do not cover the same capabilities. The command line version offers more features.

### Shamba Command line application

To start the command line application, run the `shamba_cl_.py` Python script from Anaconda prompt with the appropriate environment set.

### Shamba Graphical User Interface application

To start the application, run the `shamba.pyw` Python script from Anaconda prompt with the appropriate environment set.

When SHAMBA is launched, it will open a window containing a disclaimer about the SHAMBA tool. You must first accept this disclaimer before being able to use the tool. After accepting the terms, you will arrive at the main interface for shamba. There are four tabs: when starting any new SHAMBA project, the information in the “General” tab must first be filled out. Baselines and interventions can then be specified in the “Baselines” and “Interventions” tabs respectively. The “Mitigation Estimates” tab then allows you to plot the yearly greenhouse gas emissions for a baseline-intervention pair and calculates the mitigation estimates for that intervention.

#### General Project Information

General project information (such as location and climate) must first be specified before the rest of the SHAMBA tool can be used. In the “General” tab, click the “Enter general project information” button. A new window labelled “General Information” will appear, which contains several screens with information to enter regarding your project.

The screens can be navigated using the “Next” and “Back” buttons at the bottom of the window, and clicking the “Help” button will bring up a pop­up window with more information about the current screen. It is important to note that the screens must all be completed in order for the information to be saved. That is, you will lose all information entered if you close the window via the close button (the x in the top corner) instead of the “Save” button on the last screen. You are also advised to review all entered information before clicking “Save” since, once saved, the information cannot be edited (only overwritten).

Once the information has been saved, the program will return to the main interface. In the “General” tab you will see a text summary of the information that was entered in the other window. If the information was not entered correctly, it can be overwritten by simply pressing the “Enter general project information button” again and going through the process again. Otherwise, you are now free to move on to the “Baselines” and “Interventions” tabs.

Since this general information is used to do calculations on the baseline scenarios and interventions, it cannot be changed after creating any baselines or interventions. It is thus crucial to ensure that this information is accurate before moving on to the steps outlined in Section 2.3.

#### Baselines and Interventions

In the “Baselines” and “Interventions” tabs of the main interface, you can add information regarding the baseline scenarios and interventions in your project. To do this, click on the “Add new baseline” or “Add new intervention” button.

After entering the name of the baseline/intervention you wish to create, you will then be taken to a new window similar to the “General information” window. After providing all the required information and saving it, you will then see a text summary of the baseline/intervention in the appropriate tab of the main interface.

Multiple baselines and interventions can be created in the same manner, and the drop­down lists at the top­left of the “Baselines” and “Interventions” tabs allow you to see details about each baseline/intervention that has been created.

#### Mitigation Estimates

Once at least one baseline and one intervention have been created, you can then use the “Mitigation Estimates” tab to plot the greenhouse gas emissions/removals associated with each, and see the net impact (mitigation estimates) associated with the intervention. Simply select which baseline and intervention you would like to plot from the drop-down lists, then click the “Plot mitigation estimates” button. This can be repeated for any baseline-intervention combination, and you can also continue to define new baselines and interventions; any new additions will be automatically displayed in the drop­down lists.

#### Miscellaneous

##### Saving the Project

You can save your SHAMBA project (all raw data and calculations) to .csv files by pressing “Save” in the file menu at the top-left of the screen (or with ctrl+s on the keyboard). If this is the first save for the project, you will be prompted to enter a name/location for the save folder. If you have previously saved this project, the tool will automatically add any new information to the folder you selected already - you can specify a new save folder by using the “Save As” option.

##### Loading an Existing Project

Unfortunately, the SHAMBA tool cannot load an existing project (yet). Saved project data can be imported into Excel, Python, R, and many other tools, however, since it is all in .csv format.

## Developer guide

### Operating system

Shamba is written using Python so it is supported to run both on Linux and Windows platforms.

### Python

Shamba is compatible and has been tested on Python 2.7 version only.
If somebody wants to invest some time on making it works with version 3.x please contact us.

### Recommended tools

We recommend to:

* use Anaconda as package manager
* use Spyder version 3.3.6 to run the program (either CL and GUI)
* use Anaconda virtual environment to isolate your Shamba Python environement


### Installation procedure with Miniconda

Procedure:

1. download Miniconda on the official [website](https://docs.conda.io/en/latest/miniconda.html)

2. create a virtual environment with Python 2.7 using Conda command prompt:
`conda create -n myenv python=2.7`

3. activate the virtual environment:
`conda activate myenv`

4. Install those packages which Shamba depends on, using conda prompt:
   1. [basemap](https://anaconda.org/conda-forge/basemap): `conda install -c conda-forge basemap`
   2. [gdal](https://anaconda.org/conda-forge/gdal): `conda install -c conda-forge gdal`
   3. [scipy](https://anaconda.org/conda-forge/scipy): `conda install -c conda-forge scipy`
   4. [pandas](https://anaconda.org/conda-forge/pandas): `conda install -c conda-forge pandas`
   5. [pyqt5](https://anaconda.org/conda-forge/pyqt): `conda install -c conda-forge pyqt`
   6. [numpy](https://anaconda.org/conda-forge/numpy): `conda install -c conda-forge numpy`

### Installation procedure with Anaconda

Procedure:

1. install [Anaconda](https://www.anaconda.com/products/individual) latest version available. **choose to install Python 2.7 along Anaconda**

2. create a virtual environment named "shamba" for example. Choose Python 2.7 version. From Anaconda prompt : `conda create --name myenv`

3. add conda forge channel to your environment using the following command line: `conda config --add channels conda-forge`

4. Install Spyder 3.3.6 application from Anaconda with Anaconda Navigator. Install Spyder after ensuring you selected the newly created environment in the "Application" tab.

5. From the Anaconda prompt we are now going to install all Shamba dependencies. Please open the Anaconda prompt and install the following librairies in the newly created environment:
    1. gdal v2.2.2 : `conda install gdal`
    2. x matplotlib v2.2.3 : `conda install matplotlib`
    3. basemap 1.2.0 see <https://matplotlib.org/basemap/users/download.html> : `conda install basemap`
    4. pandas 0.24.0 : `conda install pandas`
    5. x numpy 1.16.6 : `conda install numpy`
    6. x scipy 1.2.1 : `conda install scipy`
    7. PyQt 5.6.2 : `conda install pyqt=5`

### Anaconda tips

#### Activate an environment from the Anaconda prompt

Type the following command with `myenv` being your environment name.

`conda activate myenv`

If you have more needs [please refer to Anaconda web site documentation here.](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

#### Install libray from Anaconda prompt

`conda install library-name`

If you have more needs [please refer to Anaconda web site documentation here.](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/)