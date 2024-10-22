# Tratamento de Dados - Etapa 01 #

![Img 1](Evidencias/Execucao_do_Desafio/etapa01.png)

* A função pd.read_csv() é usada para ler dados de um arquivo CSV e armazená-los em um DataFrame (df), que é uma estrutura de dados similar a uma tabela, contendo linhas e colunas.
* O nome do arquivo 'googleplaystore.csv' sugere que estamos lidando com um dataset contendo informações sobre aplicativos da Google Play Store, como nome, categoria, nota, número de downloads, etc.
* df.drop_duplicates(): Remove todas as linhas idênticas dentro do DataFrame, ou seja, elimina entradas completamente repetidas.
* A função len() é usada para contar o número de linhas antes e depois da remoção de duplicatas, permitindo que o usuário saiba quantas entradas redundantes foram eliminadas.

  
# Gráfico Barras dos 5 apps Mais Instalados - Etapa 02 #

![Img 2](Evidencias/Execucao_do_Desafio/etapa02_1.png)
<br>
![Img 3](Evidencias/Execucao_do_Desafio/etapa02_2.png)
<br>
![Img 4](Evidencias/Execucao_do_Desafio/grafico_etapa02.png)

O código tem como objetivo carregar dados de um arquivo CSV contendo informações de aplicativos da Google Play Store, realizar algumas transformações e, em seguida, visualizar os 5 aplicativos mais instalados por meio de um gráfico de barras. Abaixo está a análise detalhada de cada parte do código.

* Remove caracteres indesejados como , e +, que são comuns na contagem de instalações. Substitui valores não numéricos, como "Free", por 0. Converte os dados para o tipo inteiro (int) para facilitar operações matemáticas.
* Verifica se o DataFrame tem pelo menos 5 aplicativos. Se não, o processo é interrompido.
* Ordena o DataFrame pelos valores da coluna Installs em ordem decrescente. Seleciona os 7 primeiros aplicativos para exibição.
* Escolhe uma paleta personalizada de cores para deixar o gráfico mais atraente. A figura é dimensionada para 10x6 polegadas, garantindo que o gráfico fique bem visível.
* Cria um gráfico de barras usando os nomes dos aplicativos e o número de instalações. Com título, rótulos nos eixos e uma grade leve para facilitar a leitura dos valores.

# Gráfico Pie Chart das Categorias Mais Existentes - Etapa 03 #

![Img 4](Evidencias/Execucao_do_Desafio/etapa03_1.png)
<br>
![Img 5](Evidencias/Execucao_do_Desafio/etapa03_2.png)
<br>
![Img 6](Evidencias/Execucao_do_Desafio/grafico_etapa03.png)

Este código tem como objetivo analisar a distribuição das categorias de aplicativos da Google Play Store e visualizar as 6 principais categorias em um gráfico de pizza, agrupando as demais em "Outros".

* value_counts() conta o número de ocorrências de cada categoria.
* Seleciona as 6 categorias mais frequentes. As demais categorias são somadas e rotuladas como “Outros”.
* Define o tamanho do gráfico (10x7 polegadas). Utiliza uma paleta de cores quentes para deixar o gráfico visualmente atraente.
* Exibe percentuais com autopct='%1.1f%%'. Rotaciona o gráfico para começar em 90 graus para melhor legibilidade. Define uma distância entre o percentual e o centro do gráfico para melhorar a estética.

# App Mais Caro do Dataset - Etapa 04 #

![Img 7](Evidencias/Execucao_do_Desafio/etapa04.png)
<br>
![Img 8](Evidencias/Execucao_do_Desafio/resultado_etapa04.png)

Este código realiza a leitura e manipulação de dados de aplicativos da Google Play Store para identificar o app mais caro e converter seu preço de dólares para reais, utilizando a taxa de câmbio fornecida. Abaixo está a análise detalhada de cada parte do código.

* Define a taxa de câmbio atual para converter o preço de dólares para reais.
* Remove o caractere $ da coluna "Price". Converte os valores para float, ignorando erros com errors='coerce', o que transforma valores inválidos em NaN.
* Remove linhas onde o valor na coluna "Price" é NaN.
* Usa idxmax() para encontrar o índice do app com o maior preço e obtém suas informações
* Converte o preço do app de dólares para reais usando a taxa de câmbio definida.
* Imprime o nome, categoria, preço em dólares e reais do app mais caro.


