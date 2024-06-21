# Import libraries
import pandas as pd
from ydata_profiling import ProfileReport

# Read dataset
df = pd.read_csv('data/data.csv')

profile = ProfileReport(df)
profile.to_file(output_file="who_suicide_statistics.html")