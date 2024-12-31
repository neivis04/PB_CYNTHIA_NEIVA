import pandas as pd
import json

# Definindo os caminhos dos arquivos
LOCAL_DIR = 'C:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 7/Desafio/data.base/filmes_comedia_animacao_2024-12-16.json'
SAVE_DIR_JSON = 'C:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 8/Desafio/data.base/filmes_tratados.json'
SAVE_DIR_CSV = 'C:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 8/Desafio/data.base/filmes_tratados.csv'

# Carregar o arquivo JSON
with open(LOCAL_DIR, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Converter para DataFrame
df = pd.DataFrame(data)

# Excluir linhas nulas
df_cleaned = df.dropna()

# Excluir linhas onde a coluna 'overview' está vazia
df_cleaned = df_cleaned[df_cleaned['overview'] != '']

# Converter a coluna 'release_date' para datetime
df_cleaned['release_date'] = pd.to_datetime(df_cleaned['release_date'], errors='coerce')

# Salvar o DataFrame tratado em um novo arquivo JSON
df_cleaned.to_json(SAVE_DIR_JSON, orient='records', lines=True)

# Ou salvar como CSV
df_cleaned.to_csv(SAVE_DIR_CSV, index=False)

print("Tratamento concluído e arquivos salvos com sucesso!")