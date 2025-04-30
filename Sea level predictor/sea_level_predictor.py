import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig = plt.figure(figsize=(10,8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='data points', alpha=0.8)

    # Create first line of best fit
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    fit = linregress(x1, y1)
    extended_years = np.arange(df['Year'].min(), 2051)
    y_pred = fit.intercept + fit.slope * extended_years
    plt.plot(extended_years, y_pred, color="purple", label=f"Best fit line: y = {fit.slope:.2f}x + {fit.intercept:.2f}")

    # Create second line of best fit
    x = df.loc[df['Year'] >= 2000, "Year"]
    y = df.loc[df['Year'] >= 2000, "CSIRO Adjusted Sea Level"]
    fit2 = linregress(x, y)
    y_pred2000 = fit2.intercept + fit2.slope * np.arange(2000, 2051)
    plt.plot(np.arange(2000, 2051), y_pred2000, color="red", label=f"2nd best fit: y = {fit2.slope:.2f}x + {fit2.intercept:.2f}")

    years = np.array([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.xticks(years)


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()