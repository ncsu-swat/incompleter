#Source: https://stackoverflow.com/questions/56821579/pandas-groupby-agg-throws-typeerror-aggregate-missing-1-required-positional
qt_dy.groupby('date').agg(std_qty=('qty','std'),mean_qty=('qty','mean'),)