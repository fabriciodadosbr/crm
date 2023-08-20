import os
import pandas as pd
import sqlalchemy

# Login no localhost
user = 'root' #Login
psw = '1234' #Senha
host ='localhost' #ip/host/dns
port = '3306' # Porta
str_connection = 'mysql+pymysql://{user}:{psw}@{host}:{port}'


# Endereços d enderço do projeto e subpastas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')


# Compressão de lista
files_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]


def data_quality(x):
    if type(x) == str:
        return x.replace("\n","").replace("\r","")
    else:
        return x

# Abrindo conexão com o banco
str_connection = str_connection.format(user=user, psw=psw, host=host, port=port)
connection = sqlalchemy.create_engine(str_connection)


# Para cada arquivo é realizada uma inserção no banco de dados mySQL
for i in files_names:
    print(i)
    df_tmp = pd.read_csv(os.path.join(DATA_DIR, i)).fillna('')

    for c in df_tmp.columns:
        df_tmp[c] = df_tmp[c].apply(data_quality)

    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset", "").lower()
    df_tmp.to_sql(table_name,connection, schema='analytics',if_exists= 'replace',index=False)

