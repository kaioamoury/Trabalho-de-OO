import json
from package.biblioteca import LivroEmprestado

class Persistencia:
    @staticmethod
    def salvar(biblioteca, arquivo='data/acervo.json'):
        dados = []
        for livro in biblioteca.acervo:
            dados.append({
                'titulo': livro.titulo,
                'autor': livro.autor,
                'ano': livro.ano,
                'emprestado': livro.emprestado,
                'nome_usuario': livro.nome_usuario
            })
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    @staticmethod
    def carregar(biblioteca, arquivo='data/acervo.json'):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                for item in dados:
                    livro = LivroEmprestado(item['titulo'], item['autor'], item['ano'])
                    livro.emprestado = item['emprestado']
                    livro.nome_usuario = item['nome_usuario']
                    biblioteca.adicionar_livro(livro)
        except FileNotFoundError:
            pass