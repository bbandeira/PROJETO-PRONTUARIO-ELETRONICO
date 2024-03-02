import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os
from fpdf import FPDF




class ProntuarioPaciente(FPDF):
    def __init__(self, nome, idade, sexo, profissao, estadocivil, celular, telefonefixo, cpf, rg, email, endereco, historicomedico, historicodoencasfamiliares, alergias, medicamentosemuso, laudo, evolucao):
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao
        self.estadocivil = estadocivil
        self.celular = celular
        self.telefonefixo = telefonefixo
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.endereco = endereco
        self.historicomedico = historicomedico
        self.historicodoencasfamiliares = historicodoencasfamiliares
        self.alergias = alergias
        self.medicamentosemuso = medicamentosemuso
        self.laudo = laudo
        self.evolucao = evolucao

    def cabecalho(self):
        self.set_font("Arial", "B", 15)
        self.cell(0, 10, "Prontuário Eletrônico", 0, 1, "C")
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cell(0, 10, f"Data e hora do prontuário: {data_hora}", 0, 1, "C")
        self.ln(10)

    def detalhes_paciente(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Detalhes do paciente:", 0, 1, "L")
        self.set_fill_color(255, 255, 255)
        self.set_font("Arial", "", 12)

        detalhes = [
            f"Nome: {self.nome}",
            f"Idade: {self.idade} anos",
            f"Sexo: {self.sexo}",
            f"Profissão: {self.profissao}",
            f"Estado Civil: {self.estadocivil}",
            f"Celular: {self.celular}",
            f"Telefone Fixo: {self.telefonefixo}",
            f"CPF: {self.cpf}",
            f"RG: {self.rg}",
            f"Email: {self.email}",
            f"Endereço: {self.endereco}"
        ]

        for detalhe in detalhes:
            self.cell(0, 10, detalhe, 1, 1, "L", True)
        
        self.ln(10)

    def historicomedico_paciente(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Histórico Médico:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        historicomedico = self.historicomedico if self.historicomedico is not None else ""
        self.multi_cell(0, 10, historicomedico, 1, 1, "L")
        self.ln(10)

    def historicodoencasfamiliares_paciente(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Histórico de Doenças Familiares:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        historicodoencasfamiliares = self.historicodoencasfamiliares if self.historicodoencasfamiliares is not None else ""
        self.multi_cell(0, 10, historicodoencasfamiliares, 1, 1, "L")
        self.ln(10)

    def alergias_paciente(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Alergias:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        alergias = self.alergias if self.alergias is not None else ""
        self.multi_cell(0, 10, alergias, 1, 1, "L")
        self.ln(10)

    def medicamentosemuso_paciente(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Medicamentos em Uso:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        medicamentosemuso = self.medicamentosemuso if self.medicamentosemuso is not None else ""
        self.multi_cell(0, 10, medicamentosemuso, 1, 1, "L")
        self.ln(10)

    def adicionar_laudo(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Laudo médico:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        laudo = self.laudo if self.laudo is not None else ""
        self.multi_cell(0, 10, laudo, 1, 1, "L")
        self.ln(10)

    def adicionar_evolucao(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Evolução do paciente:", 0, 1, "L")
        self.set_font("Arial", "", 12)
        evolucao = self.evolucao if self.evolucao is not None else ""
        self.multi_cell(0, 10, evolucao, 1, 1, "L")
        self.ln(10)

    def criar_pdf(self, arquivo):
        self.add_page()
        self.cabecalho()
        self.detalhes_paciente()
        self.historicomedico_paciente()
        self.historicodoencasfamiliares_paciente()
        self.alergias_paciente()
        self.medicamentosemuso_paciente()
        self.adicionar_laudo()
        self.adicionar_evolucao()
        self.output(arquivo)


def salvar_alteracoes():
    arquivo = "prontuariopaciente.pdf"
    if os.path.exists(arquivo):
        prontuario = ProntuarioPaciente("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        
        for secao, variavel in zip(secoes, variaveis):
            setattr(prontuario, secao.replace("_", ""), variavel.get())

        prontuario.criar_pdf(arquivo)
        messagebox.showinfo("Sucesso", "Prontuário do paciente editado e salvo com sucesso.")
    else:
        messagebox.showerror("Erro", "O arquivo do prontuário do paciente não foi encontrado.")

def editar_prontuario():
    global variaveis
    variaveis = []

    top = tk.Toplevel()
    top.title("Prontuário do Paciente")

    ttk.Label(top, text="Informações do paciente:").grid(row=0, column=0, columnspan=2, pady=10)

    for i, secao in enumerate(secoes, start=1):
        ttk.Label(top, text=" ".join(secao.split("_")).capitalize() + ":").grid(row=i, column=0, sticky="e", padx=10)
        variavel = tk.StringVar()
        ttk.Entry(top, textvariable=variavel).grid(row=i, column=1, padx=10, pady=5, sticky="we")
        variavel.set(getattr(prontuario, secao.replace("_", "")))
        variaveis.append(variavel)

    ttk.Button(top, text="Salvar Alterações", command=salvar_alteracoes).grid(row=len(secoes)+1, columnspan=2, pady=20)

# Inicialização da aplicação
root = tk.Tk()
root.title("Sistema de Prontuário Eletrônico")

prontuario = ProntuarioPaciente("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

secoes = [
    "nome", "idade", "sexo", "profissao",
    "estado_civil", "celular", "telefone_fixo",
    "cpf", "rg", "email", "endereco",
    "historico_medico", "historico_doencas_familiares", "alergias",
    "medicamentos_em_uso", "laudo", "evolucao"
]

# Criar botão para editar prontuário
edit_button = ttk.Button(root, text="Prontuário do Paciente", command=editar_prontuario)
edit_button.pack(pady=80)

root.mainloop()
