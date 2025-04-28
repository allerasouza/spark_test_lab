from pyspark.sql import SparkSession
import pytest


@pytest.fixture
def spark():
    yield SparkSession.builder.appName("Debug").getOrCreate()
