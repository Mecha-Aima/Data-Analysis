import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = 'date', parse_dates=True)

# Clean data
lower_thresh = df['value'].quantile(0.025)
upper_thresh = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_thresh) & (df['value'] <= upper_thresh)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,7))
    df_copy = df.copy()
    ax.plot(df_copy.index, df_copy['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=16)
    plt.xlabel('Date',fontsize=12)
    plt.ylabel('Page Views',fontsize=12)


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['month'] = df_bar.date.dt.strftime("%B")
    df_bar['year'] = df_bar.date.dt.year
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped[month_order]
    
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111)
    
    width = 0.05  
    x = np.arange(len(df_grouped.index))
    
    for i, month in enumerate(month_order):
        ax.bar(x + i * width, df_grouped[month], 
               width, 
               label=month)
    
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.set_xticks(x + width * 5.5)  
    ax.set_xticklabels(df_grouped.index)
    plt.legend(title='Months', loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box['month'] = pd.Categorical(df_box['month'], ordered=True, categories=months)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(20,8))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1, hue='year')
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=14)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Page Views', fontsize=12)

    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, hue='month')
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=14)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_ylabel('Page Views', fontsize=12)

    fig = plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()
draw_line_plot()
draw_box_plot()