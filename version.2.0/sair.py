# Importações
import customtkinter as CTk
import os


# Funções de sistema
def sair(num):  # comando de encerramento do windows
    num = int(num)
    sec = num * 60
    os.system(f'shutdown -s -t {sec}')


def cancelar():  # comando de cancelamento de encerramento do windows
    os.system('shutdown -a')


def bloquear():  # comando de bloquear o usuário do windows
    os.system('rundll32.exe user32.dll,LockWorkStation')


def verificador():
    valor = str(valor_cmd.get()).strip()
    print(valor)


janela = CTk.CTk()
janela.title('Logoff')
janela.geometry('400x300')

CTk.CTkLabel(janela, text='Sair do Windows', text_color='white', font=('arial black', 30)).pack(padx=10, pady=10)
CTk.CTkLabel(janela, text='Em quantos minutos deseja desligar o Pc?', text_color='white', font=('montserrat', 20)).pack(padx=10, pady=10)
valor_cmd = CTk.StringVar()
cmd = CTk.CTkEntry(janela, placeholder_text='Minutos', width=300).pack(padx=10, pady=10)
CTk.CTkButton(janela, text='Iniciar', width=100, command=lambda: verificador()).pack(padx=10, pady=10)
CTk.CTkButton(janela, text='Sair', width=100, command=lambda: quit()).pack(padx=10, pady=10)

janela.mainloop()
