# importando bibliotecas necessárias
import pandas as pd
from joblib import dump # pip install joblib

caminho = 'D:/unigex/e9-2-18-unigex-cluster-projeto05/util/data/'

# criando um dicionário com o nome dos arquivos 
arquivos = {
    'categorias':'categorias.csv',
    'chats':'chats.csv',
    'clientes': 'clientes.csv',
    'contas_pagar':'contas-a-pagar.csv',
    'contas_receber':'contas-a-receber.csv',
    'movimento_contabil':'movimento-contabil.csv',
    'movimento_financeiro':'movimento-financeiro.csv',
    'naturezas_financeiras':'naturezas-financeiras.csv',
    'plano_contas':'plano-de-contas.csv',
    'produtos':'produtos.csv',
    'tickets':'tickets.csv',
    'unidades':'unidades.csv',
    'vendas':'vendas.csv',
    'vendedores':'vendedores.csv'
 } # talvez refatorar isso aqui?
  
# loop(for) para ler os arquivos.csv, os caminhos e salvar com o dump do joblib em formato .z(arquivo binário)
for nome, arquivo_nome in arquivos.items():

    df = pd.read_csv(caminho+arquivo_nome) 
    dump(df, f'util/data/df_{nome}.z')

    print(f' arquivo [{arquivo_nome}.csv] carregado') # ver se todos os arquivos foram carregados corretamente






