import os

folder_path = r"C:\Users\PRASANJIT\Desktop\AllPDFS" 

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)
    new_filename = filename.upper()
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)
