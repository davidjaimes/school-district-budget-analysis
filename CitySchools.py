# Dependencies and Setup
import pandas as pd
import numpy as np

# Read School and Student Data File and store into Pandas Data Frames
schools = pd.read_csv("Resources/schools_complete.csv")
students = pd.read_csv("Resources/students_complete.csv")

# Combine the data into a single dataset
data = pd.merge(students, schools, how="left", on="school_name")

# When you perform unique on Pandas Series it turns to Numpy array.
# This is the reason we are able to use np.ndarray.size attribute.
total_schools = data['school_name'].unique().size
total_students = data['Student ID'].unique().size
total_budget =  data['budget'].unique().sum()

# Find average math and reading scores.
average_math_score = data['math_score'].mean()
average_reading_score = data['reading_score'].mean()

# Use np.sum() to only count True elements in boolean array.
passing_math = np.sum(data['math_score'] >= 70) / total_students
passing_reading = np.sum(data['reading_score'] >= 70) / total_students
overall_average_rate = (average_math_score + average_reading_score) / 2

# Need to put index if all values are scalars.
district_summary = pd.DataFrame({
    'Total Schools': total_schools,
    'Total Students': f'{total_students:,}',
    'Total Budget': f'${total_budget:,.2f}',
    'Average Math Score': f'{average_math_score:.6f}',
    'Average Reading Score': f'{average_reading_score:.6f}',
    '% Passing Math': f'{100 * passing_math:.6f}',
    '% Passing Reading': f'{100 * passing_reading:.6f}',
    '% Overall Average Score': f'{overall_average_rate:.6}',
}, index=[0])
print(district_summary)
