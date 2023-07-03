import pandas as pd

student_data = {'Student ID': [1, 2, 3, 4, 5],
                'Test Score': [85, 90, 80, 70, 85]}

df = pd.DataFrame(student_data)

df.to_csv('student_data.csv', index=False)

