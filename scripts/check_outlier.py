import pandas as pd

class OutlierChecker:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        self.dataframe = dataframe

    def check_outliers(self, column):
        if column not in self.dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = self.dataframe[column].quantile(0.25)
        Q3 = self.dataframe[column].quantile(0.75)
        IQR = Q3 - Q1

        # Define outlier boundaries
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify outliers
        outliers = self.dataframe[(self.dataframe[column] < lower_bound) | (self.dataframe[column] > upper_bound)][column]
        return outliers