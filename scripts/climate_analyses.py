import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

class ClimateAnalysis:
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        
        required_columns = {'Tamb ', 'RH', 'GHI'}
        print(required_columns)
        print(dataframe.columns)
        # if not required_columns.issubset(dataframe.columns):
            # raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
        
        self.dataframe = dataframe

    def plot_scatter(self):
                # Scatter plot of temperature vs. relative humidity
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='RH', y='Tamb', data=self.dataframe)
        plt.title('Temperature vs. Relative Humidity')
        plt.xlabel('Relative Humidity (%)')
        plt.ylabel('Temperature (°C)')
        plt.show()

        # Scatter plot of solar radiation vs. relative humidity
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='RH', y='GHI', data=self.dataframe)
        plt.title('Solar Radiation vs. Relative Humidity')
        plt.xlabel('Relative Humidity (%)')
        plt.ylabel('Solar Radiation (W/m²)')
        plt.show()

        # Scatter plot of temperature vs. solar radiation
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='GHI', y='Tamb', data=self.dataframe)
        plt.title('Temperature vs. Solar Radiation')
        plt.xlabel('Solar Radiation (W/m²)')
        plt.ylabel('Temperature (°C)')
        plt.show()

    def plot_correlation_heatmap(self):
        # Calculate the correlation matrix
        corr_matrix = self.dataframe.corr()

        # Plot the heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap')
        plt.show()

    def linear_regression(self, dependent_var):
        if dependent_var not in ['Tamb ', 'GHI']:
            raise ValueError("dependent_var must be 'temperature' or 'solar_radiation'")
        
        # Simple linear regression: dependent_var as a function of RH
        X = self.dataframe['RH']
        y = self.dataframe[dependent_var]
        X = sm.add_constant(X)  # Add a constant term to the model
        model = sm.OLS(y, X).fit()
        
        return model.summary()
