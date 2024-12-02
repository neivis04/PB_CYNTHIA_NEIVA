# Usar uma imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo .env para o contêiner
COPY .env /app/.env

# Copiar o script Python e o arquivo .env para o container
COPY upload_s3.py ./

# Instalar dependências do Python
RUN pip install boto3 python-dotenv

# Montar volume externo para os dados
VOLUME ["/app/data.base"]

# Comando padrão do container
CMD ["python", "upload_s3.py"]
