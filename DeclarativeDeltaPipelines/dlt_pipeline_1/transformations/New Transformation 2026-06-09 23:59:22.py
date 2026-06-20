import dlt

@dlt.table(
    name='demo_stream_table'
)
def demo_stream_table():
    df=spark.readStream.table('databrickscatalog.sliver.sales_sliver')
    return df

# creating a Materialized view
@dlt.table(
    name='demo_mat_view'
    )
def demo_mat_view():
    df=spark.read.table('databrickscatalog.sliver.sales_sliver')
    return df

@dlt.view(
    name='demo_batch_view'
    )
def demo_view():
    df=spark.read.table('databrickscatalog.sliver.sales_sliver')
    return df

@dlt.view(
    name='demo_stream_view'
    )
def demo_view():
    df=spark.readStream.table('databrickscatalog.sliver.sales_sliver')
    return df
