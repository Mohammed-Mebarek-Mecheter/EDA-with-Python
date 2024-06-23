# New York City Public School SAT Performance Analysis

## Introduction
This project explores the SAT (Scholastic Assessment Test) performance of public schools within New York City. The dataset provides insights into the academic performance of schools and aims to facilitate analysis for various stakeholders, including policymakers, educators, researchers, and parents.

## Dataset Description
The dataset contains information on SAT performance for New York City public schools, including average scores in math, reading, and writing, as well as the percentage of students tested.
## Analysis Process
1. **Data Loading and Initial Exploration:**
    - Loaded the dataset into a pandas DataFrame.
    - Explored the structure of the dataset (e.g., column names, data types).
    - Checked for any missing values or anomalies in the data.

2. **Identifying Schools with the Best Math Results:**
    - Calculated the maximum possible score for the math section of the SAT.
    - Filtered schools where the average math score is at least 80% of the maximum.
    - Saved the results in a DataFrame named `best_math_schools`.

3. **Determining the Top 10 Performing Schools:**
    - Calculated the total SAT score for each school by summing the average scores in math, reading, and writing.
    - Sorted the schools based on the total SAT score in descending order.
    - Selected the top 10 performing schools and saved the results in a DataFrame named `top_10_schools`.

4. **Identifying Borough with the Largest Standard Deviation:**
    - Calculated the standard deviation of the total SAT scores for each borough.
    - Identified the borough with the largest standard deviation and saved the results in a DataFrame named `largest_std_dev`.

## Author

- Name: [Mohammed Mebarek Mecheter](https://www.linkedin.com/in/mohammed-mecheter/)
- Email: mohammedmecheter@gmail.com
- Portfolio: [Mebarek](https://mebarek.pages.dev/)