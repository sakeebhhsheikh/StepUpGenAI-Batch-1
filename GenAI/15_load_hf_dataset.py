import pandas as pd

df = pd.read_parquet("hf://datasets/rag-datasets/rag-mini-wikipedia/data/passages.parquet/part.0.parquet")

print(df.head())

documents = df.iloc[:,0].values.tolist()
print(documents[:5])