#Source: https://stackoverflow.com/questions/75575529/how-to-resolve-typeerror-expected-strexpected-type-typeerror-expected
source_row_data = [float(col_value) if col_value != "-" else 0 for col_value in source_row_data]