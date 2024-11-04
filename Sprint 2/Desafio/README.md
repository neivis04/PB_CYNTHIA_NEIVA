# Objetivos

Esses códigos, juntos, estabelecem um sistema de gerenciamento de informações que pode ser utilizado para várias finalidades comerciais, como análise de performance, desenvolvimento de estratégias de vendas, e otimização de operações de locação de veículos.

# Ativação de Chaves Estrangeiras - Etapa 1
  <img src="assets/CRIACAO_TBCLIENTE.png" width="350px">
Este comando é usado para garantir que as restrições de integridade referencial (chaves estrangeiras) estejam ativas no banco de dados SQLite. No SQLite, as chaves estrangeiras não são aplicadas por padrão, então é necessário ativá-las.

# Criação das Tabelas - Etapa 1
  <img src="assets/CRIACAO_TBCLIENTE.png" width="350px">
 Esta tabela armazena informações dos clientes. id_cliente é a chave primária (PK) e será um número único para cada cliente. <br> Outros campos armazenam o nome, cidade, estado, e país de cada cliente, com tipos de dados TEXT.

<br>
<br>
<br>

  <img src="assets/CRIACAO_TBVENDEDOR.png" width="350px">
 Esta tabela armazena dados dos vendedores.<br>
id_vendedor é a chave primária, e outros campos incluem o nome, sexo (provavelmente 0 para masculino e 1 para feminino), e o estado de residência do vendedor.

<br>
<br>
<br>

  <img src="assets/CRIACAO_TBCARRO.png" width="350px">
Esta tabela contém informações sobre os carros disponíveis para locação.<br>
id_carro é a chave primária, e os outros campos armazenam dados como a marca, modelo, classificação, ano de fabricação e quilometragem.

<br>
<br>
<br>

  <img src="assets/CRIACAO_TBCOMBUSTIVEL.png" width="350px">
Esta tabela armazena os tipos de combustíveis que os carros utilizam.<br>
id_combustivel é a chave primária, e tipo_combustivel descreve o tipo de combustível (Gasolina, Etanol, etc.).

<br>
<br>
<br>

  <img src="assets/CRIACAO_TBLOCACAO.png" width="350px">
Esta tabela registra as locações de carros.<br>
id_locacao é a chave primária.<br>
Existem chaves estrangeiras para clientes, vendedores, carros, e combustíveis, garantindo que as informações dessas tabelas estejam relacionadas corretamente.<br>
Outros campos incluem a data e hora de locação e devolução, a quantidade de dias, e o valor diário da locação.<br>

# Uso de Chaves Estrangeiras - Etapa 1
  <img src="assets/CRIACAO_TBLOCACAO.png" width="350px">
As chaves estrangeiras (foreign keys) garantem que os valores inseridos em TBLOCACAO estejam relacionados corretamente com as tabelas TBCLIENTE, TBVENDEDOR, TBCARRO, e TBCOMBUSTIVEL. Isso preserva a integridade referencial.


# Inserção de Dados - Etapa 1

<img src="assets/INSERINDO_VALORES2.png" width="350px">
O comando INSERT INTO adiciona registros à tabela TBCOMBUSTIVEL e TBLOCACAO.

# Criação da View: LOCACOES_VENDEDOR - Etapa 2

<img src="assets/VIEW_LOCACAO_VENDEDOR.png" width="350px">
CREATE VIEW LOCACOES_VENDEDOR AS: Cria uma nova view chamada LOCACOES_VENDEDOR.<br> 
SELECT V.nome_vendedor, COUNT(L.id_carro) AS total_carros_locados: Seleciona o nome do vendedor e conta o número total de carros locados por cada vendedor.<br>
FROM TBLOCACAO L: Utiliza a tabela TBLOCACAO (locações) como a tabela principal.<br>
JOIN TBVENDEDOR V ON L.id_vendedor = V.id_vendedor: Faz uma junção (JOIN) com a tabela TBVENDEDOR (vendedores) com base no id_vendedor, permitindo que você obtenha informações do vendedor correspondente a cada locação.<br>
GROUP BY V.nome_vendedor: Agrupa os resultados pelo nome do vendedor, de modo que a contagem de locações seja feita para cada vendedor.<br>
ORDER BY total_carros_locados DESC: Ordena os resultados pela contagem de carros locados em ordem decrescente, ou seja, os vendedores que locaram mais carros aparecem primeiro.

# Resultado da View: LOCACOES_VENDEDOR 

<img src="assets/RESULTADO_LOCACAO_VENDEDOR.png" width="350px">

# Criação da View: KM_CLIENTES - Etapa 2

<img src="assets/VIEW_KM_CLIENTE.png" width="350px">
RREATE VIEW KM_CLIENTES AS: Cria uma nova view chamada KM_CLIENTES.<br>
SELECT C.nome_cliente, SUM(CA.km_carro) AS total_km_rodados: Seleciona o nome do cliente e a soma dos quilômetros rodados dos carros que o cliente alugou.<br>
FROM TBLOCACAO L: Utiliza a tabela TBLOCACAO como a tabela principal.<br>
JOIN TBCLIENTE C ON L.id_cliente = C.id_cliente: Faz uma junção com a tabela TBCLIENTE (clientes) para obter o nome de cada cliente com base em seus IDs.<br>
JOIN TBCARRO CA ON L.id_carro = CA.id_carro: Faz uma junção com a tabela TBCARRO (carros) para obter os detalhes do carro, incluindo a quilometragem.<br>
GROUP BY C.nome_cliente: Agrupa os resultados pelo nome do cliente, de modo que a soma dos quilômetros rodados seja calculada para cada cliente.<br>

# Resultado da View: KM_CLIENTES

<img src="assets/RESULTADO_KM_CLIENTES.png" width="350px">

# Criação da View: SEXO_VENDEDOR - Etapa 2

<img src="assets/VIEW_SEXO_VENDEDOR.png" width="350px">
CREATE VIEW SEXO_VENDEDOR AS: Cria uma nova view chamada SEXO_VENDEDOR.<br>
SELECT V.sexo_vendedor, COUNT(L.id_carro) AS total_locacoes: Seleciona o sexo do vendedor e conta o número total de locações feitas por cada sexo.<br>
FROM TBLOCACAO L: Utiliza a tabela TBLOCACAO como a tabela principal.<br>
JOIN TBVENDEDOR V ON L.id_vendedor = V.id_vendedor: Faz uma junção com a tabela TBVENDEDOR para obter o sexo do vendedor correspondente a cada locação.<br>
GROUP BY V.sexo_vendedor: Agrupa os resultados pelo sexo do vendedor, permitindo contar quantas locações foram feitas por vendedores de cada sexo.<br>
ORDER BY total_locacoes DESC: Ordena os resultados pela contagem de locações em ordem decrescente.<br>

# Resultado da View: SEXO_VENDEDOR

<img src="assets/RESULTADO_SEXO_VENDEDOR.png" width="350px">


  
