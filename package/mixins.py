class EmprestimoMixin:
    def __init__(self):
        self.emprestado = False
        self.nome_usuario = None

    def emprestar(self, nome_usuario):
        if not self.emprestado:
            self.emprestado = True
            self.nome_usuario = nome_usuario
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            self.nome_usuario = None
            return True
        return False