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

├── app
│   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── ds_api
│   │       ├── __init__.py
│   │       └── ds_api.py
│   ├── tasks
│   │   ├── __init__.py
│   │   └── load_models
│   │       ├── __init__.py
│   │       └── load_models.py
├── code
│   ├── archive
│   ├── dev/prototype
│   ├── main
├── data
│   ├── archive
│   ├── interim
│   ├── processed
│   │   ├── exploration
│   │   └── training
│   ├── raw
│   │   ├── application
│   │   └── source
│   ├── reports
│   │   ├── analysis
│   │   └── figures
│   ├── src
│   │   ├── data
│   │   ├── features
│   │   ├── models
│   │   └── visualization
│   ├── test
│   │   └── __init__.py



├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
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

