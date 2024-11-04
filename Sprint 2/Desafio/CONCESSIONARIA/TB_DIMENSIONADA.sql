SELECT * FROM LOCACOES_VENDEDOR

SELECT * FROM KM_CLIENTES

SELECT * FROM SEXO_VENDEDOR


CREATE VIEW LOCACOES_VENDEDOR AS
SELECT 
    V.nome_vendedor, 
    COUNT(L.id_carro) AS total_carros_locados
FROM 
    TBLOCACAO L
JOIN 
    TBVENDEDOR V ON L.id_vendedor = V.id_vendedor
GROUP BY 
    V.nome_vendedor
ORDER BY 
    total_carros_locados DESC
    
    
CREATE VIEW KM_CLIENTES AS
SELECT 
    C.nome_cliente, 
    SUM(CA.km_carro) AS total_km_rodados
FROM 
    TBLOCACAO L
JOIN 
    TBCLIENTE C ON L.id_cliente = C.id_cliente
JOIN 
    TBCARRO CA ON L.id_carro = CA.id_carro
GROUP BY 
    C.nome_cliente;


   CREATE VIEW SEXO_VENDEDOR AS    
SELECT 
    V.sexo_vendedor, 
    COUNT(L.id_carro) AS total_locacoes
FROM 
    TBLOCACAO L
JOIN 
    TBVENDEDOR V ON L.id_vendedor = V.id_vendedor
GROUP BY 
    V.sexo_vendedor
ORDER BY 
    total_locacoes DESC

