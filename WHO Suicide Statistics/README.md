# WHO Suicide Statistics Analysis

This project analyzes global suicide statistics using data from the World Health Organization (WHO). It includes data cleaning, exploratory data analysis (EDA), demographic analysis, geographical analysis, and visualization of suicide rates by country.

## Project Structure

```
WHOSuicideStatistics/
├── data/
│   ├── data.csv
│   └── who_suicide_statistics.csv
├── DCT.ipynb
├── Demographic Analysis.ipynb
├── EDA.ipynb
├── Geographical Analysis.ipynb
├── main.py
├── README.md
├── requirements.txt
├── suicide_rates_map.html
├── Trend Analysis.ipynb
└── who_suicide_statistics.html
```

## Setup and Installation

1. Clone this repository:
   ```
git clone https://github.com/Mohammed-Mebarek-Mecheter/EDA-with-Python.git
   ```

2. Navigate to the project directory:
   ```
cd WHO-Suicide-Statistics
   ```

3. Install the required dependencies:
   ```
pip install -r requirements.txt
   ```

## Usage

1. Data Cleaning and Transformation (DCT.ipynb):
   - Reads the raw dataset
   - Standardizes country names
   - Handles missing values
   - Converts categorical columns to appropriate data types
   - Saves the cleaned dataset

2. Exploratory Data Analysis (EDA.ipynb):
   - Generates a comprehensive data profile using ydata-profiling
   - Explores dataset characteristics and distributions

3. Demographic Analysis (Demographic Analysis.ipynb):
   - Analyzes suicide rates across different demographic groups

4. Geographical Analysis (Geographical Analysis.ipynb):
   - Visualizes suicide rates by country using folium

5. Trend Analysis (Trend Analysis.ipynb):
   - Examines trends in suicide rates over time

## Main Script

The `main.py` script generates a detailed profile report of the dataset using ydata-profiling:

```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/data.csv')
profile = ProfileReport(df)
profile.to_file(output_file="who_suicide_statistics.html")
```

## Results

- The cleaned dataset is saved as `who_suicide_statistics.csv`
- A comprehensive data profile is generated as `who_suicide_statistics.html`
- An interactive map of global suicide rates is created as `suicide_rates_map.html`

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## Acknowledgments

- World Health Organization for providing the dataset

## Author

- Name: [Mohammed Mebarek Mecheter](https://www.linkedin.com/in/mohammed-mecheter/)
- Email: mohammedmecheter@gmail.com
- Portfolio: [Mebarek](https://mebarek.pages.dev/)

Feel free to contact me for any questions or additional information about this project.