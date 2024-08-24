import pandas as pd
import numpy as np

class ZScoreAnalyzer:
    def __init__(self, dataframe):
        """
        Initialize the ZScoreAnalyzer with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame containing the variables to analyze.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        
        self.dataframe = dataframe.copy()
    
    def calculate_z_scores(self, column):
        """
        Calculate Z-scores for a given column in the DataFrame.

        Parameters:
        - column (str): The column for which to calculate Z-scores.

        Returns:
        - pd.Series: A Series of Z-scores corresponding to the input column.
        """
        if column not in self.dataframe.columns:
            raise ValueError(f"The column '{column}' is not in the DataFrame.")
        
        mean = self.dataframe[column].mean()
        std = self.dataframe[column].std()

        z_scores = (self.dataframe[column] - mean) / std
        return z_scores
    
    def flag_outliers(self, column, threshold=3):
        """
        Flag data points as outliers if their Z-score is greater than a specified threshold.

        Parameters:
        - column (str): The column for which to flag outliers.
        - threshold (float): The Z-score threshold above which data points are flagged as outliers (default is 3).

        Returns:
        - pd.DataFrame: A DataFrame with the original data and a new column 'Outlier' indicating outliers.
        """
        self.dataframe['Z_Score'] = self.calculate_z_scores(column)
        self.dataframe['Outlier'] = self.dataframe['Z_Score'].abs() > threshold
        
        return self.dataframe[['Z_Score', 'Outlier']]
    
    def get_outliers(self, column, threshold=3):
        """
        Return data points that are flagged as outliers.

        Parameters:
        - column (str): The column for which to return outliers.
        - threshold (float): The Z-score threshold above which data points are considered outliers (default is 3).

        Returns:
        - pd.DataFrame: A DataFrame containing only the outliers.
        """
        flagged_df = self.flag_outliers(column, threshold)
        outliers = self.dataframe[self.dataframe['Outlier'] == True]
        return outliers