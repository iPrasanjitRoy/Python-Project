import pandas as pd


html_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(html_url)


csv_file_path = "Titanic.csv"
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")



