from datetime import datetime as dt

class Livro:
    def __init__(self, id, titulo, autor, DataPublicacao, resumo, numero_paginas=None, data_cadastro=None):
        self.Id = id
        self.Titulo = titulo
        self.Autor = autor

        data_limpa = DataPublicacao.split(" ")[0]  # Tratamento para evitar quebras por presenças de horas, minutos e segundos.
        self.DataPublicacao = dt.strptime(data_limpa, "%Y-%m-%d").date()

        self.resumo = resumo
        self.NumeroPaginas = numero_paginas
        self.DataCadastro = data_cadastro

    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.data_publicacao})"

