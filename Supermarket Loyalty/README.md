# Supermarket Loyalty Program Analysis and Prediction

## Project Overview

International Essentials is an international supermarket chain with a loyalty program that provides rewards based on customers' spending. The goal of this project is to analyze customer spending and engagement patterns within the loyalty program and build predictive models to estimate reward costs and predict profitability.

## Data

The dataset contains records of customers for their last full year of the loyalty program. It includes the following columns:

| Column Name          | Criteria                                                |
|----------------------|---------------------------------------------------------|
| customer_id          | Unique identifier for the customer                      |
| spend                | Total spend of the customer in their last full year     |
| first_month          | Amount spent by the customer in their first month       |
| items_in_first_month | Number of items purchased in the first month            |
| region               | Geographic region that the customer is based in         |
| loyalty_years        | Number of years the customer has been part of the program |
| joining_month        | Month the customer joined the loyalty program           |
| promotion            | Whether the customer joined the program as part of a promotion |

## Data Preprocessing

- Handled missing values.
- Ensured that the data types of each column are appropriate for analysis.
- Cleaned the data by addressing inconsistencies and errors, ensuring data quality.

## Exploratory Data Analysis (EDA)

### Customer Spending Analysis

1. **Average Spending Analysis**:
    - Calculated the average spending per customer in the loyalty program.
    - Found the average spending per customer to be $122.64.

2. **Spending Distribution Analysis**:
    - Explored how spending is distributed among different customer segments such as regions and loyalty years.
    - Discovered that the Middle East/Africa region had the highest total spending.

3. **Trend Analysis**:
    - Investigated trends and patterns in spending over time and across loyalty years.
    - Found a steady increase in spending over the years, indicating positive growth in customer spending within the loyalty program.

4. **Impact of First Month Spending Analysis**:
    - Examined whether the amount spent in the first month correlates with overall spending for the year.
    - Identified a positive correlation between first-month spending and overall spending for the year.

### Loyalty Program Engagement Analysis

1. **Promotional Participation Analysis**:
    - Identified the number of customers who participated in the loyalty program as part of a promotion.
    - Found that 611 customers joined as part of a promotion, while 635 customers did not join with a promotion.

2. **Retention Rate Analysis**:
    - Calculated the retention rate of customers after their first 3 months of enrollment.
    - Discovered that 397 customers remained active in the loyalty program after their first 3 months.

3. **Comparison of Promotional and Non-Promotional Engagement**:
    - Analyzed the engagement metrics between customers who joined with promotions and those who did not.
    - Found a slightly higher retention rate for customers who did not join as part of a promotion.

4. **First-Month Engagement Analysis**:
    - Examined trends and patterns in the number of items purchased by customers in their first month.
    - Calculated the correlation coefficient between first-month items purchased and total spending.

### Geographic Analysis

1. **Regional Spending Patterns**:
    - Calculated average spending and other engagement metrics for each geographic region.
    - Visualized the distribution of spending across regions.

2. **Regional Promotion Response**:
    - Analyzed the engagement metrics of customers in different regions who joined the loyalty program with promotions.
    - Compared metrics such as average spending, items purchased, and retention rates between regions.

3. **Market Expansion Opportunities**:
    - Examined the distribution of customer counts across regions to identify regions with lower customer counts.
    - Identified potential market expansion opportunities in regions with relatively lower customer counts.

## Model Building

1. **Feature Engineering**:
    - Created new features based on the insights gained from the exploratory data analysis.
    - Performed feature selection to identify the most relevant features for predicting customer spending.

2. **Model Selection**:
    - Evaluated various machine learning algorithms, such as Random Forest, Decision Trees, and Gradient Boosting, to find the most suitable model for predicting customer spending.

3. **Hyperparameter Tuning**:
    - Utilized techniques like GridSearchCV to tune the hyperparameters of the selected model and optimize its performance.

4. **Model Training and Evaluation**:
    - Trained the final model on the training data and evaluated its performance on the testing data.
    - Calculated evaluation metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared to assess the model's accuracy.
    - Visualized predictions vs. actual values to further analyze the model's performance.

## Conclusion

This project provides valuable insights into customer spending behavior and program engagement within the Supermarket Loyalty program. By understanding these patterns and building predictive models, International Essentials can make data-driven decisions to optimize the loyalty program, enhance customer satisfaction, estimate reward costs accurately, and maximize profitability.
