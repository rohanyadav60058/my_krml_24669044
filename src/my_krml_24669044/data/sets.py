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
    
    
    
def convert_column_to_date(
    df: pd.DataFrame,
    column: str,
    new_col: str = "date",
    drop_original: bool = False
) -> pd.DataFrame:
    """
    Convert any datetime-like column to date format and sort the DataFrame by it.

    Parameters
    ----------
    df : DataFrame
        Input pandas DataFrame.
    column : str
        Name of the column to convert (e.g., "timestamp", "created_at").
    new_col : str, default="date"
        Name of the new column to store converted dates.
    drop_original : bool, default=False
        If True, the original timestamp column is removed from the DataFrame.

    Returns
    -------
    DataFrame
        Copy of the DataFrame with a new date column added and sorted by it.

    Notes
    -----
    - Invalid or unparsable datetime values are coerced to NaT and dropped.
    - The DataFrame is sorted by the new date column in ascending order.
    - If `drop_original=True`, the original timestamp column is removed.
    """
    df = df.copy()
    df[new_col] = pd.to_datetime(df[column], errors="coerce").dt.date
    df = df[df[new_col].notna()]  # drop rows with invalid dates
    df = df.sort_values(by=new_col).reset_index(drop=True)

    if drop_original:
        df = df.drop(columns=[column], errors="ignore")

    return df
