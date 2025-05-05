import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

dataset = []
"""[age]_[gender]_[race]_[date&time].jpg

[age] is an integer from 0 to 116, indicating the age
[gender] is either 0 (male) or 1 (female)
[race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
[date&time] is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace"""

for file in os.listdir('UTKFace'):
    if file.endswith('.jpg'):
        # Split the filename into its components
        parts = file.split('_')
        if len(parts) != 4:
            print(f"Skipping file {file} due to unexpected format.")
            continue
        age = int(parts[0])
        gender = int(parts[1])
        race = int(parts[2])
        date_time = parts[3].split('.')[0]
        dataset.append({"filename": file, "age": age, "gender": gender, "race": race, "date_time": date_time})
df = pd.DataFrame(dataset)

print("Total images loaded:", len(df))
print(df.head())


