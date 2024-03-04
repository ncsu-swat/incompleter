#Source: https://stackoverflow.com/questions/67273012/how-to-fix-attributeerror-int-object-has-no-attribute-strip-while-loading-e
local_path= '../../data/RetailStore.xlsx'
out_path= '../../out/hyperstore.csv'

def load_retail_data(local_path,sheet_name):
    return pd.read_excel(
        local_path,
        header=4,
        sheet_name=sheet_name,
        parse_dates=True
    )

def clean_headers(data_frame:pd.DataFrame) -> pd.DataFrame:
    data_frame=data_frame.rename(columns=lambda x:x.strip())
    data_frame=data_frame.rename(columns=lambda x:x.replace('\n',' '))
    data_frame=data_frame.rename(columns=lambda x:x.replace("'",' '))
    data_frame=data_frame.rename(columns=lambda x:x.replace('  ',' '))
    return data_frame

def filter_ship_mode(df):
    return df[(df[ColumnsStore.ship_mode]!= 'Standard Class') & (df[ColumnsStore.ship_mode]!='Second Class')]


def calc_retail_data(local_path,sheet_name):
    retail_data=load_retail_data(local_path,sheet_name)
    retail_clean_headers=clean_headers(retail_data)
    retail_filtered=filter_ship_mode(retail_clean_headers)
    return retail_filtered


if __name__=="__main__":
    df_retail_data=calc_retail_data(local_path,'Orders')
    df_retail_data.to_csv(out_path,index=False)