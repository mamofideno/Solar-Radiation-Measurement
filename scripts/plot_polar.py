import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class WindPolarPlot:
    def __init__(self, dataframe):
        # if not isinstance(dataframe, pd.DataFrame):
            # raise ValueError("Input must be a pandas DataFrame.")
        
        # if 'WSstdev' not in dataframe.columns:
            # raise ValueError("DataFrame must contain 'wind_speed' and 'wind_direction' columns.")
        self.dataframe = dataframe.copy()
        self.dataframe['wind_direction_rad'] = np.deg2rad(self.dataframe['WD'])

    def plot_polar(self, cmap='viridis', alpha=0.75, figsize=(20, 20)):
        plt.figure(figsize=figsize)
        ax = plt.subplot(111, polar=True)

        # Plot the wind data on a polar plot
        sc = ax.scatter(self.dataframe['wind_direction_rad'], self.dataframe['WSstdev'], 
                        c=self.dataframe['WSstdev'], cmap=cmap, alpha=alpha)

        # Add a color bar to indicate wind speed
        plt.colorbar(sc, label='Wind Speed (m/s)')

        # Set the direction labels
        ax.set_theta_zero_location('N')  # North (0°) at the top
        ax.set_theta_direction(-1)  # Clockwise direction

        # Set the radius limits (for wind speed)
        ax.set_ylim(0, self.dataframe['WSstdev'].max())

        # Set title and labels
        plt.title('Wind Speed and Direction Distribution')
        ax.set_xlabel('Wind Direction (Degrees)')
        ax.set_ylabel('Wind Speed (m/s)')

        # Show the plot
        plt.show()

    def plot_binned_polar(self, bin_size=10, color='skyblue', edgecolor='black', figsize=(8, 8)):
        # Create bins for wind direction
        bins = np.arange(0, 360 + bin_size, bin_size)

        # Assign each direction to a bin
        self.dataframe['direction_bin'] = pd.cut(self.dataframe['wind_direction'], bins, include_lowest=True)

        # Calculate mean wind speed for each bin
        bin_mean_speeds = self.dataframe.groupby('direction_bin')['WSstdev'].mean()

        # Calculate the center of each bin
        bin_centers = np.deg2rad(np.arange(bin_size / 2, 360, bin_size))

        plt.figure(figsize=figsize)
        ax = plt.subplot(111, polar=True)

        # Plot the binned data as bars
        ax.bar(bin_centers, bin_mean_speeds, width=np.deg2rad(bin_size), bottom=0, 
               color=color, edgecolor=edgecolor)

        # Set the direction labels and other plot settings
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.set_ylim(0, bin_mean_speeds.max())

        # Set title
        plt.title('Binned Wind Speed and Direction Distribution')
        
        # Show the plot
        plt.show()