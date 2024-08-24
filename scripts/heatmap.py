import  pandas as pd
import matplotlib.pyplot as plt

class HeatMap:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    def plot_heatmap(self,figsize=(10, 8), cmap="coolwarm", annot=True):
        # benin_data_set_comment_removed=benin_data_set.drop(columns=['Comments','Timestamp'])
        # correlation_matrix=self.df.corr()
        plt.figure(figsize=(20, 10))
        # sns.heatmap(correlation_matrix, annot=True)
        # sns.heatmap(correlation_matrix, annot=annot, cmap=cmap, fmt='.2f', linewidths=.5, cbar=True)
        plt.show()    