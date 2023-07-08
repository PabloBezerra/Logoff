# Importações
import customtkinter as CTk
import os


# FUNÇÕES DE SISTEMA

def sair(num):  # comando de encerramento do windows
    num = int(num)
    sec = num * 60
    os.system(f'shutdown -s -t {sec}')


def cancelar():  # comando de cancelamento de encerramento do windows
    os.system('shutdown -a')


def bloquear():  # comando de bloquear o usuário do windows
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
        janela.iconbitmap('logo_Logoff.ico')

    def tema(self):  # Função de configuração de tema
        CTk.set_appearance_mode('system')

    def main(self):  # Função da tela principal

        def verificador():  # função interna de vereficador de entrada
            valor = str(minutos.get()).strip()
            if valor.isnumeric():
                # sair(valor)
                sucesso(valor)
            else:
                if valor == '':
                    erro_vasio.place(relx=0.5, y=175, anchor='center')
                    erro_letra.place_forget()
                    cancel.place_forget()
                else:
                    erro_letra.place(relx=0.5, y=175, anchor='center')
                    erro_vasio.place_forget()
                    cancel.place_forget()

        def sucesso(num):  # função interna da tela de sucesso

            # Encerrando a tela principal
            inicial_frame.pack_forget()

            # Criando a tela de sucesso

            # Fundo
            sucesso_frame = CTk.CTkFrame(janela, width=400, height=300)
            sucesso_frame.pack()

            # Título
            titulo_sucesso = CTk.CTkLabel(sucesso_frame, text='Sucesso!', font=('arial black', 30))
            titulo_sucesso.place(relx=0.5, y=30, anchor="center")

            # Subtítulo
            subtitulo_sucesso = CTk.CTkLabel(sucesso_frame, text=f'Seu Pc será encerrado em {num} minutos.\nAté mais!',
                                             font=('arial', 20))
            subtitulo_sucesso.place(relx=0.5, y=90, anchor="center")

            # Checkbox
            check = CTk.CTkCheckBox(sucesso_frame, text='Bloquear o usuário ao sair')
            check.place(relx=0.5, y=140, anchor="center")

            # Botão de finalizar
            bt_finalizar = CTk.CTkButton(sucesso_frame, text='Até mais', width=100, hover_color='darkgreen',
                                         command=lambda: finalizar(), font=('arial black', 15))
            bt_finalizar.place(x=146, y=180)

            # Botão de cancelar operação
            bt_cancelar = CTk.CTkButton(sucesso_frame, text='Cancelar', width=100, hover_color='darkred',
                                        command=lambda: voltar(), font=('arial black', 15))
            bt_cancelar.place(x=146, y=220)

            def finalizar():
                if check.get() == 1:
                    bloquear()
                    quit()
                else:
                    quit()

            def voltar():
                cancelar()
                inicial_frame.pack()
                sucesso_frame.pack_forget()
                minutos.configure(placeholder_text=" ")
                cancel.place(relx=0.5, y=175, anchor='center')
                erro_vasio.place_forget()
                erro_letra.place_forget()

        # Whidgets da tela principal

        # Fundo
        inicial_frame = CTk.CTkFrame(janela, width=400, height=300)
        inicial_frame.pack()

        # Título
        titulo = CTk.CTkLabel(inicial_frame, text='Sair do Windows', font=('arial black', 30))
        titulo.place(x=70, y=10)

        # Subtítulo
        subtitulo = CTk.CTkLabel(inicial_frame, text='Em quantos minutos deseja desligar o Pc?',
                                 font=('montserrat', 20))
        subtitulo.place(x=15, y=70)

        # Caixa de Entrada
        minutos = CTk.CTkEntry(inicial_frame, placeholder_text='Ex:20', width=300)
        minutos.place(x=50, y=130)

        # Mensagem de erro 1
        erro_vasio = CTk.CTkLabel(inicial_frame, text='Por favor, preencha o campo acima!', text_color='#FA4E4B',
                                  font=('arial black', 15))
        erro_vasio.pack_forget()

        # Mensagem de erro 2
        erro_letra = CTk.CTkLabel(inicial_frame, text='Por favor, insira apenas números!', text_color='#FA4E4B',
                                  font=('arial black', 15))
        erro_letra.pack_forget()

        # Mensagem de cancelamento
        cancel = CTk.CTkLabel(inicial_frame, text='Operação cancelada pelo usuário', text_color=('#E0B501', 'yellow'), font=('arial black', 15))
        cancel.place_forget()

        # Botão de iniciar
        bt_iniciar = CTk.CTkButton(inicial_frame, text='Iniciar', fg_color='#02AD30', width=300, hover_color='#006613',
                                   command=lambda: verificador(), font=('arial black', 15))
        bt_iniciar.place(relx=0.5, y=205, anchor='center')

        # Botão de Sair do programa
        lb_sair = CTk.CTkLabel(inicial_frame, text='Sair do programa')
        lb_sair.place(x=200, y=250)
        bt_sair = CTk.CTkButton(inicial_frame, text='Sair', command=lambda: quit(), width=50,
                                font=('arial black', 15))
        bt_sair.place(x=300, y=250)


cancelar()
aplication()
