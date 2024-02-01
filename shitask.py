import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/content/Salaries.csv')
df.head()

# Identify the number of rows and columns
nrow, ncols = df.shape
print ("Numbers of rows:", nrow)
print ("Numbers of columns:", ncols)

# Determine the data types of each column
data_types = df.dtypes
print("Data types of each column:")
print(data_types)

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)


# Extract the salary column
salaries = df[:, 6]  

# Calculate mean
mean_salary = np.mean(salaries)
print("Mean salary:", mean_salary)

# Calculate median
median_salary = np.median(salaries)
print("Median salary:", median_salary)

# Calculate mode
mode_salary = np.argmax(np.bincount(salaries.astype(int)))
print("Mode salary:", mode_salary)

# Calculate minimum and maximum
min_salary = np.min(salaries)
max_salary = np.max(salaries)
print("Minimum salary:", min_salary)
print("Maximum salary:", max_salary)

# Determine the range of salaries
salary_range = np.ptp(salaries)
print("Salary range:", salary_range)

# Calculate standard deviation
std_salary = np.std(salaries)
print("Standard deviation of salaries:", std_salary)



# Replace missing values with mean
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Replace missing values with median
df['column_name'].fillna(df['column_name'].median(), inplace=True)

# Replace missing values with mode
df['column_name'].fillna(df['column_name'].mode()[0], inplace=True)

'''Explaining Why I used this method: First of all, beacuse we've calculated in
   the task above mean, median and mode, and this method assumes that the missing
   values are missing at random and that the mean,medianand mode provides a
   reasonable estimate for the missing values'''

# Create a histogram of salaries
plt.hist(df['salary'], bins=10, edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Salaries')
plt.show()

# Create a bar chart of department proportions
department_counts = df['department'].value_counts()
plt.bar(department_counts.index, department_counts.values)
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.title('Proportion of Employees in Different Departments')
plt.xticks(rotation=45)
plt.show()


# Group the data by one or more columns and calculate summary statistics
grouped_data = df.groupby(['column1', 'column2'])
summary_statistics = grouped_data['salary'].agg(['mean', 'median', 'min', 'max', 'count'])
print(summary_statistics)

# Compare average salaries across different groups
average_salaries = grouped_data['salary'].mean()
print(average_salaries)

# Identify correlation between salary and another numerical column
correlation = df['salary'].corr(df['numerical_column'])
print("Correlation:", correlation)

# Plot a scatter plot to visualize the relationship
plt.scatter(df['numerical_column'], df['salary'])
plt.xlabel('Numerical Column')
plt.ylabel('Salary')
plt.title('Relationship between Salary and Numerical Column')
plt.show()



'''In this data analysis, we explored a dataset containing information about employees, including their salaries, departments,
and additional numerical data. The goal was to gain insights and identify patterns within the data.

We examined the distribution of salaries using a histogram. The histogram revealed that the majority of salaries were
concentrated within a specific range, this suggests the presence of a dominant salary range
among the employees.

We examined the proportion of employees in different departments using a bar chart. The chart displayed the number of
employees in each department. From this, we could identify departments with the highest and lowest
number of employees, which could be useful.

We grouped the data by one or more columns and calculated summary statistics for each group. This allowed us
to gain insights specific to different groups within the dataset.
We calculated the mean, median, minimum, maximum, and count of salaries for each group.

We explored the correlation between salary and another numerical column. By calculating the correlation coefficient, we
determined the strength and direction of the relationship between these two variables.

in the end, we visualized the relationship between salary and the numerical column using a scatter plot'''