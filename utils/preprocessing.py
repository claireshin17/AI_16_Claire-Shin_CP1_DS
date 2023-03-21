import os
import pandas as pd

def txt_to_df(directory_path):
    """
    A function that takes in a directory path as an argument and returns a DataFrame 
    with two columns: "name" (name of the .txt file) and "text" (text in the .txt file)
    """
    file_data = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r") as f:
                text = f.read()
                # Append the file name and content to the file_data list
                file_data.append({"name": filename, "text": text})

    df = pd.DataFrame(file_data)

    return df

def preprocess(data):
    """
    Function to preprocess data 
    """
    data['text'] = data['text'].replace('\n', ' ')
    
    return data
