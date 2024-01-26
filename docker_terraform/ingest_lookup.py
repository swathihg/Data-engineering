from time import time
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df = pd.read_csv('taxi+_zone_lookup.csv', iterator=True)

#  adding the column names
df.head(n=0).to_sql(name="taxi_zone_lookup", con=engine, if_exists="replace")

# adding the first batch of rows
df.to_sql(name="taxi_zone_lookup", con=engine, if_exists="append")

