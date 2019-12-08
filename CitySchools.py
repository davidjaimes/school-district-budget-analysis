# Dependencies and Setup
import pandas as pd
import numpy as np

# Read School and Student Data File and store into Pandas Data Frames
schools = pd.read_csv("Resources/schools_complete.csv")
students = pd.read_csv("Resources/students_complete.csv")

# Combine the data into a single dataset
data = pd.merge(students, schools, how="left", on="school_name")

# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]
data['school_spending'] = pd.cut(
    data['Per Student Budget'],
    bins=spending_bins,
    labels=group_names
)
print(data)
