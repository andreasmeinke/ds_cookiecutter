# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter //input repo url!!!


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── README.md           <- The top-level README for developers using this project.
├── requirements.txt    <- The basic requirements from which the environment can be built.
├── docker-compose.yaml
├── Dockerfile          <- Central Dockerfile for the Data Science Project. Ready for
│                          Deployment from the beginning.
│
├── app                 <- App Folder which defines the Application.
│   ├── __init__.py
│   ├── main.py         <- Main Function for the Microservice Application.
│   ├── settings.py     <- Setting File for the Mircroservice which shows Input and Output 
│   │                      for the application interface.
│   ├── models          <- Defines Input and Output Parameters.
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers         <- 
│   │   ├── __init__.py
│   │   └── ds_api
│   │       ├── __init__.py
│   │       └── ds_api.py
│   └── tasks           <- Subtasks which are part of the applications.
│       ├── __init__.py
│       └── load_models <- Basic Task which loads a ML Model.
│           ├── __init__.py
│           └── load_models.py
│
├── code                <- Experiment Code from the Start of the Project.
│   ├── archive         <- Outdated Code, which will not be part of the Project.
│   ├── dev/prototype   <- Work in Progress Experiments.
│   └── main            <- Experiments which are part of the result.
│
├── data                <- Storage for Data and Scripts to download or create data.
│   ├── archive
│   ├── interim
│   ├── processed
│   │   ├── exploration
│   │   └── training
│   └── raw             <- Raw Data either from Application or Source 
│       ├── application <- Data that comes from the Application and can be used for 
│       │                  Continuous Learning approaches.
│       └── source      <- Source Data that comes from the Customer and is part of 
│                          the project start.
│
├── reports             <- Data Visualization and Data Reports that are part of the Project.
│   ├── analysis        <- Definite Analysis based on Project Data.
│   └── figures         <- Diagrams based on the Project Data.
│
├── src                 <- Source Code which will be part of the Microservice and Modularized.
│   ├── data            <- Data that will be used in the Microservice.
│   ├── features        <- Deployment ready code which are core of the Application.
│   ├── models          <- ML Models which are used in the Application.
│   └── visualization   <- Code that creates Visualizations. 
│
└── test                <- Module Tests which starts with Mock Input Data.
    └── __init__.py
```

### Create new Python Environment
------------
    
    python3 -m venv <environment-name>

### Activate new Python Environment
------------

    source <environment-name>/bin/activate


### Installing development requirements
------------

    pip install -r requirements.txt

