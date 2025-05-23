import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    return df

def aggregate_counts(df):
    # Aggregate total counts by variant
    agg = df.groupby('variant')['count'].sum().reset_index()
    return agg

def plot_variant_counts(agg_df):
    sns.barplot(data=agg_df, x='variant', y='count', palette='viridis')
    plt.title('Total Counts of COVID-19 Variants')
    plt.xlabel('Variant')
    plt.ylabel('Total Count')
    plt.tight_layout()
    plt.show()

def main():
    df = load_data('variants.csv')
    agg_df = aggregate_counts(df)
    print(agg_df)
    plot_variant_counts(agg_df)

if __name__ == "__main__":
    main()


