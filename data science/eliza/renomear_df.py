import pandas as pd
from joblib import load, dump

# Corrigido o caminho para o arquivo
df_clientes = load('../../util/data/df_clientes.z')

# Renomear colunas
df_clientes.rename(columns={
    'zk': 'codigo',
    'tidfisc': 'id_fiscal',
    'nent': 'nome_entidade',
    'nentf': 'nome_ent_fiscal',
    'cnatt': 'categoria',
    'tidfisc2': 'id_fiscal_2',
    'tidfisc3': 'id_fiscal_3',
    'cicms': 'contribuinte_icms'
}, inplace=True)

# Salvar novamente
dump(df_clientes, '../../util/data/df_clientes.z')