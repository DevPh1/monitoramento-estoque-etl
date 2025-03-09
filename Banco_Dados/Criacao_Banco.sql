CREATE TABLE Produtos (
    id INT PRIMARY KEY IDENTITY(1,1),  -- Chave primaria autoincremental
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2)
);

CREATE TABLE Estoque (
    id INT PRIMARY KEY IDENTITY(1,1),
    produto_id INT FOREIGN KEY REFERENCES Produtos(id),
    quantidade INT,
    data_atualizacao DATE
);

CREATE TABLE Vendas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    produto_id INT NOT NULL,
    quantidade_vendida INT NOT NULL,
    data_venda DATE NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id) ON DELETE CASCADE
);

CREATE TABLE Fornecedores (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tempo_entrega INT NOT NULL CHECK (tempo_entrega >= 1)  
);

CREATE TABLE Fornecedores_Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    fornecedor_id INT NOT NULL,
    produto_id INT NOT NULL,
    FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);



