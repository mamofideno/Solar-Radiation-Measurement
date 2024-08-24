import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class HistogramVisualizer:
    def __init__(self, dataframe):
        """
        Initialize the HistogramVisualizer with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame containing the variables for the histograms.
        """
        required_columns = {'GHI', 'DNI', 'DHI', 'WS', 'Tamb'}
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if not required_columns.issubset(dataframe.columns):
            raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
        
        self.dataframe = dataframe.copy()
        
        # Ensure the columns are numeric
        for column in required_columns:
            self.dataframe[column] = pd.to_numeric(self.dataframe[column], errors='coerce')
    
    def plot_histogram(self, variable, bins=30):
        """
        Plot a histogram for a given variable.

        Parameters:
        - variable (str): The variable for which the histogram is to be plotted.
        - bins (int): The number of bins to use in the histogram (default is 30).
        """
        if variable not in self.dataframe.columns:
            raise ValueError(f"The variable '{variable}' is not a valid column in the DataFrame.")
        
        plt.figure(figsize=(10, 6))
        
        sns.histplot(self.dataframe[variable], bins=bins, kde=True, color='skyblue')
        
        plt.title(f'Histogram of {variable}')
        plt.xlabel(variable)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    
    def plot_all_histograms(self, bins=30):
        """
        Plot histograms for all specified variables (GHI, DNI, DHI, WS, Tamb).

        Parameters:
        - bins (int): The number of bins to use in the histograms (default is 30).
        """
        variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
        
        plt.figure(figsize=(16, 12))
        
        for i, variable in enumerate(variables, 1):
            plt.subplot(3, 2, i)
            sns.histplot(self.dataframe[variable], bins=bins, kde=True, color='skyblue')
            plt.title(f'Histogram of {variable}')
            plt.xlabel(variable)
            plt.ylabel('Frequency')
            plt.grid(True)
        
        plt.tight_layout()
        plt.show()