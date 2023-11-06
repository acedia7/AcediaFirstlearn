import pandas as pd
from sqlalchemy import create_engine

file = r'./calender.csv'
df = pd.read_csv(file)


# 连接数据库
engine = create_engine("mysql+pymysql://root:qwe123@/spyder_one")
df.to_sql('calender', con=engine, if_exists='replace', index=False)

