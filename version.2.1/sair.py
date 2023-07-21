# Importações

import customtkinter as CTk
import os

# FUNÇÕES DE SISTEMA

def sair(h,m):  # Comando de encerramento do windows
    num = (h * 60) + m
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
        janela.geometry('400x500')
        janela.resizable(False, False)

    def tema(self):  # Função de configuração de tema
        CTk.set_appearance_mode('dark')

    def main(self):  # Função da tela principal

        # FUNCINNALIDADES DA TELA PRINCIPAL

        def verificador():  # função interna de tratamento de dados
            h = int(pri_quadro.cget('text'))
            m = int(sec_quadro.cget('text')[1:3])
            if h == 1 or h == 0:
                hs = 'Hora'
            else:
                hs = 'Horas'
            if m == 1 or m == 0:
                mn = 'Minuto'
            else:
                mn = 'Minutos'
            sair(h,m)
            sucesso(h,m,hs,mn)

        def modo(x):  # Função interna para a mudança de modo
            if escolha.get() == 'Reiniciar':
                subtitulo.configure(text='Em quanto tempo deseja\nReiniciar o Pc?')
                variaveis[0] = 'r'
                variaveis[1] = 'Reiniciado'
            else:
                subtitulo.configure(text='Em quanto tempo deseja\nDesligar o Pc?')
                variaveis[0] = 's'
                variaveis[1] = 'Desligado'
        
        def atualizar_pri(n): # Função interna de funcionamento da primeira dezena
            if pri_quadro.cget("text") == '99' and sec_quadro.cget("text") == ':00' and n == 1:
                pri_quadro.configure(text='01')
            elif pri_quadro.cget("text") == '01' and sec_quadro.cget("text") == ':00' and n == 0:
                pri_quadro.configure(text='99')
            elif pri_quadro.cget("text") == '99' and n == 1:
                pri_quadro.configure(text='00')
            elif pri_quadro.cget("text") == '00' and n == 0:
                pri_quadro.configure(text='99')
            else:
                num = int(pri_quadro.cget("text"))
                num = num + 1 if n == 1 else num - 1
                if num < 10:
                    pri_quadro.configure(text=f'0{num}')
                else:
                    pri_quadro.configure(text=f'{num}')

        def atualizar_sec(n): # Função interna de funcionamento da segunda dezena
            if sec_quadro.cget('text') == ':01' and pri_quadro.cget('text') == '00' and n == 0:
                sec_quadro.configure(text=':59')
            elif sec_quadro.cget('text') == ':59' and pri_quadro.cget('text') == '00' and n == 1:
                sec_quadro.configure(text=':01')
            elif sec_quadro.cget("text") == ':59' and n == 1:
                sec_quadro.configure(text=':00')
            elif sec_quadro.cget("text") == ':00' and n == 0:
                sec_quadro.configure(text=':59')
            else:
                num = (int(sec_quadro.cget("text")[1:3]))
                num = num + 1 if n == 1 else num - 1
                if num < 10:
                    sec_quadro.configure(text=f':0{num}')
                else:
                    sec_quadro.configure(text=f':{num}')
        
        # TELA SECUNDÁRIA (tela de sucesso)

        def sucesso(h,m,hs,mn):  # função interna da tela de sucesso

            # Encerrando a tela principal
            inicial_frame.pack_forget()
            tempo.place_forget()

            # Criando a tela de sucesso

            # Fundo
            sucesso_frame = CTk.CTkFrame(janela, width=400, height=500)
            sucesso_frame.pack()

            # Título
            titulo_sucesso = CTk.CTkLabel(sucesso_frame, text='SUCESSO!', text_color='green', font=('Segoe UI', 30,'bold'))
            titulo_sucesso.place(relx=0.5, y=40, anchor="center")

            # Subfundo
            sub_fundo = CTk.CTkFrame(janela, width=350, height=250, corner_radius=20, fg_color='#212121' , bg_color='#2B2B2B')
            sub_fundo.place(relx=0.5, y=200, anchor='center')

            # Subtítulo
            subtitulo_sucesso = CTk.CTkLabel(sub_fundo, text=f'Seu Pc será {variaveis[1]} em:\n\n{h} {hs} e {m} {mn}.\n\nAté mais!', font=('Segoe UI', 25))
            subtitulo_sucesso.place(relx=0.5, rely=0.5, anchor="center")

            # Checkbox
            check = CTk.CTkCheckBox(sucesso_frame, text='Bloquear o usuário ao sair', font=('Segoe UI', 18,'bold'))
            check.place(relx=0.5, y=380, anchor="center")

            # Botão de finalizar
            bt_finalizar = CTk.CTkButton(sucesso_frame, text='Até mais', width=150, command=lambda: finalizar(), font=('Segoe UI', 15,'bold'))
            bt_finalizar.place(x=100, rely=0.9, anchor='center')

            # Botão de cancelar operação
            bt_cancelar = CTk.CTkButton(sucesso_frame, text='Cancelar', width=150, fg_color='#474747', hover_color='#171717', command=lambda: voltar(), font=('Segoe UI', 15,'bold'))
            bt_cancelar.place(x=300, rely=0.9, anchor='center')

            # FUNCIONALIDADES DA TELA SECUNDÁRIA

            def finalizar():  # Função interna para finalizar a operação bloqueando o sistema ou não
                if check.get() == 1:
                    bloquear()
                    exit()
                else:
                    exit()

            def voltar():  # Função interna para cancelar a operação
                popup()
                cancelar()
                inicial_frame.pack()
                tempo.place(relx=0.5, y=280, anchor='center')
                sucesso_frame.pack_forget()
                sub_fundo.place_forget()

            def popup():
                pass

        # TELA PRINCIPAL

        # Fundo
        inicial_frame = CTk.CTkFrame(janela, width=400, height=500)
        inicial_frame.pack()

        # Título
        titulo = CTk.CTkLabel(inicial_frame, text='SAIR DO WINDOWS', text_color=('#1F6AA5'), font=('Segoe UI', 30,'bold'))
        titulo.place(relx=0.5, y=30, anchor='center')

        # Subtítulo
        subtitulo = CTk.CTkLabel(inicial_frame, text='Em quanto tempo deseja\nDesligar o Pc?', font=('arial', 25))
        subtitulo.place(relx=0.5, y=90, anchor='center')

        # Escolha
        escolha = CTk.CTkOptionMenu(inicial_frame, values=['Desligar', 'Reiniciar'], font=('Segoe UI', 15), command=modo)
        escolha.place(x=280, y=145, anchor='center')

        # Quadro Tempo
        tempo = CTk.CTkFrame(janela, width=350, height=200, fg_color='#212121', corner_radius=20, bg_color='#2B2B2B' )
        tempo.place(relx=0.5, y=280, anchor='center')

        # Primeiro quadro
        pri_quadro = CTk.CTkLabel(tempo, text='01', font=('arial', 100))
        pri_quadro.place(x=120, y=90, anchor='center')
            # botão de cima
        top_pri = CTk.CTkButton(tempo, text='🔺', fg_color='transparent', font=('arial', 20), width=30, hover=None, command=lambda: atualizar_pri(1))
        top_pri.place(x=130, rely=0.1, anchor='center')
            # botão de baixo
        down_pri = CTk.CTkButton(tempo, text='🔻', fg_color='transparent',  font=('arial', 20), width=30, hover=None, command=lambda: atualizar_pri(0))
        down_pri.place(x=130, rely=0.9, anchor='center')

        # Segundo quadro
        sec_quadro = CTk.CTkLabel(tempo, text=':00', font=('arial', 100))
        sec_quadro.place(x=245, y=90, anchor='center')
            # botão de cima
        top_sec = CTk.CTkButton(tempo, text='🔺', fg_color='transparent',  font=('arial', 20), width=30, hover=None, command=lambda: atualizar_sec(1))
        top_sec.place(x=260, rely=0.1, anchor='center')
            # botão de baixo
        down_sec = CTk.CTkButton(tempo, text='🔻', fg_color='transparent',  font=('arial', 20), width=30, hover=None, command=lambda: atualizar_sec(0))
        down_sec.place(x=260, rely=0.9, anchor='center')

        # Legenda quadro
        ter_quadro = CTk.CTkLabel(tempo, text='Horas              Minutos', font=('Segoe UI', 20))
        ter_quadro.place(relx=0.5, y=150, anchor='center')

        # Botão de iniciar
        bt_iniciar = CTk.CTkButton(inicial_frame, text='Iniciar', width=300, command=verificador, font=('Segoe UI', 15,'bold'), corner_radius=30)
        bt_iniciar.place(relx=0.5, y=420, anchor='center')

        # Mensagem
        msg_erro = CTk.CTkLabel(inicial_frame, text='', font=('Segoe UI', 20), text_color='red')
        msg_erro.place(relx=0.5, y=460, anchor='center')


# INICIANDO O PROGRAMA

variaveis = ['s', 'Desligado']
cancelar()
aplication()
