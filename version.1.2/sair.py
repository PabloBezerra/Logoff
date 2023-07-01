# Importações
import os
import PySimpleGUI as sg
# from time import sleep #

# Tema
sg.theme('DarkBlue17')

# Variáveis
checado = True


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
        [sg.Text('Sair do Windows', font='verdana 20', text_color='white')],
        [sg.Text('Em quantos minutos deseja desligar o Pc?', key='subtitulo')],
        [sg.Input(key='min')],
        [sg.Button('Iniciar')]
    ]
    return sg.Window('Sair do Windows', layout=layout, finalize=True, return_keyboard_events=True)


def sucesso(num):  # janela de encerramento
    layout = [
        [sg.Text('Sucesso!!!', font='verdana 20', text_color='green')],
        [sg.Text(f'Seu Sistema se encerrará em {num} minutos! Até mais!', key='subtitulo')],
        [sg.Checkbox('Bloquear o Windows ao sair do programa!', key='check', default=checado)],
        [sg.Button('Até mais!')],
        [sg.Button('Cancelar')]
    ]
    return sg.Window('Sucesso!!!', layout=layout, finalize=True, return_keyboard_events=True)


# Loop Principal
janela1, janela2 = principal(), None

while True:
    window, event, values = sg.read_all_windows()

    # Fechamento da janela e do aplicativo
    if window == janela1 and event == sg.WIN_CLOSED or window == janela2 and event == 'Até mais!' or window == janela2 and event == "\r":
        if window == janela2 and values['check'] == True:
            bloquear()
            ativado = True
        else:
            ativado = False
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
        
    # Execução da ação principal
    if window == janela1 and event == 'Iniciar' or window == janela1 and event == "\r":
        minuto = values['min']
        if minuto.isnumeric():
            sair(minuto)
            janela2 = sucesso(minuto)
            janela1.hide()

        # Verificação de erro
        elif minuto == '':
            sg.popup('Erro!', 'Preencha o campo com números. Tente Novamente!')
        else:
            sg.popup('Erro!', 'Utilize apenas números. Tente Novamente!')
            janela1['min'].update('')

    # Conclusão e tela final
    if window == janela2 and event == 'Cancelar':
        cancelar()
        janela2.hide()
        janela1.un_hide()
        janela1['min'].update('')

window.close()
