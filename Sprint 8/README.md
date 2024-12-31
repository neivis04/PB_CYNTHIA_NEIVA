# Objetivo da Sprint

O objetivo do desafio é demonstrar a capacidade de integrar e processar dados em um ambiente de nuvem (AWS), utilizando diferentes tecnologias e ferramentas para:

* Coletar dados de uma API externa (no caso, a TMDB — The Movie Database) com filtros específicos, como gênero de filmes (comédia e animação), e coletar até 100 registros de cada vez. <br>
* Processar esses dados (gerando arquivos JSON contendo informações sobre filmes e séries). <br>
* Subir esses arquivos para um bucket S3 em um Data Lake em uma camada Raw (ou camada bruta). <br>
* Automatizar o processo de execução e envio utilizando o AWS Lambda, de forma a permitir a execução do processo de upload de maneira eficiente e sem a necessidade de infraestrutura adicional. <br>
* Manipulação e armazenamento de dados em um ambiente escalável e seguro, usando práticas comuns em ambientes de big data.
