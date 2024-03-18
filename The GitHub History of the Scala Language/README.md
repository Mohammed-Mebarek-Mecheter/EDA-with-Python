# Analyzing Scala Project History

This project aims to analyze the development history of the Scala programming language project on GitHub. We'll explore various aspects such as project activity, community dynamics, and contributions of specific developers.

## Project Description

Scala is a mature programming language with a rich development history spanning over ten years. Being an open-source project, its entire development history, including pull requests, commits, and code reviews, is publicly available on GitHub.

## Dataset

The dataset used in this project comprises three CSV files:

- `pulls_2011-2013.csv`: Contains basic information about pull requests from the end of 2011 up to (but not including) 2014.
- `pulls_2014-2018.csv`: Contains identical information, spanning from 2014 up to 2018.
- `pull_files.csv`: Contains the files modified by each pull request.

## Tasks

### 1. Importing and Cleaning Data
- Imported the dataset using pandas.
- Cleaned and preprocessed the data.

### 2. Project Activity Analysis
- Calculated and visualized the number of pull requests submitted each month to understand the trend of project activity.

### 3. Community Dynamics
- Analyzed the distribution of pull requests submitted by each user to understand the dynamics of the project community.

### 4. Identifying Hot Areas of Code
- Identified the files changed in the last ten pull requests to pinpoint the active areas of the codebase.

### 5. Evaluating Community Camaraderie
- Plotted a histogram of the number of pull requests submitted by each user to assess the camaraderie within the project.

### 6. Investigating Recent Changes
- Identified the files changed in the last ten pull requests to understand recent code changes.

### 7. Identifying Top Developers
- Identified the top 3 developers who submitted pull requests to a specific file, indicating their expertise in that area.

### 8. Analyzing Recent Contributors
- Identified the users who submitted the last ten pull requests to a specific file to understand recent contributors.

### 9. Understanding Developer Contributions Over Time
- Plotted the number of pull requests submitted by two developers over time to understand their contribution trends.

### 10. Analyzing Developer Contributions to Specific Files
- Analyzed the number of pull requests submitted by developers to a specific file each year to understand their expertise in that file.

## Usage

To run this project:

1. Clone this repository.
2. Install the required dependencies (`pandas`, `matplotlib`).
3. Run the Jupyter Notebook to execute the analysis.

## Conclusion

This project provides insights into the development history and community dynamics of the Scala programming language project on GitHub. By analyzing project activity, community engagement, and individual contributions, we gain a better understanding of the project's evolution and identify key areas of expertise among contributors.