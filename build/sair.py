import os
import PySimpleGUI as sg
# from time import sleep

sg.theme('DarkBlue17')

def sair(num):
    num = int(num)
    sec = num * 60
    os.system(f'shutdown -s -t {sec}')


# def timer(tim):
#     seg = 0
#     min = int(tim)
#     while True:
#         seg -= 1
#         if seg <= 0 and min < 0:
#             break
#         elif seg <= 0:
#             seg = 60
#             min -= 1
#         sleep(1)
#         janela2['subtitulo'].update(f'Seu Sistema se encerrará em {min} minutos e {seg} segundos! Até mais!')
    

def cancelar():
    os.system('shutdown -a')


def principal():
    layout = [
        [sg.Text('Sair do Windows', font='verdana 20', text_color='white')],
        [sg.Text('Em quantos minutos deseja desligar o Pc?', key='subtitulo')],
        [sg.InputText(key='min')],
        [sg.Button('Iniciar')]
    ]
    return sg.Window('Sair do Windows',layout=layout, finalize=True)


def sucesso(num):
    layout = [
        [sg.Text('Sucesso!!!', font='verdana 20', text_color='green')],
        [sg.Text(f'Seu Sistema se encerrará em {num} minutos! Até mais!', key='subtitulo')],
        [sg.Button('Até mais!')],
        [sg.Button('Cancelar')]
    ]
    return sg.Window('Sucesso!!!', layout=layout, finalize=True)


janela1, janela2 = principal(), None 

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED or window == janela2 and event == 'Até mais!' or window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Iniciar':
        minuto = values['min']
        if minuto.isnumeric():
            sair(minuto)
            janela2 = sucesso(minuto)
            janela1.hide()
        elif minuto == '':
            sg.popup('Erro!', 'Preencha o campo com números. Tente Novamente!')
        else:
            sg.popup('Erro!', 'Utilize apenas números. Tente Novamente!')
            janela1['min'].update('')
    if window == janela2 and event == 'Cancelar':
        cancelar()
        janela2.hide()
        janela1.un_hide()
        janela1['min'].update('')

janela1,janela2.close()
