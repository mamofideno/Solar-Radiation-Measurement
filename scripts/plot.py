import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class SolarDataVisualizer:
    def __init__(self, dataframe):
        """
        Initialize the SolarDataVisualizer with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame containing the solar and temperature data.
        """
        required_columns = {'GHI', 'DNI', 'DHI', 'Tamb', 'Timestamp'}
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if not required_columns.issubset(dataframe.columns):
            raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
        
        self.dataframe = dataframe
        self.dataframe['Timestamp'] = pd.to_datetime(self.dataframe['Timestamp'])

    def plot_line_graphs(self):
        """
        Plot line graphs of GHI, DNI, DHI, and Tamb over time.
        """
        plt.figure(figsize=(14, 8))
        plt.plot(self.dataframe['Timestamp'], self.dataframe['GHI'], label='GHI', color='orange')
        plt.plot(self.dataframe['Timestamp'], self.dataframe['DNI'], label='DNI', color='blue')
        plt.plot(self.dataframe['Timestamp'], self.dataframe['DHI'], label='DHI', color='green')
        plt.plot(self.dataframe['Timestamp'], self.dataframe['Tamb'], label='Tamb', color='red')
        plt.title('GHI, DNI, DHI, and Tamb Over Time')
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.legend()
        plt.show()

    def plot_area_plots(self):
        """
        Plot area plots of GHI, DNI, DHI, and Tamb over time.
        """
        plt.figure(figsize=(14, 8))
        plt.fill_between(self.dataframe['Timestamp'], self.dataframe['GHI'], label='GHI', color='orange', alpha=0.3)
        plt.fill_between(self.dataframe['Timestamp'], self.dataframe['DNI'], label='DNI', color='blue', alpha=0.3)
        plt.fill_between(self.dataframe['Timestamp'], self.dataframe['DHI'], label='DHI', color='green', alpha=0.3)
        plt.fill_between(self.dataframe['Timestamp'], self.dataframe['Tamb'], label='Tamb', color='red', alpha=0.3)
        plt.title('GHI, DNI, DHI, and Tamb Over Time (Area Plot)')
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.legend()
        plt.show()

    def plot_by_month(self):
        """
        Plot line graphs of GHI, DNI, DHI, and Tamb aggregated by month to observe patterns.
        """
        self.dataframe['month'] = self.dataframe['Timestamp'].dt.month
        self.dataframe['month'] =pd.DatetimeIndex(self.dataframe['Timestamp']).month
        monthly_data = self.dataframe.groupby('month').mean(numeric_only=True)

        plt.figure(figsize=(14, 8))
        plt.plot(monthly_data.index, monthly_data['GHI'], label='GHI', color='orange')
        plt.plot(monthly_data.index, monthly_data['DNI'], label='DNI', color='blue')
        plt.plot(monthly_data.index, monthly_data['DHI'], label='DHI', color='green')
        plt.plot(monthly_data.index, monthly_data['Tamb'], label='Tamb', color='red')
        plt.title('Monthly Average GHI, DNI, DHI, and Tamb')
        plt.xlabel('Month')
        plt.ylabel('Average Values')
        plt.legend()
        plt.show()

    def plot_by_hour(self):
        """
        Plot line graphs of GHI, DNI, DHI, and Tamb aggregated by hour of the day to observe daily trends.
        """
        self.dataframe['hour'] = self.dataframe['Timestamp'].dt.hour
        hourly_data = self.dataframe.groupby('hour').mean(numeric_only=True)

        plt.figure(figsize=(14, 8))
        plt.plot(hourly_data.index, hourly_data['GHI'], label='GHI', color='orange')
        plt.plot(hourly_data.index, hourly_data['DNI'], label='DNI', color='blue')
        plt.plot(hourly_data.index, hourly_data['DHI'], label='DHI', color='green')
        plt.plot(hourly_data.index, hourly_data['Tamb'], label='Tamb', color='red')
        plt.title('Hourly Average GHI, DNI, DHI, and Tamb')
        plt.xlabel('Hour of Day')
        plt.ylabel('Average Values')
        plt.legend()
        plt.show()