
# Objetivo do Desafio #

O objetivo deste desafio é avaliar a capacidade de manipular e analisar dados de forma eficiente utilizando Python e bibliotecas populares como Pandas, além de demonstrar familiaridade com ferramentas da AWS, como o S3. Mostra habilidades em transformar dados, realizar filtragens com base em critérios específicos, criar colunas derivadas e produzir saídas organizadas e úteis.

## Etapas do Desafio ##
 * [Etapa 01 - Script de importação para o bucket](https://github.com/neivis04/PB_CYNTHIA_NEIVA/tree/main/Sprint%201) <br>
 


## Etapa 01: Criação do Bucket ##

 <img src="../Evidencias/Execucao_Desafio/criacao_bucket.png" width="800px">

 <br>

* No console da AWS, criei um bucket para a execução do desafio.


## Etapa 01: Script de Importação para o Bucket ##

<img src="../Evidencias/Execucao_Desafio/script_boto3.png" width="800px">

<br>

Esse código realiza o upload de um arquivo local para um bucket no Amazon S3 usando a biblioteca boto3, que é o SDK oficial da AWS para Python.

 1. Importação da Biblioteca
O código começa importando a biblioteca boto3, que é o SDK oficial da AWS para Python. Essa biblioteca permite interagir com diversos serviços da AWS, incluindo o Amazon S3, que é usado para armazenar e recuperar dados na nuvem.

2. Inicialização do Cliente S3
Em seguida, o código cria um cliente para o serviço S3. Isso é feito fornecendo as credenciais de autenticação, incluindo a chave de acesso, a chave secreta e um token de sessão temporário. Esses dados permitem que o cliente S3 se conecte à AWS e autorize operações no serviço.

3. Configuração do Bucket e do Arquivo
O código define três informações principais: o nome do bucket onde o arquivo será armazenado, o caminho completo do arquivo no sistema local e o nome que o arquivo terá dentro do bucket. Essas informações são essenciais para que o upload seja realizado corretamente.

4. Realização do Upload do Arquivo
Com os dados configurados, o código tenta fazer o upload do arquivo local para o bucket S3. A função usada gerencia automaticamente a transferência de dados para a nuvem, lidando com detalhes técnicos como autenticação, conexão e upload.

5. Tratamento de Erros
Caso ocorra algum problema durante o processo de upload, o código captura o erro e exibe uma mensagem informando o motivo da falha. Isso garante que o programa não seja encerrado abruptamente e fornece informações úteis para corrigir o problema.

## Etapa 02: Manipulação do Dataframe ##

## - Filtrar Dados ##

<img src="../Evidencias/Execucao_Desafio/filtrar_dados.png" width="800px">

<br>
O código organiza e refina os dados para produzir um subconjunto claro e formatado que contém informações relevantes sobre discentes angolanos em mobilidade no campus "JK (Diamantina)"

1. Tratamento de Dados Ausentes
A primeira etapa remove linhas no DataFrame onde a coluna "paisorigem" contém valores nulos. Isso é importante para garantir que a filtragem subsequente funcione corretamente e que os dados utilizados estejam completos e consistentes.

2. Filtragem de Dados
O código aplica um filtro para selecionar somente os registros onde o país de origem é "Angola" e o campus de destino inclui "JK (Diamantina)". Essa filtragem reduz os dados ao subconjunto relevante para a análise.

3. Seleção de Colunas Relevantes
Depois de aplicar o filtro, são escolhidas apenas as colunas que possuem informações essenciais para o objetivo da análise, como o nome do discente, o país de origem, o campus de destino e o período de mobilidade. Isso ajuda a manter o foco nas informações importantes, eliminando colunas desnecessárias.

4. Renomeação de Colunas
As colunas selecionadas são renomeadas para nomes mais descritivos e amigáveis, facilitando a leitura e compreensão dos dados. Por exemplo, "nomediscente" passa a ser "Nome do Discente" e "paisorigem" é alterado para "País de Origem".

## - Funções de Agregação ##

<img src="../Evidencias/Execucao_Desafio/funcao_agregacao.png" width="800px">

<br>

O código serve para identificar e organizar a frequência de discentes por país de origem. Ele padroniza os valores para garantir precisão na contagem e organiza os resultados em ordem crescente para facilitar a interpretação dos dados.

1. Padronização dos Dados na Coluna "paisorigem"
O código aplica uma série de transformações para padronizar os valores da coluna "paisorigem". Primeiramente, os espaços em branco desnecessários nas extremidades dos textos são removidos. Em seguida, todos os valores são convertidos para letras minúsculas para garantir uniformidade e evitar diferenças causadas por capitalização. Por último, o texto é formatado para a capitalização de título, onde a primeira letra de cada palavra é maiúscula. Isso resulta em dados consistentes e uniformes para facilitar análises posteriores.

2. Contagem de Ocorrências por País
A função value_counts() é usada para contar o número de ocorrências de cada país na coluna "paisorigem". Essa contagem indica a quantidade de vezes que cada país aparece no conjunto de dados.

3. Ordenação dos Resultados
Os resultados da contagem são ordenados em ordem crescente, o que organiza os dados de maneira a facilitar a visualização de países menos frequentes primeiro e mais frequentes no final.

## - Funções de Condicional ##

<img src="../Evidencias/Execucao_Desafio/funcao_condicional.png" width="800px">

<br>

Essa etapa adiciona uma informação adicional ao conjunto de dados, permitindo identificar rapidamente os registros relacionados ao ano "2008". Isso é útil para análises ou filtros baseados nesse critério.

1. Preenchimento de Valores Nulos
A coluna periodomobilidade pode conter valores nulos, que podem causar erros ao aplicar operações de string. Para evitar isso, o método fillna("") é usado para substituir valores nulos por strings vazias (""). Isso garante que a operação subsequente funcione sem interrupções.

2. Verificação de Condição
O método str.contains("2008") verifica, linha por linha, se o texto "2008" está presente na coluna periodomobilidade. Esse método retorna um valor booleano (True ou False) para cada linha, dependendo se a condição é atendida.

3. Criação de uma Nova Coluna
Os valores resultantes dessa verificação são armazenados em uma nova coluna chamada inclui_2008. Assim, cada linha do DataFrame passa a ter um indicador que informa se o ano "2008" está mencionado no campo periodomobilidade.

## - Funções de Conversão ##

<img src="../Evidencias/Execucao_Desafio/funcao_conversao.png" width="800px">

<br>

Esse código é usado para transformar intervalos de anos em listas mais estruturadas e facilmente manipuláveis. Isso facilita análises detalhadas, como identificar anos específicos de mobilidade, fazer comparações ou realizar estatísticas sobre períodos de tempo.<br>

1. Definição da Função processar_periodo
A função é criada para processar os valores da coluna periodomobilidade. O objetivo é transformar períodos de mobilidade (normalmente representados como intervalos de anos) em uma lista de anos individuais. A lógica da função é dividida em etapas:

- Verificação de valores nulos: A função verifica se o valor da entrada não é nulo usando pd.notnull(periodo). Se o valor for nulo, retorna uma lista vazia ([]).
- Substituição de separadores: Diferentes formatos de separadores para intervalos de anos (" a ", " – ") são substituídos por um hífen simples ("-"). Isso padroniza o formato do texto.
- Remoção de espaços: O método strip() remove quaisquer espaços desnecessários no início e no final da string.
- Divisão do período: O método split('-') divide o texto com base no hífen, separando os anos do intervalo.
- Limpeza dos anos: A lista resultante é percorrida para remover espaços ao redor de cada elemento.
Se o valor de entrada for nulo, a função retorna uma lista vazia.

## - Funções de Data ##

<img src="../Evidencias/Execucao_Desafio/funcao_data.png" width="800px">

<br>

1. Definição da Função extrair_ano_inicio
Essa função é usada para extrair o primeiro ano de um período descrito na coluna periodomobilidade. Ela funciona da seguinte maneira:

- Verificação de valores nulos: Se o valor da entrada for nulo, retorna None.
- Conversão para string e divisão: Caso o valor não seja nulo, ele é convertido para string (caso não seja já) e dividido com base na vírgula usando o método split(','). O primeiro elemento da divisão (supostamente o ano inicial) é extraído.
- Tratamento de erros: Se a extração falhar devido a um erro de conversão (por exemplo, o texto não é numérico) ou o índice não existir, a função retorna None.

2. Aplicação da Função ao DataFrame
- A função extrair_ano_inicio é aplicada à coluna periodomobilidade usando o método apply(). O resultado é armazenado em uma nova coluna chamada ano_inicio. Essa coluna contém o ano inicial extraído de cada registro, ou None caso não seja possível extrair.

3. Limpeza dos Nomes das Colunas
Os nomes das colunas do DataFrame são tratados para remover espaços em branco indesejados:
- Remoção de espaços: O método str.strip() elimina espaços no início e no final dos nomes das colunas, garantindo que estejam limpos e padronizados.

4. Remoção de Colunas Não Nomeadas
As colunas com nomes que começam com "Unnamed" (geralmente criadas por erros ao ler arquivos CSV com cabeçalhos inadequados) são removidas:
- O método loc[:, ~df.columns.str.contains('^Unnamed')] seleciona todas as colunas, exceto aquelas cujo nome começa com "Unnamed". O caractere ~ atua como um operador de negação.

## - Funções de String ##

<img src="../Evidencias/Execucao_Desafio/funcao_string.png" width="800px">

<br>

O código tem como objetivo limpar, padronizar e preparar os valores da coluna nomediscente para análises ou relatórios. Ao eliminar valores nulos e garantir que os nomes estejam formatados de maneira consistente, torna-se mais fácil realizar operações como filtragem, agrupamento ou exibição de resultados.

1. Verificação da Coluna nomediscente
Antes de realizar qualquer operação, o código verifica se a coluna nomediscente existe no DataFrame. Isso é importante para evitar erros caso a coluna esteja ausente no conjunto de dados. A verificação é feita com a expressão 'nomediscente' in df.columns.

2. Preenchimento de Valores Nulos
Os valores nulos na coluna nomediscente são substituídos por strings vazias ("") usando o método fillna(''). Isso impede que operações de string falhem ao encontrar valores NaN.

3. Limpeza de Strings
As operações seguintes são aplicadas para limpar e padronizar os valores da coluna:

- Remoção de espaços: O método str.strip() elimina espaços extras no início e no final de cada nome.
- Conversão para maiúsculas: O método str.upper() converte todos os caracteres para letras maiúsculas, padronizando a formatação dos nomes.

## - Salvando o DataFrame em um Arquivo CSV ##

<img src="../Evidencias/Execucao_Desafio/salvar_arquivo_csv.png" width="800px">

<br>

1. O código usa o método to_csv() para salvar o DataFrame resultante em um arquivo CSV.

- index=False: Esse parâmetro indica que o índice do DataFrame não será incluído no arquivo CSV. Isso é útil quando o índice não tem relevância como uma coluna nos dados salvos.

## - Finalização do Bucket ##

<img src="../Evidencias/Execucao_Desafio/bucket_final.png" width="800px">

<br>

Após a execução do arquivo de manipulação, enivei os arquivos do desafio para o bucket, sendo assim finalizando o desafio.
