import os
import boto3
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurações AWS
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
SESSION_TOKEN = os.getenv("SESSION_TOKEN")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Caminho local e estrutura de destino no S3
LOCAL_DIR = '/app/data.base'
RAW_ZONE_PATH = 'data-lake-da-cynthia/raw/Local/CSV'  # Caminho base no S3

def upload_to_s3(local_file, s3_path):
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
        region_name=AWS_REGION
    )
    try:
        # Fazer upload do arquivo
        s3.upload_file(local_file, BUCKET_NAME, s3_path)
        print(f"Arquivo enviado: {local_file} -> s3://{BUCKET_NAME}/{s3_path}")
    except Exception as e:
        print(f"Erro ao enviar {local_file}: {e}")

def process_and_upload():
    
    if not os.path.exists(LOCAL_DIR):
        print(f"Diretório local não encontrado: {LOCAL_DIR}")
        return

    for root, dirs, files in os.walk(LOCAL_DIR):
        for file in files:
            if file.endswith('.csv'):
                # Determinar a categoria com base no nome do arquivo
                category = 'Movies' if 'movies' in file.lower() else 'Series'
                
                # Criar caminho dinâmico no S3 baseado na data atual
                today = datetime.now()
                s3_path = f"{RAW_ZONE_PATH}/{category}/{today.year}/{today.month:02}/{today.day:02}/{file}"
                
                # Caminho completo local do arquivo
                local_file = os.path.join(root, file)
                
                # Fazer upload para o S3
                print(f"Iniciando upload de {local_file} para s3://{BUCKET_NAME}/{s3_path}")
                upload_to_s3(local_file, s3_path)

if __name__ == "__main__":
    print("Iniciando processo de upload...")
    process_and_upload()
    print("Processo concluído!")
