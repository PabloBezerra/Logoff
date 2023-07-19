# Importações

import customtkinter as CTk
import os

# FUNÇÕES DE SISTEMA

def sair(num):  # Comando de encerramento do windows
    num = int(num)
    sec = num * 60
    os.system(f'shutdown -{variaveis[0]} -t {sec}')


def cancelar():  # Comando de cancelamento de encerramento do windows
    os.system('shutdown -a')


def bloquear():  # Comando de bloquear o usuário do windows
    os.system('rundll32.exe user32.dll,LockWorkStation')


# INICIO DA JANELA PRINCIPAL

janela = CTk.CTk()


class aplication():  # Classe principal
    def __init__(self):  # Função de configuração da estrutura
        self.janela = janela
        self.tela()
        self.tema()
        self.main()
        janela.mainloop()

    def tela(self):  # Função de configuração de tela
        janela.title('Logoff')
        janela.geometry('400x300')
        janela.resizable(False, False)

    def tema(self):  # Função de configuração de tema
        CTk.set_appearance_mode('dark')

    def main(self):  # Função da tela principal

        def verificador():  # função interna de verificador de entrada
            valor = str(minutos.get()).strip()
            if valor.isnumeric():
                sair(valor)
                sucesso(valor)
            else:
                if valor == '':
                    erro.configure(text='Por favor, preencha o campo acima!', text_color='#FA4E4B')
                else:
                    erro.configure(text='Por favor, insira apenas números', text_color='#FA4E4B')

        def modo(x):  # Função interna para a mudança de modo
            if escolha.get() == 'Reiniciar':
                subtitulo.configure(text='Em quantos minutos deseja\nReiniciar o Pc?')
                variaveis[0] = 'r'
                variaveis[1] = 'Reiniciado'
            else:
                subtitulo.configure(text='Em quantos minutos deseja\nDesligar o Pc?')
                variaveis[0] = 's'
                variaveis[1] = 'Desligado'

        def sucesso(num):  # função interna da tela de sucesso

            # Encerrando a tela principal
            inicial_frame.pack_forget()

            # Criando a tela de sucesso

            # Fundo
            sucesso_frame = CTk.CTkFrame(janela, width=400, height=300)
            sucesso_frame.pack()

            # Título
            titulo_sucesso = CTk.CTkLabel(sucesso_frame, text='SUCESSO!', text_color='green', font=('Segoe UI', 30,'bold'))
            titulo_sucesso.place(relx=0.5, y=30, anchor="center")

            # Subtítulo
            subtitulo_sucesso = CTk.CTkLabel(sucesso_frame, text=f'Seu Pc será {variaveis[1]}\nem {num} minutos. Até mais!',
                                             font=('Segoe UI', 25))
            subtitulo_sucesso.place(relx=0.5, y=100, anchor="center")

            # Checkbox
            check = CTk.CTkCheckBox(sucesso_frame, text='Bloquear o usuário ao sair', font=('Segoe UI', 18,'bold'))
            check.place(relx=0.5, y=180, anchor="center")

            # Botão de finalizar
            bt_finalizar = CTk.CTkButton(sucesso_frame, text='Até mais', width=150, command=lambda: finalizar(), font=('Segoe UI', 15,'bold'))
            bt_finalizar.place(x=100, y=240, anchor='center')

            # Botão de cancelar operação
            bt_cancelar = CTk.CTkButton(sucesso_frame, text='Cancelar', width=150, fg_color='#474747', hover_color='#171717',
                                        command=lambda: voltar(), font=('Segoe UI', 15,'bold'))
            bt_cancelar.place(x=300, y=240, anchor='center')

            def finalizar():  # Função interna para finalizar a operação bloqueando o sistema ou não
                if check.get() == 1:
                    bloquear()
                    quit()
                else:
                    quit()

            def voltar():  # Função interna para cancelar a operação
                cancelar()
                inicial_frame.pack()
                sucesso_frame.pack_forget()
                erro.configure(text='Operação cancelada pelo usuário', text_color=('#E0B501', 'yellow'))

        # Whidgets da tela principal

        # Fundo
        inicial_frame = CTk.CTkFrame(janela, width=400, height=300)
        inicial_frame.pack()

        # Título
        titulo = CTk.CTkLabel(inicial_frame, text='SAIR DO WINDOWS', text_color=('#1F6AA5'), font=('Segoe UI', 30,'bold'))
        titulo.place(relx=0.5, y=30, anchor='center')

        # Subtítulo
        subtitulo = CTk.CTkLabel(inicial_frame, text='Em quantos minutos deseja\nDesligar o Pc?',
                                 font=('arial', 25))
        subtitulo.place(relx=0.5, y=90, anchor='center')

        # Escolha
        escolha = CTk.CTkOptionMenu(inicial_frame, values=['Desligar', 'Reiniciar'], font=('Segoe UI', 15), command=modo)
        escolha.place(x=280, y=145, anchor='center')

        # Caixa de Entrada
        minutos = CTk.CTkEntry(inicial_frame, placeholder_text='Ex:20', width=300, height=35)
        minutos.place(x=50, y=175)

        # Botão de iniciar
        bt_iniciar = CTk.CTkButton(inicial_frame, text='Iniciar', width=300,
                                   command=lambda: verificador(), font=('Segoe UI', 15,'bold'), corner_radius=30)
        bt_iniciar.place(relx=0.5, y=240, anchor='center')

        # Mensagens de erro
        erro = CTk.CTkLabel(inicial_frame, text=' ', text_color='#FA4E4B', font=('Segoe UI', 15,'bold'))
        erro.place(relx=0.5, y=273, anchor='center')

# INICIANDO O PROGRAMA

variaveis = ['s', 'Desligado']
cancelar()
aplication()
