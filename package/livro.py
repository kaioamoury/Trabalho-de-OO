class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_info(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"
