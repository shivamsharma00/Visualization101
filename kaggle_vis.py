import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Set up code checking
import os
if not os.path.exists("../input/fifa.csv"):
    os.symlink("../input/data-for-datavis/fifa.csv", "../input/fifa.csv")  
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex1 import *
print("Setup Complete")

# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Check your answer
step_2.check()

