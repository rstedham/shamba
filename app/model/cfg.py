#!/usr/bin/py

"""Module for global variables for all of SHAMBA."""

import os
from time import gmtime,strftime
import uuid
import pathlib

# input and output files for specific project
# change this for specific projects
DATA_DIR = os.path.join(pathlib.Path().absolute(), 'data')
PROJ_DIR = os.path.join(DATA_DIR, 'projects')
PROJECT_NAME = 'shamba-sample'

# no need to specify SAV, INP, OUT directories if specified in cl file
SAV_DIR =  os.path.join(PROJ_DIR, PROJECT_NAME)
INP_DIR = os.path.join(SAV_DIR, 'input')
OUT_DIR = os.path.join(SAV_DIR, 'output')

# raster data
CLIMATE_RASTER = os.path.join(DATA_DIR, 'default-data', 'raster', 'climate')
SOIL_RASTER = os.path.join(DATA_DIR, 'default-data', 'raster', 'soil')
# default input
DEFAULT_INPUT = os.path.join(DATA_DIR, 'default-data', 'default-input')

# For holding command-line arguments
args = []

# Number of years for model to run and accounting period
# NOTE: change this in main after tree max age data is read
# no need to specify years if specified in cl file
N_YEARS = 30
N_ACCT = 30

# Save the time (that cfg is imported) and generate 
# universally unique identifier (uuid) for the project

# convert seconds since the epoch to an ISO-8601 time in UTC
TIME = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
ID = uuid.uuid4().hex

