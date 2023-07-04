# Importações
import os
import PySimpleGUI as sg
from PySimpleGUI import Push
# from time import sleep #


# Funções de sistema
def sair(num):  # comando de encerramento do windows
    num = int(num)
    sec = num * 60
    os.system(f'shutdown -s -t {sec}')


def cancelar():  # comando de cancelamento de encerramento do windows
    os.system('shutdown -a')


def bloquear():  # comando de bloquear o usuário do windows
    os.system('rundll32.exe user32.dll,LockWorkStation')


# Função de tempo
'''def timer(tim):
    seg = 0
    min = int(tim)
    while True:
        seg -= 1
        if seg <= 0 and min < 0:
            break
        elif seg <= 0:
            seg = 60
            min -= 1
        sleep(1)
        janela2['subtitulo'].update(f'Seu Sistema se encerrará em {min} minutos e {seg} segundos! Até mais!')'''


# Funções de Janela
def principal():  # janela de apresentação
    layout = [
        [Push(), sg.Text('Sair do Windows', font='Arial 20', text_color='white'), Push()],
        [sg.Text('Em quantos minutos deseja desligar o Pc?', key='subtitulo')],
        [sg.Input(key='min')],
        [sg.Button('Iniciar'), Push(), sg.Button('Sair')]
    ]
    return sg.Window('Sair do Windows', layout=layout, finalize=True, return_keyboard_events=True)


def erro():  # janela de erro de imput
    layout = [
        [Push(), sg.Text('ERRO!', font='verdana 20', text_color='red', key='titulo'), Push()],
        [sg.Text('', key='tipo')],
        [Push(), sg.Button('Ok'), Push()]
    ]
    return sg.Window('Aviso', layout=layout, finalize=True, return_keyboard_events=True)


def sucesso(num):  # janela de encerramento
    layout = [
        [Push(), sg.Text('Sucesso!!!', font='verdana 20', text_color='green'), Push()],
        [sg.Text(f'Seu Sistema se encerrará em {num} minutos! Até mais!', key='subtitulo')],
        [sg.Checkbox('Bloquear o Windows ao sair do programa!', key='check', default=checado)],
        [sg.Button('Até mais!'), Push(), sg.Button('Cancelar')]
    ]
    return sg.Window('Sucesso!!!', layout=layout, finalize=True, return_keyboard_events=True)


# Tema
sg.theme('DarkBlue17')

# Variáveis
arquivo = 'log.txt'
janela_main = principal()
janela_aviso = None
janela_sucesso = None

# Verificação e criação de arquivo
if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        f.write('')

# Mudança de variável
with open(arquivo, 'r') as r:
    if r.readline() == 'Ativado':
        checado = True
    else:
        checado = False


# Loop Principal
while True:
    window, event, values = sg.read_all_windows()

    # Fechamento de janelas e do aplicativo
    if window == janela_sucesso and event == sg.WIN_CLOSED or window == janela_main and event == sg.WIN_CLOSED or window == janela_main and event == 'Sair':
        break
    if window == janela_sucesso and event == 'Até mais!' or window == janela_sucesso and event == "\r":
        if window == janela_sucesso and values['check'] == True:
            bloquear()
            with open(arquivo, 'w') as f:
                f.write('Ativado')
        else:
            with open(arquivo, 'w') as f:
                f.write('Desativado')
        break
    if window == janela_aviso and event == sg.WIN_CLOSED or window == janela_aviso and event == 'Ok' or window == janela_aviso and event == '\r':
        janela_main.un_hide()
        janela_main['min'].update('')
        janela_aviso.close()

    # Execução da ação principal
    if window == janela_main and event == 'Iniciar' or window == janela_main and event == "\r":
        minuto = str(values['min']).strip()

        # Sucesso da operação
        if minuto.isnumeric():
            sair(minuto)
            janela_sucesso = sucesso(minuto)
            janela_main.hide()

        # Verificação de erro
        else:
            janela_aviso = erro()
            janela_main.hide()
            if minuto == '':
                janela_aviso['tipo'].update('Preencha o campo com números. Tente Novamente!')
            else:
                janela_aviso['tipo'].update('Utilize apenas números. Tente Novamente!')

    # Cancelamento da operação
    if window == janela_sucesso and event == 'Cancelar':
        cancelar()
        janela_sucesso.close()
        janela_aviso = erro()
        janela_aviso['titulo'].update('Cancelado!', text_color='yellow')
        janela_aviso['tipo'].update('Operação cancelada pelo usuário')

window.close()
