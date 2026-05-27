import dlt

# create a stream table
@dlt.table
def demo_stream_table():
  df=spark.readStream.table("databrickscatalog.sliver.sales_sliver")
  return df

#create a materlized view
@dlt.table
def demo_mat_view():
  df=spark.read.table("databrickscatalog.sliver.sales_sliver")
  return df

#create temp view(batch)
@dlt.view
def demo_batch_temp_view():
  df=spark.read.table("databrickscatalog.sliver.sales_sliver")
  return df

  #create temp view(stream)
@dlt.view
def demo_stream_temp_view():
  df=spark.readStream.table("databrickscatalog.sliver.sales_sliver")
  return df
