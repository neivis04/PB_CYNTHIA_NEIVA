import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis do ambiente
load_dotenv()

# Configuração da API TMDB
API_KEY = os.getenv("TMDB_API_KEY")  # Chave da API TMDB
BASE_URL_MOVIE = "https://api.themoviedb.org/3/discover/movie"
BASE_URL_TV = "https://api.themoviedb.org/3/discover/tv"

# Parâmetros base para busca
BASE_PARAMS = {
    "api_key": API_KEY,
    "language": "pt-BR",
    "include_adult": False,
    "include_video": False,
    "with_genres": "16,35",  # 16 = Animação, 35 = Comédia
    "primary_release_date.lte": "2023-12-31",
    "page": 1,
}

# Diretório local para salvar JSONs
LOCAL_DIR = "C:/Users/STTE\OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 7/Desafio/data.base"
os.makedirs(LOCAL_DIR, exist_ok=True)

# Função para buscar dados da API TMDB
def fetch_data(url, tipo):
    page = 1
    records = []  # Lista para armazenar os registros

    while len(records) < 100:
        params = BASE_PARAMS.copy()
        params["page"] = page

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            # Adicionar registros à lista (limitando a 100 no total)
            for result in results:
                if len(records) < 100:
                    records.append(result)
                else:
                    break  # Parar ao atingir 100 registros

            print(f"[{tipo}] Página {page} processada. Total de registros: {len(records)}")
            page += 1

            # Parar caso não haja mais páginas
            if page > data.get("total_pages", 1):
                break
        else:
            print(f"Erro ao buscar dados ({tipo}): {response.status_code}")
            break

    # Salvar registros em um único arquivo JSON
    save_to_json(records, tipo)

# Função para salvar dados em JSON
def save_to_json(data, tipo):
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(LOCAL_DIR, f"{tipo}_comedia_animacao_{today}.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Arquivo salvo ({tipo}): {file_path} com {len(data)} registros")

if __name__ == "__main__":
    print("Iniciando coleta de dados da API TMDB...")

    # Coletar filmes
    fetch_data(BASE_URL_MOVIE, "filmes")

    # Coletar séries
    fetch_data(BASE_URL_TV, "series")

    print("Dados coletados com sucesso!")
