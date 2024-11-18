import pandas as pd

df = pd.DataFrame({
    'nomediscente': ['Shaban Mirco Burgoa', 'Andrea de Fátima Xavier', 'Elder Patrik Paiva', 'Adelia Isaura Cainda'],
    'paisorigem': ['Angola', 'Angola', 'Brasil', 'Angola'],
    'campusdestino': ['JK (Diamantina)', 'JK (Diamantina)', 'JK (Diamantina)', 'Outro Campus'],
    'periodomobilidade': ['2020,2021', '2019,2020', '2020,2021', '2021,2022']
})

# Filtro de Dados
df = df.dropna(subset=['paisorigem'])

# Filtrar os dados de interesse (Angola e campus destino "JK (Diamantina)")
filtro = df[(df['paisorigem'] == 'Angola') & (df['campusdestino'].str.contains('JK (Diamantina)', regex=False))]

# Selecionar apenas as colunas mais relevantes
colunas_relevantes = ['nomediscente', 'paisorigem', 'campusdestino', 'periodomobilidade']
filtro_organizado = filtro[colunas_relevantes]

# Renomear colunas para melhor visualização
filtro_organizado = filtro_organizado.rename(columns={
    'nomediscente': 'Nome do Discente',
    'paisorigem': 'País de Origem',
    'campusdestino': 'Campus de Destino',
    'periodomobilidade': 'Período de Mobilidade'
})

# Funções de Agregação
df['paisorigem'] = df['paisorigem'].str.strip().str.lower().str.title()
contagem_pais = df['paisorigem'].value_counts().sort_values()

# Função Condicional
df['inclui_2008'] = df['periodomobilidade'].fillna("").str.contains("2008")

# Função Conversão
def processar_periodo(periodo):
    if pd.notnull(periodo):
        periodo = periodo.replace(' a ', '-').replace(' – ', '-').strip()
        anos = [ano.strip() for ano in periodo.split('-')]
        return anos
    return []

df['anos_lista'] = df['periodomobilidade'].apply(processar_periodo)

# Função Data
def extrair_ano_inicio(periodo):
    if pd.notnull(periodo):
        try:
            return int(str(periodo).split(',')[0])
        except (ValueError, IndexError):
            return None
    return None

df['ano_inicio'] = df['periodomobilidade'].apply(extrair_ano_inicio)

# Limpeza das colunas
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Função String
if 'nomediscente' in df.columns:
    df['nomediscente'] = df['nomediscente'].fillna('').str.strip().str.upper()

# Salvar o DataFrame resultante em um arquivo CSV
df.to_csv('/Users/STTE/OneDrive/Área de Trabalho/cynthia/PB_CYNTHIA_NEIVA/Sprint 5/Desafio/dados_manipulados.csv', index=False)

