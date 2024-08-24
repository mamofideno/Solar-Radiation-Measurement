import pandas as pd
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_line(self, columns: list = None, title: str = "Solar Data Over Time", xlabel: str = "Timestamp", ylabel: str = "Value",figsize: tuple = (20, 15)):
        if columns is None:
            columns = ['GHI', 'DNI', 'DHI', 'Tamb']
        # df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        # df.set_index('Timestamp', inplace=True)
        # Plot the line graph
        self.df[columns].plot(kind='line', marker='o')
        # Add labels and title
        plt.figure(figsize=(20,10))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gcf().autofmt_xdate()
        # Show the plot
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()

    def plot_area(self, columns: list = None, title: str = "Solar Data Over Time", xlabel: str = "Timestamp", ylabel: str = "Value"):
        if columns is None:
            columns = ['GHI', 'DNI', 'DHI', 'Tamb']

        # Plot the area graph
        self.df[columns].plot(kind='area', alpha=0.5)
        # Add labels and title
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # Show the plot
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()