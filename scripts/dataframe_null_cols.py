import pandas as pd

class DataFrameNullCols:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def columns_with_nulls(self) -> list:
        return self.df.columns[self.df.isnull().any()].tolist()
