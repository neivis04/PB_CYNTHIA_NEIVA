# Usa uma imagem base com Python
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script Python para dentro do container
COPY hash.py .

# Define o comando padrão para executar o script
CMD ["python", "hash.py"]
