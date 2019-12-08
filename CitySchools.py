# Dependencies and Setup
import pandas as pd
import numpy as np

# Read School and Student Data File and store into Pandas Data Frames
schools = pd.read_csv("Resources/schools_complete.csv")
students = pd.read_csv("Resources/students_complete.csv")

# Combine the data into a single dataset
data = pd.merge(students, schools, how="left", on="school_name")

# Create group by school name and use keys() to get list of school names
group = data.groupby(['school_name'])
school_name = group.groups.keys()

# Use explode() function to unflatten list of lists
school_type = group['type'].unique().explode()
total_students = group.size()
total_budget = group['budget'].unique().explode()

# Note: Not allowed to divide list array by pd.Series
budget_per_student = total_budget / total_students
average_math = group['math_score'].mean()
average_reading = group['reading_score'].mean()

# Take each group array, set condition, and sum up all True values in array.
# Also, underscore is used because key in group is not being used.
passing_math = np.array([np.sum(val >= 70) for (_, val) in group['math_score']])
passing_reading = np.array([np.sum(val >= 70) for (_, val) in group['reading_score']])
overall_passing = (passing_math + passing_reading) / 2


school_summary = pd.DataFrame({
    'School Type':  school_type,
    'Total Students': total_students,
    'Total Budget': [f'${x:,.2f}' for x in total_budget],
    'Per Student Budget': [f'${x:,.2f}' for x in budget_per_student],
    'Average Math Score': average_math,
    'Average Reading Score': average_reading,
    '% Passing Math': 100 * passing_math / total_students,
    '% Passing Reading': 100 * passing_reading / total_students,
    '% Overall Passing Rate': 100 * overall_passing / total_students
}, index=school_name)
print(school_summary.sort_values(by='% Overall Passing Rate', ascending=True).head(5))
