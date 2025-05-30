from package.livro import Livro
from package.mixins import EmprestimoMixin

class LivroEmprestado(Livro, EmprestimoMixin):
    def __init__(self, titulo, autor, ano):
        Livro.__init__(self, titulo, autor, ano)
        EmprestimoMixin.__init__(self)

    def exibir_info(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{super().exibir_info()} - [{status}]"

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def remover_livro(self, indice):
        if 0 <= indice < len(self.acervo):
            del self.acervo[indice]

    def buscar_livros(self, termo):
        return [livro for livro in self.acervo if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]