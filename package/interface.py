import tkinter as tk
from tkinter import simpledialog, messagebox
from package.biblioteca import Biblioteca, LivroEmprestado
from package.persistencia import Persistencia

class SistemaInterface:
    def __init__(self, master):
        self.master = master
        master.title("Biblioteca")

        self.biblioteca = Biblioteca()
        Persistencia.carregar(self.biblioteca)

        self.lista = tk.Listbox(master, width=60)
        self.lista.pack()

        self.atualizar_lista()

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="Adicionar", command=self.adicionar).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Remover", command=self.remover).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Emprestar", command=self.emprestar).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Devolver", command=self.devolver).pack(side=tk.LEFT)

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for idx, livro in enumerate(self.biblioteca.acervo):
            self.lista.insert(tk.END, f"{idx}: {livro.exibir_info()}")

    def adicionar(self):
        titulo = simpledialog.askstring("Título", "Informe o título:")
        autor = simpledialog.askstring("Autor", "Informe o autor:")
        ano = simpledialog.askstring("Ano", "Informe o ano:")
        if titulo and autor and ano:
            livro = LivroEmprestado(titulo, autor, ano)
            self.biblioteca.adicionar_livro(livro)
            Persistencia.salvar(self.biblioteca)
            self.atualizar_lista()

    def remover(self):
        try:
            idx = self.lista.curselection()[0]
            self.biblioteca.remover_livro(idx)
            Persistencia.salvar(self.biblioteca)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um livro para remover.")

    def emprestar(self):
        try:
            idx = self.lista.curselection()[0]
            nome = simpledialog.askstring("Empréstimo", "Informe o nome do usuário:")
            livro = self.biblioteca.acervo[idx]
            if livro.emprestar(nome):
                Persistencia.salvar(self.biblioteca)
                self.atualizar_lista()
            else:
                messagebox.showinfo("Info", "Livro já emprestado.")
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um livro para emprestar.")

    def devolver(self):
        try:
            idx = self.lista.curselection()[0]
            livro = self.biblioteca.acervo[idx]
            if livro.devolver():
                Persistencia.salvar(self.biblioteca)
                self.atualizar_lista()
            else:
                messagebox.showinfo("Info", "Livro não está emprestado.")
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um livro para devolver.")