from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.testing import assertDataFrameEqual

from src.transformations import calculate_sale_price


def test_example(spark):
    # Arrange
    input_schema = StructType([
        StructField("id_venda", IntegerType(), True),
        StructField("produto", StringType(), True),
        StructField("categoria", StringType(), True),
        StructField("quantidade", IntegerType(), True),
        StructField("preco_unitario", FloatType(), True),
        StructField("data_compra", StringType(), True),
        StructField("cliente", StringType(), True),
        StructField("regiao", StringType(), True)
    ])
    input_data = [
        (1, "Notebook", "Eletrônicos", 2, 3500.00, "2023-01-15", "João Silva", "Sudeste"),
        (2, "Mesa", "Móveis", 1, 899.90, "2023-01-16", "Maria Souza", "Sul"),
        (3, "Celular", "Eletrônicos", 3, 1200.00, "2023-01-17", "Carlos Lima", "Nordeste"),
        (4, "Cadeira", "Móveis", 4, 250.50, "2023-01-18", "Ana Costa", "Sudeste"),
        (5, "Monitor", "Eletrônicos", 1, 750.00, "2023-01-19", "Pedro Santos", "Sudeste"),
        (6, "Teclado", "Acessórios", 2, 150.00, "2023-01-20", "Lucia Oliveira", "Norte"),
        (7, "Mouse", "Acessórios", 5, 80.90, "2023-01-21", "Marcos Rocha", "Centro-Oeste"),
        (8, "Notebook", "Eletrônicos", 1, 4200.00, "2023-01-22", "Fernanda Lima", "Sudeste"),
        (9, "Cadeira", "Móveis", 2, 300.00, "2023-01-23", "Ricardo Alves", "Nordeste"),
        (10, "Impressora", "Eletrônicos", 1, 650.00, "2023-01-24", "Patricia Gomes", "Sul")
    ]
    input_df = spark.createDataFrame(input_data, input_schema)
    expected_schema = input_schema = StructType([
        StructField("id_venda", IntegerType(), True),
        StructField("produto", StringType(), True),
        StructField("categoria", StringType(), True),
        StructField("quantidade", IntegerType(), True),
        StructField("preco_unitario", FloatType(), True),
        StructField("data_compra", StringType(), True),
        StructField("cliente", StringType(), True),
        StructField("regiao", StringType(), True),
        StructField("sale_price", FloatType(), True),
    ])
    expected_data = [
        (1, "Notebook", "Eletrônicos", 2, 3500.00, "2023-01-15", "João Silva", "Sudeste", 7000.0),
        (2, "Mesa", "Móveis", 1, 899.90, "2023-01-16", "Maria Souza", "Sul", 899.90),
        (3, "Celular", "Eletrônicos", 3, 1200.00, "2023-01-17", "Carlos Lima", "Nordeste", 3600.0),
        (4, "Cadeira", "Móveis", 4, 250.50, "2023-01-18", "Ana Costa", "Sudeste", 1002.0),
        (5, "Monitor", "Eletrônicos", 1, 750.00, "2023-01-19", "Pedro Santos", "Sudeste", 750.0),
        (6, "Teclado", "Acessórios", 2, 150.00, "2023-01-20", "Lucia Oliveira", "Norte", 300.0),
        (7, "Mouse", "Acessórios", 5, 80.90, "2023-01-21", "Marcos Rocha", "Centro-Oeste", 404.5),
        (8, "Notebook", "Eletrônicos", 1, 4200.00, "2023-01-22", "Fernanda Lima", "Sudeste", 4200.0),
        (9, "Cadeira", "Móveis", 2, 300.00, "2023-01-23", "Ricardo Alves", "Nordeste", 600.0),
        (10, "Impressora", "Eletrônicos", 1, 650.00, "2023-01-24", "Patricia Gomes", "Sul", 650.0),
    ]
    expected_df = spark.createDataFrame(expected_data, expected_schema)

    # Act
    actual_df = calculate_sale_price(input_df)

    # Assert
    assertDataFrameEqual(actual_df, expected_df)