# Apps Classificados como "Mature 17+" - Etapa 05 #

![Img 9](Evidencias/Execucao_do_Desafio/etapa05.png)

Este código tem como objetivo analisar um conjunto de dados sobre aplicativos da Google Play Store para identificar quantos deles são classificados como "Mature 17+". Ele realiza a leitura dos dados, remove duplicatas, filtra as classificações e exibe o resultado. Abaixo está a análise detalhada de cada parte do código.

* Filtra o DataFrame para incluir apenas os aplicativos com classificação "Mature 17+" na coluna Content Rating.
* Usa shape[0] para contar o número de linhas (apps) no DataFrame filtrado.
* Imprime o total de aplicativos com a classificação "Mature 17+".


# Lista dos 10 Apps com Mais Reviews - Etapa 06 #

![Img 10](Evidencias/Execucao_do_Desafio/etapa06.png)
<br>
![Img 11](Evidencias/Execucao_do_Desafio/resultado_etapa06.png)

O código lê um conjunto de dados sobre aplicativos da Google Play Store, limpa e processa os dados para identificar os 10 aplicativos com o maior número de avaliações (reviews). Abaixo está a análise detalhada de cada parte do código.

* Converte os valores da coluna Reviews para numérico, transformando valores inválidos em NaN com errors='coerce'.
* Ordena o DataFrame com base na coluna Reviews em ordem decrescente.
* Seleciona os 10 primeiros aplicativos com o maior número de reviews, focando nas colunas App e Reviews.
* Exibe a lista dos 10 aplicativos com o maior número de reviews.

# Média das Avaliações das 7 Principais Categorias - Etapa 07 #

![Img 12](Evidencias/Execucao_do_Desafio/etapa07_1.png)
<br>
![Img 13](Evidencias/Execucao_do_Desafio/resultado_etapa07_1.png)

Este código processa um conjunto de dados sobre aplicativos da Google Play Store com o objetivo de calcular e exibir a média das avaliações (ratings) por categoria. Ele inclui etapas de limpeza e manipulação dos dados, além de apresentar os resultados de forma organizada. Abaixo está a análise detalhada de cada parte do código.

* Remove entradas duplicadas com base na coluna App.
* Filtra o DataFrame para remover o aplicativo Life Made WI-Fi Touchscreen Photo Frame.
* Converte os valores da coluna Rating para numérico, transformando entradas inválidas em NaN.
* Remove linhas onde a coluna Rating contém NaN.
* Agrupa os dados por Category e calcula a média das Rating.
* Ordena as categorias pela média das avaliações em ordem decrescente.
* Seleciona as 7 categorias com as melhores médias de avaliação.

# Grafico da Média das Avaliações das 7 Principais Categorias - Etapa 07 #

![Img 14](Evidencias/Execucao_do_Desafio/grafico_etapa07_1.png)

# Listas e Média dos 03 Aplicativos Mais Baratos e os 03 Aplicativos Mais Caros #

![Img 15](Evidencias/Execucao_do_Desafio/etapa07_2.png)
<br>
![Img 16](Evidencias/Execucao_do_Desafio/resultado_etapa07_2.png)

Este código realiza uma análise de preços de aplicativos na Google Play Store, destacando os três aplicativos mais caros e mais baratos, além de calcular a média de preços dessas duas categorias. Abaixo está uma descrição detalhada de cada etapa.

* A coluna Price é convertida para o tipo float, substituindo valores inválidos por NaN.
* Filtra o DataFrame para incluir apenas aplicativos que têm um preço maior que zero, ou seja, os aplicativos pagos.
* Os três aplicativos com os preços mais altos são selecionados e a média desses preços é calculada.
* Da mesma forma, os três aplicativos com os preços mais baixos são selecionados e a média desses preços é calculada.
* Os resultados são formatados e exibidos, mostrando os três aplicativos mais caros e baratos, bem como as médias de preço dessas categorias.

# Gráfico da Listas e Média dos 03 Aplicativos Mais Baratos e os 03 Aplicativos Mais Caros #
![Img 17](Evidencias/Execucao_do_Desafio/grafico_etapa07_2.png)

