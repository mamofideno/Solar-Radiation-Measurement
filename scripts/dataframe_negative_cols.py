import pandas as pd

class NegativeValueChecker:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        self.dataframe = dataframe
    def get_columns_with_negatives(self):
        columns_with_negatives = [col for col in self.dataframe.columns if (self.dataframe[col] < 0).any()]

        return columns_with_negatives
