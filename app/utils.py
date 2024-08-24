import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
class DataFrameLoader:
    def __init__(self, file_path):
       self.file_path = file_path
       
    def load(self):
        # print(self.file_path)
        # Get the file extension
        _, file_extension = os.path.splitext(self.file_path)
        # Check the file extension and load the file accordingly
        if file_extension == '.csv':
            df = pd.read_csv(self.file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(self.file_path)
        elif file_extension == '.json':
            df = pd.read_json(self.file_path)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
        
        return df
    
class HistogramPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_histogram(self, column: str, bins: int = 10):
        fig, ax = plt.subplots()
        ax.hist(self.df[column], bins=bins, edgecolor='black')
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        return fig