import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df.loc[(df["value"] > df["value"].quantile(0.025)) &
            (df["value"] < df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))

    df.plot(kind="line", xlabel="Date", ylabel="Page Views",
                title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
                legend=False, color="red", ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(pd.Grouper(freq="1M")).mean()
    df_bar["year"] = df_bar.index.strftime("%Y")
    df_bar["month"] = df_bar.index.strftime("%B")
    df_bar.reset_index(drop=True, inplace=True)

    # Draw bar plot
    fig = plt.figure(figsize=(7, 7))
    order = ["January", "February", "March", "April", "May",
             "June", "July", "August", "September",
             "October", "November", "December"]
    ax = sns.barplot(data=df_bar, x="year", y="value", hue="month",
                 hue_order=order, palette="bright")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", loc="upper left")
    plt.xticks(rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22,8))
    ax1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=order)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
