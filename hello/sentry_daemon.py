import sentry_sdk
from sentry_sdk.integrations.spark import SparkWorkerIntegration
import pyspark.daemon as orginal_daemon
from sentry_sdk import capture_exception
from sentry_sdk import capture_message

if __name__ == "__main__":
  sentry_sdk.init(
    dsn = "https://dc3d919ce65c49528e43198448a06fe1@sentry.cauchy.link/4",
    integrations = [SparkWorkerIntegration()],
    traces_sample_rate = 1.0
  )

  try:
    raise Exception('Example exception in Spark worker')
  except Exception as e:
    capture_exception(e)

  capture_message('Worker starting...')

  original_daemon.manager()
