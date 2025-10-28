import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from my_krml_24669044.data.sets import find_duplicates, drop_duplicates, drop_rows_with_missing , convert_column_to_date

import pandas as pd

def test_find_duplicates():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
        "Age": [25, 30, 25, 35, 30]
    })
    duplicates = find_duplicates(df)
    assert len(duplicates) == 4  # Alice and Bob appear twice each

def test_drop_duplicates():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
        "Age": [25, 30, 25, 35, 30]
    })
    cleaned = drop_duplicates(df)
    assert len(cleaned) == 3  # Alice, Bob, Charlie
    

def drop_rows_with_missing():
    df = pd.DataFrame({
    "a": [1, 2, None, 4],
    "b": [5, None, 7, 8],
    })

    print("Original:")
    print(df)

    clean = drop_rows_with_missing(df)
    print("After dropping missing rows:")
    print(clean)

def test_convert_column_to_date_drop_original_flag():
    df = pd.DataFrame({
        "timestamp": ["2025-01-05 10:00:00", "2024-12-31 08:00:00"],
        "val": [5, 10],
    })

    keep_df = convert_column_to_date(df, "timestamp")
    drop_df = convert_column_to_date(df, "timestamp", drop_original=True)

    # Keep version should retain timestamp column
    assert "timestamp" in keep_df.columns
    # Drop version should remove timestamp column
    assert "timestamp" not in drop_df.columns
    # Both should have 'date' and be sorted
    assert list(drop_df["date"]) == sorted(drop_df["date"])
