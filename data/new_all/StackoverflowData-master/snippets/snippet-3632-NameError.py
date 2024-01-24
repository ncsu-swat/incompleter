#Source: https://stackoverflow.com/questions/70980690/aws-glue-attributeerror-dataframe-object-has-no-attribute-to-datetime-cus
def MyTransform (glueContext, dfc) -> DynamicFrameCollection:
    import datetime
    df = dfc.select(list(dfc.keys())[0]).toDF()
    df['submissionTime'] = df.to_datetime(df.partition_0.str[-19:])
    df.sort_values('submissionTime').drop_duplicates('Id',keep='last')
    return(DynamicFrameCollection({"CustomTransform0": dyf_filtered}, glueContext))     