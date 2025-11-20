DROP TABLE IF EXISTS Livros;

CREATE TABLE IF NOT EXISTS Livros (
    -- Obrigatórios:
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    DataPublicacao TEXT NOT NULL,   

    -- Não Obrigatórios:                                                                                                                                                                                                                                                                         
    Resumo TEXT,
    NumeroPaginas INTEGER,   
    DataCadastro TEXT DEFAULT CURRENT_TIMESTAMP -- Cadastrado automaticamente
);  

-- Carga inicial de dados
INSERT INTO Livros (Titulo, Autor, DataPublicacao)
VALUES ('Código Limpo', 'Robert C. Martin', '2008-08-01'),
       ('Assasinato no Expresso do Oriente', 'Agatha Christie', '1984-01-01');

INSERT INTO Livros (Titulo, Autor, DataPublicacao, Resumo)
VALUES ('Data Science do Zero: Noções Fundamentais com Python', 'Joel Grus', '2021-04-27', 'Foca em apresentar os princípios e ferramentas essenciais da ciência de dados para quem já tem noções básicas de programação e matemática'),
       ('Arsène Lupin: O ladrão de Casaca', 'Maurice Leblanc', '2021-03-24', 'Arsène Lupin, um ladrão charmoso e inteligente que se destaca por realizar roubos ousados e espetaculares, muitas vezes com um código de honra. As histórias o mostram se infiltrando na alta sociedade, enganando a polícia e até mesmo resolvendo crimes, em um estilo que desafia o papel tradicional do vilão');

INSERT INTO Livros (Titulo, Autor, DataPublicacao, Resumo, NumeroPaginas)
VALUES ('Dom Casmurro', 'Machado de Assis', '1899-01-01', 'Narra a história de Bento Santiago, conhecido como Bentinho, que na velhice tenta reconstruir sua vida e a história do seu casamento com Capitu, movido pela dúvida se ela o traiu com seu melhor amigo, Escobar', 408),
       ('O Senhor dos Anéis', 'J.R.R. Tolkien', '1954-07-29', 'Narra a saga épica de Frodo Bolseiro, um hobbit que precisa destruir o Um Anel, artefato maligno forjado por Sauron, o Senhor Sombrio', 1200);