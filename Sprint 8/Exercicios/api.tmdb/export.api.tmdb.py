import os
import json
import requests
import pandas as pd
from datetime import datetime

# Definindo o caminho para salvar os arquivos CSV
SAVE_DIR_CSV = 'C:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 8/Exercicios/api.tmdb/data.base/filmes_tratados1.csv'

# Configuração da API TMDB
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL_MOVIE = "https://api.themoviedb.org/3/discover/movie"

# Parâmetros de consulta para buscar filmes
BASE_PARAMS = {
    "api_key": API_KEY,
    "language": "pt-BR",
    "include_adult": False,
    "include_video": False,
    "with_genres": "16,35",  # Gêneros: Animação e Comédia
    "primary_release_date.lte": "2023-12-31",  # Para pegar filmes até 2023
    "page": 1,
}

# Função para buscar dados da API TMDB
def fetch_data(url, tipo):
    page = 1
    records = []

    while len(records) < 100:
        params = BASE_PARAMS.copy()
        params["page"] = page

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            # Adicionar registros até atingir 100
            for result in results:
                if len(records) < 100:
                    records.append(result)
                else:
                    break

            print(f"[{tipo}] Página {page} processada. Total de registros: {len(records)}")
            page += 1

            if page > data.get("total_pages", 1):
                break
        else:
            print(f"Erro ao buscar dados ({tipo}): {response.status_code}")
            break

    return records

# Função para salvar os dados tratados no formato CSV
def process_and_save(data):
    # Converter os dados para um DataFrame
    df = pd.DataFrame(data)

    # Verificar se a coluna 'overview' existe antes de fazer o filtro
    if 'overview' in df.columns:
        # Excluir linhas onde a coluna 'overview' está vazia
        df_cleaned = df[df['overview'] != '']
    else:
        # Se não houver a coluna, ignoramos a exclusão de 'overview' vazia
        df_cleaned = df

    # Excluir linhas nulas
    df_cleaned = df_cleaned.dropna()

    # Converter a coluna 'release_date' para datetime, caso exista
    if 'release_date' in df_cleaned.columns:
        df_cleaned['release_date'] = pd.to_datetime(df_cleaned['release_date'], errors='coerce')

    # Salvar o DataFrame tratado em um arquivo CSV
    df_cleaned.to_csv(SAVE_DIR_CSV, index=False)

    print(f"Tratamento concluído e arquivo salvo como CSV em: {SAVE_DIR_CSV}")

# Função principal
def main():
    print("Iniciando a coleta de dados...")

    # Coletar dados de filmes
    filmes = fetch_data(BASE_URL_MOVIE, "filmes")

    # Processar e salvar os dados tratados
    process_and_save(filmes)

if __name__ == "__main__":
    main()
