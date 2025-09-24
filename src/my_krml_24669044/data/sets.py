import pandas as pd

def find_duplicates(df: pd.DataFrame, subset=None):
    """
    Identify duplicate rows in a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    subset : list or None, optional
        Column names to consider for duplicate detection.
        If None, all columns are considered.
    
    Returns
    -------
    pd.DataFrame
        DataFrame containing only the duplicate rows.
    """
    return df[df.duplicated(subset=subset, keep=False)]

def drop_duplicates(df: pd.DataFrame, subset=None, keep='first'):
    """
    Remove duplicate rows from a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    subset : list or None, optional
        Column names to consider for duplicate removal.
        If None, all columns are considered.
    keep : {'first', 'last', False}, default 'first'
        Determines which duplicates to keep.
        - 'first' : keep first occurrence
        - 'last' : keep last occurrence
        - False : drop all duplicates
    
    Returns
    -------
    pd.DataFrame
        DataFrame without duplicates.
    """
    return df.drop_duplicates(subset=subset, keep=keep).reset_index(drop=True)
    

def drop_rows_with_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove any rows that contain one or more missing (NaN/None) values.

    Parameters
    ----------
    df : DataFrame
        Input pandas DataFrame.

    Returns
    -------
    DataFrame
        Copy of the DataFrame with rows containing missing values removed.
    """
    return df.dropna()
