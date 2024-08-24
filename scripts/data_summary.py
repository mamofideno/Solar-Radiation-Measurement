import pandas as pd
import os

class DataSummary:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary(self) -> list:
        return self.df.describe()
