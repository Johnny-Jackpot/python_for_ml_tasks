import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyse_numeric_col(df: pd.DataFrame, null_percentage: pd.DataFrame, null_count: pd.DataFrame, columns: list) -> None:
    result_df = pd.DataFrame(columns=['column_name', 'min',  'mean', 'median', 'max', 'mode'])
    for col_name in columns:
        print(f'=== {col_name} ==='),
        print(f'Min: {df[col_name].min()}')
        print(f'Mean: {df[col_name].mean()}')
        print(f'Median: {df[col_name].median()}')
        print(f'Max: {df[col_name].max()}')
        print(f'Mode: {df[col_name].mode()[0]}')
        print(f'Null Percentage: {null_percentage[col_name]}%')
        print(f'Null Count: {null_count[col_name]}')


def hw2_analyse(df: pd.DataFrame, null_df_under1: pd.DataFrame, column_name: str) -> None:
    print(null_df_under1[null_df_under1.column_name == column_name])
    print('VALUE COUNTS:')
    print(df[column_name].value_counts().head(10))
    sns.boxplot(df[column_name])
    plt.show()
    print('QUANTILE:')
    print(df[column_name].quantile(q = [0.25,0.5,0.75,1]))
    print(f'MODE: {df[column_name].mode()[0]}')
    print(f'MEAN: {df[column_name].mean()}')