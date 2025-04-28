from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def calculate_sale_price(df) -> DataFrame:
    transformed_df = df.withColumn(
        "sale_price",
        col("quantidade") * col("preco_unitario")
    )
    temp_df = transformed_df.collect()
    print(transformed_df.explain(True))
    qe = transformed_df._jdf.queryExecution()
    print(qe.optimizedPlan())  # Plano otimizado
    print(qe.executedPlan())  # Plano físico
    return transformed_df
