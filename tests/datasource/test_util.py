import pandas as pd
import pytest

from great_expectations.execution_engine.pandas_execution_engine import (
    hash_pandas_dataframe,
)


@pytest.mark.unit
def test_hash_pandas_dataframe_hashable_df():
    data = [{"col_1": 1}]
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data)
    assert hash_pandas_dataframe(df1) == hash_pandas_dataframe(df2)


@pytest.mark.unit
def test_hash_pandas_dataframe_unhashable_df():
    data = [{"col_1": {"val": 1}}]
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data)
    assert hash_pandas_dataframe(df1) == hash_pandas_dataframe(df2)
