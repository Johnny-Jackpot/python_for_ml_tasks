import pandas as pd

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