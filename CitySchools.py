# Dependencies and Setup
import pandas as pd
import numpy as np

# Read School and Student Data File and store into Pandas Data Frames
schools = pd.read_csv("Resources/schools_complete.csv")
students = pd.read_csv("Resources/students_complete.csv")

# Combine the data into a single dataset
data = pd.merge(students, schools, how="left", on="school_name")

# Create group by school name and grade.
group = data.groupby(['school_name', 'grade'])

# This creates a pd.Series with two indices.
math_scores = group['math_score'].mean()

# Remove index names: school_name and grade.
math_scores.index.names = [None] * 2

# Unstack MultiIndex dataframe.
print(math_scores.unstack()[['9th', '10th', '11th', '12th']])
