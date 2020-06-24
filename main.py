import pandas as pd
import numpy as np
import matplotlib as mpl
import pprint

import clean


def timedeltas_hist_bylength(later, before):
    """
    later: later datetimes, before: previous datetimes
    """
    intervals = [x for x in list(later-before)]
    intervals = pd.to_numeric(intervals, errors='ignore')
    intervals = pd.DataFrame({'interval': intervals})
    intervals = (intervals / np.timedelta64(1, 's')).astype(int)
    print("\n"+"#"*50)
    print("Intervals:")
    print(intervals)
    intervals.hist(bins=20)
    return None


def timedeltas_hist_times(df, error_values=[999], criteria_name=None, criteria=None):
    """
    Show histograms by hour, weekday, etc.
    Criteria: list of criteria in another column
    """
    df_ = clean.splitdatetime(df, 'entry_date')
    df__ = clean.clean_column_pair(df_, 'age', 'entry_date', error_values)
    df__.hist(column='hour', bins=24)
    df__.hist(column='weekday', bins=7)

    if criteria_name is not None and criteria is not None:
        for c in criteria[:5]:
            print("Filtering by criteria:", criteria_name, "=", c)
            d_sub = df__.loc[df[criteria_name] == c]
            d_sub.hist(column='hour', bins=24)
            d_sub.hist(column='weekday', bins=7)

    return None


def main ():
    FILENAME = 'xrays_visits.csv'
    DELIMITER = ","
    ERROR_VALUES = [999]
    DEPARTMENTS = list(range(199))

    d = clean.convert(FILENAME, DELIMITER)
    df1 = clean.getdatetimes(d[0], 'entry_date', 'exit_date', ERROR_VALUES)

    timedeltas_hist_bylength(df1[1], df1[0])
    timedeltas_hist_times(d[0], ERROR_VALUES, "department", DEPARTMENTS)


    main()
