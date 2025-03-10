"""
Test for issue 249:
https://github.com/pandas-profiling/pandas-profiling/issues/249
"""
import pandas as pd

from pandas_profiling import ProfileReport


def test_issue249():
    df = pd.DataFrame(data=[[1], [2]], index=["foo", 1], columns=["a"])
    report = ProfileReport(df, explorative=True)
    assert type(report.config.title) == str
    assert len(report.to_html()) > 0
