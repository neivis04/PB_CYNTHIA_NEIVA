import os
import json
import boto3
import requests
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis do ambiente
load_dotenv()

# Configuração da API TMDB
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL_MOVIE = "https://api.themoviedb.org/3/discover/movie"
BASE_URL_TV = "https://api.themoviedb.org/3/discover/tv"

# Configurações AWS
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
SESSION_TOKEN = os.getenv("SESSION_TOKEN")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=SESSION_TOKEN,
    region_name=AWS_REGION
)

# Diretório local para salvar os arquivos JSON
LOCAL_DIR = 'C:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 7/Desafio/cod.lambdadata.base'
os.makedirs(LOCAL_DIR, exist_ok=True)

# Caminho da camada RAW no S3
RAW_ZONE_PATH = 'data-lake-da-cynthia/raw/TMDB/JSON'

# Parâmetros base para busca na API
BASE_PARAMS = {
    "api_key": API_KEY,
    "language": "pt-BR",
    "include_adult": False,
    "include_video": False,
    "with_genres": "16,35",  # Animação e Comédia
    "primary_release_date.lte": "2023-12-31",
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

# Função para salvar dados localmente
def save_to_local(data, tipo):
    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{tipo}_comedia_animacao_{today}.json"
    file_path = os.path.join(LOCAL_DIR, file_name)

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Arquivo salvo localmente: {file_path}")
    return file_path

# Função para fazer upload para o S3
def upload_to_s3(local_file, s3_path):
    try:
        s3_client.upload_file(local_file, BUCKET_NAME, s3_path)
        print(f"Arquivo enviado: {local_file} -> s3://{BUCKET_NAME}/{s3_path}")
    except Exception as e:
        print(f"Erro ao enviar {local_file}: {e}")

# Função principal
def lambda_handler(event=None, context=None):
    print("Iniciando coleta de dados e upload para o S3...")

    # Coleta dados de filmes
    filmes = fetch_data(BASE_URL_MOVIE, "filmes")
    local_filmes = save_to_local(filmes, "filmes")

    # Coleta dados de séries
    series = fetch_data(BASE_URL_TV, "series")
    local_series = save_to_local(series, "series")

    # Estrutura do caminho no S3
    today = datetime.now()
    s3_filmes_path = f"{RAW_ZONE_PATH}/Movies/{today.year}/{today.month:02}/{today.day:02}/{os.path.basename(local_filmes)}"
    s3_series_path = f"{RAW_ZONE_PATH}/Series/{today.year}/{today.month:02}/{today.day:02}/{os.path.basename(local_series)}"

    # Upload dos arquivos para o S3
    upload_to_s3(local_filmes, s3_filmes_path)
    upload_to_s3(local_series, s3_series_path)

    print("Processo concluído com sucesso!")

    return {
        "statusCode": 200,
        "body": json.dumps("Dados coletados e armazenados na camada raw do S3 com sucesso!")
    }

if __name__ == "__main__":
    lambda_handler()
