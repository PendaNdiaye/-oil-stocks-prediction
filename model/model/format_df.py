import pandas as pd

def list_of_dict_to_dataframe(l):
    return pd.DataFrame(l)

def remove_cols(df, cols="scraping_date"):
    return df.drop(cols, axis=1)

def rename_cols(df):
    return df.rename(columns={'new_header':'news', 'public_date': 'date'})

def pivot_date(s):
    t = s.split('/')
    y, m, d = t
    return '/'.join([d, m, y])

def format_date(df, date_col='date'):
    df[date_col] = df[date_col].apply(lambda s:  s.replace('-', '/'))
    df[date_col] = df[date_col].apply(lambda s: pivot_date(s))
    return df

def aggregate(df):
    df['daily_news'] = df.groupby(['date'])['news'].transform(lambda x : ' '.join(x))
    df = df.drop('news', axis=1)
    df = df.drop_duplicates()
    df = df.set_index("date")
    return df


def format_data(l):
    df = list_of_dict_to_dataframe(l)
    df = remove_cols(df)
    df = rename_cols(df)
    df = format_date(df)
    df = aggregate(df)
    return df