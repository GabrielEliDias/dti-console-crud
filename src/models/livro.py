import datetime

class Livro:
    def __init__(self, id, titulo, autor, data_publicacao, resumo, numero_paginas=None, data_cadastro=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        
        self.data_publicacao = data_publicacao 
        
        self.resumo = resumo
        self.numero_paginas = numero_paginas
        self.data_cadastro = data_cadastro

    def __str__(self):
        data_fmt = self.data_publicacao.strftime('%d/%m/%Y') if self.data_publicacao else "Data desc."
        return f"{self.titulo} ({self.autor}) - {data_fmt}"
    
    def __repr__(self):
        return f"Livro(id={self.id}, titulo='{self.titulo}')"