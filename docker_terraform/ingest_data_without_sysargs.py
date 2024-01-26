from time import time
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df_iter = pd.read_csv('green_tripdata_2019-09.csv', iterator=True, chunksize=100000)
df = next(df_iter)

lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

#  adding the column names
df.head(n=0).to_sql(name="green_taxi_data", con=engine, if_exists="replace")

# adding the first batch of rows
df.to_sql(name="green_taxi_data", con=engine, if_exists="append")

while True:
	#t_start = time()

	df = next(df_iter)

	lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
	lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

	df.to_sql(name="green_taxi_data", con=engine, if_exists="append")

	#t_end = time()

	#print('Inserted another chunk... took %.3f second(s)' % (t_end - t_start))
