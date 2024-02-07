-- Creating external table referring to gcs path
CREATE EXTERNAL TABLE `dtc-de-course-412201.ny_taxi.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_zoomcamp_data_lake_new/green_taxi_trip_data/green_tripdata_2022-*.parquet']
);

SELECT count(*) 
FROM dtc-de-course-412201.ny_taxi.external_green_tripdata;

SELECT count(*) AS trip_amount
FROM dtc-de-course-412201.ny_taxi.external_green_tripdata
WHERE fare_amount=0;

SELECT count(DISTINCT PULocationID) 
FROM dtc-de-course-412201.ny_taxi.external_green_tripdata;

SELECT count(DISTINCT PULocationID) 
FROM dtc-de-course-412201.green_trip_data.green_taxi;

--TABLE WITH PARTITION 
CREATE OR REPLACE TABLE dtc-de-course-412201.ny_taxi.external_green_tripdata_PC
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM dtc-de-course-412201.green_trip_data.green_taxi;

--QUERY ON PARTITION CLUSTER DATA
SELECT DISTINCT PUlocationID FROM dtc-de-course-412201.ny_taxi.external_green_tripdata_PC WHERE
DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' and '2022-06-30';

--QUERY ON NON-PARTITION
SELECT DISTINCT PUlocationID FROM dtc-de-course-412201.green_trip_data.green_taxi WHERE
DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' and '2022-06-30'
