PRAGMA foreign_keys = ON;
CREATE TABLE TBCLIENTE(
	id_cliente INTEGER PRIMARY KEY,
	nome_cliente TEXT(50),
	cidade TEXT(50),
	estado TEXT(50),
	pais TEXT(50)
);

CREATE TABLE TBVENDEDOR(
	id_vendedor INTEGER PRIMARY KEY,
	nome_vendedor TEXT(255),
	sexo_vendedor INTEGER,
	estado_vendedor TEXT(50)
);

CREATE TABLE TBCARRO(
	id_carro INTEGER PRIMARY KEY,
	marca_carro TEXT(50),
	modelo_carro TEXT(50),
	classificacao_carro TEXT(50),
	ano_carro INTEGER,
	km_carro INTEGER
);

CREATE TABLE TBCOMBUSTIVEL(
	id_combustivel INTEGER PRIMARY KEY,
	tipo_combustivel TEXT(40)
);

CREATE TABLE TBLOCACAO(
    id_locacao INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_carro INTEGER,
    id_vendedor INTEGER,
	id_combustivel INTEGER,
    data_locacao DATE,
    hora_locacao TIME,
    quantidade_diaria INTEGER,
    valor_diaria REAL(10, 2),
    data_devolucao DATE,
    hora_devolucao TIME,
    FOREIGN KEY (id_cliente) REFERENCES TBCLIENTE(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES TBVENDEDOR(id_vendedor),
    FOREIGN KEY (id_carro) REFERENCES TBCARRO(id_carro),
    FOREIGN KEY (id_combustivel) REFERENCES TBCOMBUSTIVEL(id_combustivel)
    
);

INSERT INTO TBCLIENTE(id_cliente,nome_cliente,cidade,estado,pais)VALUES
(2,'Cliente dois','São Paulo','São Paulo','Brasil'),
(3,'Cliente tres','Rio de Janeiro','Rio de Janeiro','Brasil'),
(4,'Cliente quatro','Rio de Janeiro','Rio de Janeiro','Brasil'),
(5,'Cliente cinco','Manaus','Amazonas','Brasil'),
(6,'Cliente seis','Belo Horizonte','Minas Gerais','Brasil'),
(10,'Cliente dez','Rio Branco','Acre','Brasil'),
(20,'Cliente vinte','Macapá','Amapá','Brasil'),
(22,'Cliente vinte e dois','Porto Alegre','Rio Grande do Sul','Brasil'),
(23,'Cliente vinte e tres','Eusébio','Ceará','Brasil'),
(26,'Cliente vinte e seis','Campo Grande','Mato Grosso do Sul','Brasil');

INSERT INTO TBVENDEDOR(id_vendedor,nome_vendedor,sexo_vendedor,estado_vendedor)VALUES
(5,'Vendedor cinco',0,'São Paulo'),
(6,'Vendedora seis',1,'São Paulo'),
(7,'Vendedora sete',1,'Rio de Janeiro'),
(8,'Vendedora oito',1,'Minas Gerais'),
(16,'Vendedor dezesseis',0,'Amazonas'),
(30,'Vendedor trinta',0,'Rio Grande do Sul'),
(31,'Vendedor trinta e um',0,'Ceará'),
(32,'Vendedora trinta e dois',1,'Mato Grosso do Sul');

INSERT INTO TBCARRO(id_carro,km_carro,classificacao_carro,marca_carro,modelo_carro,ano_carro)VALUES
(1,1800,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023),
(2,10000,'AKIUNS1JS76S39','Nissan','Versa',2019),
(3,121700,'DKSHKNS8JS76S39','VW','Fusca 78',1978),
(4,55000,'LLLUNS1JS76S39','Nissan','Versa',2020),
(5,28000,'MSLUNS1JS76S39','Nissan','Frontier',2022),
(6,21800,'SKIUNS8JS76S39','Nissan','Versa',2019),
(7,212800,'SSIUNS8JS76S39','Fiat','Fiat 147',1996),
(10,211800,'LKIUNS8JS76S39','Fiat','Fiat 147',1996),
(98,25412,'AKJHKN98JY76539','Fiat','Fiat Uno',2000),
(99,20000,'IKJHKN98JY76539','Fiat','Fiat Palio',2010);

INSERT INTO TBCOMBUSTIVEL(id_combustivel, tipo_combustivel) VALUES
(1, 'Gasolina'),
(2, 'Etanol'),
(3, 'Flex'),
(4, 'Diesel');

INSERT INTO TBLOCACAO(id_locacao,id_cliente,id_carro,id_vendedor, id_combustivel,data_locacao, hora_locacao, quantidade_diaria,valor_diaria,data_devolucao,hora_devolucao)VALUES
(1,2,98,5,1,'2015-01-10','10:00',2,100,'2015-01-12','10:00'),
(2,2,98,5,1,'2015-02-10','12:00',2,100,'2015-02-12','12:00'),
(3,3,99,6,1,'2015-02-13','12:00',2,150,'2015-02-15','12:00'),
(4,4,99,6,1,'2015-02-15','13:00',5,150,'2015-02-20','13:00'),
(5,4,99,7,1,'2015-03-02','14:00',5,150,'2015-03-07','14:00'),
(6,6,3,8,1,'2016-03-02','14:00',10,250,'2016-03-12','14:00'),
(7,6,3,8,1,'2016-08-02','14:00',10,250,'2016-08-12','14:00'),
(8,4,3,6,1,'2017-01-02','18:00',10,250,'2017-01-12','18:00'),
(9,4,3,6,1,'2018-01-02','18:00',10,280,'2018-01-12','18:00'),
(10,10,10,16,1,'2018-03-02','18:00',10,50,'2018-03-12','18:00'),
(11,20,7,16,1,'2018-04-01','11:00',10,50,'2018-04-11','11:00'),
(12,20,6,16,1,'2020-04-01','11:00',10,150,'2020-04-11','11:00'),
(13,22,2,30,2,'2022-05-01','8:00',20,150,'2022-05-21','18:00'),
(14,22,2,30,2,'2022-06-01','8:00',20,150,'2022-06-21','18:00'),
(15,22,2,30,2,'2022-07-01','8:00',20,150,'2022-07-21','18:00'),
(16,22,2,30,2,'2022-08-01','8:00',20,150,'2022-07-21','18:00'),
(17,23,4,31,2,'2022-09-01','8:00',20,150,'2022-09-21','18:00'),
(18,23,4,31,2,'2022-10-01','8:00',20,150,'2022-10-21','18:00'),
(19,23,4,31,2,'2022-11-01','8:00',20,150,'2022-11-21','18:00'),
(20,5,1,16,3,'2023-01-02','18:00',10,880,'2023-01-12','18:00'),
(21,5,1,16,3,'2023-01-15','18:00',10,880,'2023-01-25','18:00'),
(22,26,5,32,4,'2023-01-25','8:00',5,600,'2023-01-30','18:00'),
(23,26,5,32,4,'2023-01-31','8:00',5,600,'2023-02-05','18:00'),
(24,26,5,32,4,'2023-02-06','8:00',5,600,'2023-02-11','18:00'),
(25,26,5,32,4,'2023-02-12','8:00',5,600,'2023-02-17','18:00'),
(26,26,5,32,4,'2023-02-18','8:00',1,600,'2023-02-19','18:00');
