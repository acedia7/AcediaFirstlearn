import pandas as pd
from sqlalchemy import create_engine

file1 = r'./data_new.csv'
df1 = pd.read_csv(file1)
engine = create_engine("mysql+pymysql://root:qwe123@/spyder_one")
df1.to_sql('data_school', con=engine, if_exists='replace', index=False)