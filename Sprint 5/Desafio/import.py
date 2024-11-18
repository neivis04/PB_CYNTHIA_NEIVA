import boto3

# Inicializar o cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id='ASIARHQBNIL2NJTOZCUV',
    aws_secret_access_key='lIWvzSoFgsgTIJ5Q69+n7vVcb3eKn5wSTgqBZQBL',
    aws_session_token='IQoJb3JpZ2luX2VjEMf//////////wEaCXVzLWVhc3QtMSJIMEYCIQC2PFc3Lv88fQ7D4BlvD+RhF2UfPwU2foFXT3K7LCcy6gIhAPtpbBI5pNrrbMrYqnozJu3YIYfFWDyblpwsjL/1DKTtKp8DCGAQABoMMDg0ODI4NTcwMzU2Igys1w/fepya31AIfbEq/AJ2qulmH4B6DCQd1M1Kg581u+Tb7UH4V2LBmonaxP2zrtLx8SFwtJLtsX9Z9txWb3aIbdAptnBG5dlGQ9ybMi3XzMNza1m8NeajVOmFPlEzp9AlrA89NzEsU3WtSkoz4ZQdn81Jwa1NTunQaVV0Daeaw/odEaysoiYYBeQfB4ht+NvLT3mEtzuUf0RqQaaBLlXHfWpsrqmTbDdAAnvhcal1Vik0hCN0uWrEaVwL57DaraeKRDU/GEMEb8Kz987mw5FJjFGivu3umc/lPTjTryUTSk2UErJ+miUJ7NbADKpbN3GUiiUtBq6KYx2GTnfidlLZD2wBBeyptS/Ixg36YBFV+1v3//R/bZDG238MJj/rvE68BKZau+VeJ2qb+7iaqSqd9GXZOuWxmeAyv3kub/O5dbzaRigmj/QokUGFUkN20kLQIiGTq03TN3fBinCp8BYwzYto+aWbGCPBjsfArbtd5kup8hIr9W+WmA5Zl4dCOSKuebzxblFAQpJOvDC+ou25BjqlAVx7GNM/195y4e+U0MW6BJEXl2IF4wPLY8GYLlGRsUogAeAck5pItiHKnk4cNAHiGRuByf91C0Jcd6sbPlz//YUAKE+r9vKHlOTwuLpS37J80XXu+z62Z57NT3CKzE/cae8F8ppPOCsxaewgGzy4xJq80/6ccQ+Ix3eFMTkFT4q95gzOs1oG1OD2d3djL7AnBMHAm0F3/b9XIkOUcKkzoxrPQ+f5IA==',
)

# Nome do bucket e arquivo
bucket_name = 'desafio.sprint05'
local_file_path = r'c:/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 5/Desafio/dados.csv'
file_key = 'dados.csv'  # Nome com o qual será salvo no bucket

try:
    # Fazer upload do arquivo
    s3.upload_file(local_file_path, bucket_name, file_key)
    print(f"Arquivo {local_file_path} enviado com sucesso para o bucket {bucket_name} com o nome {file_key}.")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")
