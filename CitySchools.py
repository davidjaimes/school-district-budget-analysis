# Dependencies and Setup
import pandas as pd
import numpy as np

# Read School and Student Data File and store into Pandas Data Frames
schools = pd.read_csv("Resources/schools_complete.csv")
students = pd.read_csv("Resources/students_complete.csv")

# Combine the data into a single dataset
data = pd.merge(students, schools, how="left", on="school_name")

group = data.groupby(['school_name'])
school_name = group.groups.keys()
school_type = group['type'].unique().explode()
total_students = group.size()
total_budget = group['budget'].unique().explode()
budget_per_student = np.array(total_budget) / total_students
average_math = group['math_score'].mean()
average_reading = group['reading_score'].mean()
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
print(school_summary.sort_values(by='% Overall Passing Rate', ascending=False).head(5))
