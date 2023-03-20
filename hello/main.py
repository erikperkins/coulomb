import findspark
findspark.init()

from pyspark.sql import SparkSession
import sentry_sdk
from sentry_sdk.integrations.spark import SparkIntegration
from sentry_sdk import capture_exception
from sentry_sdk import capture_message

if __name__ == "__main__":
  sentry_sdk.init(
    dsn = "https://dc3d919ce65c49528e43198448a06fe1@sentry.cauchy.link/4",
    # integrations = [SparkIntegration()],
    traces_sample_rate = 1.0
  )

  spark = SparkSession.builder.getOrCreate()

  try:
    raise Exception('Example exception in Spark driver')
  except Exception as e:
    capture_exception(e)

  try:
    dataframe = spark.read.json('s3a://orders/*')
  except Exception as e:
    capture_exception(e)

  average = dataframe.agg({'amount': 'avg'})
  average.write.mode("OVERWRITE").json('s3a://results/orders/average')

  capture_message('Job succeeded!')